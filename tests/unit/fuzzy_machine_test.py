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
from continentalfuzzy.domain.FuzzyMachine import FuzzyMachine
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.MamdaniOrMethods import MamdaniOrMethods
from continentalfuzzy.service.SystemService import SystemService
from continentalfuzzy.util.FuzzyUtil import FuzzyUtil


class FuzzyMachineTest(unittest.TestCase):
    def test_DICT_AND_METHODS_min(self):
        self.assertEqual(FuzzyMachine.DICT_AND_METHODS[MamdaniAndMethods.min],
                         np.min,
                         msg='Test DICT_AND_METHODS min')

    def test_DICT_AND_METHODS_not_found(self):
        my_exception = "maybe"
        with self.assertRaises(Exception) as context:
            _ = FuzzyMachine.DICT_AND_METHODS['maybe']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test DICT_AND_METHODS not found")

    def test_DICT_OR_METHODS_max(self):
        self.assertEqual(FuzzyMachine.DICT_OR_METHODS[MamdaniOrMethods.max],
                         np.max,
                         msg='Test DICT_OR_METHODS max')

    def test_DICT_OR_METHODS_not_found(self):
        my_exception = "maybe"
        with self.assertRaises(Exception) as context:
            _ = FuzzyMachine.DICT_OR_METHODS['maybe']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test DICT_OR_METHODS not found")

    def test_DICT_CONNECTORS_and(self):
        self.assertEqual(FuzzyMachine.DICT_CONNECTORS[Connections.AND],
                         '&',
                         msg='Test DICT_CONNECTORSS and')

    def test_DICT_CONNECTORS_or(self):
        self.assertEqual(FuzzyMachine.DICT_CONNECTORS[Connections.OR],
                         '|',
                         msg='Test DICT_CONNECTORS or')

    def test_DICT_CONNECTORS_not_found(self):
        my_exception = "maybe"
        with self.assertRaises(Exception) as context:
            _ = FuzzyMachine.DICT_CONNECTORS['maybe']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test DICT_CONNECTORS not found")

    def test_create_FuzzyController_1(self):
        my_machine = FuzzyMachine()

        self.assertEqual(dict(), my_machine.inputs, msg='Test inputs')
        self.assertEqual(dict(), my_machine.outputs, msg='Test outputs')
        self.assertEqual(list(), my_machine.rules, msg='Test rules')
        self.assertIsNone(my_machine.controller, msg='Test controller')
        self.assertIsNone(my_machine.simulator, msg='Test simulator')

    def test_create_FuzzyController_2(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_system = systemService.system

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

        my_input_2 = my_system.inputs[2]
        my_range_2 = my_input_2.range

        my_input_3 = my_system.inputs[3]
        my_range_3 = my_input_3.range

        my_output = my_system.outputs[1]
        my_range = my_output.range

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

        my_inputs = {'Distance': distance,
                     'Slope': slope,
                     'Depth': depth}

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

        my_outputs = {'output1': output1}

        my_rules = [ctrl.Rule(antecedent=(distance['Near'] & (~depth['Deep'])),
                              consequent=(output1['Lagoon'] % 1.0),
                              and_func=np.fmin, or_func=np.fmax)]

        my_controller = ctrl.ControlSystem(my_rules)
        my_simulator = ctrl.ControlSystemSimulation(my_controller)
        my_f_controller = FuzzyMachine(my_inputs,
                                       my_outputs,
                                       my_rules,
                                       my_controller,
                                       my_simulator)

        self.assertEqual(my_inputs, my_f_controller.inputs,
                         msg='Test inputs')
        self.assertEqual(my_outputs, my_f_controller.outputs,
                         msg='Test outputs')
        self.assertEqual(my_rules, my_f_controller.rules,
                         msg='Test rules')
        self.assertEqual(my_controller, my_f_controller.controller,
                         msg='Test controller')
        self.assertEqual(my_simulator, my_f_controller.simulator,
                         msg='Test simulator')

    def test_property_inputs(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_inputs = {'Distance': distance,
                     'Slope': slope,
                     'Depth': depth}

        my_f_controller = FuzzyMachine()
        my_f_controller.inputs = my_inputs
        self.assertEqual(my_inputs, my_f_controller.inputs,
                         msg='Test inputs')

    def test_property_inputs_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O parâmetro não é um dicionário!"
        with self.assertRaises(Exception) as context:
            my_f_controller.inputs = 10

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 1')

    def test_property_inputs_exception_2(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O nome do antecedente não é uma string!"
        with self.assertRaises(Exception) as context:
            my_f_controller.inputs = {10: 10}

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 2')

    def test_property_inputs_exception_3(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Antecedent!"
        with self.assertRaises(Exception) as context:
            my_f_controller.inputs = {'distance': 10}

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 3')

    def test_add_input(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

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

        my_inputs = {'Distance': distance}

        my_f_controller = FuzzyMachine()
        my_f_controller.add_input('Distance', distance)
        self.assertEqual(my_inputs, my_f_controller.inputs,
                         msg='Test inputs')

    def test_add_input_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O nome do antecedente não é uma string!"
        with self.assertRaises(Exception) as context:
            my_f_controller.add_input(10, 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 1')

    def test_add_input_exception_2(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Antecedent!"
        with self.assertRaises(Exception) as context:
            my_f_controller.add_input('Distance', 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 2')

    def test_property_outputs(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_outputs = {'output1': output1}

        my_f_controller = FuzzyMachine()
        my_f_controller.outputs = my_outputs
        self.assertEqual(my_outputs, my_f_controller.outputs,
                         msg='Test outputs')

    def test_property_outputs_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O parâmetro não é um dicionário!"
        with self.assertRaises(Exception) as context:
            my_f_controller.outputs = 10

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_outputs_exception_2(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O nome do consequente não é uma string!"
        with self.assertRaises(Exception) as context:
            my_f_controller.outputs = {10: 10}

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_property_outputs_exception_3(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Consequent!"
        with self.assertRaises(Exception) as context:
            my_f_controller.outputs = {'distance': 10}

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 3')

    def test_add_output(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_outputs = {'output1': output1}

        my_f_controller = FuzzyMachine()
        my_f_controller.add_output('output1', output1)
        self.assertEqual(my_outputs, my_f_controller.outputs,
                         msg='Test add_output')

    def test_add_output_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O nome do consequente não é uma string!"
        with self.assertRaises(Exception) as context:
            my_f_controller.add_output(10, 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 1')

    def test_add_output_exception_2(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Consequent!"
        with self.assertRaises(Exception) as context:
            my_f_controller.add_output('Distance', 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 2')

    def test_property_rules(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_system = systemService.system

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

        my_input_2 = my_system.inputs[2]
        my_range_2 = my_input_2.range

        my_input_3 = my_system.inputs[3]
        my_range_3 = my_input_3.range

        my_output = my_system.outputs[1]
        my_range = my_output.range

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

        my_rule = ctrl.Rule(antecedent=(distance['Near'] & (~depth['Deep'])),
                            consequent=(output1['Lagoon'] % 1.0),
                            and_func=np.fmin, or_func=np.fmax)

        my_f_controller = FuzzyMachine()
        my_f_controller.rules = [my_rule]

        self.assertEqual([my_rule], my_f_controller.rules, msg='Test rules')

    def test_property_rules_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_f_controller.rules = 10

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rules exception 1')

    def test_property_rules_exception_2(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Rule!"
        with self.assertRaises(Exception) as context:
            my_f_controller.rules = [10]

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rules exception 2')

    def test_add_rule(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
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

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_system = systemService.system

        my_input_1 = my_system.inputs[1]
        my_range_1 = my_input_1.range

        my_input_2 = my_system.inputs[2]
        my_range_2 = my_input_2.range

        my_input_3 = my_system.inputs[3]
        my_range_3 = my_input_3.range

        my_output = my_system.outputs[1]
        my_range = my_output.range

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

        my_rule = ctrl.Rule(antecedent=(distance['Near'] & (~depth['Deep'])),
                            consequent=(output1['Lagoon'] % 1.0),
                            and_func=np.fmin, or_func=np.fmax)

        my_f_controller = FuzzyMachine()
        my_f_controller.add_rule(my_rule)

        self.assertEqual(my_rule, my_f_controller.rules,
                         msg='Test add_rule')

    def test_add_rule_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = "O valor não é uma instância da classe Rule!"
        with self.assertRaises(Exception) as context:
            my_f_controller.add_rule(10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_rule exception 1')

    def test_property_controller(self):
        my_controller = ctrl.ControlSystem()
        my_f_controller = FuzzyMachine()
        my_f_controller.controller = my_controller
        self.assertEqual(my_controller, my_f_controller.controller,
                         msg='Test controller')

    def test_property_controller_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = ("O parâmetro não é uma instância da classe "
                        "ControlSystem!")
        with self.assertRaises(Exception) as context:
            my_f_controller.controller = 10

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property controller exception 1')

    def test_property_simulator(self):
        my_controller = ctrl.ControlSystem()
        my_simulator = ctrl.ControlSystemSimulation(my_controller)
        my_f_controller = FuzzyMachine()
        my_f_controller.simulator = my_simulator
        self.assertEqual(my_simulator, my_f_controller.simulator,
                         msg='Test simulator')

    def test_property_simulator_exception_1(self):
        my_f_controller = FuzzyMachine()
        my_exception = ("O parâmetro não é uma instância da classe "
                        "ControlSystemSimulation!")
        with self.assertRaises(Exception) as context:
            my_f_controller.simulator = 10

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property simulator exception 1')
