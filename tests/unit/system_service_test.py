"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.domain.definition.AggMethods import AggMethods
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.definition.ImpMethods import ImpMethods
from continentalfuzzy.domain.definition.OrMethods import OrMethods
from continentalfuzzy.service.SystemService import SystemService


class SystemTest(unittest.TestCase):
    def test_create_system_from_list_mamdani(self):
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

        self.assertEqual('EnvironmentMamdani', my_system.name,
                         msg='Test name')
        self.assertEqual(ControllerType.mamdani, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.min, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.max, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.centroid, my_system.defuzz_method,
                         msg='Test defuzz_method')

    def test_create_system_from_list_mamdani_exception_1(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='tsukamoto'",
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

        my_exception = "O controlador tsukamoto não foi implementado!"

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 1')

    def test_create_system_from_list_mamdani_exception_2(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='other'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]

        my_exception = ("O método AND other não foi implementado para "
                        "inferência Mamdani!")

        systemService = SystemService()

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 2')

    def test_create_system_from_list_mamdani_exception_3(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='other'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()

        my_exception = ("O método OR other não foi implementado para "
                        "inferência Mamdani!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 3')

    def test_create_system_from_list_mamdani_exception_4(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='other'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()

        my_exception = ("O método de implicação other não foi implementado "
                        "para inferência Mamdani!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 4')

    def test_create_system_from_list_mamdani_exception_5(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='other'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()

        my_exception = ("O método de agregação other não foi implementado "
                        "para inferência Mamdani!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 5')

    def test_create_system_from_list_mamdani_exception_6(self):
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
                       "DefuzzMethod='other'"]
        systemService = SystemService()

        my_exception = ("O método de defuzzificação other não foi "
                        "implementado para inferência Mamdani!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 6')

    def test_create_system_from_list_sugeno(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='prod'",
                       "AggMethod='sum'",
                       "DefuzzMethod='wtaver'"]

        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system

        self.assertEqual('EnvironmentSugeno', my_system.name,
                         msg='Test name')
        self.assertEqual(ControllerType.sugeno, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.prod, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.sum, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.wtaver, my_system.defuzz_method,
                         msg='Test defuzz_method')

    def test_create_system_from_list_sugeno_exception_1(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='tsukamoto'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='prod'",
                       "AggMethod='sum'",
                       "DefuzzMethod='wtaver'"]

        systemService = SystemService()

        my_exception = "O controlador tsukamoto não foi implementado!"

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 1')

    def test_create_system_from_list_sugeno_exception_2(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='other'",
                       "OrMethod='max'",
                       "ImpMethod='prod'",
                       "AggMethod='sum'",
                       "DefuzzMethod='wtaver'"]

        my_exception = ("O método AND other não foi implementado para "
                        "inferência Sugeno!")

        systemService = SystemService()

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 2')

    def test_create_system_from_list_sugeno_exception_3(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='other'",
                       "ImpMethod='prod'",
                       "AggMethod='sum'",
                       "DefuzzMethod='wtaver'"]
        systemService = SystemService()

        my_exception = ("O método OR other não foi implementado para "
                        "inferência Sugeno!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 3')

    def test_create_system_from_list_sugeno_exception_4(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='other'",
                       "AggMethod='sum'",
                       "DefuzzMethod='wtaver'"]
        systemService = SystemService()

        my_exception = ("O método de implicação other não foi implementado "
                        "para inferência Sugeno!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 4')

    def test_create_system_from_list_sugeno_exception_5(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='prod'",
                       "AggMethod='other'",
                       "DefuzzMethod='wtaver'"]
        systemService = SystemService()

        my_exception = ("O método de agregação other não foi implementado "
                        "para inferência Sugeno!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 5')

    def test_create_system_from_list_sugeno_exception_6(self):
        my_sys_list = ["Name='EnvironmentSugeno'",
                       "Type='sugeno'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='prod'",
                       "AggMethod='sum'",
                       "DefuzzMethod='other'"]
        systemService = SystemService()

        my_exception = ("O método de defuzzificação other não foi "
                        "implementado para inferência Sugeno!")

        with self.assertRaises(Exception) as context:
            systemService.create_system_from_list(my_sys_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_system_from_list exception 6')

    def test_valid_system(self):
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
        my_system.filename = 'filename.fis'
        systemService.valid_system()

        self.assertEqual('EnvironmentMamdani', my_system.name,
                         msg='Test name')
        self.assertEqual('filename.fis', my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.mamdani, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.min, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.max, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.centroid, my_system.defuzz_method,
                         msg='Test defuzz_method')

    def test_valid_system_exception_name(self):
        my_sys_list = ["Type='mamdani'",
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

        my_exception = "O nome não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception name')

    def test_valid_system_exception_filename(self):
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

        my_exception = "O nome do arquivo não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception name')

    def test_valid_system_exception_type(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
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
        my_system.filename = 'filename.fis'

        my_exception = "O tipo não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception type')

    def test_valid_system_exception_version(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
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
        my_system.filename = 'filename.fis'

        my_exception = "A versão não foi informada!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception version')

    def test_valid_system_exception_num_inputs(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
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
        my_system.filename = 'filename.fis'

        my_exception = "O número de antecedentes não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception num_inputs')

    def test_valid_system_exception_num_outputs(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O número de consequentes não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception num_outputs')

    def test_valid_system_exception_num_rules(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O número de regras não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception num_rules')

    def test_valid_system_exception_and_method(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O método AND fuzzy não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception and_method')

    def test_valid_system_exception_or_method(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "ImpMethod='min'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O método OR fuzzy não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception or_method')

    def test_valid_system_exception_imp_method(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "AggMethod='max'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O método de implicação não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception imp_method')

    def test_valid_system_exception_agg_method(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "DefuzzMethod='centroid'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O método de agregação não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception agg_method')

    def test_valid_system_exception_defuzz_method(self):
        my_sys_list = ["Name='EnvironmentMamdani'",
                       "Type='mamdani'",
                       'Version=2.0',
                       'NumInputs=3',
                       'NumOutputs=1',
                       'NumRules=4',
                       "AndMethod='min'",
                       "OrMethod='max'",
                       "ImpMethod='min'",
                       "AggMethod='max'"]
        systemService = SystemService()
        systemService.create_system_from_list(my_sys_list)
        my_system = systemService.system
        my_system.filename = 'filename.fis'

        my_exception = "O método de defuzzificação não foi informado!"

        with self.assertRaises(Exception) as context:
            systemService.valid_system()

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test valid_system exception defuzz_method')

    def test_valid_system_exception_1(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3, 1 (1) : 1',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        systemService.create_rules_from_list(my_list)

        my_exception = "O caminho do arquivo não foi informado!"
        with self.assertRaises(Exception) as context:
            systemService.valid_import()
        self.assertEqual(my_exception, context.exception.args[0])

    def test_valid_system_exception_2(self):
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
        my_system.filename = "filename.fis"

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "Não foi importada a quantidade correta de antecedentes!"
        with self.assertRaises(Exception) as context:
            systemService.valid_import()
        self.assertEqual(my_exception, context.exception.args[0])

    def test_valid_system_exception_3(self):
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
        my_system.filename = "filename.fis"

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_exception = "Não foi importada a quantidade correta de consequentes!"
        with self.assertRaises(Exception) as context:
            systemService.valid_import()
        self.assertEqual(my_exception, context.exception.args[0])

    def test_valid_system_exception_4(self):
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
        my_system.filename = "filename.fis"

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "Não foi importada a quantidade correta de regras!"
        with self.assertRaises(Exception) as context:
            systemService.valid_import()
        self.assertEqual(my_exception, context.exception.args[0])

    def test_create_inputs_from_list(self):
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

    def test_create_inputs_from_list_exception_1(self):
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
                   ["Name='Depth'", 'Range=[0 3000]', 'NumMFs=3',
                    "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                    "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                    "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]]

        my_exception = ("Quantidade de antecedentes é diferente do número de "
                        "antecedentes informado no bloco System!")
        with self.assertRaises(Exception) as context:
            systemService.create_inputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_from_list exception 1')

    def test_create_inputs_from_list_exception_2(self):
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
                   'sdkf',
                   ["Name='Depth'", 'Range=[0 3000]', 'NumMFs=3',
                    "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                    "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                    "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]]

        my_exception = "Um dos itens não é um lista!"
        with self.assertRaises(Exception) as context:
            systemService.create_inputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_from_list exception 2')

    def test_create_inputs_from_list_exception_3(self):
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

        my_list = {'notnum': 1,
                   'entries': ["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
                               "MF1='Near':'gaussmf',[0.2 0]",
                               "MF2='Far':'gaussmf',[0.42 1]"]}

        my_exception = "O parâmetro não é um lista!"
        with self.assertRaises(Exception) as context:
            systemService.create_inputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_from_list exception 3')

    def test_create_inputs_from_list_exception_4(self):
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

        my_list = [[{1: 'input'},
                    "MF1='Near':'gaussmf',[0.2 0]",
                    "MF2='Far':'gaussmf',[0.42 1]"],
                   'sdkf',
                   ["Name='Depth'", 'Range=[0 3000]', 'NumMFs=3',
                    "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                    "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                    "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]]

        my_exception = "Um dos items da lista não é uma string!"
        with self.assertRaises(Exception) as context:
            systemService.create_inputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_from_list exception 4')

    def test_create_outputs_from_list(self):
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

        my_list = [["Name='output1'",
                    'Range=[1 4]',
                    'NumMFs=4',
                    "MF1='Lagoon':'gaussmf',[0.4247 1]",
                    "MF2='Reef':'gaussmf',[0.4247 2]",
                    "MF3='ForeReef':'gaussmf',[0.4247 3]",
                    "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_list)
        my_system = systemService.system

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

    def test_create_outputs_from_list_exception_1(self):
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
                   ["Name='Depth'", 'Range=[0 3000]', 'NumMFs=3',
                    "MF1='Shallow':'gauss2mf',[10.3 -56.35 6.65 2.384]",
                    "MF2='Medium':'gauss2mf',[18.6 62.2 17.81 84.92]",
                    "MF3='Deep':'gauss2mf',[77.9 260 28.3 3042]"]]

        my_exception = ("Quantidade de consequentes é diferente do número de "
                        "consequentes informado no bloco System!")
        with self.assertRaises(Exception) as context:
            systemService.create_outputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_from_list exception 1')

    def test_create_outputs_from_list_exception_2(self):
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

        my_exception = "O parâmetro não é um lista!"
        with self.assertRaises(Exception) as context:
            systemService.create_outputs_from_list(10)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_from_list exception 2')

    def test_create_outputs_from_list_exception_3(self):
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

        my_list = [[{1: 'name'}, 'Range=[0 1]', 'NumMFs=2',
                    "MF1='Near':'gaussmf',[0.2 0]",
                    "MF2='Far':'gaussmf',[0.42 1]"]]

        my_exception = "Um dos items da lista não é uma string!"
        with self.assertRaises(Exception) as context:
            systemService.create_outputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_from_list exception 3')

    def test_create_outputs_from_list_exception_4(self):
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

        my_list = [10]

        my_exception = "Um dos itens não é um lista!"
        with self.assertRaises(Exception) as context:
            systemService.create_outputs_from_list(my_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_from_list exception 4')

    def test_create_inputs_rule(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        r_inputs = systemService.create_inputs_rule(['1', '0', '-3'])

        self.assertEqual(2, len(r_inputs))

        self.assertEqual('Distance', r_inputs[0].name, msg='Rule input 1 name')
        self.assertEqual('antecedent', r_inputs[0].var_type,
                         msg='Rule input 1 var_type')
        self.assertEqual(False, r_inputs[0].var_not, msg='Rule input 1 var_not')
        self.assertEqual('Near', r_inputs[0].mf, msg='Rule input 1 mf')

        self.assertEqual('Depth', r_inputs[1].name, msg='Rule input 2 name')
        self.assertEqual('antecedent', r_inputs[1].var_type,
                         msg='Rule input 2 var_type')
        self.assertEqual(True, r_inputs[1].var_not, msg='Rule input 2 var_not')
        self.assertEqual('Deep', r_inputs[1].mf, msg='Rule input 2 mf')

    def test_create_inputs_rule_exception_1(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "O antecedente da regra não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            _ = systemService.create_inputs_rule(['a', '0', '-3'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_rule exception 1')

    def test_create_inputs_rule_exception_2(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "O antecedente número: 4, não foi cadastrado!"
        with self.assertRaises(Exception) as context:
            _ = systemService.create_inputs_rule(['1', '0', '-3', '1', '1'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_rule exception 2')

    def test_create_inputs_rule_exception_3(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = ("A função de pertinência 7 do antecedente Distance, "
                        "não foi cadastrada!")
        with self.assertRaises(Exception) as context:
            _ = systemService.create_inputs_rule(['7', '0', '-3'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_inputs_rule exception 3')

    def test_create_outputs_rule_1(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        r_outputs = systemService.create_outputs_rule(['1'])

        self.assertEqual(1, len(r_outputs))

        self.assertEqual('output1', r_outputs[0].name, msg='Test name')
        self.assertEqual('consequent', r_outputs[0].var_type,
                         msg='Test var_type')
        self.assertEqual('Lagoon', r_outputs[0].mf, msg='Test mf')

    def test_create_outputs_rule_2(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        r_outputs = systemService.create_outputs_rule(['0'])

        self.assertEqual(0, len(r_outputs), msg='Test rule output 0')

    def test_create_outputs_rule_exception_1(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "O consequente da regra não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            _ = systemService.create_outputs_rule(['a'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_rule exception 1')

    def test_create_outputs_rule_exception_2(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "O consequente número: 2, não foi cadastrado!"
        with self.assertRaises(Exception) as context:
            _ = systemService.create_outputs_rule(['1', '2'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_rule exception 2')

    def test_create_outputs_rule_exception_3(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = ("A função de pertinência 7 do consequente output1, "
                        "não foi cadastrada!")
        with self.assertRaises(Exception) as context:
            _ = systemService.create_outputs_rule(['7'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_rule exception 3')

    def test_create_outputs_rule_exception_4(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_exception = "O consequente da regra não pode ser negado!"
        with self.assertRaises(Exception) as context:
            _ = systemService.create_outputs_rule(['-1'])
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_outputs_rule exception 4')

    def test_create_rules_from_list(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3, 1 (1) : 1',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        systemService.create_rules_from_list(my_list)
        my_system = systemService.system

        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.AND, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(2, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('Distance', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('Near', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(True, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('output1', my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('Lagoon', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(2, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('Distance', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('Far', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual('Depth', my_system.rules[1].inputs[1].name,
                         msg='Test rule_2 input 2 name')
        self.assertEqual(False, my_system.rules[1].inputs[1].var_not,
                         msg='Test rule_2 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[1].var_type,
                         msg='Test rule_2 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[1].inputs[1].mf,
                         msg='Test rule_2 input 2 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('output1', my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('Reef', my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.AND, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(0.5, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(3, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('Distance', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('Far', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('Slope', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 2 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 2 var_type')
        self.assertEqual('High', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 2 mf')
        self.assertEqual('Depth', my_system.rules[2].inputs[2].name,
                         msg='Test rule_3 input 3 name')
        self.assertEqual(True, my_system.rules[2].inputs[2].var_not,
                         msg='Test rule_3 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[2].var_type,
                         msg='Test rule_3 input 3 var_type')
        self.assertEqual('Deep', my_system.rules[2].inputs[2].mf,
                         msg='Test rule_3 input 3 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('output1', my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('ForeReef', my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 var_type')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.OR, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(1, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('Depth', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('Deep', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('output1', my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('Basin', my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

    def test_create_rules_from_list_exception_1(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3 1, 1 (1) : 1',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        my_exception = ("Quantidade de antecedentes da regra é diferente do "
                        "número de antecedentes informado no bloco System!")
        with self.assertRaises(Exception) as context:
            systemService.create_rules_from_list(my_list)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_rules_from_list exception 1')

    def test_create_rules_from_list_exception_2(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3, 1 (1) : 1']

        my_exception = ("Quantidade de regras é diferente do número de regras "
                        "informado no bloco System!")
        with self.assertRaises(Exception) as context:
            systemService.create_rules_from_list(my_list)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_rules_from_list exception 2')

    def test_create_rules_from_list_exception_3(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3 , 1 1 (1) : 1',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        my_exception = ("Quantidade de consequentes da regra é diferente do "
                        "número de consequentes informado no bloco System!")
        with self.assertRaises(Exception) as context:
            systemService.create_rules_from_list(my_list)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_rules_from_list exception 3')

    def test_create_rules_from_list_exception_4(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3 , 1 (a) : 1',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        my_exception = "O peso do consequente da regra não é um número float!"
        with self.assertRaises(Exception) as context:
            systemService.create_rules_from_list(my_list)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_rules_from_list exception 4')

    def test_create_rules_from_list_exception_5(self):
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

        my_inputs = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=2',
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

        systemService.create_inputs_from_list(my_inputs)

        my_outputs = [["Name='output1'",
                       'Range=[1 4]',
                       'NumMFs=4',
                       "MF1='Lagoon':'gaussmf',[0.4247 1]",
                       "MF2='Reef':'gaussmf',[0.4247 2]",
                       "MF3='ForeReef':'gaussmf',[0.4247 3]",
                       "MF4='Basin':'gaussmf',[0.4247 4]"]]

        systemService.create_outputs_from_list(my_outputs)

        my_list = ['1 0 -3 , 1 (1) : 7',
                   '2 0 1, 2 (1) : 1',
                   '2 3 -3, 3 (0.5) : 1',
                   '0 0 3, 4 (1) : 2']

        my_exception = "O conector 7 da regra rule_1, não foi implementado!"
        with self.assertRaises(Exception) as context:
            systemService.create_rules_from_list(my_list)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create_rules_from_list exception 5')

    def test_import_file_1(self):
        my_filename = "tests/test_data/EnvironmentMamdani.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        # System
        self.assertEqual('EnvironmentMamdani', my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.mamdani, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.min, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.max, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.centroid, my_system.defuzz_method,
                         msg='Test defuzz_method')

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

        # Rules
        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.AND, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(2, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('Distance', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('Near', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(True, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('output1', my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('Lagoon', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(2, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('Distance', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('Far', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual('Depth', my_system.rules[1].inputs[1].name,
                         msg='Test rule_2 input 2 name')
        self.assertEqual(False, my_system.rules[1].inputs[1].var_not,
                         msg='Test rule_2 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[1].var_type,
                         msg='Test rule_2 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[1].inputs[1].mf,
                         msg='Test rule_2 input 2 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('output1', my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('Reef', my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.AND, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(1.0, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(3, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('Distance', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('Far', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('Slope', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 2 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 2 var_type')
        self.assertEqual('High', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 2 mf')
        self.assertEqual('Depth', my_system.rules[2].inputs[2].name,
                         msg='Test rule_3 input 3 name')
        self.assertEqual(True, my_system.rules[2].inputs[2].var_not,
                         msg='Test rule_3 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[2].var_type,
                         msg='Test rule_3 input 3 var_type')
        self.assertEqual('Deep', my_system.rules[2].inputs[2].mf,
                         msg='Test rule_3 input 3 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('output1', my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('ForeReef', my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 var_type')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.AND, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(1, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('Depth', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('Deep', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('output1', my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('Basin', my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

    def test_import_file_2(self):
        my_filename = "tests/test_data/Ramp.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        # System
        self.assertEqual('Ramp', my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.mamdani, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(14, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.min, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.max, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.centroid, my_system.defuzz_method,
                         msg='Test defuzz_method')

        # Input_1
        self.assertEqual('Climate', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 1], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(2, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('Arid', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([-0.1, -0.1, 0.5, 0.5],
                         my_system.inputs.get(1).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('Wet', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 2 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 2 function')
        self.assertEqual([0.5, 0.5, 1.1, 1.1],
                         my_system.inputs.get(1).mfs.get(2).abcd,
                         msg='Test input 1 mf 2 abcd')

        # Input_2
        self.assertEqual('Depth', my_system.inputs.get(2).name,
                         msg='Test input 2 name')
        self.assertEqual([0, 3000], my_system.inputs.get(2).range,
                         msg='Test input 2 range')
        self.assertEqual(3, my_system.inputs.get(2).num_mfs,
                         msg='Test input 2 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(2).var_type,
                         msg='Test input 2 var_type')

        self.assertEqual('Shallow', my_system.inputs.get(2).mfs.get(1).name,
                         msg='Test input 2 mf 1 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(1).function,
                         msg='Test input 2 mf 1 function')
        self.assertEqual(10.3, my_system.inputs.get(2).mfs.get(1).sigma1,
                         msg='Test input 2 mf 1 sigma1')
        self.assertEqual(-56.35, my_system.inputs.get(2).mfs.get(1).mean1,
                         msg='Test input 2 mf 1 mean1')
        self.assertEqual(6.65, my_system.inputs.get(2).mfs.get(1).sigma2,
                         msg='Test input 2 mf 1 sigma2')
        self.assertEqual(2.384, my_system.inputs.get(2).mfs.get(1).mean2,
                         msg='Test input 2 mf 1 mean2')

        self.assertEqual('Intermediary', my_system.inputs.get(2).mfs.get(2).name,
                         msg='Test input 2 mf 2 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(2).function,
                         msg='Test input 2 mf 2 function')
        self.assertEqual(18.6, my_system.inputs.get(2).mfs.get(2).sigma1,
                         msg='Test input 2 mf 2 sigma1')
        self.assertEqual(62.2, my_system.inputs.get(2).mfs.get(2).mean1,
                         msg='Test input 2 mf 2 mean1')
        self.assertEqual(17.81, my_system.inputs.get(2).mfs.get(2).sigma2,
                         msg='Test input 2 mf 2 sigma2')
        self.assertEqual(84.92, my_system.inputs.get(2).mfs.get(2).mean2,
                         msg='Test input 2 mf 2 mean2')

        self.assertEqual('Deep', my_system.inputs.get(2).mfs.get(3).name,
                         msg='Test input 2 mf 3 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(3).function,
                         msg='Test input 2 mf 3 function')
        self.assertEqual(77.9, my_system.inputs.get(2).mfs.get(3).sigma1,
                         msg='Test input 2 mf 3 sigma1')
        self.assertEqual(260, my_system.inputs.get(2).mfs.get(3).mean1,
                         msg='Test input 2 mf 3 mean1')
        self.assertEqual(28.3, my_system.inputs.get(2).mfs.get(3).sigma2,
                         msg='Test input 2 mf 3 sigma2')
        self.assertEqual(3042, my_system.inputs.get(2).mfs.get(3).mean2,
                         msg='Test input 2 mf 3 mean2')

        # Input_3
        self.assertEqual('WaveEnergy', my_system.inputs.get(3).name,
                         msg='Test input 3 name')
        self.assertEqual([0, 1], my_system.inputs.get(3).range,
                         msg='Test input 3 range')
        self.assertEqual(3, my_system.inputs.get(3).num_mfs,
                         msg='Test input 3 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(3).var_type,
                         msg='Test input 3 var_type')

        self.assertEqual('Low', my_system.inputs.get(3).mfs.get(1).name,
                         msg='Test input 3 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(1).function,
                         msg='Test input 3 mf 1 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(1).sigma,
                         msg='Test input 3 mf 1 sigma')
        self.assertEqual(0, my_system.inputs.get(3).mfs.get(1).mean,
                         msg='Test input 3 mf 1 mean')

        self.assertEqual('Moderate', my_system.inputs.get(3).mfs.get(2).name,
                         msg='Test input 3 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(2).function,
                         msg='Test input 3 mf 2 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(2).sigma,
                         msg='Test input 3 mf 1 sigma')
        self.assertEqual(0.5, my_system.inputs.get(3).mfs.get(2).mean,
                         msg='Test input 3 mf 1 mean')

        self.assertEqual('High', my_system.inputs.get(3).mfs.get(3).name,
                         msg='Test input 3 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(3).function,
                         msg='Test input 3 mf 3 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(3).sigma,
                         msg='Test input 3 mf 3 sigma')
        self.assertEqual(1, my_system.inputs.get(3).mfs.get(3).mean,
                         msg='Test input 3 mf 3 mean')

        # Output_1
        self.assertEqual('FaciesAssociation', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([0, 12], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(13, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('ClayeyEmbayment',
                         my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(1).sigma,
                         msg='Test output 1 mf 1 sigma')
        self.assertEqual(0, my_system.outputs.get(1).mfs.get(1).mean,
                         msg='Test output 1 mf 1 mean')

        self.assertEqual('ShallowPlain',
                         my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 2 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(2).sigma,
                         msg='Test output 1 mf 2 sigma')
        self.assertEqual(1, my_system.outputs.get(1).mfs.get(2).mean,
                         msg='Test output 1 mf 2 mean')

        self.assertEqual('Cape',
                         my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 3 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(3).sigma,
                         msg='Test output 1 mf 3 sigma')
        self.assertEqual(2, my_system.outputs.get(1).mfs.get(3).mean,
                         msg='Test output 1 mf 3 mean')

        self.assertEqual('LowEnergyUnderwaterPlain',
                         my_system.outputs.get(1).mfs.get(4).name,
                         msg='Test output 1 mf 4 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(4).function,
                         msg='Test output 1 mf 4 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(4).sigma,
                         msg='Test output 1 mf 4 sigma')
        self.assertEqual(3, my_system.outputs.get(1).mfs.get(4).mean,
                         msg='Test output 1 mf 4 mean')

        self.assertEqual('StromatoliteEmbayment',
                         my_system.outputs.get(1).mfs.get(5).name,
                         msg='Test output 1 mf 5 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(5).function,
                         msg='Test output 1 mf 5 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(5).sigma,
                         msg='Test output 1 mf 5 sigma')
        self.assertEqual(4, my_system.outputs.get(1).mfs.get(5).mean,
                         msg='Test output 1 mf 5 mean')

        self.assertEqual('HighEnergyIntraclastic',
                         my_system.outputs.get(1).mfs.get(6).name,
                         msg='Test output 1 mf 6 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(6).function,
                         msg='Test output 1 mf 6 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(6).sigma,
                         msg='Test output 1 mf 6 sigma')
        self.assertEqual(5, my_system.outputs.get(1).mfs.get(6).mean,
                         msg='Test output 1 mf 6 mean')

        self.assertEqual('AridSubCoastal',
                         my_system.outputs.get(1).mfs.get(7).name,
                         msg='Test output 1 mf 7 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(7).function,
                         msg='Test output 1 mf 7 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(7).sigma,
                         msg='Test output 1 mf 7 sigma')
        self.assertEqual(6, my_system.outputs.get(1).mfs.get(7).mean,
                         msg='Test output 1 mf 7 mean')

        self.assertEqual('ModerateEnergyIntraclastic',
                         my_system.outputs.get(1).mfs.get(8).name,
                         msg='Test output 1 mf 8 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(8).function,
                         msg='Test output 1 mf 8 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(8).sigma,
                         msg='Test output 1 mf 8 sigma')
        self.assertEqual(7, my_system.outputs.get(1).mfs.get(8).mean,
                         msg='Test output 1 mf 8 mean')

        self.assertEqual('Reef',
                         my_system.outputs.get(1).mfs.get(9).name,
                         msg='Test output 1 mf 9 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(9).function,
                         msg='Test output 1 mf 9 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(9).sigma,
                         msg='Test output 1 mf 9 sigma')
        self.assertEqual(8, my_system.outputs.get(1).mfs.get(9).mean,
                         msg='Test output 1 mf 9 mean')

        self.assertEqual('InterpatchesPlain',
                         my_system.outputs.get(1).mfs.get(10).name,
                         msg='Test output 1 mf 10 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(10).function,
                         msg='Test output 1 mf 10 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(10).sigma,
                         msg='Test output 1 mf 10 sigma')
        self.assertEqual(9, my_system.outputs.get(1).mfs.get(10).mean,
                         msg='Test output 1 mf 10 mean')

        self.assertEqual('ClayeyClasticDeposit',
                         my_system.outputs.get(1).mfs.get(11).name,
                         msg='Test output 1 mf 11 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(11).function,
                         msg='Test output 1 mf 11 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(11).sigma,
                         msg='Test output 1 mf 11 sigma')
        self.assertEqual(10, my_system.outputs.get(1).mfs.get(11).mean,
                         msg='Test output 1 mf 11 mean')

        self.assertEqual('WetSubCoastal',
                         my_system.outputs.get(1).mfs.get(12).name,
                         msg='Test output 1 mf 12 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(12).function,
                         msg='Test output 1 mf 12 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(12).sigma,
                         msg='Test output 1 mf 12 sigma')
        self.assertEqual(11, my_system.outputs.get(1).mfs.get(12).mean,
                         msg='Test output 1 mf 12 mean')

        self.assertEqual('LaminiteRamp',
                         my_system.outputs.get(1).mfs.get(13).name,
                         msg='Test output 1 mf 13 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(13).function,
                         msg='Test output 1 mf 13 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(13).sigma,
                         msg='Test output 1 mf 13 sigma')
        self.assertEqual(12, my_system.outputs.get(1).mfs.get(13).mean,
                         msg='Test output 1 mf 13 mean')

        # Rules
        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.AND, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(3, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('Climate', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(False, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[0].inputs[2].name,
                         msg='Test rule_1 input 3 name')
        self.assertEqual(False, my_system.rules[0].inputs[2].var_not,
                         msg='Test rule_1 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[2].var_type,
                         msg='Test rule_1 input 3 var_type')
        self.assertEqual('Low', my_system.rules[0].inputs[2].mf,
                         msg='Test rule_1 input 3 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('LaminiteRamp', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(3, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('Climate', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual('Depth', my_system.rules[1].inputs[1].name,
                         msg='Test rule_2 input 2 name')
        self.assertEqual(False, my_system.rules[1].inputs[1].var_not,
                         msg='Test rule_2 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[1].var_type,
                         msg='Test rule_2 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[1].inputs[1].mf,
                         msg='Test rule_2 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[1].inputs[2].name,
                         msg='Test rule_2 input 3 name')
        self.assertEqual(False, my_system.rules[1].inputs[2].var_not,
                         msg='Test rule_2 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[2].var_type,
                         msg='Test rule_2 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[1].inputs[2].mf,
                         msg='Test rule_2 input 3 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('ModerateEnergyIntraclastic',
                         my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.AND, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(1.0, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(3, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('Climate', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('Depth', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 2 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[2].inputs[2].name,
                         msg='Test rule_3 input 3 name')
        self.assertEqual(False, my_system.rules[2].inputs[2].var_not,
                         msg='Test rule_3 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[2].var_type,
                         msg='Test rule_3 input 3 var_type')
        self.assertEqual('High', my_system.rules[2].inputs[2].mf,
                         msg='Test rule_3 input 3 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('Cape',
                         my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 mf')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.AND, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(3, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('Climate', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual('Depth', my_system.rules[3].inputs[1].name,
                         msg='Test rule_4 input 2 name')
        self.assertEqual(False, my_system.rules[3].inputs[1].var_not,
                         msg='Test rule_4 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[1].var_type,
                         msg='Test rule_4 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[3].inputs[1].mf,
                         msg='Test rule_4 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[3].inputs[2].name,
                         msg='Test rule_4 input 3 name')
        self.assertEqual(False, my_system.rules[3].inputs[2].var_not,
                         msg='Test rule_4 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[2].var_type,
                         msg='Test rule_4 input 3 var_type')
        self.assertEqual('Low', my_system.rules[3].inputs[2].mf,
                         msg='Test rule_4 input 3 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

        self.assertEqual('rule_5', my_system.rules[4].name,
                         msg='Test rule_5 name')
        self.assertEqual(Connections.AND, my_system.rules[4].connection,
                         msg='Test rule_5 connection')
        self.assertEqual(1.0, my_system.rules[4].weight,
                         msg='Test rule_5 weight')
        self.assertEqual(3, len(my_system.rules[4].inputs),
                         msg='Test rule_5 inputs')
        self.assertEqual('Climate', my_system.rules[4].inputs[0].name,
                         msg='Test rule_5 input 1 name')
        self.assertEqual(False, my_system.rules[4].inputs[0].var_not,
                         msg='Test rule_5 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[0].var_type,
                         msg='Test rule_5 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[4].inputs[0].mf,
                         msg='Test rule_5 input 1 mf')
        self.assertEqual('Depth', my_system.rules[4].inputs[1].name,
                         msg='Test rule_5 input 2 name')
        self.assertEqual(False, my_system.rules[4].inputs[1].var_not,
                         msg='Test rule_5 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[1].var_type,
                         msg='Test rule_5 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[4].inputs[1].mf,
                         msg='Test rule_5 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[4].inputs[2].name,
                         msg='Test rule_5 input 3 name')
        self.assertEqual(False, my_system.rules[4].inputs[2].var_not,
                         msg='Test rule_5 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[2].var_type,
                         msg='Test rule_5 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[4].inputs[2].mf,
                         msg='Test rule_5 input 3 mf')
        self.assertEqual(1, len(my_system.rules[4].outputs),
                         msg='Test rule_5 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[4].outputs[0].name,
                         msg='Test rule_5 output 1 name')
        self.assertEqual('consequent', my_system.rules[4].outputs[0].var_type,
                         msg='Test rule_5 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[4].outputs[0].mf,
                         msg='Test rule_5 output 1 mf')

        self.assertEqual('rule_6', my_system.rules[5].name,
                         msg='Test rule_6 name')
        self.assertEqual(Connections.AND, my_system.rules[5].connection,
                         msg='Test rule_6 connection')
        self.assertEqual(1.0, my_system.rules[5].weight,
                         msg='Test rule_6 weight')
        self.assertEqual(3, len(my_system.rules[5].inputs),
                         msg='Test rule_6 inputs')
        self.assertEqual('Climate', my_system.rules[5].inputs[0].name,
                         msg='Test rule_6 input 1 name')
        self.assertEqual(False, my_system.rules[5].inputs[0].var_not,
                         msg='Test rule_6 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[0].var_type,
                         msg='Test rule_6 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[5].inputs[0].mf,
                         msg='Test rule_6 input 1 mf')
        self.assertEqual('Depth', my_system.rules[5].inputs[1].name,
                         msg='Test rule_6 input 2 name')
        self.assertEqual(False, my_system.rules[5].inputs[1].var_not,
                         msg='Test rule_6 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[1].var_type,
                         msg='Test rule_6 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[5].inputs[1].mf,
                         msg='Test rule_6 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[5].inputs[2].name,
                         msg='Test rule_6 input 3 name')
        self.assertEqual(False, my_system.rules[5].inputs[2].var_not,
                         msg='Test rule_6 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[2].var_type,
                         msg='Test rule_6 input 3 var_type')
        self.assertEqual('High', my_system.rules[5].inputs[2].mf,
                         msg='Test rule_6 input 3 mf')
        self.assertEqual(1, len(my_system.rules[5].outputs),
                         msg='Test rule_6 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[5].outputs[0].name,
                         msg='Test rule_6 output 1 name')
        self.assertEqual('consequent', my_system.rules[5].outputs[0].var_type,
                         msg='Test rule_6 output 1 var_type')
        self.assertEqual('HighEnergyIntraclastic',
                         my_system.rules[5].outputs[0].mf,
                         msg='Test rule_6 output 1 mf')

        self.assertEqual('rule_7', my_system.rules[6].name,
                         msg='Test rule_7 name')
        self.assertEqual(Connections.AND, my_system.rules[6].connection,
                         msg='Test rule_7 connection')
        self.assertEqual(1.0, my_system.rules[6].weight,
                         msg='Test rule_7 weight')
        self.assertEqual(3, len(my_system.rules[6].inputs),
                         msg='Test rule_7 inputs')
        self.assertEqual('Climate', my_system.rules[6].inputs[0].name,
                         msg='Test rule_7 input 1 name')
        self.assertEqual(False, my_system.rules[6].inputs[0].var_not,
                         msg='Test rule_7 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[0].var_type,
                         msg='Test rule_7 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[6].inputs[0].mf,
                         msg='Test rule_7 input 1 mf')
        self.assertEqual('Depth', my_system.rules[6].inputs[1].name,
                         msg='Test rule_7 input 2 name')
        self.assertEqual(False, my_system.rules[6].inputs[1].var_not,
                         msg='Test rule_7 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[1].var_type,
                         msg='Test rule_7 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[6].inputs[1].mf,
                         msg='Test rule_7 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[6].inputs[2].name,
                         msg='Test rule_7 input 3 name')
        self.assertEqual(False, my_system.rules[6].inputs[2].var_not,
                         msg='Test rule_7 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[2].var_type,
                         msg='Test rule_7 input 3 var_type')
        self.assertEqual('Low', my_system.rules[6].inputs[2].mf,
                         msg='Test rule_7 input 3 mf')
        self.assertEqual(1, len(my_system.rules[6].outputs),
                         msg='Test rule_7 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[6].outputs[0].name,
                         msg='Test rule_7 output 1 name')
        self.assertEqual('consequent', my_system.rules[6].outputs[0].var_type,
                         msg='Test rule_7 output 1 var_type')
        self.assertEqual('AridSubCoastal',
                         my_system.rules[6].outputs[0].mf,
                         msg='Test rule_7 output 1 mf')

        self.assertEqual('rule_8', my_system.rules[7].name,
                         msg='Test rule_8 name')
        self.assertEqual(Connections.AND, my_system.rules[7].connection,
                         msg='Test rule_8 connection')
        self.assertEqual(1.0, my_system.rules[7].weight,
                         msg='Test rule_8 weight')
        self.assertEqual(3, len(my_system.rules[7].inputs),
                         msg='Test rule_8 inputs')
        self.assertEqual('Climate', my_system.rules[7].inputs[0].name,
                         msg='Test rule_8 input 1 name')
        self.assertEqual(False, my_system.rules[7].inputs[0].var_not,
                         msg='Test rule_8 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[0].var_type,
                         msg='Test rule_8 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[7].inputs[0].mf,
                         msg='Test rule_8 input 1 mf')
        self.assertEqual('Depth', my_system.rules[7].inputs[1].name,
                         msg='Test rule_8 input 2 name')
        self.assertEqual(False, my_system.rules[7].inputs[1].var_not,
                         msg='Test rule_8 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[1].var_type,
                         msg='Test rule_8 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[7].inputs[1].mf,
                         msg='Test rule_8 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[7].inputs[2].name,
                         msg='Test rule_8 input 3 name')
        self.assertEqual(False, my_system.rules[7].inputs[2].var_not,
                         msg='Test rule_8 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[2].var_type,
                         msg='Test rule_8 input 3 var_type')
        self.assertEqual('Low', my_system.rules[7].inputs[2].mf,
                         msg='Test rule_8 input 3 mf')
        self.assertEqual(1, len(my_system.rules[7].outputs),
                         msg='Test rule_8 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[7].outputs[0].name,
                         msg='Test rule_8 output 1 name')
        self.assertEqual('consequent', my_system.rules[7].outputs[0].var_type,
                         msg='Test rule_8 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[7].outputs[0].mf,
                         msg='Test rule_8 output 1 mf')

        self.assertEqual('rule_9', my_system.rules[8].name,
                         msg='Test rule_9 name')
        self.assertEqual(Connections.AND, my_system.rules[8].connection,
                         msg='Test rule_9 connection')
        self.assertEqual(1.0, my_system.rules[8].weight,
                         msg='Test rule_9 weight')
        self.assertEqual(3, len(my_system.rules[8].inputs),
                         msg='Test rule_9 inputs')
        self.assertEqual('Climate', my_system.rules[8].inputs[0].name,
                         msg='Test rule_9 input 1 name')
        self.assertEqual(False, my_system.rules[8].inputs[0].var_not,
                         msg='Test rule_9 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[0].var_type,
                         msg='Test rule_9 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[8].inputs[0].mf,
                         msg='Test rule_9 input 1 mf')
        self.assertEqual('Depth', my_system.rules[8].inputs[1].name,
                         msg='Test rule_9 input 2 name')
        self.assertEqual(False, my_system.rules[8].inputs[1].var_not,
                         msg='Test rule_9 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[1].var_type,
                         msg='Test rule_9 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[8].inputs[1].mf,
                         msg='Test rule_9 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[8].inputs[2].name,
                         msg='Test rule_9 input 3 name')
        self.assertEqual(False, my_system.rules[8].inputs[2].var_not,
                         msg='Test rule_9 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[2].var_type,
                         msg='Test rule_9 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[8].inputs[2].mf,
                         msg='Test rule_9 input 3 mf')
        self.assertEqual(1, len(my_system.rules[8].outputs),
                         msg='Test rule_9 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[8].outputs[0].name,
                         msg='Test rule_9 output 1 name')
        self.assertEqual('consequent', my_system.rules[8].outputs[0].var_type,
                         msg='Test rule_9 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[8].outputs[0].mf,
                         msg='Test rule_9 output 1 mf')

        self.assertEqual('rule_10', my_system.rules[9].name,
                         msg='Test rule_10 name')
        self.assertEqual(Connections.AND, my_system.rules[9].connection,
                         msg='Test rule_10 connection')
        self.assertEqual(1.0, my_system.rules[9].weight,
                         msg='Test rule_10 weight')
        self.assertEqual(3, len(my_system.rules[9].inputs),
                         msg='Test rule_10 inputs')
        self.assertEqual('Climate', my_system.rules[9].inputs[0].name,
                         msg='Test rule_10 input 1 name')
        self.assertEqual(False, my_system.rules[9].inputs[0].var_not,
                         msg='Test rule_10 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[0].var_type,
                         msg='Test rule_10 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[9].inputs[0].mf,
                         msg='Test rule_10 input 1 mf')
        self.assertEqual('Depth', my_system.rules[9].inputs[1].name,
                         msg='Test rule_10 input 2 name')
        self.assertEqual(False, my_system.rules[9].inputs[1].var_not,
                         msg='Test rule_10 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[1].var_type,
                         msg='Test rule_10 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[9].inputs[1].mf,
                         msg='Test rule_10 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[9].inputs[2].name,
                         msg='Test rule_10 input 3 name')
        self.assertEqual(False, my_system.rules[9].inputs[2].var_not,
                         msg='Test rule_10 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[2].var_type,
                         msg='Test rule_10 input 3 var_type')
        self.assertEqual('High', my_system.rules[9].inputs[2].mf,
                         msg='Test rule_10 input 3 mf')
        self.assertEqual(1, len(my_system.rules[9].outputs),
                         msg='Test rule_10 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[9].outputs[0].name,
                         msg='Test rule_10 output 1 name')
        self.assertEqual('consequent', my_system.rules[9].outputs[0].var_type,
                         msg='Test rule_10 output 1 var_type')
        self.assertEqual('Cape',
                         my_system.rules[9].outputs[0].mf,
                         msg='Test rule_10 output 1 mf')

        self.assertEqual('rule_11', my_system.rules[10].name,
                         msg='Test rule_11 name')
        self.assertEqual(Connections.AND, my_system.rules[10].connection,
                         msg='Test rule_11 connection')
        self.assertEqual(1.0, my_system.rules[10].weight,
                         msg='Test rule_11 weight')
        self.assertEqual(3, len(my_system.rules[10].inputs),
                         msg='Test rule_11 inputs')
        self.assertEqual('Climate', my_system.rules[10].inputs[0].name,
                         msg='Test rule_11 input 1 name')
        self.assertEqual(False, my_system.rules[10].inputs[0].var_not,
                         msg='Test rule_11 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[0].var_type,
                         msg='Test rule_11 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[10].inputs[0].mf,
                         msg='Test rule_11 input 1 mf')
        self.assertEqual('Depth', my_system.rules[10].inputs[1].name,
                         msg='Test rule_11 input 2 name')
        self.assertEqual(False, my_system.rules[10].inputs[1].var_not,
                         msg='Test rule_11 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[1].var_type,
                         msg='Test rule_11 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[10].inputs[1].mf,
                         msg='Test rule_11 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[10].inputs[2].name,
                         msg='Test rule_11 input 3 name')
        self.assertEqual(False, my_system.rules[10].inputs[2].var_not,
                         msg='Test rule_11 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[2].var_type,
                         msg='Test rule_11 input 3 var_type')
        self.assertEqual('Low', my_system.rules[10].inputs[2].mf,
                         msg='Test rule_11 input 3 mf')
        self.assertEqual(1, len(my_system.rules[10].outputs),
                         msg='Test rule_11 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[10].outputs[0].name,
                         msg='Test rule_11 output 1 name')
        self.assertEqual('consequent', my_system.rules[10].outputs[0].var_type,
                         msg='Test rule_11 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[10].outputs[0].mf,
                         msg='Test rule_11 output 1 mf')

        self.assertEqual('rule_12', my_system.rules[11].name,
                         msg='Test rule_12 name')
        self.assertEqual(Connections.AND, my_system.rules[11].connection,
                         msg='Test rule_12 connection')
        self.assertEqual(1.0, my_system.rules[11].weight,
                         msg='Test rule_12 weight')
        self.assertEqual(3, len(my_system.rules[11].inputs),
                         msg='Test rule_12 inputs')
        self.assertEqual('Climate', my_system.rules[11].inputs[0].name,
                         msg='Test rule_12 input 1 name')
        self.assertEqual(False, my_system.rules[11].inputs[0].var_not,
                         msg='Test rule_12 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[0].var_type,
                         msg='Test rule_12 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[11].inputs[0].mf,
                         msg='Test rule_12 input 1 mf')
        self.assertEqual('Depth', my_system.rules[11].inputs[1].name,
                         msg='Test rule_12 input 2 name')
        self.assertEqual(False, my_system.rules[11].inputs[1].var_not,
                         msg='Test rule_12 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[1].var_type,
                         msg='Test rule_12 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[11].inputs[1].mf,
                         msg='Test rule_12 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[11].inputs[2].name,
                         msg='Test rule_12 input 3 name')
        self.assertEqual(False, my_system.rules[11].inputs[2].var_not,
                         msg='Test rule_12 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[2].var_type,
                         msg='Test rule_12 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[11].inputs[2].mf,
                         msg='Test rule_12 input 3 mf')
        self.assertEqual(1, len(my_system.rules[11].outputs),
                         msg='Test rule_12 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[11].outputs[0].name,
                         msg='Test rule_12 output 1 name')
        self.assertEqual('consequent', my_system.rules[11].outputs[0].var_type,
                         msg='Test rule_12 output 1 var_type')
        self.assertEqual('LaminiteRamp',
                         my_system.rules[11].outputs[0].mf,
                         msg='Test rule_12 output 1 mf')

        self.assertEqual('rule_13', my_system.rules[12].name,
                         msg='Test rule_13 name')
        self.assertEqual(Connections.AND, my_system.rules[12].connection,
                         msg='Test rule_13 connection')
        self.assertEqual(1.0, my_system.rules[12].weight,
                         msg='Test rule_13 weight')
        self.assertEqual(3, len(my_system.rules[12].inputs),
                         msg='Test rule_13 inputs')
        self.assertEqual('Climate', my_system.rules[12].inputs[0].name,
                         msg='Test rule_13 input 1 name')
        self.assertEqual(False, my_system.rules[12].inputs[0].var_not,
                         msg='Test rule_13 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[0].var_type,
                         msg='Test rule_13 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[12].inputs[0].mf,
                         msg='Test rule_13 input 1 mf')
        self.assertEqual('Depth', my_system.rules[12].inputs[1].name,
                         msg='Test rule_13 input 2 name')
        self.assertEqual(False, my_system.rules[12].inputs[1].var_not,
                         msg='Test rule_13 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[1].var_type,
                         msg='Test rule_13 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[12].inputs[1].mf,
                         msg='Test rule_13 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[12].inputs[2].name,
                         msg='Test rule_13 input 3 name')
        self.assertEqual(False, my_system.rules[12].inputs[2].var_not,
                         msg='Test rule_13 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[2].var_type,
                         msg='Test rule_13 input 3 var_type')
        self.assertEqual('High', my_system.rules[12].inputs[2].mf,
                         msg='Test rule_13 input 3 mf')
        self.assertEqual(1, len(my_system.rules[12].outputs),
                         msg='Test rule_13 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[12].outputs[0].name,
                         msg='Test rule_13 output 1 name')
        self.assertEqual('consequent', my_system.rules[12].outputs[0].var_type,
                         msg='Test rule_13 output 1 var_type')
        self.assertEqual('Cape',
                         my_system.rules[12].outputs[0].mf,
                         msg='Test rule_13 output 1 mf')

        self.assertEqual('rule_14', my_system.rules[13].name,
                         msg='Test rule_14 name')
        self.assertEqual(Connections.AND, my_system.rules[13].connection,
                         msg='Test rule_14 connection')
        self.assertEqual(1.0, my_system.rules[13].weight,
                         msg='Test rule_14 weight')
        self.assertEqual(3, len(my_system.rules[13].inputs),
                         msg='Test rule_14 inputs')
        self.assertEqual('Climate', my_system.rules[13].inputs[0].name,
                         msg='Test rule_14 input 1 name')
        self.assertEqual(False, my_system.rules[13].inputs[0].var_not,
                         msg='Test rule_14 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[0].var_type,
                         msg='Test rule_14 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[13].inputs[0].mf,
                         msg='Test rule_14 input 1 mf')
        self.assertEqual('Depth', my_system.rules[13].inputs[1].name,
                         msg='Test rule_14 input 2 name')
        self.assertEqual(False, my_system.rules[13].inputs[1].var_not,
                         msg='Test rule_14 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[1].var_type,
                         msg='Test rule_14 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[13].inputs[1].mf,
                         msg='Test rule_14 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[13].inputs[2].name,
                         msg='Test rule_14 input 3 name')
        self.assertEqual(False, my_system.rules[13].inputs[2].var_not,
                         msg='Test rule_14 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[2].var_type,
                         msg='Test rule_14 input 3 var_type')
        self.assertEqual('Low', my_system.rules[13].inputs[2].mf,
                         msg='Test rule_14 input 3 mf')
        self.assertEqual(1, len(my_system.rules[13].outputs),
                         msg='Test rule_14 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[13].outputs[0].name,
                         msg='Test rule_14 output 1 name')
        self.assertEqual('consequent', my_system.rules[13].outputs[0].var_type,
                         msg='Test rule_14 output 1 var_type')
        self.assertEqual('WetSubCoastal',
                         my_system.rules[13].outputs[0].mf,
                         msg='Test rule_14 output 1 mf')

    def test_import_file_3(self):
        my_filename = "tests/test_data/Shelf.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        # System
        self.assertEqual('Shelf', my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.mamdani, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(3, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(14, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.min, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.max, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.centroid, my_system.defuzz_method,
                         msg='Test defuzz_method')

        # Input_1
        self.assertEqual('Climate', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 1], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(2, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('Arid', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([-0.1, -0.1, 0.5, 0.5],
                         my_system.inputs.get(1).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('Wet', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 2 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 2 function')
        self.assertEqual([0.5, 0.5, 1.1, 1.1],
                         my_system.inputs.get(1).mfs.get(2).abcd,
                         msg='Test input 1 mf 2 abcd')

        # Input_2
        self.assertEqual('Depth', my_system.inputs.get(2).name,
                         msg='Test input 2 name')
        self.assertEqual([0, 3000], my_system.inputs.get(2).range,
                         msg='Test input 2 range')
        self.assertEqual(3, my_system.inputs.get(2).num_mfs,
                         msg='Test input 2 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(2).var_type,
                         msg='Test input 2 var_type')

        self.assertEqual('Shallow', my_system.inputs.get(2).mfs.get(1).name,
                         msg='Test input 2 mf 1 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(1).function,
                         msg='Test input 2 mf 1 function')
        self.assertEqual(10.3, my_system.inputs.get(2).mfs.get(1).sigma1,
                         msg='Test input 2 mf 1 sigma1')
        self.assertEqual(-56.35, my_system.inputs.get(2).mfs.get(1).mean1,
                         msg='Test input 2 mf 1 mean1')
        self.assertEqual(6.65, my_system.inputs.get(2).mfs.get(1).sigma2,
                         msg='Test input 2 mf 1 sigma2')
        self.assertEqual(2.384, my_system.inputs.get(2).mfs.get(1).mean2,
                         msg='Test input 2 mf 1 mean2')

        self.assertEqual('Intermediary', my_system.inputs.get(2).mfs.get(2).name,
                         msg='Test input 2 mf 2 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(2).function,
                         msg='Test input 2 mf 2 function')
        self.assertEqual(18.6, my_system.inputs.get(2).mfs.get(2).sigma1,
                         msg='Test input 2 mf 2 sigma1')
        self.assertEqual(62.2, my_system.inputs.get(2).mfs.get(2).mean1,
                         msg='Test input 2 mf 2 mean1')
        self.assertEqual(17.81, my_system.inputs.get(2).mfs.get(2).sigma2,
                         msg='Test input 2 mf 2 sigma2')
        self.assertEqual(84.92, my_system.inputs.get(2).mfs.get(2).mean2,
                         msg='Test input 2 mf 2 mean2')

        self.assertEqual('Deep', my_system.inputs.get(2).mfs.get(3).name,
                         msg='Test input 2 mf 3 name')
        self.assertEqual(Functions.gauss2mf,
                         my_system.inputs.get(2).mfs.get(3).function,
                         msg='Test input 2 mf 3 function')
        self.assertEqual(77.9, my_system.inputs.get(2).mfs.get(3).sigma1,
                         msg='Test input 2 mf 3 sigma1')
        self.assertEqual(260, my_system.inputs.get(2).mfs.get(3).mean1,
                         msg='Test input 2 mf 3 mean1')
        self.assertEqual(28.3, my_system.inputs.get(2).mfs.get(3).sigma2,
                         msg='Test input 2 mf 3 sigma2')
        self.assertEqual(3042, my_system.inputs.get(2).mfs.get(3).mean2,
                         msg='Test input 2 mf 3 mean2')

        # Input_3
        self.assertEqual('WaveEnergy', my_system.inputs.get(3).name,
                         msg='Test input 3 name')
        self.assertEqual([0, 1], my_system.inputs.get(3).range,
                         msg='Test input 3 range')
        self.assertEqual(3, my_system.inputs.get(3).num_mfs,
                         msg='Test input 3 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(3).var_type,
                         msg='Test input 3 var_type')

        self.assertEqual('Low', my_system.inputs.get(3).mfs.get(1).name,
                         msg='Test input 3 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(1).function,
                         msg='Test input 3 mf 1 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(1).sigma,
                         msg='Test input 3 mf 1 sigma')
        self.assertEqual(0, my_system.inputs.get(3).mfs.get(1).mean,
                         msg='Test input 3 mf 1 mean')

        self.assertEqual('Moderate', my_system.inputs.get(3).mfs.get(2).name,
                         msg='Test input 3 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(2).function,
                         msg='Test input 3 mf 2 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(2).sigma,
                         msg='Test input 3 mf 1 sigma')
        self.assertEqual(0.5, my_system.inputs.get(3).mfs.get(2).mean,
                         msg='Test input 3 mf 1 mean')

        self.assertEqual('High', my_system.inputs.get(3).mfs.get(3).name,
                         msg='Test input 3 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.inputs.get(3).mfs.get(3).function,
                         msg='Test input 3 mf 3 function')
        self.assertEqual(0.2123, my_system.inputs.get(3).mfs.get(3).sigma,
                         msg='Test input 3 mf 3 sigma')
        self.assertEqual(1, my_system.inputs.get(3).mfs.get(3).mean,
                         msg='Test input 3 mf 3 mean')

        # Output_1
        self.assertEqual('FaciesAssociation', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([0, 12], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(13, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('ClayeyEmbayment',
                         my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(1).sigma,
                         msg='Test output 1 mf 1 sigma')
        self.assertEqual(0, my_system.outputs.get(1).mfs.get(1).mean,
                         msg='Test output 1 mf 1 mean')

        self.assertEqual('ShallowPlain',
                         my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 2 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(2).sigma,
                         msg='Test output 1 mf 2 sigma')
        self.assertEqual(1, my_system.outputs.get(1).mfs.get(2).mean,
                         msg='Test output 1 mf 2 mean')

        self.assertEqual('Cape',
                         my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 3 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 3 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(3).sigma,
                         msg='Test output 1 mf 3 sigma')
        self.assertEqual(2, my_system.outputs.get(1).mfs.get(3).mean,
                         msg='Test output 1 mf 3 mean')

        self.assertEqual('LowEnergyUnderwaterPlain',
                         my_system.outputs.get(1).mfs.get(4).name,
                         msg='Test output 1 mf 4 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(4).function,
                         msg='Test output 1 mf 4 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(4).sigma,
                         msg='Test output 1 mf 4 sigma')
        self.assertEqual(3, my_system.outputs.get(1).mfs.get(4).mean,
                         msg='Test output 1 mf 4 mean')

        self.assertEqual('StromatoliteEmbayment',
                         my_system.outputs.get(1).mfs.get(5).name,
                         msg='Test output 1 mf 5 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(5).function,
                         msg='Test output 1 mf 5 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(5).sigma,
                         msg='Test output 1 mf 5 sigma')
        self.assertEqual(4, my_system.outputs.get(1).mfs.get(5).mean,
                         msg='Test output 1 mf 5 mean')

        self.assertEqual('HighEnergyIntraclastic',
                         my_system.outputs.get(1).mfs.get(6).name,
                         msg='Test output 1 mf 6 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(6).function,
                         msg='Test output 1 mf 6 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(6).sigma,
                         msg='Test output 1 mf 6 sigma')
        self.assertEqual(5, my_system.outputs.get(1).mfs.get(6).mean,
                         msg='Test output 1 mf 6 mean')

        self.assertEqual('AridSubCoastal',
                         my_system.outputs.get(1).mfs.get(7).name,
                         msg='Test output 1 mf 7 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(7).function,
                         msg='Test output 1 mf 7 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(7).sigma,
                         msg='Test output 1 mf 7 sigma')
        self.assertEqual(6, my_system.outputs.get(1).mfs.get(7).mean,
                         msg='Test output 1 mf 7 mean')

        self.assertEqual('ModerateEnergyIntraclastic',
                         my_system.outputs.get(1).mfs.get(8).name,
                         msg='Test output 1 mf 8 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(8).function,
                         msg='Test output 1 mf 8 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(8).sigma,
                         msg='Test output 1 mf 8 sigma')
        self.assertEqual(7, my_system.outputs.get(1).mfs.get(8).mean,
                         msg='Test output 1 mf 8 mean')

        self.assertEqual('Reef',
                         my_system.outputs.get(1).mfs.get(9).name,
                         msg='Test output 1 mf 9 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(9).function,
                         msg='Test output 1 mf 9 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(9).sigma,
                         msg='Test output 1 mf 9 sigma')
        self.assertEqual(8, my_system.outputs.get(1).mfs.get(9).mean,
                         msg='Test output 1 mf 9 mean')

        self.assertEqual('InterpatchesPlain',
                         my_system.outputs.get(1).mfs.get(10).name,
                         msg='Test output 1 mf 10 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(10).function,
                         msg='Test output 1 mf 10 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(10).sigma,
                         msg='Test output 1 mf 10 sigma')
        self.assertEqual(9, my_system.outputs.get(1).mfs.get(10).mean,
                         msg='Test output 1 mf 10 mean')

        self.assertEqual('ClayeyClasticDeposit',
                         my_system.outputs.get(1).mfs.get(11).name,
                         msg='Test output 1 mf 11 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(11).function,
                         msg='Test output 1 mf 11 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(11).sigma,
                         msg='Test output 1 mf 11 sigma')
        self.assertEqual(10, my_system.outputs.get(1).mfs.get(11).mean,
                         msg='Test output 1 mf 11 mean')

        self.assertEqual('WetSubCoastal',
                         my_system.outputs.get(1).mfs.get(12).name,
                         msg='Test output 1 mf 12 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(12).function,
                         msg='Test output 1 mf 12 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(12).sigma,
                         msg='Test output 1 mf 12 sigma')
        self.assertEqual(11, my_system.outputs.get(1).mfs.get(12).mean,
                         msg='Test output 1 mf 12 mean')

        self.assertEqual('LaminiteRamp',
                         my_system.outputs.get(1).mfs.get(13).name,
                         msg='Test output 1 mf 13 name')
        self.assertEqual(Functions.gaussmf,
                         my_system.outputs.get(1).mfs.get(13).function,
                         msg='Test output 1 mf 13 function')
        self.assertEqual(0.4247, my_system.outputs.get(1).mfs.get(13).sigma,
                         msg='Test output 1 mf 13 sigma')
        self.assertEqual(12, my_system.outputs.get(1).mfs.get(13).mean,
                         msg='Test output 1 mf 13 mean')

        # Rules
        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.AND, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(3, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('Climate', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('Depth', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(False, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[0].inputs[2].name,
                         msg='Test rule_1 input 3 name')
        self.assertEqual(False, my_system.rules[0].inputs[2].var_not,
                         msg='Test rule_1 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[2].var_type,
                         msg='Test rule_1 input 3 var_type')
        self.assertEqual('Low', my_system.rules[0].inputs[2].mf,
                         msg='Test rule_1 input 3 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('ClayeyEmbayment', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(3, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('Climate', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual('Depth', my_system.rules[1].inputs[1].name,
                         msg='Test rule_2 input 2 name')
        self.assertEqual(False, my_system.rules[1].inputs[1].var_not,
                         msg='Test rule_2 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[1].var_type,
                         msg='Test rule_2 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[1].inputs[1].mf,
                         msg='Test rule_2 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[1].inputs[2].name,
                         msg='Test rule_2 input 3 name')
        self.assertEqual(False, my_system.rules[1].inputs[2].var_not,
                         msg='Test rule_2 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[2].var_type,
                         msg='Test rule_2 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[1].inputs[2].mf,
                         msg='Test rule_2 input 3 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('ShallowPlain',
                         my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.AND, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(1.0, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(3, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('Climate', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('Depth', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 2 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[2].inputs[2].name,
                         msg='Test rule_3 input 3 name')
        self.assertEqual(False, my_system.rules[2].inputs[2].var_not,
                         msg='Test rule_3 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[2].var_type,
                         msg='Test rule_3 input 3 var_type')
        self.assertEqual('High', my_system.rules[2].inputs[2].mf,
                         msg='Test rule_3 input 3 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('Cape',
                         my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 mf')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.AND, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(3, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('Climate', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual('Depth', my_system.rules[3].inputs[1].name,
                         msg='Test rule_4 input 2 name')
        self.assertEqual(False, my_system.rules[3].inputs[1].var_not,
                         msg='Test rule_4 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[1].var_type,
                         msg='Test rule_4 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[3].inputs[1].mf,
                         msg='Test rule_4 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[3].inputs[2].name,
                         msg='Test rule_4 input 3 name')
        self.assertEqual(False, my_system.rules[3].inputs[2].var_not,
                         msg='Test rule_4 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[2].var_type,
                         msg='Test rule_4 input 3 var_type')
        self.assertEqual('Low', my_system.rules[3].inputs[2].mf,
                         msg='Test rule_4 input 3 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('LowEnergyUnderwaterPlain',
                         my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

        self.assertEqual('rule_5', my_system.rules[4].name,
                         msg='Test rule_5 name')
        self.assertEqual(Connections.AND, my_system.rules[4].connection,
                         msg='Test rule_5 connection')
        self.assertEqual(1.0, my_system.rules[4].weight,
                         msg='Test rule_5 weight')
        self.assertEqual(3, len(my_system.rules[4].inputs),
                         msg='Test rule_5 inputs')
        self.assertEqual('Climate', my_system.rules[4].inputs[0].name,
                         msg='Test rule_5 input 1 name')
        self.assertEqual(False, my_system.rules[4].inputs[0].var_not,
                         msg='Test rule_5 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[0].var_type,
                         msg='Test rule_5 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[4].inputs[0].mf,
                         msg='Test rule_5 input 1 mf')
        self.assertEqual('Depth', my_system.rules[4].inputs[1].name,
                         msg='Test rule_5 input 2 name')
        self.assertEqual(False, my_system.rules[4].inputs[1].var_not,
                         msg='Test rule_5 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[1].var_type,
                         msg='Test rule_5 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[4].inputs[1].mf,
                         msg='Test rule_5 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[4].inputs[2].name,
                         msg='Test rule_5 input 3 name')
        self.assertEqual(False, my_system.rules[4].inputs[2].var_not,
                         msg='Test rule_5 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[4].inputs[2].var_type,
                         msg='Test rule_5 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[4].inputs[2].mf,
                         msg='Test rule_5 input 3 mf')
        self.assertEqual(1, len(my_system.rules[4].outputs),
                         msg='Test rule_5 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[4].outputs[0].name,
                         msg='Test rule_5 output 1 name')
        self.assertEqual('consequent', my_system.rules[4].outputs[0].var_type,
                         msg='Test rule_5 output 1 var_type')
        self.assertEqual('StromatoliteEmbayment',
                         my_system.rules[4].outputs[0].mf,
                         msg='Test rule_5 output 1 mf')

        self.assertEqual('rule_6', my_system.rules[5].name,
                         msg='Test rule_6 name')
        self.assertEqual(Connections.AND, my_system.rules[5].connection,
                         msg='Test rule_6 connection')
        self.assertEqual(1.0, my_system.rules[5].weight,
                         msg='Test rule_6 weight')
        self.assertEqual(3, len(my_system.rules[5].inputs),
                         msg='Test rule_6 inputs')
        self.assertEqual('Climate', my_system.rules[5].inputs[0].name,
                         msg='Test rule_6 input 1 name')
        self.assertEqual(False, my_system.rules[5].inputs[0].var_not,
                         msg='Test rule_6 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[0].var_type,
                         msg='Test rule_6 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[5].inputs[0].mf,
                         msg='Test rule_6 input 1 mf')
        self.assertEqual('Depth', my_system.rules[5].inputs[1].name,
                         msg='Test rule_6 input 2 name')
        self.assertEqual(False, my_system.rules[5].inputs[1].var_not,
                         msg='Test rule_6 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[1].var_type,
                         msg='Test rule_6 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[5].inputs[1].mf,
                         msg='Test rule_6 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[5].inputs[2].name,
                         msg='Test rule_6 input 3 name')
        self.assertEqual(False, my_system.rules[5].inputs[2].var_not,
                         msg='Test rule_6 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[5].inputs[2].var_type,
                         msg='Test rule_6 input 3 var_type')
        self.assertEqual('High', my_system.rules[5].inputs[2].mf,
                         msg='Test rule_6 input 3 mf')
        self.assertEqual(1, len(my_system.rules[5].outputs),
                         msg='Test rule_6 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[5].outputs[0].name,
                         msg='Test rule_6 output 1 name')
        self.assertEqual('consequent', my_system.rules[5].outputs[0].var_type,
                         msg='Test rule_6 output 1 var_type')
        self.assertEqual('HighEnergyIntraclastic',
                         my_system.rules[5].outputs[0].mf,
                         msg='Test rule_6 output 1 mf')

        self.assertEqual('rule_7', my_system.rules[6].name,
                         msg='Test rule_7 name')
        self.assertEqual(Connections.AND, my_system.rules[6].connection,
                         msg='Test rule_7 connection')
        self.assertEqual(1.0, my_system.rules[6].weight,
                         msg='Test rule_7 weight')
        self.assertEqual(3, len(my_system.rules[6].inputs),
                         msg='Test rule_7 inputs')
        self.assertEqual('Climate', my_system.rules[6].inputs[0].name,
                         msg='Test rule_7 input 1 name')
        self.assertEqual(False, my_system.rules[6].inputs[0].var_not,
                         msg='Test rule_7 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[0].var_type,
                         msg='Test rule_7 input 1 var_type')
        self.assertEqual('Arid', my_system.rules[6].inputs[0].mf,
                         msg='Test rule_7 input 1 mf')
        self.assertEqual('Depth', my_system.rules[6].inputs[1].name,
                         msg='Test rule_7 input 2 name')
        self.assertEqual(False, my_system.rules[6].inputs[1].var_not,
                         msg='Test rule_7 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[1].var_type,
                         msg='Test rule_7 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[6].inputs[1].mf,
                         msg='Test rule_7 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[6].inputs[2].name,
                         msg='Test rule_7 input 3 name')
        self.assertEqual(False, my_system.rules[6].inputs[2].var_not,
                         msg='Test rule_7 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[6].inputs[2].var_type,
                         msg='Test rule_7 input 3 var_type')
        self.assertEqual('Low', my_system.rules[6].inputs[2].mf,
                         msg='Test rule_7 input 3 mf')
        self.assertEqual(1, len(my_system.rules[6].outputs),
                         msg='Test rule_7 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[6].outputs[0].name,
                         msg='Test rule_7 output 1 name')
        self.assertEqual('consequent', my_system.rules[6].outputs[0].var_type,
                         msg='Test rule_7 output 1 var_type')
        self.assertEqual('AridSubCoastal',
                         my_system.rules[6].outputs[0].mf,
                         msg='Test rule_7 output 1 mf')

        self.assertEqual('rule_8', my_system.rules[7].name,
                         msg='Test rule_8 name')
        self.assertEqual(Connections.AND, my_system.rules[7].connection,
                         msg='Test rule_8 connection')
        self.assertEqual(1.0, my_system.rules[7].weight,
                         msg='Test rule_8 weight')
        self.assertEqual(3, len(my_system.rules[7].inputs),
                         msg='Test rule_8 inputs')
        self.assertEqual('Climate', my_system.rules[7].inputs[0].name,
                         msg='Test rule_8 input 1 name')
        self.assertEqual(False, my_system.rules[7].inputs[0].var_not,
                         msg='Test rule_8 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[0].var_type,
                         msg='Test rule_8 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[7].inputs[0].mf,
                         msg='Test rule_8 input 1 mf')
        self.assertEqual('Depth', my_system.rules[7].inputs[1].name,
                         msg='Test rule_8 input 2 name')
        self.assertEqual(False, my_system.rules[7].inputs[1].var_not,
                         msg='Test rule_8 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[1].var_type,
                         msg='Test rule_8 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[7].inputs[1].mf,
                         msg='Test rule_8 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[7].inputs[2].name,
                         msg='Test rule_8 input 3 name')
        self.assertEqual(False, my_system.rules[7].inputs[2].var_not,
                         msg='Test rule_8 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[7].inputs[2].var_type,
                         msg='Test rule_8 input 3 var_type')
        self.assertEqual('Low', my_system.rules[7].inputs[2].mf,
                         msg='Test rule_8 input 3 mf')
        self.assertEqual(1, len(my_system.rules[7].outputs),
                         msg='Test rule_8 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[7].outputs[0].name,
                         msg='Test rule_8 output 1 name')
        self.assertEqual('consequent', my_system.rules[7].outputs[0].var_type,
                         msg='Test rule_8 output 1 var_type')
        self.assertEqual('ModerateEnergyIntraclastic',
                         my_system.rules[7].outputs[0].mf,
                         msg='Test rule_8 output 1 mf')

        self.assertEqual('rule_9', my_system.rules[8].name,
                         msg='Test rule_9 name')
        self.assertEqual(Connections.AND, my_system.rules[8].connection,
                         msg='Test rule_9 connection')
        self.assertEqual(1.0, my_system.rules[8].weight,
                         msg='Test rule_9 weight')
        self.assertEqual(3, len(my_system.rules[8].inputs),
                         msg='Test rule_9 inputs')
        self.assertEqual('Climate', my_system.rules[8].inputs[0].name,
                         msg='Test rule_9 input 1 name')
        self.assertEqual(False, my_system.rules[8].inputs[0].var_not,
                         msg='Test rule_9 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[0].var_type,
                         msg='Test rule_9 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[8].inputs[0].mf,
                         msg='Test rule_9 input 1 mf')
        self.assertEqual('Depth', my_system.rules[8].inputs[1].name,
                         msg='Test rule_9 input 2 name')
        self.assertEqual(False, my_system.rules[8].inputs[1].var_not,
                         msg='Test rule_9 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[1].var_type,
                         msg='Test rule_9 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[8].inputs[1].mf,
                         msg='Test rule_9 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[8].inputs[2].name,
                         msg='Test rule_9 input 3 name')
        self.assertEqual(False, my_system.rules[8].inputs[2].var_not,
                         msg='Test rule_9 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[8].inputs[2].var_type,
                         msg='Test rule_9 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[8].inputs[2].mf,
                         msg='Test rule_9 input 3 mf')
        self.assertEqual(1, len(my_system.rules[8].outputs),
                         msg='Test rule_9 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[8].outputs[0].name,
                         msg='Test rule_9 output 1 name')
        self.assertEqual('consequent', my_system.rules[8].outputs[0].var_type,
                         msg='Test rule_9 output 1 var_type')
        self.assertEqual('Reef',
                         my_system.rules[8].outputs[0].mf,
                         msg='Test rule_9 output 1 mf')

        self.assertEqual('rule_10', my_system.rules[9].name,
                         msg='Test rule_10 name')
        self.assertEqual(Connections.AND, my_system.rules[9].connection,
                         msg='Test rule_10 connection')
        self.assertEqual(1.0, my_system.rules[9].weight,
                         msg='Test rule_10 weight')
        self.assertEqual(3, len(my_system.rules[9].inputs),
                         msg='Test rule_10 inputs')
        self.assertEqual('Climate', my_system.rules[9].inputs[0].name,
                         msg='Test rule_10 input 1 name')
        self.assertEqual(False, my_system.rules[9].inputs[0].var_not,
                         msg='Test rule_10 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[0].var_type,
                         msg='Test rule_10 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[9].inputs[0].mf,
                         msg='Test rule_10 input 1 mf')
        self.assertEqual('Depth', my_system.rules[9].inputs[1].name,
                         msg='Test rule_10 input 2 name')
        self.assertEqual(False, my_system.rules[9].inputs[1].var_not,
                         msg='Test rule_10 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[1].var_type,
                         msg='Test rule_10 input 2 var_type')
        self.assertEqual('Shallow', my_system.rules[9].inputs[1].mf,
                         msg='Test rule_10 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[9].inputs[2].name,
                         msg='Test rule_10 input 3 name')
        self.assertEqual(False, my_system.rules[9].inputs[2].var_not,
                         msg='Test rule_10 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[9].inputs[2].var_type,
                         msg='Test rule_10 input 3 var_type')
        self.assertEqual('High', my_system.rules[9].inputs[2].mf,
                         msg='Test rule_10 input 3 mf')
        self.assertEqual(1, len(my_system.rules[9].outputs),
                         msg='Test rule_10 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[9].outputs[0].name,
                         msg='Test rule_10 output 1 name')
        self.assertEqual('consequent', my_system.rules[9].outputs[0].var_type,
                         msg='Test rule_10 output 1 var_type')
        self.assertEqual('Reef',
                         my_system.rules[9].outputs[0].mf,
                         msg='Test rule_10 output 1 mf')

        self.assertEqual('rule_11', my_system.rules[10].name,
                         msg='Test rule_11 name')
        self.assertEqual(Connections.AND, my_system.rules[10].connection,
                         msg='Test rule_11 connection')
        self.assertEqual(1.0, my_system.rules[10].weight,
                         msg='Test rule_11 weight')
        self.assertEqual(3, len(my_system.rules[10].inputs),
                         msg='Test rule_11 inputs')
        self.assertEqual('Climate', my_system.rules[10].inputs[0].name,
                         msg='Test rule_11 input 1 name')
        self.assertEqual(False, my_system.rules[10].inputs[0].var_not,
                         msg='Test rule_11 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[0].var_type,
                         msg='Test rule_11 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[10].inputs[0].mf,
                         msg='Test rule_11 input 1 mf')
        self.assertEqual('Depth', my_system.rules[10].inputs[1].name,
                         msg='Test rule_11 input 2 name')
        self.assertEqual(False, my_system.rules[10].inputs[1].var_not,
                         msg='Test rule_11 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[1].var_type,
                         msg='Test rule_11 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[10].inputs[1].mf,
                         msg='Test rule_11 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[10].inputs[2].name,
                         msg='Test rule_11 input 3 name')
        self.assertEqual(False, my_system.rules[10].inputs[2].var_not,
                         msg='Test rule_11 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[10].inputs[2].var_type,
                         msg='Test rule_11 input 3 var_type')
        self.assertEqual('Low', my_system.rules[10].inputs[2].mf,
                         msg='Test rule_11 input 3 mf')
        self.assertEqual(1, len(my_system.rules[10].outputs),
                         msg='Test rule_11 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[10].outputs[0].name,
                         msg='Test rule_11 output 1 name')
        self.assertEqual('consequent', my_system.rules[10].outputs[0].var_type,
                         msg='Test rule_11 output 1 var_type')
        self.assertEqual('InterpatchesPlain',
                         my_system.rules[10].outputs[0].mf,
                         msg='Test rule_11 output 1 mf')

        self.assertEqual('rule_12', my_system.rules[11].name,
                         msg='Test rule_12 name')
        self.assertEqual(Connections.AND, my_system.rules[11].connection,
                         msg='Test rule_12 connection')
        self.assertEqual(1.0, my_system.rules[11].weight,
                         msg='Test rule_12 weight')
        self.assertEqual(3, len(my_system.rules[11].inputs),
                         msg='Test rule_12 inputs')
        self.assertEqual('Climate', my_system.rules[11].inputs[0].name,
                         msg='Test rule_12 input 1 name')
        self.assertEqual(False, my_system.rules[11].inputs[0].var_not,
                         msg='Test rule_12 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[0].var_type,
                         msg='Test rule_12 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[11].inputs[0].mf,
                         msg='Test rule_12 input 1 mf')
        self.assertEqual('Depth', my_system.rules[11].inputs[1].name,
                         msg='Test rule_12 input 2 name')
        self.assertEqual(False, my_system.rules[11].inputs[1].var_not,
                         msg='Test rule_12 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[1].var_type,
                         msg='Test rule_12 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[11].inputs[1].mf,
                         msg='Test rule_12 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[11].inputs[2].name,
                         msg='Test rule_12 input 3 name')
        self.assertEqual(False, my_system.rules[11].inputs[2].var_not,
                         msg='Test rule_12 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[11].inputs[2].var_type,
                         msg='Test rule_12 input 3 var_type')
        self.assertEqual('Moderate', my_system.rules[11].inputs[2].mf,
                         msg='Test rule_12 input 3 mf')
        self.assertEqual(1, len(my_system.rules[11].outputs),
                         msg='Test rule_12 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[11].outputs[0].name,
                         msg='Test rule_12 output 1 name')
        self.assertEqual('consequent', my_system.rules[11].outputs[0].var_type,
                         msg='Test rule_12 output 1 var_type')
        self.assertEqual('ClayeyClasticDeposit',
                         my_system.rules[11].outputs[0].mf,
                         msg='Test rule_12 output 1 mf')

        self.assertEqual('rule_13', my_system.rules[12].name,
                         msg='Test rule_13 name')
        self.assertEqual(Connections.AND, my_system.rules[12].connection,
                         msg='Test rule_13 connection')
        self.assertEqual(1.0, my_system.rules[12].weight,
                         msg='Test rule_13 weight')
        self.assertEqual(3, len(my_system.rules[12].inputs),
                         msg='Test rule_13 inputs')
        self.assertEqual('Climate', my_system.rules[12].inputs[0].name,
                         msg='Test rule_13 input 1 name')
        self.assertEqual(False, my_system.rules[12].inputs[0].var_not,
                         msg='Test rule_13 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[0].var_type,
                         msg='Test rule_13 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[12].inputs[0].mf,
                         msg='Test rule_13 input 1 mf')
        self.assertEqual('Depth', my_system.rules[12].inputs[1].name,
                         msg='Test rule_13 input 2 name')
        self.assertEqual(False, my_system.rules[12].inputs[1].var_not,
                         msg='Test rule_13 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[1].var_type,
                         msg='Test rule_13 input 2 var_type')
        self.assertEqual('Intermediary', my_system.rules[12].inputs[1].mf,
                         msg='Test rule_13 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[12].inputs[2].name,
                         msg='Test rule_13 input 3 name')
        self.assertEqual(False, my_system.rules[12].inputs[2].var_not,
                         msg='Test rule_13 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[12].inputs[2].var_type,
                         msg='Test rule_13 input 3 var_type')
        self.assertEqual('High', my_system.rules[12].inputs[2].mf,
                         msg='Test rule_13 input 3 mf')
        self.assertEqual(1, len(my_system.rules[12].outputs),
                         msg='Test rule_13 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[12].outputs[0].name,
                         msg='Test rule_13 output 1 name')
        self.assertEqual('consequent', my_system.rules[12].outputs[0].var_type,
                         msg='Test rule_13 output 1 var_type')
        self.assertEqual('Reef',
                         my_system.rules[12].outputs[0].mf,
                         msg='Test rule_13 output 1 mf')

        self.assertEqual('rule_14', my_system.rules[13].name,
                         msg='Test rule_14 name')
        self.assertEqual(Connections.AND, my_system.rules[13].connection,
                         msg='Test rule_14 connection')
        self.assertEqual(1.0, my_system.rules[13].weight,
                         msg='Test rule_14 weight')
        self.assertEqual(3, len(my_system.rules[13].inputs),
                         msg='Test rule_14 inputs')
        self.assertEqual('Climate', my_system.rules[13].inputs[0].name,
                         msg='Test rule_14 input 1 name')
        self.assertEqual(False, my_system.rules[13].inputs[0].var_not,
                         msg='Test rule_14 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[0].var_type,
                         msg='Test rule_14 input 1 var_type')
        self.assertEqual('Wet', my_system.rules[13].inputs[0].mf,
                         msg='Test rule_14 input 1 mf')
        self.assertEqual('Depth', my_system.rules[13].inputs[1].name,
                         msg='Test rule_14 input 2 name')
        self.assertEqual(False, my_system.rules[13].inputs[1].var_not,
                         msg='Test rule_14 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[1].var_type,
                         msg='Test rule_14 input 2 var_type')
        self.assertEqual('Deep', my_system.rules[13].inputs[1].mf,
                         msg='Test rule_14 input 2 mf')
        self.assertEqual('WaveEnergy', my_system.rules[13].inputs[2].name,
                         msg='Test rule_14 input 3 name')
        self.assertEqual(False, my_system.rules[13].inputs[2].var_not,
                         msg='Test rule_14 input 3 var_not')
        self.assertEqual('antecedent', my_system.rules[13].inputs[2].var_type,
                         msg='Test rule_14 input 3 var_type')
        self.assertEqual('Low', my_system.rules[13].inputs[2].mf,
                         msg='Test rule_14 input 3 mf')
        self.assertEqual(1, len(my_system.rules[13].outputs),
                         msg='Test rule_14 outputs')
        self.assertEqual('FaciesAssociation',
                         my_system.rules[13].outputs[0].name,
                         msg='Test rule_14 output 1 name')
        self.assertEqual('consequent', my_system.rules[13].outputs[0].var_type,
                         msg='Test rule_14 output 1 var_type')
        self.assertEqual('WetSubCoastal',
                         my_system.rules[13].outputs[0].mf,
                         msg='Test rule_14 output 1 mf')

    def test_import_file_4(self):
        my_filename = "tests/test_data/Tip_fuzzylite_1.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        # System
        self.assertEqual('tip', my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.sugeno, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(2, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.min, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.max, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.prod, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.sum, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.wtaver, my_system.defuzz_method,
                         msg='Test defuzz_method')

        # Input_1
        self.assertEqual('service', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 10], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(3, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('poor', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([0.000, 0.000, 2.500, 5.000],
                         my_system.inputs.get(1).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('good', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trimf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([2.500, 5.000, 7.500],
                         my_system.inputs.get(1).mfs.get(2).abc,
                         msg='Test input 1 mf 1 abc')

        self.assertEqual('excellent', my_system.inputs.get(1).mfs.get(3).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(3).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([5.000, 7.500, 10.000, 10.000],
                         my_system.inputs.get(1).mfs.get(3).abcd,
                         msg='Test input 1 mf 1 abcd')

        # Input_2
        self.assertEqual('food', my_system.inputs.get(2).name,
                         msg='Test input 2 name')
        self.assertEqual([0, 10], my_system.inputs.get(2).range,
                         msg='Test input 2 range')
        self.assertEqual(2, my_system.inputs.get(2).num_mfs,
                         msg='Test input 2 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(2).var_type,
                         msg='Test input 2 var_type')

        self.assertEqual('rancid', my_system.inputs.get(2).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([0.000, 0.000, 2.500, 7.500],
                         my_system.inputs.get(2).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('delicious', my_system.inputs.get(2).mfs.get(2).name,
                         msg='Test input 2 mf 2 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(2).function,
                         msg='Test input 2 mf 2 function')
        self.assertEqual([2.5, 7.5, 10, 10],
                         my_system.inputs.get(2).mfs.get(2).abcd,
                         msg='Test input 2 mf 2 abcd')

        # Output_1
        self.assertEqual('Tip', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([0, 30], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(3, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('cheap', my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(5,
                         my_system.outputs.get(1).mfs.get(1).value,
                         msg='Test output 1 mf 1 constant')

        self.assertEqual('average', my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(15,
                         my_system.outputs.get(1).mfs.get(2).value,
                         msg='Test output 1 mf 1 constant')

        self.assertEqual('generous', my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(25,
                         my_system.outputs.get(1).mfs.get(3).value,
                         msg='Test output 1 mf 1 constant')

        # Rules
        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.OR, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(2, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('service', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('poor', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('food', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(False, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('rancid', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('Tip', my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('cheap', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(1, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('service', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('good', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('Tip', my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('average', my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.OR, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(0.5, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(2, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('service', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('excellent', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('food', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('delicious', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('Tip', my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('generous', my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 mf')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.AND, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(2, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('service', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('excellent', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual('food', my_system.rules[3].inputs[1].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[1].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[1].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('delicious', my_system.rules[3].inputs[1].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('Tip', my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('generous', my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

    def test_import_file_5(self):
        my_filename = "tests/test_data/Tip_fuzzylite_2.fis"
        systemService = SystemService()
        systemService.import_file(my_filename)
        my_system = systemService.system

        # System
        self.assertEqual('tip', my_system.name,
                         msg='Test name')
        self.assertEqual(my_filename, my_system.filename,
                         msg='Test filename')
        self.assertEqual(ControllerType.sugeno, my_system.type,
                         msg='Test type')
        self.assertEqual('2.0', my_system.version, msg='Test version')
        self.assertEqual(2, my_system.num_inputs, msg='Test num_inputs')
        self.assertEqual(1, my_system.num_outputs, msg='Test num_outputs')
        self.assertEqual(4, my_system.num_rules, msg='Test num_rules')
        self.assertEqual(AndMethods.prod, my_system.and_method,
                         msg='Test and_method')
        self.assertEqual(OrMethods.probor, my_system.or_method,
                         msg='Test or_method')
        self.assertEqual(ImpMethods.prod, my_system.imp_method,
                         msg='Test imp_method')
        self.assertEqual(AggMethods.sum, my_system.agg_method,
                         msg='Test agg_method')
        self.assertEqual(DefuzzMethods.wtsum, my_system.defuzz_method,
                         msg='Test defuzz_method')

        # Input_1
        self.assertEqual('service', my_system.inputs.get(1).name,
                         msg='Test input 1 name')
        self.assertEqual([0, 10], my_system.inputs.get(1).range,
                         msg='Test input 1 range')
        self.assertEqual(3, my_system.inputs.get(1).num_mfs,
                         msg='Test input 1 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(1).var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('poor', my_system.inputs.get(1).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([0.000, 0.000, 2.500, 5.000],
                         my_system.inputs.get(1).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('good', my_system.inputs.get(1).mfs.get(2).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trimf,
                         my_system.inputs.get(1).mfs.get(2).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([2.500, 5.000, 7.500],
                         my_system.inputs.get(1).mfs.get(2).abc,
                         msg='Test input 1 mf 1 abc')

        self.assertEqual('excellent', my_system.inputs.get(1).mfs.get(3).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(1).mfs.get(3).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([5.000, 7.500, 10.000, 10.000],
                         my_system.inputs.get(1).mfs.get(3).abcd,
                         msg='Test input 1 mf 1 abcd')

        # Input_2
        self.assertEqual('food', my_system.inputs.get(2).name,
                         msg='Test input 2 name')
        self.assertEqual([0, 10], my_system.inputs.get(2).range,
                         msg='Test input 2 range')
        self.assertEqual(2, my_system.inputs.get(2).num_mfs,
                         msg='Test input 2 num_mfs')
        self.assertEqual('antecedent', my_system.inputs.get(2).var_type,
                         msg='Test input 2 var_type')

        self.assertEqual('rancid', my_system.inputs.get(2).mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual([0.000, 0.000, 2.500, 7.500],
                         my_system.inputs.get(2).mfs.get(1).abcd,
                         msg='Test input 1 mf 1 abcd')

        self.assertEqual('delicious', my_system.inputs.get(2).mfs.get(2).name,
                         msg='Test input 2 mf 2 name')
        self.assertEqual(Functions.trapmf,
                         my_system.inputs.get(2).mfs.get(2).function,
                         msg='Test input 2 mf 2 function')
        self.assertEqual([2.5, 7.5, 10, 10],
                         my_system.inputs.get(2).mfs.get(2).abcd,
                         msg='Test input 2 mf 2 abcd')

        # Output_1
        self.assertEqual('Tip', my_system.outputs.get(1).name,
                         msg='Test output 1 name')
        self.assertEqual([0, 30], my_system.outputs.get(1).range,
                         msg='Test output 1 range')
        self.assertEqual(3, my_system.outputs.get(1).num_mfs,
                         msg='Test output 1 num_mfs')
        self.assertEqual('consequent', my_system.outputs.get(1).var_type,
                         msg='Test output 1 var_type')

        self.assertEqual('cheap', my_system.outputs.get(1).mfs.get(1).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(1).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(5,
                         my_system.outputs.get(1).mfs.get(1).value,
                         msg='Test output 1 mf 1 constant')

        self.assertEqual('average', my_system.outputs.get(1).mfs.get(2).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(2).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(15,
                         my_system.outputs.get(1).mfs.get(2).value,
                         msg='Test output 1 mf 1 constant')

        self.assertEqual('generous', my_system.outputs.get(1).mfs.get(3).name,
                         msg='Test output 1 mf 1 name')
        self.assertEqual(Functions.constant,
                         my_system.outputs.get(1).mfs.get(3).function,
                         msg='Test output 1 mf 1 function')
        self.assertEqual(25,
                         my_system.outputs.get(1).mfs.get(3).value,
                         msg='Test output 1 mf 1 constant')

        # Rules
        self.assertEqual('rule_1', my_system.rules[0].name,
                         msg='Test rule_1 name')
        self.assertEqual(Connections.OR, my_system.rules[0].connection,
                         msg='Test rule_1 connection')
        self.assertEqual(1.0, my_system.rules[0].weight,
                         msg='Test rule_1 weight')
        self.assertEqual(2, len(my_system.rules[0].inputs),
                         msg='Test rule_1 inputs')
        self.assertEqual('service', my_system.rules[0].inputs[0].name,
                         msg='Test rule_1 input 1 name')
        self.assertEqual(False, my_system.rules[0].inputs[0].var_not,
                         msg='Test rule_1 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[0].var_type,
                         msg='Test rule_1 input 1 var_type')
        self.assertEqual('poor', my_system.rules[0].inputs[0].mf,
                         msg='Test rule_1 input 1 mf')
        self.assertEqual('food', my_system.rules[0].inputs[1].name,
                         msg='Test rule_1 input 2 name')
        self.assertEqual(False, my_system.rules[0].inputs[1].var_not,
                         msg='Test rule_1 input 2 var_not')
        self.assertEqual('antecedent', my_system.rules[0].inputs[1].var_type,
                         msg='Test rule_1 input 2 var_type')
        self.assertEqual('rancid', my_system.rules[0].inputs[1].mf,
                         msg='Test rule_1 input 2 mf')
        self.assertEqual(1, len(my_system.rules[0].outputs),
                         msg='Test rule_1 outputs')
        self.assertEqual('Tip', my_system.rules[0].outputs[0].name,
                         msg='Test rule_1 output 1 name')
        self.assertEqual('consequent', my_system.rules[0].outputs[0].var_type,
                         msg='Test rule_1 output 1 var_type')
        self.assertEqual('cheap', my_system.rules[0].outputs[0].mf,
                         msg='Test rule_1 output 1 mf')

        self.assertEqual('rule_2', my_system.rules[1].name,
                         msg='Test rule_2 name')
        self.assertEqual(Connections.AND, my_system.rules[1].connection,
                         msg='Test rule_2 connection')
        self.assertEqual(1.0, my_system.rules[1].weight,
                         msg='Test rule_2 weight')
        self.assertEqual(1, len(my_system.rules[1].inputs),
                         msg='Test rule_2 inputs')
        self.assertEqual('service', my_system.rules[1].inputs[0].name,
                         msg='Test rule_2 input 1 name')
        self.assertEqual(False, my_system.rules[1].inputs[0].var_not,
                         msg='Test rule_2 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[1].inputs[0].var_type,
                         msg='Test rule_2 input 1 var_type')
        self.assertEqual('good', my_system.rules[1].inputs[0].mf,
                         msg='Test rule_2 input 1 mf')
        self.assertEqual(1, len(my_system.rules[1].outputs),
                         msg='Test rule_2 outputs')
        self.assertEqual('Tip', my_system.rules[1].outputs[0].name,
                         msg='Test rule_2 output 1 name')
        self.assertEqual('consequent', my_system.rules[1].outputs[0].var_type,
                         msg='Test rule_2 output 1 var_type')
        self.assertEqual('average', my_system.rules[1].outputs[0].mf,
                         msg='Test rule_2 output 1 mf')

        self.assertEqual('rule_3', my_system.rules[2].name,
                         msg='Test rule_3 name')
        self.assertEqual(Connections.OR, my_system.rules[2].connection,
                         msg='Test rule_3 connection')
        self.assertEqual(0.5, my_system.rules[2].weight,
                         msg='Test rule_3 weight')
        self.assertEqual(2, len(my_system.rules[2].inputs),
                         msg='Test rule_3 inputs')
        self.assertEqual('service', my_system.rules[2].inputs[0].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[0].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[0].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('excellent', my_system.rules[2].inputs[0].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual('food', my_system.rules[2].inputs[1].name,
                         msg='Test rule_3 input 1 name')
        self.assertEqual(False, my_system.rules[2].inputs[1].var_not,
                         msg='Test rule_3 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[2].inputs[1].var_type,
                         msg='Test rule_3 input 1 var_type')
        self.assertEqual('delicious', my_system.rules[2].inputs[1].mf,
                         msg='Test rule_3 input 1 mf')
        self.assertEqual(1, len(my_system.rules[2].outputs),
                         msg='Test rule_3 outputs')
        self.assertEqual('Tip', my_system.rules[2].outputs[0].name,
                         msg='Test rule_3 output 1 name')
        self.assertEqual('consequent', my_system.rules[2].outputs[0].var_type,
                         msg='Test rule_3 output 1 var_type')
        self.assertEqual('generous', my_system.rules[2].outputs[0].mf,
                         msg='Test rule_3 output 1 mf')

        self.assertEqual('rule_4', my_system.rules[3].name,
                         msg='Test rule_4 name')
        self.assertEqual(Connections.AND, my_system.rules[3].connection,
                         msg='Test rule_4 connection')
        self.assertEqual(1.0, my_system.rules[3].weight,
                         msg='Test rule_4 weight')
        self.assertEqual(2, len(my_system.rules[3].inputs),
                         msg='Test rule_4 inputs')
        self.assertEqual('service', my_system.rules[3].inputs[0].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[0].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[0].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('excellent', my_system.rules[3].inputs[0].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual('food', my_system.rules[3].inputs[1].name,
                         msg='Test rule_4 input 1 name')
        self.assertEqual(False, my_system.rules[3].inputs[1].var_not,
                         msg='Test rule_4 input 1 var_not')
        self.assertEqual('antecedent', my_system.rules[3].inputs[1].var_type,
                         msg='Test rule_4 input 1 var_type')
        self.assertEqual('delicious', my_system.rules[3].inputs[1].mf,
                         msg='Test rule_4 input 1 mf')
        self.assertEqual(1, len(my_system.rules[3].outputs),
                         msg='Test rule_4 outputs')
        self.assertEqual('Tip', my_system.rules[3].outputs[0].name,
                         msg='Test rule_4 output 1 name')
        self.assertEqual('consequent', my_system.rules[3].outputs[0].var_type,
                         msg='Test rule_4 output 1 var_type')
        self.assertEqual('generous', my_system.rules[3].outputs[0].mf,
                         msg='Test rule_4 output 1 mf')

    def test_import_file_exception_1(self):
        my_filename = "tests/test_data/EnvironmentTeste.fis"
        systemService = SystemService()

        my_exception = "O controlador tsukamoto não foi implementado!"
        with self.assertRaises(Exception) as context:
            systemService.import_file(my_filename)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test import_file exception 1')

    def test_import_file_exception_2(self):
        my_filename = "tests/test_data/EnvironmentTeste2.fis"
        systemService = SystemService()

        my_exception = "Bloco [My_block] não é válido!"
        with self.assertRaises(Exception) as context:
            systemService.import_file(my_filename)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test import_file exception 2')

    def test_import_file_exception_3(self):
        my_filename = "tests/test_data/EnvironmentMamdani2.fis"
        systemService = SystemService()

        my_exception = "Os inputs não estão ordenados!"
        with self.assertRaises(Exception) as context:
            systemService.import_file(my_filename)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test import_file exception 3')

    def test_import_file_exception_4(self):
        my_filename = "tests/test_data/EnvironmentMamdani3.fis"
        systemService = SystemService()

        my_exception = "Os outputs não estão ordenados!"
        with self.assertRaises(Exception) as context:
            systemService.import_file(my_filename)
        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test import_file exception 3')
