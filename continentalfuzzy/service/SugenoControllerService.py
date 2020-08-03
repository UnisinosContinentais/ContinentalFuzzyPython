"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np
from typing import Optional
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.SugenoController import SugenoController
from continentalfuzzy.domain.SugenoRule import SugenoRule
from continentalfuzzy.domain.System import System
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.OrMethods import OrMethods
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleOutput import \
    SugenoRuleOutput
from continentalfuzzy.domain.sugeno_variable.SugenoInput import SugenoInput
from continentalfuzzy.domain.sugeno_variable.SugenoOutput import SugenoOutput
from continentalfuzzy.service.sugeno_membership_functions.GaussMembershipFunction import \
    GaussMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.GaussTwoMembershipFunction import \
    GaussTwoMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TrapezoidalMembershipFunction import \
    TrapezoidalMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.LinearMembershipFunction import \
    LinearMembershipFunction
from continentalfuzzy.service.sugeno_operators.MaxOrMethod import MaxOrMethod
from continentalfuzzy.service.sugeno_operators.MinAndMethod import MinAndMethod
from continentalfuzzy.service.sugeno_operators.NotMethod import NotMethod
from continentalfuzzy.service.sugeno_operators.ProborOrMethod import \
    ProborOrMethod
from continentalfuzzy.service.sugeno_operators.ProdAndMethod import \
    ProdAndMethod


class SugenoControllerService:
    def __init__(self,
                 sugeno_controller: Optional[SugenoController] = None):
        """ Inicializador da classe SugenoControllerService"""
        self.__sugeno_controller = SugenoController()

        if sugeno_controller is not None:
            self.__sugeno_controller = sugeno_controller

    @property
    def sugeno_controller(self):
        return self.__sugeno_controller

    def get_connection(self, p_rule: Rule):
        if p_rule.connection == Connections.AND:
            if self.sugeno_controller.fis_system.and_method == AndMethods.min:
                return MinAndMethod.calculate_min_and

            elif self.sugeno_controller.fis_system.and_method == AndMethods.prod:
                return ProdAndMethod.calculate_prod_and

        elif p_rule.connection == Connections.OR:
            if self.sugeno_controller.fis_system.or_method == OrMethods.max:
                return MaxOrMethod.calculate_max_or
            elif self.sugeno_controller.fis_system.or_method == OrMethods.probor:
                return ProborOrMethod.calculate_probor_or

    def get_mf_function(self, p_membershipfunction):
        if p_membershipfunction.function == Functions.trimf:
            return {'func': TriangularMembershipFunction.calculate_trimf,
                    'params': {'abc': p_membershipfunction.abc}}

        elif p_membershipfunction.function == Functions.trapmf:
            return {'func': TrapezoidalMembershipFunction.calculate_trapmf,
                    'params': {'abcd': p_membershipfunction.abcd}}

        elif p_membershipfunction.function == Functions.gaussmf:
            return {'func': GaussMembershipFunction.calculate_gaussmf,
                    'params': {'mean': p_membershipfunction.mean,
                               'sigma': p_membershipfunction.sigma}}

        elif p_membershipfunction.function == Functions.gauss2mf:
            return {'func': GaussTwoMembershipFunction.calculate_gauss2mf,
                    'params': {'mean1': p_membershipfunction.mean1,
                               'sigma1': p_membershipfunction.sigma1,
                               'mean2': p_membershipfunction.mean2,
                               'sigma2': p_membershipfunction.sigma2}}

        elif p_membershipfunction.function == Functions.constant:
            dict_params = dict()
            f_inputs = self.sugeno_controller.fis_system.inputs
            for f_input in f_inputs.values():
                dict_params[f_input.name] = 0
            dict_params['__constant__'] = p_membershipfunction.value
            return {'func': LinearMembershipFunction.calculate_linear,
                    'params': dict_params}

        elif p_membershipfunction.function == Functions.linear:
            dict_params = dict()
            f_inputs = self.sugeno_controller.fis_system.inputs
            for num, param in enumerate(p_membershipfunction.params):
                if f_inputs.get(num + 1) is None:
                    dict_params['__constant__'] = param
                else:
                    dict_params[f_inputs.get(num + 1).name] = param
            return {'func': LinearMembershipFunction.calculate_linear,
                    'params': dict_params}

    def create_from_fis_system(self, fis_system: System):
        self.sugeno_controller.fis_system = fis_system

        # Import inputs
        for f_input in fis_system.inputs.values():
            sugeno_input = SugenoInput()
            sugeno_input.range = f_input.range
            sugeno_input.num_mfs = f_input.num_mfs
            for f_mf in f_input.mfs.values():
                sugeno_input.add_mfs(f_mf.name, self.get_mf_function(f_mf))

            self.sugeno_controller.add_input(f_input.name,
                                             sugeno_input)

        # Import outputs
        for f_output in fis_system.outputs.values():
            sugeno_output = SugenoOutput()
            sugeno_output.range = f_output.range
            sugeno_output.num_mfs = f_output.num_mfs
            for f_mf in f_output.mfs.values():
                sugeno_output.add_mfs(f_mf.name, self.get_mf_function(f_mf))

            self.sugeno_controller.add_output(f_output.name,
                                              sugeno_output)

        # Import rules
        for rule in fis_system.rules:
            sugeno_rule = SugenoRule()
            sugeno_rule.weight = rule.weight
            sugeno_rule.connection_func = self.get_connection(rule)

            for i_rule in rule.inputs:
                sugeno_i_rule = SugenoRuleInput()
                sugeno_i_rule.name = i_rule.name
                sugeno_i_rule.var_not = i_rule.var_not
                sugeno_i_rule.rule_func = self.sugeno_controller.inputs[i_rule.name].mfs[i_rule.mf]['func']
                sugeno_i_rule.params = self.sugeno_controller.inputs[i_rule.name].mfs[i_rule.mf]['params']

                sugeno_rule.add_input(sugeno_i_rule)

            for o_rule in rule.outputs:
                sugeno_o_rule = SugenoRuleOutput()
                sugeno_o_rule.name = o_rule.name
                sugeno_o_rule.rule_func = self.sugeno_controller.outputs[o_rule.name].mfs[o_rule.mf]['func']
                sugeno_o_rule.params = self.sugeno_controller.outputs[o_rule.name].mfs[o_rule.mf]['params']
                sugeno_rule.add_output(sugeno_o_rule)

            self.sugeno_controller.add_rule(sugeno_rule)

    def calc_rule_weights(self):
        weights_list = list()

        for rule in self.sugeno_controller.rules:
            weights_list.append(rule.weight)

        return weights_list

    def calc_rule_output_level(self, v_inputs):
        list_results = list()
        for rule in self.sugeno_controller.rules:
            r_output = rule.outputs[0]
            list_results.append(
                LinearMembershipFunction.calculate_linear(r_output.params,
                                                          v_inputs))

        return np.array(list_results)

    def calc_rule_firing(self, v_inputs):
        list_results = list()
        for rule in self.sugeno_controller.rules:
            if len(rule.inputs) == 1:
                r_input = rule.inputs[0]
                result = r_input.rule_func(v_inputs[r_input.name],
                                           **r_input.params)
                if r_input.var_not:
                    list_results.append(NotMethod.calculate_not(result))
                else:
                    list_results.append(result)
            else:
                list_results.append(rule.connection_func(
                    rule.inputs,
                    v_inputs))
        return np.array(list_results)

    def sugeno_calc_single_value(self, v_inputs):
        if len(v_inputs) != len(self.sugeno_controller.inputs):
            raise Exception("Número de inputs inválido!!")

        if self.sugeno_controller.fis_system.defuzz_method == DefuzzMethods.wtaver:
            w_array = self.calc_rule_firing(v_inputs)
            z_array = self.calc_rule_output_level(v_inputs)

            weights = self.calc_rule_weights()
            w_array_weights = w_array * weights

            result = np.sum(w_array_weights * z_array) / sum(w_array_weights)

            return result

        elif self.sugeno_controller.fis_system.defuzz_method == DefuzzMethods.wtsum:
            w_array = self.calc_rule_firing(v_inputs)
            z_array = self.calc_rule_output_level(v_inputs)

            weights = self.calc_rule_weights()
            w_array_weights = w_array * weights

            result = np.sum(w_array_weights * z_array)

            return result
