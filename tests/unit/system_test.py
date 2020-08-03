"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.System import System
from continentalfuzzy.domain.definition.AggMethods import AggMethods
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.definition.ImpMethods import ImpMethods
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.OrMethods import OrMethods
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.domain.variable.Output import Output
from continentalfuzzy.service.InputService import InputService
from continentalfuzzy.service.OutputService import OutputService
from continentalfuzzy.service.SystemService import SystemService


class SystemTest(unittest.TestCase):
    def test_MAX_NUM_OUTPUTS(self):
        self.assertEqual(1, System.MAX_NUM_OUTPUTS,
                         msg='Test MAX_NUM_OUTPUTS')

    def test_create_system_1(self):
        my_system = System()

        self.assertIsNone(my_system.name, msg='Test name')
        self.assertIsNone(my_system.filename, msg='Test filename')
        self.assertIsNone(my_system.type, msg='Test type')
        self.assertIsNone(my_system.version, msg='Test version')
        self.assertIsNone(my_system.num_inputs, msg='Test inputs')
        self.assertIsNone(my_system.num_outputs, msg='Test outputs')
        self.assertIsNone(my_system.num_rules, msg='Test rules')
        self.assertIsNone(my_system.and_method, msg='Test and_method')
        self.assertIsNone(my_system.or_method, msg='Test or_method')
        self.assertIsNone(my_system.imp_method, msg='Test imp_method')
        self.assertIsNone(my_system.agg_method, msg='Test agg_method')
        self.assertIsNone(my_system.defuzz_method, msg='Test defuzz_method')
        self.assertEqual(dict(), my_system.inputs, msg='Test inputs')
        self.assertEqual(dict(), my_system.outputs, msg='Test outputs')
        self.assertEqual(list(), my_system.rules, msg='Test rules')

    def test_create_system_2(self):
        # MF 1
        my_trimf_name = "Near"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        my_i_name = "Distance"
        my_i_range = [0, 10]
        my_i_num_mfs = 1
        my_i_mfs = {1: my_trimf}

        # MF 2
        my_gaussmf_name = "Lagoon"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        my_o_name = "output"
        my_o_range = [0, 10]
        my_o_num_mfs = 1
        my_o_mfs = {1: my_gaussmf}

        # Rule input
        my_r_i_name = 'Distance'
        my_r_i_mf = 'Near'
        my_r_i_var_not = True
        my_rule_inputs = [RuleInput(my_r_i_name, my_r_i_mf, my_r_i_var_not)]

        # Rule output
        my_r_o_name = 'output'
        my_r_o_mf = 'Lagoon'
        my_rule_outputs = [RuleOutput(my_r_o_name, my_r_o_mf)]

        # Rule
        my_r_name = 'rule 1'
        my_r_weight = 0.8
        my_r_connection = Connections.AND

        my_name = 'EnvironmentMamdani'
        my_filename = 'test.fis'
        my_type = ControllerType.mamdani
        my_version = '2.0'
        my_num_inputs = 1
        my_num_outputs = 1
        my_num_rules = 1
        my_and_method = AndMethods.min
        my_or_method = OrMethods.max
        my_imp_method = ImpMethods.min
        my_agg_method = AggMethods.max
        my_defuzz_method = DefuzzMethods.centroid
        my_input = {1: Input(my_i_name,
                             my_i_range,
                             my_i_num_mfs,
                             my_i_mfs)}
        my_output = {1: Output(my_o_name,
                               my_o_range,
                               my_o_num_mfs,
                               my_o_mfs)}
        my_rule = [Rule(my_r_name,
                        my_r_weight,
                        my_r_connection,
                        my_rule_inputs,
                        my_rule_outputs)]
        my_system = System(my_name,
                           my_filename,
                           my_type,
                           my_version,
                           my_num_inputs,
                           my_num_outputs,
                           my_num_rules,
                           my_and_method,
                           my_or_method,
                           my_imp_method,
                           my_agg_method,
                           my_defuzz_method,
                           my_input,
                           my_output,
                           my_rule)

        self.assertEqual(my_name, my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(my_type, my_system.type,
                         msg='Test type')
        self.assertEqual(my_version, my_system.version, msg='Test version')
        self.assertEqual(my_num_inputs, my_system.num_inputs,
                         msg='Test inputs')
        self.assertEqual(my_num_outputs, my_system.num_outputs,
                         msg='Test outputs')
        self.assertEqual(my_num_rules, my_system.num_rules, msg='Test rules')
        self.assertEqual(my_and_method, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(my_or_method, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(my_imp_method, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(my_agg_method, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(my_defuzz_method, my_system.defuzz_method,
                         msg='Test defuzz_method')
        self.assertEqual(my_input, my_system.inputs, msg='Test inputs')
        self.assertEqual(my_output, my_system.outputs, msg='Test outputs')
        self.assertEqual(my_rule, my_system.rules, msg='Test rules')

    def test_property_name(self):
        my_system = System()
        my_name = 'test name'
        my_system.name = my_name

        self.assertEqual(my_name, my_system.name, msg='Test name')

    def test_property_name_exception(self):
        my_system = System()
        my_name = [10, 12]
        my_exception = "O nome não é uma String!"
        with self.assertRaises(Exception) as context:
            my_system.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception')

    def test_property_filename(self):
        my_system = System()
        my_filename = 'test filename'
        my_system.filename = my_filename

        self.assertEqual(my_filename, my_system.filename, msg='Test filename')

    def test_property_filename_exception(self):
        my_system = System()
        my_filename = [10, 12]
        my_exception = "O caminho do arquivo .fis. não é uma String!"
        with self.assertRaises(Exception) as context:
            my_system.filename = my_filename

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property filename exception')

    def test_property_type(self):
        my_system = System()
        my_type = ControllerType.mamdani
        my_system.type = my_type

        self.assertEqual(my_type, my_system.type, msg='Test type')

    def test_property_type_exception(self):
        my_system = System()
        my_type = '1982'
        my_exception = ("O tipo de inferência não é uma instância da classe "
                        "ControllerType!")
        with self.assertRaises(Exception) as context:
            my_system.type = my_type

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property type exception')

    def test_property_version(self):
        my_system = System()
        my_version = '2.00'
        my_system.version = my_version

        self.assertEqual(my_version, my_system.version, msg='Test version')

    def test_property_version_exception(self):
        my_system = System()
        my_version = 2.00
        my_exception = ("A versão da biblioteca fuzzy do Matlab não é uma "
                        "String!")
        with self.assertRaises(Exception) as context:
            my_system.version = my_version

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property version exception')

    def test_property_num_inputs(self):
        my_system = System()
        my_num_inputs = 5
        my_system.num_inputs = my_num_inputs

        self.assertEqual(my_num_inputs, my_system.num_inputs,
                         msg='Test num_inputs')

    def test_property_num_inputs_exception(self):
        my_system = System()
        my_num_inputs = 10.7
        my_exception = ("O número de antecedentes do Sistema Fuzzy não é um "
                        "número inteiro!")
        with self.assertRaises(Exception) as context:
            my_system.num_inputs = my_num_inputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property num_inputs exception')

    def test_property_num_outputs(self):
        my_system = System()
        my_num_outputs = 1
        my_system.num_outputs = my_num_outputs

        self.assertEqual(my_num_outputs, my_system.num_outputs,
                         msg='Test num_outputs')

    def test_property_num_outputs_exception_1(self):
        my_system = System()
        my_num_outputs = 10
        my_exception = ("Número máximo de consequentes é "
                        f"{System.MAX_NUM_OUTPUTS}, número informado "
                        f"é {my_num_outputs}!")
        with self.assertRaises(Exception) as context:
            my_system.num_outputs = my_num_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property num_outputs exception 1')

    def test_property_num_outputs_exception_2(self):
        my_system = System()
        my_num_outputs = 'a'
        my_exception = ("O número de consequentes do Sistema Fuzzy não é um "
                        "número inteiro!")
        with self.assertRaises(Exception) as context:
            my_system.num_outputs = my_num_outputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property num_outputs exception 2')

    def test_property_num_rules(self):
        my_system = System()
        my_num_rules = 25
        my_system.num_rules = my_num_rules

        self.assertEqual(my_num_rules, my_system.num_rules,
                         msg='Test num_rules')

    def test_property_num_rules_exception(self):
        my_system = System()
        my_num_rules = 10.7
        my_exception = ("O número de regras do Sistema Fuzzy não é um "
                        "número inteiro!")
        with self.assertRaises(Exception) as context:
            my_system.num_rules = my_num_rules

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property num_rules exception')

    def test_property_and_method(self):
        my_system = System()
        my_and_method = AndMethods.min
        my_system.and_method = my_and_method

        self.assertEqual(my_and_method, my_system.and_method,
                         msg='Test and_method')

    def test_property_and_method_exception(self):
        my_system = System()
        my_and_method = 'variogram'
        my_exception = ("O método AND fuzzy não é uma instância da classe "
                        "ANDMethods!")

        with self.assertRaises(Exception) as context:
            my_system.and_method = my_and_method

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property and_method exception')

    def test_property_or_method(self):
        my_system = System()
        my_or_method = OrMethods.max
        my_system.or_method = my_or_method

        self.assertEqual(my_or_method, my_system.or_method,
                         msg='Test or_method')

    def test_property_or_method_exception(self):
        my_system = System()
        my_or_method = 'variogram'
        my_exception = ("O método OR fuzzy não é uma instância da classe "
                        "ORMethods!")

        with self.assertRaises(Exception) as context:
            my_system.or_method = my_or_method

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property or_method exception')

    def test_property_imp_method(self):
        my_system = System()
        my_imp_method = ImpMethods.min
        my_system.imp_method = my_imp_method

        self.assertEqual(my_imp_method, my_system.imp_method,
                         msg='Test imp_method')

    def test_property_imp_method_exception(self):
        my_system = System()
        my_imp_method = 'variogram'
        my_exception = ("O método de implicação não é uma instância da classe "
                        "ImpMethods!")

        with self.assertRaises(Exception) as context:
            my_system.imp_method = my_imp_method

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property imp_method exception')

    def test_property_agg_method(self):
        my_system = System()
        my_agg_method = AggMethods.max
        my_system.agg_method = my_agg_method

        self.assertEqual(my_agg_method, my_system.agg_method,
                         msg='Test agg_method')

    def test_property_agg_method_exception(self):
        my_system = System()
        my_agg_method = 'variogram'
        my_exception = ("O método de agregação não é uma instância da classe "
                        "AggMethods!")

        with self.assertRaises(Exception) as context:
            my_system.agg_method = my_agg_method

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property agg_method exception')

    def test_property_defuzz_method(self):
        my_system = System()
        my_defuzz_method = DefuzzMethods.centroid
        my_system.defuzz_method = my_defuzz_method

        self.assertEqual(my_defuzz_method, my_system.defuzz_method,
                         msg='Test defuzz_method')

    def test_property_defuzz_method_exception(self):
        my_system = System()
        my_defuzz_method = 'variogram'
        my_exception = ("O método de defuzzificação não é uma instância da "
                        "classe DefuzzMethods!")

        with self.assertRaises(Exception) as context:
            my_system.defuzz_method = my_defuzz_method

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property defuzz_method exception')

    def test_property_inputs(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_input = InputService()
        my_entry_2 = ["Name='Slope'",
                      "Range=[0 0.05]",
                      "NumMFs=3",
                      "MF1='Low':'trapmf',[-0.01 -0.005 0.001 0.002]",
                      "MF2='Medium':'trapmf',[0.0015 0.0025 0.004 0.005]",
                      "MF3='High':'trapmf',[0.004 0.005 0.06 0.07]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_2)
        my_input_2 = my_input.input

        my_input = InputService()
        my_entry_3 = ["Name='Depth'",
                      "Range=[0 3000]",
                      "NumMFs=3",
                      "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                      "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                      "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_3)
        my_input_3 = my_input.input

        my_dict = {1: my_input_1,
                   2: my_input_2,
                   3: my_input_3}

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
        my_system = systemService.system
        my_system.inputs = my_dict

        # Input_1
        self.assertEqual('Distance', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 1], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(2, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('Near', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual(0.2, my_system.inputs.get(1).mfs.get(1).sigma,
                         msg='Test input 1 mf 1 sigma')
        self.assertEqual(0, my_system.inputs.get(1).mfs.get(1).mean,
                         msg='Test input 1 mf 1 mean')

        self.assertEqual('Far', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 2 function')
        self.assertEqual(0.42, my_system.inputs.get(1).mfs.get(2).sigma,
                         msg='Test input 1 mf 2 sigma')
        self.assertEqual(1, my_system.inputs.get(1).mfs.get(2).mean,
                         msg='Test input 1 mf 2 mean')

        # Input_2
        self.assertEqual('Slope', my_system.inputs.get(2).name,
                         msg='Test input 2 name')
        self.assertEqual([0, 0.05], my_system.inputs.get(2).range,
                         msg='Test input 2 range')
        self.assertEqual(3, my_system.inputs.get(2).num_mfs,
                         msg='Test input 2 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(2).var_type,
                         msg='Test input 2 var_type')

        self.assertEqual('Low', my_system.inputs.get(2).mfs.get(1).name,
                         msg='Test input 2 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(1).function,
                         msg='Test input 2 mf 1 function')
        self.assertEqual([-0.01, -0.005, 0.001, 0.002],
                         my_system.inputs.get(2).mfs.get(1).abcd,
                         msg='Test input 2 mf 1 abcd')

        self.assertEqual('Medium', my_system.inputs.get(2).mfs.get(2).name,
                         msg='Test input 2 mf 2 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(2).function,
                         msg='Test input 2 mf 2 function')
        self.assertEqual([0.0015, 0.0025, 0.004, 0.005],
                         my_system.inputs.get(2).mfs.get(2).abcd,
                         msg='Test input 2 mf 2 abcd')

        self.assertEqual('High', my_system.inputs.get(2).mfs.get(3).name,
                         msg='Test input 2 mf 3 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(3).function,
                         msg='Test input 2 mf 3 function')
        self.assertEqual([0.004, 0.005, 0.06, 0.07],
                         my_system.inputs.get(2).mfs.get(3).abcd,
                         msg='Test input 2 mf 3 abcd')

        # # Input_3
        self.assertEqual('Depth', my_system.inputs.get(3).name,
                         msg='Test input 3 name')
        self.assertEqual([0, 3000], my_system.inputs.get(3).range,
                         msg='Test input 3 range')
        self.assertEqual(3, my_system.inputs.get(3).num_mfs,
                         msg='Test input 3 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(3).var_type,
                         msg='Test input 3 var_type')

        self.assertEqual('Shallow', my_system.inputs.get(3).mfs.get(1).name,
                         msg='Test input 3 mf 1 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(3).mfs.get(1).function,
                         msg='Test input 3 mf 1 function')
        self.assertEqual(10.3, my_system.inputs.get(3).mfs.get(1).sigma1,
                         msg='Test input 3 mf 1 sigma1')
        self.assertEqual(-56.35, my_system.inputs.get(3).mfs.get(1).mean1,
                         msg='Test input 3 mf 1 mean1')
        self.assertEqual(6.65, my_system.inputs.get(3).mfs.get(1).sigma2,
                         msg='Test input 3 mf 1 sigma2')
        self.assertEqual(2.384, my_system.inputs.get(3).mfs.get(1).mean2,
                         msg='Test input 3 mf 1 mean2')

        self.assertEqual('Medium', my_system.inputs.get(3).mfs.get(2).name,
                         msg='Test input 3 mf 2 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(3).mfs.get(2).function,
                         msg='Test input 3 mf 2 function')
        self.assertEqual(18.6, my_system.inputs.get(3).mfs.get(2).sigma1,
                         msg='Test input 3 mf 1 sigma1')
        self.assertEqual(62.2, my_system.inputs.get(3).mfs.get(2).mean1,
                         msg='Test input 3 mf 1 mean1')
        self.assertEqual(17.81, my_system.inputs.get(3).mfs.get(2).sigma2,
                         msg='Test input 3 mf 1 sigma2')
        self.assertEqual(84.92, my_system.inputs.get(3).mfs.get(2).mean2,
                         msg='Test input 3 mf 1 mean2')

        self.assertEqual('Deep', my_system.inputs.get(3).mfs.get(3).name,
                         msg='Test input 3 mf 3 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(3).mfs.get(3).function,
                         msg='Test input 3 mf 3 function')
        self.assertEqual(77.9, my_system.inputs.get(3).mfs.get(3).sigma1,
                         msg='Test input 3 mf 3 sigma1')
        self.assertEqual(260, my_system.inputs.get(3).mfs.get(3).mean1,
                         msg='Test input 3 mf 3 mean1')
        self.assertEqual(28.3, my_system.inputs.get(3).mfs.get(3).sigma2,
                         msg='Test input 3 mf 3 sigma2')
        self.assertEqual(3042, my_system.inputs.get(3).mfs.get(3).mean2,
                         msg='Test input 3 mf 3 mean2')

    def test_property_inputs_exception_1(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_dict = {1: my_input_1}

        my_system = System()

        my_exception = "O número de antecedentes não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 1')

    def test_property_inputs_exception_2(self):
        my_dict = {}

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
        my_system = systemService.system

        my_exception = ("Quantidade de antecedentes é diferente da informada "
                        "no bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 2')

    def test_property_inputs_exception_3(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_dict = {1: my_input_1}

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
        my_system = systemService.system

        my_exception = ("Quantidade de antecedentes é diferente da informada "
                        "no bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 3')

    def test_property_inputs_exception_4(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_dict = {1: my_input_1,
                   2: my_input_1,
                   3: my_input_1,
                   4: my_input_1}

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
        my_system = systemService.system

        my_exception = ("Quantidade de antecedentes é diferente da informada "
                        "no bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 4')

    def test_property_inputs_exception_5(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_dict = {1: my_input_1,
                   2: my_input_1,
                   3: 10}

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
        my_system = systemService.system

        my_exception = "O valor não é uma instância da classe Input!"
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 5')

    def test_property_inputs_exception_6(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_dict = {1: my_input_1,
                   2: my_input_1,
                   'a': my_input_1}

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
        my_system = systemService.system

        my_exception = "A chave não é uma número inteiro!"
        with self.assertRaises(Exception) as context:
            my_system.inputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property inputs exception 6')

    def test_add_input_1(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

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
        my_system = systemService.system
        my_system.add_input(1, my_input_1)

        # Input_1
        self.assertEqual('Distance', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 1], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(2, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('Near', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual(0.2, my_system.inputs.get(1).mfs.get(1).sigma,
                         msg='Test input 1 mf 1 sigma')
        self.assertEqual(0, my_system.inputs.get(1).mfs.get(1).mean,
                         msg='Test input 1 mf 1 mean')

        self.assertEqual('Far', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 2 function')
        self.assertEqual(0.42, my_system.inputs.get(1).mfs.get(2).sigma,
                         msg='Test input 1 mf 2 sigma')
        self.assertEqual(1, my_system.inputs.get(1).mfs.get(2).mean,
                         msg='Test input 1 mf 2 mean')

    def test_add_input_exception_1(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

        my_system = System()

        my_exception = "O número de antecedentes não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.add_input(1, my_input_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 1')

    def test_add_input_exception_2(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

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
        my_system = systemService.system
        my_system.add_input(1, my_input_1)

        my_exception = "Número do antecedente 1 já cadastrado!"
        with self.assertRaises(Exception) as context:
            my_system.add_input(1, my_input_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 2')

    def test_add_input_exception_3(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

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
        my_system = systemService.system

        my_system.add_input(1, my_input_1)
        my_system.add_input(2, my_input_1)
        my_system.add_input(3, my_input_1)

        my_exception = "Não é possível adicionar mais antecedentes!"
        with self.assertRaises(Exception) as context:
            my_system.add_input(4, my_input_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 3')

    def test_add_input_exception_4(self):
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
        my_system = systemService.system

        my_exception = "O valor não é uma instância da classe Input!"
        with self.assertRaises(Exception) as context:
            my_system.add_input(1, 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 4')

    def test_add_input_exception_5(self):
        my_input = InputService()
        my_entry_1 = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]
        my_input.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_input_1 = my_input.input

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
        my_system = systemService.system

        my_exception = "O número do antecedente não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_system.add_input(['a'], my_input_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_input exception 5')

    def test_property_outputs(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

        my_dict = {1: my_output_1}

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
        my_system = systemService.system
        my_system.outputs = my_dict

        # Output_1
        self.assertEqual('output1', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([1, 4], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(4, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('Lagoon', my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(1).sigma,
                         msg='Test output 1 mf 1 sigma')
        self.assertEqual(1, my_system.outputs.get(1).mfs.get(1).mean,
                         msg='Test output 1 mf 1 mean')

        self.assertEqual('Reef', my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 2 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(2).sigma,
                         msg='Test output 1 mf 2 sigma')
        self.assertEqual(2, my_system.outputs.get(1).mfs.get(2).mean,
                         msg='Test output 1 mf 2 mean')

        self.assertEqual('ForeReef', my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 3 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(3).sigma,
                         msg='Test output 1 mf 3 sigma')
        self.assertEqual(3, my_system.outputs.get(1).mfs.get(3).mean,
                         msg='Test output 1 mf 3 mean')

        self.assertEqual('Basin', my_system.outputs.get(1).mfs.get(4).name,
                         msg='Test output 1 mf 4 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(4).function,
                         msg='Test output 1 mf 4 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(4).sigma,
                         msg='Test output 1 mf 4 sigma')
        self.assertEqual(4, my_system.outputs.get(1).mfs.get(4).mean,
                         msg='Test output 1 mf 4 mean')

    def test_property_outputs_exception_1(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

        my_dict = {1: my_output_1}

        my_system = System()

        my_exception = "O número de consequentes não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.outputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 1')

    def test_property_outputs_exception_2(self):
        my_dict = {}

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
        my_system = systemService.system

        my_exception = ("Quantidade de consequentes é diferente da informada "
                        "no bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.outputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 2')

    def test_property_outputs_exception_3(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

        my_dict = {1: my_output_1,
                   2: my_output_1}

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
        my_system = systemService.system

        my_exception = ("Quantidade de consequentes é diferente da informada "
                        "no bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.outputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 3')

    def test_property_outputs_exception_4(self):
        my_dict = {1: 10}

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
        my_system = systemService.system

        my_exception = "O valor não é uma instância da classe Output!"
        with self.assertRaises(Exception) as context:
            my_system.outputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 4')

    def test_property_outputs_exception_5(self):
        my_dict = {'a': 10}

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
        my_system = systemService.system

        my_exception = "A chave não é uma número inteiro!"
        with self.assertRaises(Exception) as context:
            my_system.outputs = my_dict

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property outputs exception 5')

    def test_add_output(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

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
        my_system = systemService.system
        my_system.add_output(1, my_output_1)

        # Output_1
        self.assertEqual('output1', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([1, 4], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(4, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('Lagoon', my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(1).sigma,
                         msg='Test output 1 mf 1 sigma')
        self.assertEqual(1, my_system.outputs.get(1).mfs.get(1).mean,
                         msg='Test output 1 mf 1 mean')

        self.assertEqual('Reef', my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 2 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(2).sigma,
                         msg='Test output 1 mf 2 sigma')
        self.assertEqual(2, my_system.outputs.get(1).mfs.get(2).mean,
                         msg='Test output 1 mf 2 mean')

        self.assertEqual('ForeReef', my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 3 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(3).sigma,
                         msg='Test output 1 mf 3 sigma')
        self.assertEqual(3, my_system.outputs.get(1).mfs.get(3).mean,
                         msg='Test output 1 mf 3 mean')

        self.assertEqual('Basin', my_system.outputs.get(1).mfs.get(4).name,
                         msg='Test output 1 mf 4 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(4).function,
                         msg='Test output 1 mf 4 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(4).sigma,
                         msg='Test output 1 mf 4 sigma')
        self.assertEqual(4, my_system.outputs.get(1).mfs.get(4).mean,
                         msg='Test output 1 mf 4 mean')

    def test_add_output_exception_1(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

        my_system = System()

        my_exception = "O número de consequentes não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.add_output(1, my_output_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 1')

    def test_add_output_exception_2(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

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
        my_system = systemService.system
        my_system._System__num_outputs = 2

        my_system.add_output(1, my_output_1)

        my_exception = "Número do consequente 1 já cadastrado!"
        with self.assertRaises(Exception) as context:
            my_system.add_output(1, my_output_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 2')

    def test_add_output_exception_3(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

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
        my_system = systemService.system

        my_system.add_output(1, my_output_1)

        my_exception = "Não é possível adicionar mais consequentes!"
        with self.assertRaises(Exception) as context:
            my_system.add_output(2, my_output_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 3')

    def test_add_output_exception_4(self):
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
        my_system = systemService.system

        my_exception = "O valor não é uma instância da classe Output!"
        with self.assertRaises(Exception) as context:
            my_system.add_output(1, 10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 4')

    def test_add_output_exception_5(self):
        my_output = OutputService()
        my_entry_1 = ["Name='output1'",
                      "Range=[1 4]",
                      "NumMFs=4",
                      "MF1='Lagoon':'gaussmf',[0.4247 1]",
                      "MF2='Reef':'gaussmf',[0.4247 2]",
                      "MF3='ForeReef':'gaussmf',[0.4247 3]",
                      "MF4='Basin':'gaussmf',[0.4247 4]"]
        my_output.create_from_fis_block(ControllerType.mamdani, my_entry_1)
        my_output_1 = my_output.output

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
        my_system = systemService.system

        my_exception = "O número do consequente não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_system.add_output(['a'], my_output_1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_output exception 5')

    def test_property_rules(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=2',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]

        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        # *** Rule 2
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Far'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Shallow'
        my_rule_input2.var_not = False

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_output_list1 = [my_rule_output1]

        my_rule2 = Rule()
        my_rule2.name = 'Rule_2'
        my_rule2.weight = 0.9
        my_rule2.connection = Connections.OR
        my_rule2.inputs = my_input_list1
        my_rule2.outputs = my_output_list1

        my_rules_list = [my_rule1, my_rule2]

        my_system.rules = my_rules_list

        # *** Rule 1
        self.assertEqual('Rule_1', my_system.rules[0].name,
                         msg='Test rule 1 name')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule 1 weight')
        self.assertEqual(Connections.OR, my_system.rules[0].connection,
                         msg='Test rule 1 connection')

        # Input rule 1
        self.assertEqual('Distance', my_system.rules[0].inputs[0].name,
                         msg='Test rule 1 distance name')
        self.assertEqual('Near', my_system.rules[0].inputs[0].mf,
                         msg='Test rule 1 distance mf')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule 1 distance var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule 1 distance var_type')

        # Input rule 2
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule 1 depth name')
        self.assertEqual('Deep', my_system.rules[0].inputs[1].mf,
                         msg='Test rule 1 depth mf')
        self.assertEqual(True, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule 1 depth var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule 1 depth var_type')

        # Output rule 1
        self.assertEqual('output1', my_system.rules[0].outputs[0].name,
                         msg='Test rule 1 output1 name')
        self.assertEqual('Lagoon', my_system.rules[0].outputs[0].mf,
                         msg='Test rule 1 output1 mf')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule 1 output1 var_type')

        # *** Rule 2
        self.assertEqual('Rule_2', my_system.rules[1].name,
                         msg='Test rule 2 name')
        self.assertEqual(0.9, my_system.rules[1].weight,
                         msg='Test rule 2 weight')
        self.assertEqual(Connections.OR, my_system.rules[1].connection,
                         msg='Test rule 2 connection')

        # Input rule 1
        self.assertEqual('Distance', my_system.rules[1].inputs[0].name,
                         msg='Test rule 2 distance name')
        self.assertEqual('Far', my_system.rules[1].inputs[0].mf,
                         msg='Test rule 2 distance mf')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule 2 distance var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule 2 distance var_type')

        # Input rule 2
        self.assertEqual('Depth', my_system.rules[1].inputs[1].name,
                         msg='Test rule 2 depth name')
        self.assertEqual('Shallow', my_system.rules[1].inputs[1].mf,
                         msg='Test rule 2 depth mf')
        self.assertEqual(False, my_system.rules[1].inputs[1].var_not,
                         msg='Test rule 2 depth var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[1].var_type,
                         msg='Test rule 2 depth var_type')

        # Output rule 1
        self.assertEqual('output1', my_system.rules[1].outputs[0].name,
                         msg='Test rule 2 output1 name')
        self.assertEqual('Reef', my_system.rules[1].outputs[0].mf,
                         msg='Test rule 2 output1 mf')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule 2 output1 var_type')

    def test_property_rules_exception_1(self):
        my_system = System()

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        # *** Rule 2
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Far'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Shallow'
        my_rule_input2.var_not = False

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Reef'

        my_output_list1 = [my_rule_output1]

        my_rule2 = Rule()
        my_rule2.name = 'Rule_2'
        my_rule2.weight = 0.9
        my_rule2.connection = Connections.OR
        my_rule2.inputs = my_input_list1
        my_rule2.outputs = my_output_list1

        my_rules_list = [my_rule1, my_rule2]

        my_exception = "O número de regras não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.rules = my_rules_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rules exception 1')

    def test_property_rules_exception_2(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=2',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]

        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        my_rules_list = [my_rule1]

        my_exception = ("Quantidade de regras é diferente da informada no "
                        "bloco do sistema!")
        with self.assertRaises(Exception) as context:
            my_system.rules = my_rules_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rules exception 2')

    def test_property_rules_exception_3(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=2',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]

        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        my_rules_list = [my_rule1, {'I dont': 'know'}]

        my_exception = "O valor não é uma instância da classe Rule!"
        with self.assertRaises(Exception) as context:
            my_system.rules = my_rules_list

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property rules exception 3')

    def test_add_rule(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=2',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]

        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        my_system.add_rule(my_rule1)

        # *** Rule 1
        self.assertEqual('Rule_1', my_system.rules[0].name,
                         msg='Test rule 1 name')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule 1 weight')
        self.assertEqual(Connections.OR, my_system.rules[0].connection,
                         msg='Test rule 1 connection')

        # Input rule 1
        self.assertEqual('Distance', my_system.rules[0].inputs[0].name,
                         msg='Test rule 1 distance name')
        self.assertEqual('Near', my_system.rules[0].inputs[0].mf,
                         msg='Test rule 1 distance mf')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule 1 distance var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule 1 distance var_type')

        # Input rule 2
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule 1 depth name')
        self.assertEqual('Deep', my_system.rules[0].inputs[1].mf,
                         msg='Test rule 1 depth mf')
        self.assertEqual(True, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule 1 depth var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule 1 depth var_type')

        # Output rule 1
        self.assertEqual('output1', my_system.rules[0].outputs[0].name,
                         msg='Test rule 1 output1 name')
        self.assertEqual('Lagoon', my_system.rules[0].outputs[0].mf,
                         msg='Test rule 1 output1 mf')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule 1 output1 var_type')

    def test_add_rule_exception_1(self):
        my_system = System()

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        my_exception = "O número de regras não foi informado!"
        with self.assertRaises(Exception) as context:
            my_system.add_rule(my_rule1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_rule exception 1')

    def test_add_rule_exception_2(self):
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
        my_system = systemService.system

        # *** Rule 1
        my_rule_input1 = RuleInput()
        my_rule_input1.name = 'Distance'
        my_rule_input1.mf = 'Near'
        my_rule_input1.var_not = False

        my_rule_input2 = RuleInput()
        my_rule_input2.name = 'Depth'
        my_rule_input2.mf = 'Deep'
        my_rule_input2.var_not = True

        my_input_list1 = [my_rule_input1, my_rule_input2]

        my_rule_output1 = RuleOutput()
        my_rule_output1.name = 'output1'
        my_rule_output1.mf = 'Lagoon'

        my_output_list1 = [my_rule_output1]

        my_rule1 = Rule()
        my_rule1.name = 'Rule_1'
        my_rule1.weight = 1.0
        my_rule1.connection = Connections.OR
        my_rule1.inputs = my_input_list1
        my_rule1.outputs = my_output_list1

        my_system.add_rule(my_rule1)

        my_exception = "Não é possível adicionar mais regras!"
        with self.assertRaises(Exception) as context:
            my_system.add_rule(my_rule1)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_rule exception 2')

    def test_add_rule_exception_3(self):
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
        my_system = systemService.system

        my_exception = "O valor não é uma instância da classe Rule!"
        with self.assertRaises(Exception) as context:
            my_system.add_rule(10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test add_rule exception 3')
