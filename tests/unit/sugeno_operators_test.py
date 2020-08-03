"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.domain.sugeno.rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.service.sugeno.membership_functions.GaussMembershipFunction import \
    GaussMembershipFunction
from continentalfuzzy.service.sugeno.membership_functions.GaussTwoMembershipFunction import \
    GaussTwoMembershipFunction
from continentalfuzzy.service.sugeno.operators.MaxOrMethod import MaxOrMethod
from continentalfuzzy.service.sugeno.operators.MinAndMethod import MinAndMethod
from continentalfuzzy.service.sugeno.operators.NotMethod import NotMethod
from continentalfuzzy.service.sugeno.operators.ProborOrMethod import \
    ProborOrMethod
from continentalfuzzy.service.sugeno.operators.ProdAndMethod import \
    ProdAndMethod


class MaxOrMethodTest(unittest.TestCase):
    def test_calculate_max_or(self):
        my_value = {'Distance': 0.7, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.7

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = False
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(MaxOrMethod.calculate_max_or(my_rule_inputs,
                                                            my_value), 1),
                         msg='Test calculate_max_or')

    def test_calculate_max_or_not(self):
        my_value = {'Distance': 0.7, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.3

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = True
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(MaxOrMethod.calculate_max_or(my_rule_inputs,
                                                            my_value), 1),
                         msg='Test calculate_max_or_not')


class ProdAndMethodTest(unittest.TestCase):
    def test_calculate_prod_and(self):
        my_value = {'Distance': 0.2, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.5

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = False
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(ProdAndMethod.calculate_prod_and(my_rule_inputs,
                                                                my_value), 1),
                         msg='Test calculate_prod_and')

    def test_calculate_prod_and_not(self):
        my_value = {'Distance': 0.1, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.2

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = True
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(ProdAndMethod.calculate_prod_and(my_rule_inputs,
                                                                my_value), 1),
                         msg='Test calculate_prod_and_not')


class ProborOrMethodTest(unittest.TestCase):
    def test_calculate_probor_or(self):
        my_value = {'Distance': 0.3, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.8

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = False
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(
            my_and_value,
            round(ProborOrMethod.calculate_probor_or(my_rule_inputs,
                                                     my_value), 1),
            msg='Test calculate_probor_or')

    def test_calculate_probor_or_not(self):
        my_value = {'Distance': 0.3, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.5

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = True
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(
            my_and_value,
            round(ProborOrMethod.calculate_probor_or(my_rule_inputs,
                                                     my_value), 1),
            msg='Test calculate_probor_or_not')


class NotMethodTest(unittest.TestCase):
    def test_calculate_not(self):
        my_value = 0.8
        my_not_value = 0.2
        self.assertEqual(my_not_value,
                         round(NotMethod.calculate_not(my_value), 1),
                         msg='Test Not Method')


class MinAndMethodTest(unittest.TestCase):
    def test_calculate_max_or(self):
        my_value = {'Distance': 0.2, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.6

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = False
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(MinAndMethod.calculate_min_and(my_rule_inputs,
                                                              my_value), 1),
                         msg='Test calculate_max_or')

    def test_calculate_max_or_not(self):
        my_value = {'Distance': 0.1, 'Slope': 0.01, 'Depth': 200.0}
        my_and_value = 0.3

        my_name_1 = 'Distance'
        my_rule_func_1 = GaussMembershipFunction.calculate_gaussmf
        my_params_1 = {'mean': 0,
                       'sigma': 0.2}
        my_var_not_1 = False
        my_rule_input_1 = SugenoRuleInput(my_name_1,
                                          my_rule_func_1,
                                          my_params_1,
                                          my_var_not_1)

        my_name_2 = 'Depth'
        my_rule_func_2 = GaussTwoMembershipFunction.calculate_gauss2mf
        my_params_2 = {'mean1': 260,
                       'sigma1': 77.9,
                       'mean2': 3042.08,
                       'sigma2': 28.3}
        my_var_not_2 = True
        my_rule_input_2 = SugenoRuleInput(my_name_2,
                                          my_rule_func_2,
                                          my_params_2,
                                          my_var_not_2)

        my_rule_inputs = [my_rule_input_1, my_rule_input_2]

        self.assertEqual(my_and_value,
                         round(MinAndMethod.calculate_min_and(my_rule_inputs,
                                                              my_value), 1),
                         msg='Test calculate_max_or_not')
