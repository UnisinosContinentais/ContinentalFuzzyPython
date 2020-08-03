"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.SugenoController import SugenoController
from continentalfuzzy.domain.SugenoRule import SugenoRule
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleOutput import \
    SugenoRuleOutput
from continentalfuzzy.domain.sugeno_variable.SugenoInput import SugenoInput
from continentalfuzzy.domain.sugeno_variable.SugenoOutput import SugenoOutput
from continentalfuzzy.service.SystemService import SystemService
from continentalfuzzy.service.sugeno_membership_functions.LinearMembershipFunction import \
    LinearMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction
from continentalfuzzy.service.sugeno_operators.MinAndMethod import MinAndMethod


class SugenoControllerTest(unittest.TestCase):
    def test_create_FuzzyController_1(self):
        my_sugeno = SugenoController()

        self.assertIsNone(my_sugeno.fis_system, msg='Test fis_system')
        self.assertEqual(dict(), my_sugeno.inputs, msg='Test inputs')
        self.assertEqual(dict(), my_sugeno.outputs, msg='Test outputs')
        self.assertEqual(list(), my_sugeno.rules, msg='Test rules')

    def test_create_FuzzyController_2(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_range = [0, 10]
        my_num_mfs = 2

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'mf 1': my_trimf,
                   'mf 2': my_gaussmf}

        my_variable = SugenoInput(my_range, my_num_mfs, mf_dict)

        my_inputs = {'Input 1': my_variable}

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'var 1': my_trimf,
                   'var 2': my_gaussmf}

        my_range = [0, 10]
        my_num_mfs = 2

        my_variable = SugenoOutput(my_range, my_num_mfs, mf_dict)

        my_outputs = {'Output 1': my_variable}

        # Rule input
        my_rule_input = SugenoRuleInput('Input 1',
                                        TriangularMembershipFunction.calculate_trimf,
                                        {'abcd': [0, 1, 2, 4]},
                                        True)
        my_rule_inputs = [my_rule_input]

        # Rule output
        my_rule_output = SugenoRuleOutput('Output 1',
                                          LinearMembershipFunction.calculate_linear,
                                          {'Input 1': 0, '__constant__': 1})
        my_rule_outputs = [my_rule_output]

        # Rule
        my_weight = 0.8
        my_connection = MinAndMethod.calculate_min_and

        my_rule = [SugenoRule(my_weight,
                              my_connection,
                              my_rule_inputs,
                              my_rule_outputs)]

        my_sugeno = SugenoController(my_fuzzy, my_inputs, my_outputs, my_rule)

        self.assertEqual(my_fuzzy, my_sugeno.fis_system, msg='Test fis_system')
        self.assertEqual(my_inputs, my_sugeno.inputs, msg='Test inputs')
        self.assertEqual(my_outputs, my_sugeno.outputs, msg='Test outputs')
        self.assertEqual(my_rule, my_sugeno.rules, msg='Test rules')

    def test_property_fis_system(self):
        my_sugeno = SugenoController()

        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_sugeno.fis_system = my_fuzzy

        self.assertEqual(my_fuzzy, my_sugeno.fis_system, msg='Test fis_system')

    def test_property_fis_system_exception_1(self):
        my_sugeno = SugenoController()
        my_fuzzy = 'test'

        my_exception = f"O parâmetro não é uma instância da classe System!"
        with self.assertRaises(Exception) as context:
            my_sugeno.fis_system = my_fuzzy

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property fis_system exception 1')

    def test_property_inputs(self):
        my_sugeno = SugenoController()

        my_range = [0, 10]
        my_num_mfs = 2

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'mf 1': my_trimf,
                   'mf 2': my_gaussmf}

        my_variable = SugenoInput(my_range, my_num_mfs, mf_dict)

        my_inputs = {'Input 1': my_variable}

        my_sugeno.inputs = my_inputs

        self.assertEqual(my_inputs, my_sugeno.inputs, msg='Test inputs')

    def test_property_inputs_exception_1(self):
        my_sugeno = SugenoController()
        my_inputs = 'inputs'

        my_exception = f"O input não é um dicionário!"
        with self.assertRaises(Exception) as context:
            my_sugeno.inputs = my_inputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 1')

    def test_property_inputs_exception_2(self):
        my_sugeno = SugenoController()
        my_inputs = {10: 'value'}

        my_exception = f"A chave não é uma string!"
        with self.assertRaises(Exception) as context:
            my_sugeno.inputs = my_inputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 2')

    def test_property_inputs_exception_3(self):
        my_sugeno = SugenoController()
        my_inputs = {'Input 1': 'value'}

        my_exception = f"O valor não é uma instância da classe SugenoInput!"
        with self.assertRaises(Exception) as context:
            my_sugeno.inputs = my_inputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 3')

    def test_add_input(self):
        my_sugeno = SugenoController()

        my_range = [0, 10]
        my_num_mfs = 2

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'mf 1': my_trimf,
                   'mf 2': my_gaussmf}

        my_variable = SugenoInput(my_range, my_num_mfs, mf_dict)

        my_inputs = {'Input 1': my_variable}

        my_sugeno.add_input('Input 1', my_variable)

        self.assertEqual(my_inputs, my_sugeno.inputs, msg='Test add_input')

    def test_add_input_exception_1(self):
        my_sugeno = SugenoController()

        my_exception = f"A chave não é uma string!"
        with self.assertRaises(Exception) as context:
            my_sugeno.add_input(10, 'test')

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 1')

    def test_add_input_exception_2(self):
        my_sugeno = SugenoController()

        my_exception = f"O valor não é uma instância da classe SugenoInput!"
        with self.assertRaises(Exception) as context:
            my_sugeno.add_input('test 1', 'value')

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 2')

    def test_property_outputs(self):
        my_sugeno = SugenoController()

        my_range = [0, 10]
        my_num_mfs = 2

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'mf 1': my_trimf,
                   'mf 2': my_gaussmf}

        my_variable = SugenoOutput(my_range, my_num_mfs, mf_dict)

        my_outputs = {'Ouput 1': my_variable}

        my_sugeno.outputs = my_outputs

        self.assertEqual(my_outputs, my_sugeno.outputs, msg='Test outputs')

    def test_property_outputs_exception_1(self):
        my_sugeno = SugenoController()
        my_outputs = 'output'

        my_exception = f"O output não é um dicionário!"
        with self.assertRaises(Exception) as context:
            my_sugeno.outputs = my_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_outputs_exception_2(self):
        my_sugeno = SugenoController()
        my_outputs = {10: 'value'}

        my_exception = f"A chave não é uma string!"
        with self.assertRaises(Exception) as context:
            my_sugeno.outputs = my_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_property_outputs_exception_3(self):
        my_sugeno = SugenoController()
        my_outputs = {'Output 1': 'value'}

        my_exception = f"O valor não é uma instância da classe SugenoOutput!"
        with self.assertRaises(Exception) as context:
            my_sugeno.outputs = my_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 3')

    def test_add_output(self):
        my_sugeno = SugenoController()

        my_range = [0, 10]
        my_num_mfs = 2

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'mf 1': my_trimf,
                   'mf 2': my_gaussmf}

        my_variable = SugenoOutput(my_range, my_num_mfs, mf_dict)

        my_outputs = {'Output 1': my_variable}

        my_sugeno.add_output('Output 1', my_variable)

        self.assertEqual(my_outputs, my_sugeno.outputs, msg='Test add_output')

    def test_add_output_exception_1(self):
        my_sugeno = SugenoController()

        my_exception = f"A chave não é uma string!"
        with self.assertRaises(Exception) as context:
            my_sugeno.add_output(10, 'test')

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 1')

    def test_add_output_exception_2(self):
        my_sugeno = SugenoController()

        my_exception = f"O valor não é uma instância da classe SugenoOutput!"
        with self.assertRaises(Exception) as context:
            my_sugeno.add_output('test 1', 'value')

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 2')

    def test_property_rules(self):
        my_sugeno = SugenoController()

        # Rule input
        my_rule_input = SugenoRuleInput('Input 1',
                                        TriangularMembershipFunction.calculate_trimf,
                                        {'abcd': [0, 1, 2, 4]},
                                        True)
        my_rule_inputs = [my_rule_input]

        # Rule output
        my_rule_output = SugenoRuleOutput('Output 1',
                                          LinearMembershipFunction.calculate_linear,
                                          {'Input 1': 0, '__constant__': 1})
        my_rule_outputs = [my_rule_output]

        # Rule
        my_weight = 0.8
        my_connection = MinAndMethod.calculate_min_and

        my_rule = SugenoRule(my_weight,
                             my_connection,
                             my_rule_inputs,
                             my_rule_outputs)

        my_rules = [my_rule]

        my_sugeno.rules = my_rules

        self.assertEqual(my_rules, my_sugeno.rules, msg='Test rules')

    def test_property_rules_exception_1(self):
        my_sugeno = SugenoController()
        my_rule = 'rule'

        my_exception = f"O rule não é um dicionário!"
        with self.assertRaises(Exception) as context:
            my_sugeno.rules = my_rule

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_rules_exception_2(self):
        my_sugeno = SugenoController()
        my_outputs = ['value']

        my_exception = f"O valor não é uma instância da classe SugenoRule!"
        with self.assertRaises(Exception) as context:
            my_sugeno.rules = my_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_add_rule(self):
        my_sugeno = SugenoController()

        # Rule input
        my_rule_input = SugenoRuleInput('Input 1',
                                        TriangularMembershipFunction.calculate_trimf,
                                        {'abcd': [0, 1, 2, 4]},
                                        True)
        my_rule_inputs = [my_rule_input]

        # Rule output
        my_rule_output = SugenoRuleOutput('Output 1',
                                          LinearMembershipFunction.calculate_linear,
                                          {'Input 1': 0, '__constant__': 1})
        my_rule_outputs = [my_rule_output]

        # Rule
        my_weight = 0.8
        my_connection = MinAndMethod.calculate_min_and

        my_rule = SugenoRule(my_weight,
                             my_connection,
                             my_rule_inputs,
                             my_rule_outputs)

        my_rules = [my_rule]

        my_sugeno.add_rule(my_rule)

        self.assertEqual(my_rules, my_sugeno.rules, msg='Test add_rule')

    def test_add_rule_exception_1(self):
        my_sugeno = SugenoController()

        my_exception = f"O valor não é uma instância da classe SugenoRule!"
        with self.assertRaises(Exception) as context:
            my_sugeno.add_rule('test')

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_rule exception 1')
