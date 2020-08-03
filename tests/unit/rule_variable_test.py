"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.RuleVariable import RuleVariable
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput


class RuleVariableTest(unittest.TestCase):
    def test_create_rule_var_1(self):
        my_rule_var = RuleVariable()

        self.assertIsNone(my_rule_var.name, msg='Test name')
        self.assertIsNone(my_rule_var.mf, msg='Test mf')

    def test_create_rule_var_2(self):
        my_name = 'Depth'
        my_mf = 'Medium'
        my_rule_var = RuleVariable(my_name, my_mf)

        self.assertEqual(my_name, my_rule_var.name, msg='Test name')
        self.assertEqual(my_mf, my_rule_var.mf, msg='Test mf')

    def test_property_name(self):
        my_rule_var = RuleVariable()
        my_name = 'test name'

        my_rule_var.name = my_name

        self.assertEqual(my_name, my_rule_var.name, msg='Test name')

    def test_property_name_exception(self):
        my_rule_var = RuleVariable()
        my_name = [10, 20, 30]

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            my_rule_var.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception')

    def test_property_mf(self):
        my_rule_var = RuleVariable()
        my_mf = 'test mf'
        my_rule_var.mf = my_mf

        self.assertEqual(my_mf, my_rule_var.mf, msg='Test mf')

    def test_property_mf_exception(self):
        my_rule_var = RuleVariable()
        my_mf = [10, 20, 30]

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            my_rule_var.mf = my_mf

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mf exception')


class RuleInputTest(unittest.TestCase):
    def test_create_rule_input(self):
        my_rule_input = RuleInput()

        self.assertIsNone(my_rule_input.name, msg='Test name')
        self.assertIsNone(my_rule_input.mf, msg='Test mf')
        self.assertEqual('antecedent', my_rule_input.var_type,
                         msg='Test var_type')
        self.assertIsNone(my_rule_input.var_not, msg='Test var_not')

    def test_create_rule_input_2(self):
        my_name = 'Depth'
        my_mf = 'Medium'
        my_var_not = True
        my_rule_input = RuleInput(my_name, my_mf, my_var_not)

        self.assertEqual(my_name, my_rule_input.name, msg='Test name')
        self.assertEqual(my_mf, my_rule_input.mf, msg='Test mf')
        self.assertEqual('antecedent', my_rule_input.var_type,
                         msg='Test var_type')
        self.assertEqual(my_var_not, my_rule_input.var_not, msg='Test mf')

    def test_property_var_type(self):
        my_rule_input = RuleInput()
        my_var_type = 'antecedent'

        self.assertEqual(my_var_type, my_rule_input.var_type,
                         msg='Test var_type')

    def test_property_var_not(self):
        my_rule_input = RuleInput()
        my_var_not = True
        my_rule_input.var_not = my_var_not

        self.assertEqual(my_var_not, my_rule_input.var_not, msg='Test mf')

    def test_property_var_not_exception(self):
        my_rule_input = RuleInput()
        my_var_not = 14

        my_exception = "O operador lógico NOT não é um booleano!"
        with self.assertRaises(Exception) as context:
            my_rule_input.var_not = my_var_not

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mf exception')


class RuleOutputTest(unittest.TestCase):
    def test_create_rule_output(self):
        my_rule_output = RuleOutput()

        self.assertIsNone(my_rule_output.name, msg='Test name')
        self.assertIsNone(my_rule_output.mf, msg='Test mf')
        self.assertEqual('consequent', my_rule_output.var_type,
                         msg='Test var_type')

    def test_property_var_type(self):
        my_rule_output = RuleOutput()
        my_var_type = 'consequent'

        self.assertEqual(my_var_type, my_rule_output.var_type,
                         msg='Test var_type')
