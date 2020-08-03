"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.domain.SugenoRuleVariable import SugenoRuleVariable
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleOutput import \
    SugenoRuleOutput
from continentalfuzzy.service.sugeno_membership_functions.TrapezoidalMembershipFunction import \
    TrapezoidalMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction


class SugenoRuleVariableTest(unittest.TestCase):
    def test_create_rule_var_1(self):
        my_rule_var = SugenoRuleVariable()

        self.assertIsNone(my_rule_var.name, msg='Test name')
        self.assertIsNone(my_rule_var.rule_func, msg='Test rule_func')
        self.assertEqual(dict(),my_rule_var.params, msg='Test params')

    def test_create_rule_var_2(self):
        my_name = 'test name'
        my_rule_func = TriangularMembershipFunction.calculate_trimf
        my_params = {'abcd': [0, 1, 2, 4]}
        my_rule_var = SugenoRuleVariable(my_name, my_rule_func, my_params)

        self.assertEqual(my_name, my_rule_var.name, msg='Test name')
        self.assertEqual(my_rule_func, my_rule_var.rule_func,
                         msg='Test rule_func')
        self.assertEqual(my_params, my_rule_var.params, msg='Test params')

    def test_property_name(self):
        my_rule_var = SugenoRuleVariable()
        my_name = 'test name'

        my_rule_var.name = my_name

        self.assertEqual(my_name, my_rule_var.name, msg='Test name')

    def test_property_name_exception(self):
        my_rule_var = SugenoRuleVariable()
        my_name = [10, 20, 30]

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            my_rule_var.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception')

    def test_property_rule_func(self):
        my_rule_var = SugenoRuleVariable()
        my_rule_var.rule_func = TrapezoidalMembershipFunction.calculate_trapmf

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         my_rule_var.rule_func, msg='Test rule_func')

    def test_property_rule_func_exception(self):
        my_rule_var = SugenoRuleVariable()
        my_mf = [10, 20, 30]

        my_exception = "A função da regra não é uma função!"
        with self.assertRaises(Exception) as context:
            my_rule_var.rule_func = my_mf

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rule_func exception')

    def test_property_params(self):
        my_rule_var = SugenoRuleVariable()
        my_mf = 'test mf'
        my_rule_var.params = {'abc': [1, 2, 3]}

        self.assertEqual({'abc': [1, 2, 3]},
                         my_rule_var.params, msg='Test params')

    def test_property_params_exception(self):
        my_rule_var = SugenoRuleVariable()
        my_mf = [10, 20, 30]

        my_exception = "Os parâmetros não são dicionários!"
        with self.assertRaises(Exception) as context:
            my_rule_var.params = my_mf

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property params exception')


class SugenoRuleInputTest(unittest.TestCase):
    def test_create_rule_input(self):
        my_rule_input = SugenoRuleInput()

        self.assertIsNone(my_rule_input.name, msg='Test name')
        self.assertIsNone(my_rule_input.rule_func,
                         msg='Test rule_func')
        self.assertEqual(dict(), my_rule_input.params, msg='Test params')
        self.assertEqual('antecedent', my_rule_input.var_type,
                         msg='Test var_type')
        self.assertIsNone(my_rule_input.var_not, msg='Test var_not')

    def test_create_rule_input_2(self):
        my_name = 'Depth'
        my_rule_func = TriangularMembershipFunction.calculate_trimf
        my_params = {'abcd': [0, 1, 2, 4]}
        my_var_not = True
        my_rule_input = SugenoRuleInput(my_name,
                                        my_rule_func,
                                        my_params,
                                        my_var_not)

        self.assertEqual(my_name, my_rule_input.name, msg='Test name')
        self.assertEqual(my_rule_func, my_rule_input.rule_func,
                         msg='Test rule_func')
        self.assertEqual(my_params, my_rule_input.params, msg='Test params')
        self.assertEqual('antecedent', my_rule_input.var_type,
                         msg='Test var_type')
        self.assertEqual(my_var_not, my_rule_input.var_not, msg='Test mf')

    def test_property_var_type(self):
        my_rule_input = SugenoRuleInput()
        my_var_type = 'antecedent'

        self.assertEqual(my_var_type, my_rule_input.var_type,
                         msg='Test var_type')

    def test_property_var_not(self):
        my_rule_input = SugenoRuleInput()
        my_var_not = True
        my_rule_input.var_not = my_var_not

        self.assertEqual(my_var_not, my_rule_input.var_not, msg='Test mf')

    def test_property_var_not_exception(self):
        my_rule_input = SugenoRuleInput()
        my_var_not = 14

        my_exception = "O operador lógico NOT não é um booleano!"
        with self.assertRaises(Exception) as context:
            my_rule_input.var_not = my_var_not

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mf exception')


class SugenoRuleOutputTest(unittest.TestCase):
    def test_create_rule_output(self):
        my_rule_output = SugenoRuleOutput()

        self.assertIsNone(my_rule_output.name, msg='Test name')
        self.assertIsNone(my_rule_output.rule_func,
                         msg='Test rule_func')
        self.assertEqual(dict(), my_rule_output.params, msg='Test params')
        self.assertEqual('consequent', my_rule_output.var_type,
                         msg='Test var_type')

    def test_property_var_type(self):
        my_rule_output = SugenoRuleOutput()
        my_var_type = 'consequent'

        self.assertEqual(my_var_type, my_rule_output.var_type,
                         msg='Test var_type')
