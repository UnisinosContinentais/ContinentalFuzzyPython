"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np
from skfuzzy import control as ctrl

from typing import Dict, List
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.System import System
from continentalfuzzy.domain.FuzzyMachine import FuzzyMachine
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.domain.variable.Output import Output
from continentalfuzzy.domain.definition.MamdaniAndMethods import AndMethods
from continentalfuzzy.domain.definition.MamdaniDefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.MamdaniOrMethods import OrMethods
from continentalfuzzy.util.FuzzyUtil import FuzzyUtil

class FuzzyController:
    """
    Classe usada para criar um controlador fuzzy da biblioteca scikit-fuzzy.
    """

    def __init__(self):
        """ Inicializador da classe FuzzyController"""
        self.__fuzzy_machine = FuzzyMachine()

    @property
    def fuzzy_machine(self) -> FuzzyMachine:
        return self.__fuzzy_machine

    def create_inputs_from_fis(self, fis_inputs: Dict[int, Input]):
        """
        Cria os antecedentes do controlador usando instâncias da classe
        FISInput.

        Parâmetros
        ----------
        fis_inputs : Dict[int, FISInput]
            Dicionário com as chaves sendo o número dos antecedentes e os
            valores sendo instâncias da classe FISInput.
        """
        # Percorre todos os valores do dicionário dos antecedentes
        for f_input in fis_inputs.values():
            f_range = f_input.range
            f_name = f_input.name

            # Cria o universo do antecedente
            f_universe = FuzzyUtil.create_universe(f_range, f_input.mfs)

            # Cria o antecedente usando o scikit-fuzzy
            val_input = ctrl.Antecedent(universe=f_universe, label=f_name)
            self.fuzzy_machine.add_input(f_name, val_input)

            # Cria as curvas de pertinência
            f_ant = self.fuzzy_machine.inputs[f_name]
            for f_mf in f_input.mfs.values():
                mf_name = f_mf.name
                f_ant[mf_name] = FuzzyUtil.membership_function(mf=f_mf,
                                                               univ=f_universe)

    def create_outputs_from_fis(self,
                                fis_defuzz: DefuzzMethods,
                                fis_outputs: Dict[int, Output]):
        """
        Cria os consequentes do controlador usando instâncias da classe
        FISOutput.

        Parâmetros
        ----------
        fis_defuzz : FISDefuzzMethods
            Instância da classe FISDefuzzMethods.

        fis_outputs : Dict[int, FISOutput]
            Dicionário com as chaves sendo o número dos consequentes e os
            valores sendo instâncias da classe FISOutput.
        """
        # Percorre todos os valores do dicionário dos consequentes
        for f_output in fis_outputs.values():
            f_range = f_output.range
            f_name = f_output.name

            # Cria o universo do consequente
            f_universe = FuzzyUtil.create_universe(f_range, f_output.mfs)

            # Cria o antecedente usando o scikit-fuzzy
            val_output = ctrl.Consequent(universe=f_universe,
                                         label=f_name,
                                         defuzzify_method=fis_defuzz.name)
            self.fuzzy_machine.add_output(f_name, val_output)

            f_cons = self.fuzzy_machine.outputs[f_name]
            for f_mf in f_output.mfs.values():
                mf_name = f_mf.name
                f_cons[mf_name] = FuzzyUtil.membership_function(mf=f_mf,
                                                                univ=f_universe)

    def create_rules_from_fis(self,
                              fis_and: AndMethods,
                              fis_or: OrMethods,
                              fis_rules: List[Rule]):
        """
        Cria as regras do controlador usando instâncias da classe
        FISRule.

        Parâmetros
        ----------
        fis_and : FISANDMethods
            Instância da classe FISANDMethods.

        fis_or : FISORMethods
            Instância da classe FISORMethods.

        fis_rules : List[FISRule]
            Lista com os valores sendo instâncias da classe FISRule.
        """
        # Percorre todos os valores da lista das regras
        for f_rule in fis_rules:
            f_con = f_rule.connection

            first_input = True
            aux_inputs = ""
            # Percorre todos os antecedentes da regra
            for f_input in f_rule.inputs:
                if first_input:
                    first_input = False
                else:
                    aux_inputs += self.fuzzy_machine.DICT_CONNECTORS.get(f_con)

                inp_name = f_input.name
                mf_name = f_input.mf

                # Verifica se o antecedente possui o operador NOT
                if f_input.var_not:
                    aux_inputs += f"(~self.fuzzy_machine.inputs['{inp_name}']" \
                                  f"['{mf_name}'])"
                else:
                    aux_inputs += f"self.fuzzy_machine.inputs['{inp_name}']" \
                                  f"['{mf_name}']"

            # Cria o antecedente
            f_ant = (eval(aux_inputs))

            # Percorre todos os consequentes da regra
            for f_output in f_rule.outputs:
                out_name = f_output.name
                mf_name = f_output.mf

                # Cria o consequente
                f_output_name = self.fuzzy_machine.outputs[out_name]
                f_con = (f_output_name[mf_name] % f_rule.weight)

            # Cria a regra usando o scikit-fuzzy
            self.fuzzy_machine.rules.append(
                ctrl.Rule(antecedent=f_ant,
                          consequent=f_con,
                          and_func=self.fuzzy_machine.DICT_AND_METHODS.get(fis_and),
                          or_func=self.fuzzy_machine.DICT_OR_METHODS.get(fis_or)))

    def create_from_fis_system(self, fis_system: System):
        """
        Cria o do controlador usando instâncias da classe FISSystem.

        Parâmetros
        ----------
        fis_system : FISSystem
            Instância da classe FISSystem.
        """
        if not isinstance(fis_system, System):
            raise Exception(
                "O valor não é uma instância da classe FISSystem!")

        # Cria os antecedentes
        self.create_inputs_from_fis(fis_system.inputs)

        # Cria os consequentes
        self.create_outputs_from_fis(fis_system.defuzz_method,
                                     fis_system.outputs)

        # Cria as regras
        self.create_rules_from_fis(fis_system.and_method,
                                   fis_system.or_method,
                                   fis_system.rules)

        # Criar o controlador
        self.fuzzy_machine.controller = ctrl.ControlSystem(self.fuzzy_machine.rules)

        # Criar o simulador
        self.fuzzy_machine.simulator = ctrl.ControlSystemSimulation(self.fuzzy_machine.controller)

    def fuzzy_calc_single_value(self,
                                dict_inputs: Dict[str, float],
                                output: str):
        """
        Calcula um valor do consequente fuzzy, baseado no dicionário com os
        valores dos antecedentes.

        Parâmetros
        ----------
        dict_inputs : Dict[str, float]
            Dicionário com as chaves sendo o nome dos antecedentes e os
            valores sendo números float.

        output : str
        """
        # Percorre o dicionário dos antecedesntes
        for name_input, value_input in dict_inputs.items():
            self.fuzzy_machine.simulator.input[name_input] = value_input
        self.fuzzy_machine.simulator.compute()

        # Retorna o output selecionado
        return self.fuzzy_machine.simulator.output[output]
