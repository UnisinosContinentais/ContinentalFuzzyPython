"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput


class RuleTest(unittest.TestCase):
    def test_create_rule_1(self):
        my_rule = Rule()

        self.assertIsNone(my_rule.name, msg='Test name')
        self.assertIsNone(my_rule.weight, msg='Test weight')
        self.assertIsNone(my_rule.connection, msg='Test connection')
        self.assertEqual(list(), my_rule.inputs, msg='Test inputs')
        self.assertEqual(list(), my_rule.outputs, msg='Test outputs')

    def test_create_rule_2(self):
        # Rule input
        my_i_name = 'Depth'
        my_i_mf = 'Medium'
        my_i_var_not = True
        my_rule_inputs = [RuleInput(my_i_name, my_i_mf, my_i_var_not)]

        # Rule output
        my_o_name = 'Depth'
        my_o_mf = 'Medium'
        my_rule_outputs = [RuleOutput(my_o_name, my_o_mf)]

        # Rule
        my_name = 'Test rule'
        my_weight = 0.8
        my_connection = Connections.AND

        my_rule = Rule(my_name,
                       my_weight,
                       my_connection,
                       my_rule_inputs,
                       my_rule_outputs)

        self.assertEqual(my_name, my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(my_connection, my_rule.connection,
                         msg='Test connection')
        self.assertEqual(my_rule_inputs, my_rule.inputs, msg='Test inputs')
        self.assertEqual(my_rule_outputs, my_rule.outputs, msg='Test outputs')

    def test_property_name(self):
        my_rule = Rule()
        my_name = 'test name'
        my_rule.name = my_name

        self.assertEqual(my_name, my_rule.name, msg='Test name')

    def test_property_name_exception_1(self):
        my_rule = Rule()
        my_name = {1: 'rule'}

        my_exception = "O nome não é uma String!"
        with self.assertRaises(Exception) as context:
            my_rule.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception 1')

    def test_property_weight(self):
        my_rule = Rule()
        my_weight = 1.0
        my_rule.weight = my_weight

        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')

    def test_property_weight_exception_1(self):
        my_rule = Rule()
        my_weight = 'weight'

        my_exception = f"O parâmetro peso não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 1')

    def test_property_weight_exception_2(self):
        my_rule = Rule()
        my_weight = 1.2

        my_exception = f"O peso precisa estar no intervalo 0 e 1!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 2')

    def test_property_weight_exception_3(self):
        my_rule = Rule()
        my_weight = -0.1

        my_exception = f"O peso precisa estar no intervalo 0 e 1!"
        with self.assertRaises(Exception) as context:
            my_rule.weight = my_weight

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property weight exception 3')

    def test_property_AND(self):
        my_rule = Rule()
        my_connection = Connections.AND
        my_rule.connection = my_connection

        self.assertEqual(my_connection, my_rule.connection,
                         msg='Test property connection and')

    def test_property_OR(self):
        my_rule = Rule()
        my_connection = Connections.OR
        my_rule.connection = my_connection

        self.assertEqual(my_connection, my_rule.connection,
                         msg='Test property connection or')

    def test_property_connection_exception(self):
        my_rule = Rule()
        my_connection = 'maybe'

        my_exception = (f"Conector {my_connection} não é uma instância "
                        f"da classe FISConnections!")
        with self.assertRaises(Exception) as context:
            my_rule.connection = my_connection

        self.assertEqual(my_exception, context.exception.args[0])

    def test_property_inputs(self):
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_list = [my_rule_input1, my_rule_input2]

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR
        my_rule.inputs = my_list

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(Connections.OR, my_rule.connection,
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
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_list = [my_rule_input1, 10]

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O valor não é uma instância da classe FISRuleInput!"
        with self.assertRaises(Exception) as context:
            my_rule.inputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 1')

    def test_property_inputs_exception_2(self):
        my_list = 10

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_rule.inputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 2')

    def test_add_input(self):
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_rule.add_input(my_rule_input1)

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(Connections.OR, my_rule.connection,
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
        my_rule_input1 = RuleOutput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O valor não é uma instância da classe FISRuleInput!"
        with self.assertRaises(Exception) as context:
            my_rule.add_input(my_rule_input1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception')

    def test_property_outputs(self):
        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_list = [my_rule_output1]

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR
        my_rule.outputs = my_list

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(Connections.OR, my_rule.connection,
                         msg='Test connection')

        # Output rule 1
        self.assertEqual('output1', my_rule.outputs[0].name,
                         msg='Test output rule 1 name')
        self.assertEqual('Reef', my_rule.outputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual('consequent', my_rule.outputs[0].var_type,
                         msg='Test input rule 1 var_type')

    def test_property_outputs_exception_1(self):
        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'Distance'
        my_rule_output1.mf = 'Near'

        my_list = [my_rule_output1, 10]

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O valor não é uma instância da classe FISRuleOutput!"
        with self.assertRaises(Exception) as context:
            my_rule.outputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_outputs_exception_2(self):
        my_list = 10

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_rule.outputs = my_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_property_add_output(self):
        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_rule.add_output(my_rule_output1)

        self.assertEqual('Rule_1', my_rule.name, msg='Test name')
        self.assertEqual(my_weight, my_rule.weight, msg='Test weight')
        self.assertEqual(Connections.OR, my_rule.connection,
                         msg='Test connection')

        # Output rule 1
        self.assertEqual('output1', my_rule.outputs[0].name,
                         msg='Test output rule 1 name')
        self.assertEqual('Reef', my_rule.outputs[0].mf,
                         msg='Test input rule 1 mf')
        self.assertEqual('consequent', my_rule.outputs[0].var_type,
                         msg='Test input rule 1 var_type')

    def test_add_output_exception(self):
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule = Rule()
        my_rule.name = 'Rule_1'
        my_weight = 1.0
        my_rule.weight = my_weight
        my_rule.connection = Connections.OR

        my_exception = "O valor não é uma instância da classe FISRuleOutput!"
        with self.assertRaises(Exception) as context:
            my_rule.add_output(my_rule_input1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception')
