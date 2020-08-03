"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from continentalfuzzy.domain.definition.MamdaniAndMethods import MamdaniAndMethods
from continentalfuzzy.domain.definition.MamdaniDefuzzMethods import MamdaniDefuzzMethods
from continentalfuzzy.domain.definition.MamdaniOrMethods import MamdaniOrMethods
from continentalfuzzy.service.FuzzyControllerService import FuzzyController
from continentalfuzzy.service.SystemService import SystemService
from continentalfuzzy.util.FuzzyUtil import FuzzyUtil


class FuzzyControllerServiceTest(unittest.TestCase):
    def test_create_inputs_from_fis(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=1',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
                    "MF1='Near':'gaussmf',[0.2 0]",
                    "MF2='Far':'gaussmf',[0.42 1]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system
        my_inputs_FIS = my_system.inputs

        my_input = my_system.inputs[1]
        my_range = my_input.range

        # Input 1
        i_universe_1 = FuzzyUtil.create_universe(my_range, my_input.mfs)

        distance = ctrl.Antecedent(universe=i_universe_1,
                                   label='Distance')
        distance['Near'] = fuzz.gaussmf(x=i_universe_1,
                                        sigma=0.2,
                                        mean=0)
        distance['Far'] = fuzz.gaussmf(x=i_universe_1,
                                       sigma=0.42,
                                       mean=1)

        my_f_controller = FuzzyController()
        my_f_controller.create_inputs_from_fis(my_inputs_FIS)
        my_machine = my_f_controller.fuzzy_machine
        c_distance = my_machine.inputs['Distance']

        self.assertEqual(distance.label, c_distance.label, msg='Test label')

        self.assertTrue((distance.universe == c_distance.universe).all(),
                        msg='Test universe')

        for key, value in distance.terms.items():
            mf_name = distance.terms[key].label
            c_mf_name = c_distance.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = distance.terms[key].mf
            c_mf_value = c_distance.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg=f'Test mf {key} universe')

    def test_create_outputs_from_fis(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=1',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)
        my_system = systemService.system
        my_outputs_FIS = my_system.outputs

        my_output = my_system.outputs[1]
        my_range = my_output.range

        # Output 1
        o_universe_1 = FuzzyUtil.create_universe(my_range, my_output.mfs)

        output1 = ctrl.Consequent(universe=o_universe_1,
                                  label='output1',
                                  defuzzify_method='centroid')

        output1['Lagoon'] = fuzz.gaussmf(x=o_universe_1,
                                         sigma=0.4247,
                                         mean=1)
        output1['Reef'] = fuzz.gaussmf(x=o_universe_1,
                                       sigma=0.4247,
                                       mean=2)
        output1['ForeReef'] = fuzz.gaussmf(x=o_universe_1,
                                           sigma=0.4247,
                                           mean=3)
        output1['Basin'] = fuzz.gaussmf(x=o_universe_1,
                                        sigma=0.4247,
                                        mean=4)
        my_f_controller = FuzzyController()

        my_f_controller.create_outputs_from_fis(MamdaniDefuzzMethods.centroid,
                                                my_outputs_FIS)
        my_machine = my_f_controller.fuzzy_machine
        c_output1 = my_machine.outputs['output1']

        self.assertEqual(output1.label, c_output1.label, msg='Test label')

        self.assertTrue((output1.universe == c_output1.universe).all(),
                        msg='Test universe')

        for key, value in output1.terms.items():
            mf_name = output1.terms[key].label
            c_mf_name = output1.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = output1.terms[key].mf
            c_mf_value = output1.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg='Test mf {key} universe')

    def test_create_rules_from_fis(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=1',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
                    "MF1='Near':'gaussmf',[0.2 0]",
                    "MF2='Far':'gaussmf',[0.42 1]"],
                   ["Name='Slope'",
                    'Range=[0 0.05]',
                    'NumMFs=3',
                    "MF1='Low':'trapmf',[-0.01 -0.005 0.001 0.002]",
                    "MF2='Medium':'trapmf',[0.0015 0.0025 0.004 0.005]",
                    "MF3='High':'trapmf',[0.004 0.005 0.06 0.07]"],
                   ["Name='Depth'", 'Range=[0 3000]', 'NumMFs=3',
                    "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                    "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                    "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system
        my_inputs_FIS = my_system.inputs

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

        my_input_2 = my_system.inputs[2]
        my_range_2 = my_input_2.range

        my_input_3 = my_system.inputs[3]
        my_range_3 = my_input_3.range

        # Input 1
        i_universe_1 = FuzzyUtil.create_universe(my_range_1, my_input_1.mfs)
        distance = ctrl.Antecedent(universe=i_universe_1,
                                   label='Distance')
        distance['Near'] = fuzz.gaussmf(x=i_universe_1,
                                        sigma=0.2,
                                        mean=0)
        distance['Far'] = fuzz.gaussmf(x=i_universe_1,
                                       sigma=0.42,
                                       mean=1)

        # Input 2
        i_universe_2 = FuzzyUtil.create_universe(my_range_2, my_input_2.mfs)
        slope = ctrl.Antecedent(universe=i_universe_2,
                                label='Slope')
        slope['Low'] = fuzz.trapmf(x=i_universe_2,
                                   abcd=[-0.01, -0.005, 0.001, 0.002])
        slope['Medium'] = fuzz.trapmf(x=i_universe_2,
                                      abcd=[0.0015, 0.0025, 0.004, 0.005])
        slope['High'] = fuzz.trapmf(x=i_universe_2,
                                    abcd=[0.004, 0.005, 0.06, 0.07])

        # Input 3
        i_universe_3 = FuzzyUtil.create_universe(my_range_3, my_input_3.mfs)
        depth = ctrl.Antecedent(universe=i_universe_3,
                                label='Depth')
        depth['Shallow'] = fuzz.gauss2mf(x=i_universe_3,
                                         sigma1=10.3,
                                         mean1=-56.35,
                                         sigma2=6.65,
                                         mean2=2.384)
        depth['Medium'] = fuzz.gauss2mf(x=i_universe_3,
                                        sigma1=18.6,
                                        mean1=62.2,
                                        sigma2=17.81,
                                        mean2=84.92)
        depth['Deep'] = fuzz.gauss2mf(x=i_universe_3,
                                      sigma1=77.9,
                                      mean1=260,
                                      sigma2=28.3,
                                      mean2=3042.07612175964)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)
        my_outputs_FIS = my_system.outputs

        my_output = my_system.outputs[1]
        my_range = my_output.range

        # Output 1
        o_universe_1 = FuzzyUtil.create_universe(my_range, my_output.mfs)
        output1 = ctrl.Consequent(universe=o_universe_1,
                                  label='output1',
                                  defuzzify_method='centroid')
        output1['Lagoon'] = fuzz.gaussmf(x=o_universe_1,
                                         sigma=0.4247,
                                         mean=1)
        output1['Reef'] = fuzz.gaussmf(x=o_universe_1,
                                       sigma=0.4247,
                                       mean=2)
        output1['ForeReef'] = fuzz.gaussmf(x=o_universe_1,
                                           sigma=0.4247,
                                           mean=3)
        output1['Basin'] = fuzz.gaussmf(x=o_universe_1,
                                        sigma=0.4247,
                                        mean=4)

        my_list = ['1 0 -3, 1 (1) : 1']

        systemService.create_rules_from_list(my_list)
        my_rules_FIS = my_system.rules

        my_rules = [ctrl.Rule(antecedent=(distance['Near'] & (~depth['Deep'])),
                              consequent=(output1['Lagoon'] % 1.0),
                              and_func=np.fmin, or_func=np.fmax)]

        my_f_controller = FuzzyController()
        my_f_controller.create_inputs_from_fis(my_inputs_FIS)
        my_f_controller.create_outputs_from_fis(MamdaniDefuzzMethods.centroid,
                                                my_outputs_FIS)
        my_f_controller.create_rules_from_fis(MamdaniAndMethods.min,
                                              MamdaniOrMethods.max,
                                              my_rules_FIS)

        my_f_controller_rule_0 = my_f_controller.fuzzy_machine.rules[0]

        for n_input in range(len(my_f_controller_rule_0.antecedent_terms)):
            self.assertEqual(
                my_rules[0].antecedent_terms[n_input].full_label,
                my_f_controller_rule_0.antecedent_terms[n_input].full_label,
                msg='Test consequent')

        self.assertEqual(
            my_rules[0].consequent[0].term.full_label,
            my_f_controller_rule_0.consequent[0].term.full_label,
            msg='Test consequent')

    def test_create_from_fis_system(self):
        my_filename = "tests/test_data/EnvironmentMamdani.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

        my_input_2 = my_system.inputs[2]
        my_range_2 = my_input_2.range

        my_input_3 = my_system.inputs[3]
        my_range_3 = my_input_3.range

        my_output = my_system.outputs[1]
        my_range = my_output.range

        my_f_controller = FuzzyController()
        my_f_controller.create_from_fis_system(my_system)
        my_machine = my_f_controller.fuzzy_machine

        # Input 1
        i_universe_1 = FuzzyUtil.create_universe(my_range_1, my_input_1.mfs)

        distance = ctrl.Antecedent(universe=i_universe_1,
                                   label='Distance')
        distance['Near'] = fuzz.gaussmf(x=i_universe_1,
                                        sigma=0.2,
                                        mean=0)
        distance['Far'] = fuzz.gaussmf(x=i_universe_1,
                                       sigma=0.42,
                                       mean=1)

        c_distance = my_machine.inputs['Distance']

        self.assertEqual(distance.label, c_distance.label, msg='Test label')

        self.assertTrue((distance.universe == c_distance.universe).all(),
                        msg='Test universe')

        for key, value in distance.terms.items():
            mf_name = distance.terms[key].label
            c_mf_name = c_distance.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = distance.terms[key].mf
            c_mf_value = c_distance.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg=f'Test mf {key} universe')

        # Input 2
        i_universe_2 = FuzzyUtil.create_universe(my_range_2, my_input_2.mfs)

        slope = ctrl.Antecedent(universe=i_universe_2,
                                label='Slope')

        slope['Low'] = fuzz.trapmf(x=i_universe_2,
                                   abcd=[-0.01, -0.005, 0.001, 0.002])
        slope['Medium'] = fuzz.trapmf(x=i_universe_2,
                                      abcd=[0.0015, 0.0025, 0.004, 0.005])
        slope['High'] = fuzz.trapmf(x=i_universe_2,
                                    abcd=[0.004, 0.005, 0.06, 0.07])

        c_slope = my_machine.inputs['Slope']

        self.assertEqual(slope.label, c_slope.label, msg='Test label')
        self.assertTrue((slope.universe == c_slope.universe).all(),
                        msg='Test universe')

        for key, value in slope.terms.items():
            mf_name = slope.terms[key].label
            c_mf_name = c_slope.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = slope.terms[key].mf
            c_mf_value = c_slope.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg=f'Test mf {key} universe')

        # Input 3
        i_universe_3 = FuzzyUtil.create_universe(my_range_3, my_input_3.mfs)

        depth = ctrl.Antecedent(universe=i_universe_3,
                                label='Depth')

        depth['Shallow'] = fuzz.gauss2mf(x=i_universe_3,
                                         sigma1=10.3,
                                         mean1=-56.35,
                                         sigma2=6.65,
                                         mean2=2.384)
        depth['Medium'] = fuzz.gauss2mf(x=i_universe_3,
                                        sigma1=18.6,
                                        mean1=62.2,
                                        sigma2=17.81,
                                        mean2=84.92)
        depth['Deep'] = fuzz.gauss2mf(x=i_universe_3,
                                      sigma1=77.9,
                                      mean1=260,
                                      sigma2=28.3,
                                      mean2=3042.07612175964)

        c_depth = my_machine.inputs['Depth']

        self.assertEqual(depth.label, c_depth.label, msg='Test label')

        self.assertTrue((depth.universe == c_depth.universe).all(),
                        msg='Test universe')

        for key, value in depth.terms.items():
            mf_name = depth.terms[key].label
            c_mf_name = c_depth.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = depth.terms[key].mf
            c_mf_value = c_depth.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg=f'Test mf {key} universe')

        # Output 1
        o_universe_1 = FuzzyUtil.create_universe(my_range, my_output.mfs)

        output1 = ctrl.Consequent(universe=o_universe_1,
                                  label='output1',
                                  defuzzify_method='centroid')

        output1['Lagoon'] = fuzz.gaussmf(x=o_universe_1,
                                         sigma=0.4247,
                                         mean=1)
        output1['Reef'] = fuzz.gaussmf(x=o_universe_1,
                                       sigma=0.4247,
                                       mean=2)
        output1['ForeReef'] = fuzz.gaussmf(x=o_universe_1,
                                           sigma=0.4247,
                                           mean=3)
        output1['Basin'] = fuzz.gaussmf(x=o_universe_1,
                                        sigma=0.4247,
                                        mean=4)

        c_output_1 = my_machine.outputs['output1']

        self.assertEqual(output1.label, c_output_1.label, msg='Test label')

        self.assertTrue((output1.universe == c_output_1.universe).all(),
                        msg='Test universe')

        for key, value in output1.terms.items():
            mf_name = output1.terms[key].label
            c_mf_name = c_output_1.terms[key].label
            self.assertEqual(mf_name, c_mf_name, msg=f'Test mf {key} label')

            mf_value = output1.terms[key].mf
            c_mf_value = c_output_1.terms[key].mf
            self.assertTrue((mf_value == c_mf_value).all(),
                            msg=f'Test mf {key} universe')

        my_rules = [ctrl.Rule(antecedent=(distance['Near'] & (~depth['Deep'])),
                              consequent=(output1['Lagoon'] % 1.0),
                              and_func=np.fmin, or_func=np.fmax)]

        my_f_controller_rule_0 = my_f_controller.fuzzy_machine.rules[0]

        for n_input in range(len(my_f_controller_rule_0.antecedent_terms)):
            self.assertEqual(
                my_rules[0].antecedent_terms[n_input].full_label,
                my_f_controller_rule_0.antecedent_terms[n_input].full_label,
                msg='Test consequent')

        self.assertEqual(
            my_rules[0].consequent[0].term.full_label,
            my_f_controller_rule_0.consequent[0].term.full_label,
            msg='Test consequent')

    def test_create_from_fis_system_exception_1(self):
        my_f_controller = FuzzyController()

        my_exception = "O valor não é uma instância da classe FISSystem!"
        with self.assertRaises(Exception) as context:
            my_f_controller.create_from_fis_system(10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test membership_function exception 1')

    def test_fuzzy_calc_single_value(self):
        my_filename = "tests/test_data/EnvironmentMamdani.fis"
        fisSystemService = SystemService()
        fisSystem = fisSystemService.import_file(my_filename)

        fuzzyController = FuzzyController()
        fuzzyController.create_from_fis_system(fisSystem)

        fuzzy_result = fuzzyController.fuzzy_calc_single_value(
            {'Distance': 0.3,
             'Slope': 0.0015,
             'Depth': 50},
            'output1')

        self.assertEqual(round(fuzzy_result, 4), 1.6539,
                         msg='Test fuzzy_calc_single_value')
