"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.SugenoController import SugenoController
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.membership_function.ConstantMF import ConstantMF
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.LinearMF import LinearMF
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput
from continentalfuzzy.service.SugenoControllerService import \
    SugenoControllerService
from continentalfuzzy.service.SystemService import SystemService
from continentalfuzzy.service.sugeno_membership_functions.GaussMembershipFunction import \
    GaussMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.GaussTwoMembershipFunction import \
    GaussTwoMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.LinearMembershipFunction import \
    LinearMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TrapezoidalMembershipFunction import \
    TrapezoidalMembershipFunction
from continentalfuzzy.service.sugeno_membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction
from continentalfuzzy.service.sugeno_operators.MaxOrMethod import MaxOrMethod
from continentalfuzzy.service.sugeno_operators.MinAndMethod import MinAndMethod
from continentalfuzzy.service.sugeno_operators.ProborOrMethod import \
    ProborOrMethod
from continentalfuzzy.service.sugeno_operators.ProdAndMethod import \
    ProdAndMethod


class SugenoControllerServiceTest(unittest.TestCase):
    def test_create_sugeno_controller_service(self):
        my_controller = SugenoControllerService()
        self.assertTrue(isinstance(my_controller.sugeno_controller,
                                   SugenoController),
                        msg='Test rules')

    def test_get_connection_1(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

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

        self.assertEqual(MinAndMethod.calculate_min_and,
                         my_service.get_connection(my_rule),
                         msg='Test get_connection 1')

    def test_get_connection_2(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

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
        my_connection = Connections.OR

        my_rule = Rule(my_name,
                       my_weight,
                       my_connection,
                       my_rule_inputs,
                       my_rule_outputs)

        self.assertEqual(MaxOrMethod.calculate_max_or,
                         my_service.get_connection(my_rule),
                         msg='Test get_connection 2')

    def test_get_connection_3(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_2.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

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

        self.assertEqual(ProdAndMethod.calculate_prod_and,
                         my_service.get_connection(my_rule),
                         msg='Test get_connection 3')

    def test_get_connection_4(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_2.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

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
        my_connection = Connections.OR

        my_rule = Rule(my_name,
                       my_weight,
                       my_connection,
                       my_rule_inputs,
                       my_rule_outputs)

        self.assertEqual(ProborOrMethod.calculate_probor_or,
                         my_service.get_connection(my_rule),
                         msg='Test get_connection 4')

    def test_get_mf_function_1(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test Name"
        my_abc = [1, 2, 3]
        my_trimf = TriMF(my_name, my_abc)

        my_mf = {'func': TriangularMembershipFunction.calculate_trimf,
                 'params': {'abc': my_trimf.abc}}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_trimf),
                         msg='Test get_mf_function 1')

    def test_get_mf_function_2(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test Name"
        my_abcd = [1, 2, 3, 4]
        my_trapmf = TrapMF(my_name, my_abcd)

        my_mf = {'func': TrapezoidalMembershipFunction.calculate_trapmf,
                 'params': {'abcd': my_trapmf.abcd}}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_trapmf),
                         msg='Test get_mf_function 2')

    def test_get_mf_function_3(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test Name"
        my_sigma = 1
        my_mean = 0
        my_gaussmf = GaussMF(my_name, my_sigma, my_mean)

        my_mf = {'func': GaussMembershipFunction.calculate_gaussmf,
                 'params': {'mean': my_gaussmf.mean,
                            'sigma': my_gaussmf.sigma}}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_gaussmf),
                         msg='Test get_mf_function 3')

    def test_get_mf_function_4(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test Name"
        my_sigma1 = 1
        my_mean1 = 0
        my_sigma2 = 10
        my_mean2 = 5
        my_gaussmf2 = Gauss2MF(my_name,
                               my_sigma1,
                               my_mean1,
                               my_sigma2,
                               my_mean2)

        my_mf = {'func': GaussTwoMembershipFunction.calculate_gauss2mf,
                 'params': {'mean1': my_gaussmf2.mean1,
                            'sigma1': my_gaussmf2.sigma1,
                            'mean2': my_gaussmf2.mean2,
                            'sigma2': my_gaussmf2.sigma2}}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_gaussmf2),
                         msg='Test get_mf_function 4')

    def test_get_mf_function_5(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test name"
        my_value = 15
        my_constant = ConstantMF(my_name, my_value)
        dict_params = {'service': 0,
                       'food': 0,
                       '__constant__': 15.0}

        my_mf =  {'func': LinearMembershipFunction.calculate_linear,
                  'params': dict_params}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_constant),
                         msg='Test get_mf_function 5')

    def test_get_mf_function_6(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_controller = SugenoController()
        my_controller.fis_system = my_fuzzy

        my_service = SugenoControllerService(my_controller)

        my_name = "Test name"
        my_num_inputs = 2
        my_params = [1, 2, 3]
        my_linear = LinearMF(my_name, my_num_inputs, my_params)

        dict_params = {'service': 1,
                       'food': 2,
                       '__constant__': 3}

        my_mf =  {'func': LinearMembershipFunction.calculate_linear,
                  'params': dict_params}

        self.assertEqual(my_mf,
                         my_service.get_mf_function(my_linear),
                         msg='Test get_mf_function 6')

    def test_create_from_fis_system(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        self.assertEqual(my_fuzzy,
                         my_service.sugeno_controller.fis_system,
                         msg='Test fis_system')

        sugeno_service = my_service.sugeno_controller.inputs.get('service')

        self.assertEqual('antecedent',
                         sugeno_service.var_type,
                         msg='Test var_type')
        self.assertEqual([0, 10],
                         sugeno_service.range,
                         msg='Test range')
        self.assertEqual(3,
                         sugeno_service.num_mfs,
                         msg='Test num_mfs')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_service.mfs.get('excellent').get('func'),
                         msg='Test service mfs excellent func')
        self.assertEqual({'abcd': [5.0, 7.5, 10.0, 10.0]},
                         sugeno_service.mfs.get('excellent').get('params'),
                         msg='Test service mfs excellent func')

        self.assertEqual(TriangularMembershipFunction.calculate_trimf,
                         sugeno_service.mfs.get('good').get('func'),
                         msg='Test service mfs good func')
        self.assertEqual({'abc': [2.5, 5.0, 7.5]},
                         sugeno_service.mfs.get('good').get('params'),
                         msg='Test service mfs good func')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_service.mfs.get('poor').get('func'),
                         msg='Test service mfs poor func')
        self.assertEqual({'abcd': [0.0, 0.0, 2.5, 5.0]},
                         sugeno_service.mfs.get('poor').get('params'),
                         msg='Test service mfs poor func')

        sugeno_food = my_service.sugeno_controller.inputs.get('food')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_food.mfs.get('rancid').get('func'),
                         msg='Test food mfs rancid func')
        self.assertEqual({'abcd': [0.0, 0.0, 2.5, 7.5]},
                         sugeno_food.mfs.get('rancid').get('params'),
                         msg='Test food mfs rancid func')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_food.mfs.get('delicious').get('func'),
                         msg='Test food mfs delicious func')
        self.assertEqual({'abcd': [2.5, 7.5, 10.0, 10.0]},
                         sugeno_food.mfs.get('delicious').get('params'),
                         msg='Test food mfs delicious func')

        sugeno_tip = my_service.sugeno_controller.outputs.get('Tip')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_tip.mfs.get('cheap').get('func'),
                         msg='Test Tip mfs cheap func')
        self.assertEqual({'service': 0, 'food': 0, '__constant__': 5.0},
                         sugeno_tip.mfs.get('cheap').get('params'),
                         msg='Test Tip mfs cheap func')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_tip.mfs.get('average').get('func'),
                         msg='Test Tip mfs average func')
        self.assertEqual({'service': 0, 'food': 0, '__constant__': 15.0},
                         sugeno_tip.mfs.get('average').get('params'),
                         msg='Test Tip mfs average func')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_tip.mfs.get('generous').get('func'),
                         msg='Test Tip mfs generous func')
        self.assertEqual({'service': 0, 'food': 0, '__constant__': 25.0},
                         sugeno_tip.mfs.get('generous').get('params'),
                         msg='Test Tip mfs generous func')

        sugeno_rule_1 = my_service.sugeno_controller.rules[0]

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_1.inputs[0].rule_func,
                         msg='Test Rule 1 service rule_func')
        self.assertEqual({'abcd': [0.0, 0.0, 2.5, 5.0]},
                         sugeno_rule_1.inputs[0].params,
                         msg='Test Rule 1 service params')
        self.assertEqual(False,
                         sugeno_rule_1.inputs[0].var_not,
                         msg='Test Rule 1 service var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_1.inputs[0].var_type,
                         msg='Test Rule 1 service var_type')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_1.inputs[1].rule_func,
                         msg='Test Rule 1 food rule_func')
        self.assertEqual({'abcd': [0.0, 0.0, 2.5, 7.5]},
                         sugeno_rule_1.inputs[1].params,
                         msg='Test Rule 1 food params')
        self.assertEqual(False,
                         sugeno_rule_1.inputs[1].var_not,
                         msg='Test Rule 1 food var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_1.inputs[1].var_type,
                         msg='Test Rule 1 food var_type')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_rule_1.outputs[0].rule_func,
                         msg='Test Rule 1 tip rule_func')
        self.assertEqual({'__constant__': 5.0, 'food': 0, 'service': 0},
                         sugeno_rule_1.outputs[0].params,
                         msg='Test Rule 1 tip params')
        self.assertEqual('consequent',
                         sugeno_rule_1.outputs[0].var_type,
                         msg='Test Rule 1 tip var_type')

        self.assertEqual(1,
                         sugeno_rule_1.weight,
                         msg='Test Rule 1 weight')
        self.assertEqual(MaxOrMethod.calculate_max_or,
                         sugeno_rule_1.connection_func,
                         msg='Test Rule 1 connection_func')

        sugeno_rule_2 = my_service.sugeno_controller.rules[1]

        self.assertEqual(TriangularMembershipFunction.calculate_trimf,
                         sugeno_rule_2.inputs[0].rule_func,
                         msg='Test Rule 2 service rule_func')
        self.assertEqual({'abc': [2.5, 5.0, 7.5]},
                         sugeno_rule_2.inputs[0].params,
                         msg='Test Rule 2 service params')
        self.assertEqual(False,
                         sugeno_rule_2.inputs[0].var_not,
                         msg='Test Rule 2 service var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_2.inputs[0].var_type,
                         msg='Test Rule 2 service var_type')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_rule_2.outputs[0].rule_func,
                         msg='Test Rule 2 tip rule_func')
        self.assertEqual({'__constant__': 15.0, 'food': 0, 'service': 0},
                         sugeno_rule_2.outputs[0].params,
                         msg='Test Rule 2 tip params')
        self.assertEqual('consequent',
                         sugeno_rule_2.outputs[0].var_type,
                         msg='Test Rule 2 tip var_type')

        self.assertEqual(1,
                         sugeno_rule_2.weight,
                         msg='Test Rule 2 weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         sugeno_rule_2.connection_func,
                         msg='Test Rule 2 connection_func')

        sugeno_rule_3 = my_service.sugeno_controller.rules[2]

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_3.inputs[0].rule_func,
                         msg='Test Rule 3 service rule_func')
        self.assertEqual({'abcd': [5.0, 7.5, 10.0, 10.0]},
                         sugeno_rule_3.inputs[0].params,
                         msg='Test Rule 3 service params')
        self.assertEqual(False,
                         sugeno_rule_3.inputs[0].var_not,
                         msg='Test Rule 3 service var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_3.inputs[0].var_type,
                         msg='Test Rule 3 service var_type')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_3.inputs[1].rule_func,
                         msg='Test Rule 3 food rule_func')
        self.assertEqual({'abcd': [2.5, 7.5, 10.0, 10.0]},
                         sugeno_rule_3.inputs[1].params,
                         msg='Test Rule 3 food params')
        self.assertEqual(False,
                         sugeno_rule_3.inputs[1].var_not,
                         msg='Test Rule 3 food var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_3.inputs[1].var_type,
                         msg='Test Rule 3 food var_type')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_rule_3.outputs[0].rule_func,
                         msg='Test Rule 3 tip rule_func')
        self.assertEqual({'__constant__': 25.0, 'food': 0, 'service': 0},
                         sugeno_rule_3.outputs[0].params,
                         msg='Test Rule 3 tip params')
        self.assertEqual('consequent',
                         sugeno_rule_3.outputs[0].var_type,
                         msg='Test Rule 3 tip var_type')

        self.assertEqual(0.5,
                         sugeno_rule_3.weight,
                         msg='Test Rule 3 weight')
        self.assertEqual(MaxOrMethod.calculate_max_or,
                         sugeno_rule_3.connection_func,
                         msg='Test Rule 3 connection_func')

        sugeno_rule_4 = my_service.sugeno_controller.rules[3]

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_4.inputs[0].rule_func,
                         msg='Test Rule 4 service rule_func')
        self.assertEqual({'abcd': [5.0, 7.5, 10.0, 10.0]},
                         sugeno_rule_4.inputs[0].params,
                         msg='Test Rule 4 service params')
        self.assertEqual(False,
                         sugeno_rule_4.inputs[0].var_not,
                         msg='Test Rule 4 service var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_4.inputs[0].var_type,
                         msg='Test Rule 4 service var_type')

        self.assertEqual(TrapezoidalMembershipFunction.calculate_trapmf,
                         sugeno_rule_4.inputs[1].rule_func,
                         msg='Test Rule 4 food rule_func')
        self.assertEqual({'abcd': [2.5, 7.5, 10.0, 10.0]},
                         sugeno_rule_4.inputs[1].params,
                         msg='Test Rule 4 food params')
        self.assertEqual(False,
                         sugeno_rule_4.inputs[1].var_not,
                         msg='Test Rule 4 food var_not')
        self.assertEqual('antecedent',
                         sugeno_rule_4.inputs[1].var_type,
                         msg='Test Rule 4 food var_type')

        self.assertEqual(LinearMembershipFunction.calculate_linear,
                         sugeno_rule_4.outputs[0].rule_func,
                         msg='Test Rule 4 tip rule_func')
        self.assertEqual({'__constant__': 25.0, 'food': 0, 'service': 0},
                         sugeno_rule_4.outputs[0].params,
                         msg='Test Rule 4 tip params')
        self.assertEqual('consequent',
                         sugeno_rule_4.outputs[0].var_type,
                         msg='Test Rule 4 tip var_type')

        self.assertEqual(1,
                         sugeno_rule_4.weight,
                         msg='Test Rule 4 weight')
        self.assertEqual(MinAndMethod.calculate_min_and,
                         sugeno_rule_4.connection_func,
                         msg='Test Rule 4 connection_func')

    def test_calc_rule_weights(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        self.assertEqual([1.0, 1.0, 0.5, 1.0],
                         my_service.calc_rule_weights(),
                         msg='Test calc_rule_weights')

    def test_calc_rule_output_level(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1, 'food': 2}

        self.assertTrue(
            ([5, 15, 25, 25] == my_service.calc_rule_output_level(my_inputs)).all(),
            msg='Test calc_rule_output_level 1')

    def test_calc_rule_firing_1(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1, 'food': 2}

        self.assertTrue(
            ([1, 0, 0, 0] == my_service.calc_rule_firing(my_inputs)).all(),
            msg='Test calc_rule_firing 1')

    def test_calc_rule_firing_2(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_3.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1, 'food': 7}

        self.assertTrue(
            ([1, 0, 0.9, 0] == my_service.calc_rule_firing(my_inputs)).all(),
            msg='Test calc_rule_firing 1')


    def test_sugeno_calc_single_value_1(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1, 'food': 7}

        self.assertEqual(
            11.21,
            round(my_service.sugeno_calc_single_value(my_inputs), 2),
            msg='Test sugeno_calc_single_value 1')

    def test_sugeno_calc_single_value_2(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_2.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1, 'food': 7}

        self.assertEqual(
            16.25,
            round(my_service.sugeno_calc_single_value(my_inputs), 2),
            msg='Test sugeno_calc_single_value 2')

    def test_sugeno_calc_single_value_exception_1(self):
        sugeno_filename = "tests/test_data/Tip_fuzzylite_2.fis"
        fisSystemService = SystemService()
        my_fuzzy = fisSystemService.import_file(sugeno_filename)

        my_service = SugenoControllerService()
        my_service.create_from_fis_system(my_fuzzy)

        my_inputs = {'service': 1}

        my_exception = f"Número de inputs inválido!!"
        with self.assertRaises(Exception) as context:
            _ = my_service.sugeno_calc_single_value(my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test sugeno_calc_single_value exception 1')