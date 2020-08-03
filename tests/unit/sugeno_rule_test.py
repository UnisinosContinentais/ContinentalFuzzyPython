"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.SugenoRule import SugenoRule
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.domain.sugeno_rule_variable.SugenoRuleOutput import \
    SugenoRuleOutput
from continentalfuzzy.service.sugeno_membership_functions.LinearMembershipFunction import \
    LinearMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction
from continentalfuzzy.service.sugeno_operators.MinAndMethod import MinAndMethod


class SugenoRuleTest(unittest.TestCase):
    def test_create_rule_1(self):
        my_rule = SugenoRule()

        self.assertIsNone(my_rule.weight, msg='Test weight')
        self.assertIsNone(my_rule.connection_func, msg='Test connection')
        self.assertEqual(list(), my_rule.inputs, msg='Test inputs')
        self.assertEqual(list(), my_rule.outputs, msg='Test outputs')

    def test_create_rule_2(self):
        # Rule input
        my_rule_input = SugenoRuleInput('input',
                                        TriangularMembershipFunction.calculate_trimf,
                                        {'abcd': [0, 1, 2, 4]},
                                        True)
        my_rule_inputs = [my_rule_input]

        # Rule output
        my_rule_output = SugenoRuleOutput('output',
                                          LinearMembershipFunction.calculate_linear,
                                          {'input': 0, '__constant__': 1})
        my_rule_outputs = [my_rule_output]

        # Rule
        my_name = 'Test rule'
        my_weight = 0.8
        my_connection = MinAndMethod.calculate_min_and

        my_rule = SugenoRule(my_weight,
                             my_connection,
                             my_rule_inputs,
                             my_rule_outputs)

        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(my_connection, my_rule.connection_func,
                         msg='Test connection')
        self.assertEqual(my_rule_inputs, my_rule.inputs, msg='Test inputs')
        self.assertEqual(my_rule_outputs, my_rule.outputs, msg='Test outputs')

    def test_property_weight(self):
        my_rule = SugenoRule()
        my_weight = 1.0
        my_rule.weight = my_weight

        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')

    def test_property_weight_exception_1(self):
        my_rule = SugenoRule()
        my_weight = 'weight'

        my_exception = f"O parâmetro peso não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 1')

    def test_property_weight_exception_2(self):
        my_rule = SugenoRule()
        my_weight = 1.2

        my_exception = f"O peso precisa estar no intervalo 0 e 1!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 2')

    def test_property_weight_exception_3(self):
        my_rule = SugenoRule()
        my_weight = -0.1

        my_exception = f"O peso precisa estar no intervalo 0 e 1!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 3')

    def test_property_connection_exception(self):
        my_rule = SugenoRule()
        my_connection = 'maybe'

        my_exception = "O parâmetro não é um método!"
        with self.assertRaises(Exception) as context:
            my_rule.connection_func = my_connection

        self.assertEqual(my_exception, context.exception.args[0])

    def test_property_inputs(self):
        my_rule_input1 = SugenoRuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = SugenoRuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_list = [my_rule_input1, my_rule_input2]

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and
        my_rule.inputs = my_list

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         my_rule.connection_func,
                         msg='Test connections')

        # Input rule 1
        self.assertEqual('Distance', my_rule.inputs[0].name,
                         msg='Test input rule 1 name')
        self.assertEqual('Near', my_rule.inputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual(False, my_rule.inputs[0].var_not,
                         msg='Test input rule 1 var_not')
        self.assertEqual('antecedent', my_rule.inputs[0].var_type,
                         msg='Test input rule 1 var_type')

        # Input rule 2
        self.assertEqual('Depth', my_rule.inputs[1].name,
                         msg='Test input rule 2 name')
        self.assertEqual('Deep', my_rule.inputs[1].mf,
                         msg='Test input rule 2 mf')
        self.assertEqual(True, my_rule.inputs[1].var_not,
                         msg='Test input rule 1 var_not')
        self.assertEqual('antecedent', my_rule.inputs[1].var_type,
                         msg='Test input rule 1 var_type')

    def test_property_inputs_exception_1(self):
        my_rule_input1 = SugenoRuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_list = [my_rule_input1, 10]

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O valor não é uma instância da classe SugenoRuleInput!"
        with self.assertRaises(Exception) as context:
            my_rule.inputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 1')

    def test_property_inputs_exception_2(self):
        my_list = 10

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_rule.inputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 2')

    def test_add_input(self):
        my_rule_input1 = SugenoRuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_rule.add_input(my_rule_input1)

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         my_rule.connection_func,
                         msg='Test connection')

        # Input rule 1
        self.assertEqual('Distance', my_rule.inputs[0].name,
                         msg='Test input rule 1 name')
        self.assertEqual('Near', my_rule.inputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual(False, my_rule.inputs[0].var_not,
                         msg='Test input rule 1 var_not')
        self.assertEqual('antecedent', my_rule.inputs[0].var_type,
                         msg='Test input rule 1 var_type')

    def test_add_input_exception(self):
        my_rule_input1 = SugenoRuleOutput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O valor não é uma instância da classe SugenoRuleInput!"
        with self.assertRaises(Exception) as context:
            my_rule.add_input(my_rule_input1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception')

    def test_property_outputs(self):
        my_rule_output1 = SugenoRuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_list = [my_rule_output1]

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and
        my_rule.outputs = my_list

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         my_rule.connection_func,
                         msg='Test connection')

        # Output rule 1
        self.assertEqual('output1', my_rule.outputs[0].name,
                         msg='Test output rule 1 name')
        self.assertEqual('Reef', my_rule.outputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual('consequent', my_rule.outputs[0].var_type,
                         msg='Test input rule 1 var_type')

    def test_property_outputs_exception_1(self):
        my_rule_output1 = SugenoRuleOutput()
        my_rule_output1.name = 'Distance'
        my_rule_output1.mf = 'Near'

        my_list = [my_rule_output1, 10]

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O valor não é uma instância da classe SugenoRuleOutput!"
        with self.assertRaises(Exception) as context:
            my_rule.outputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_outputs_exception_2(self):
        my_list = 10

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_rule.outputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_property_add_output(self):
        my_rule_output1 = SugenoRuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_rule.add_output(my_rule_output1)

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         my_rule.connection_func,
                         msg='Test connection')

        # Output rule 1
        self.assertEqual('output1', my_rule.outputs[0].name,
                         msg='Test output rule 1 name')
        self.assertEqual('Reef', my_rule.outputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual('consequent', my_rule.outputs[0].var_type,
                         msg='Test input rule 1 var_type')

    def test_add_output_exception(self):
        my_rule_input1 = SugenoRuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = SugenoRule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection_func = MinAndMethod.calculate_min_and

        my_exception = "O valor não é uma instância da classe SugenoRuleOutput!"
        with self.assertRaises(Exception) as context:
            my_rule.add_output(my_rule_input1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception')
