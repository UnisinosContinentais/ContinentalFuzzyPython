"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.service.InputService import InputService


class InputServiceTest(unittest.TestCase):
    def test_create_input_service_1(self):
        my_input_service = InputService()

        self.assertTrue(
            isinstance(my_input_service.input, Input),
            msg='Test create input service function')

    def test_create_from_fis_block_1(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_variable.create_from_fis_block(ControllerType.mamdani,
                                          my_entries)

        my_input = my_variable.input

        self.assertEqual('Distance',
                         my_input.name,
                         msg='Test name')
        self.assertEqual([0, 1],
                         my_input.range,
                         msg='Test range')
        self.assertEqual(2, my_input.num_mfs,
                         msg='Test num_mfs')
        self.assertEqual('antecedent', my_input.var_type,
                         msg='Test var_type')

        self.assertEqual('Near', my_input.mfs.get(1).name,
                         msg='Test mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_input.mfs.get(1).function,
                         msg='Test mf 1 function')
        self.assertEqual(0.2, my_input.mfs.get(1).sigma,
                         msg='Test mf 1 sigma')
        self.assertEqual(0, my_input.mfs.get(1).mean,
                         msg='Test mf 1 mean')

        self.assertEqual('Far', my_input.mfs.get(2).name,
                         msg='Test mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_input.mfs.get(2).function,
                         msg='Test mf 2 function')
        self.assertEqual(0.42, my_input.mfs.get(2).sigma,
                         msg='Test mf 2 sigma')
        self.assertEqual(1, my_input.mfs.get(2).mean,
                         msg='Test mf 2 mean')

    def test_create_from_fis_block_2(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_variable.create_from_fis_block(ControllerType.sugeno,
                                          my_entries)

        my_input = my_variable.input

        self.assertEqual('Distance',
                         my_input.name,
                         msg='Test name')
        self.assertEqual([0, 1],
                         my_input.range,
                         msg='Test range')
        self.assertEqual(2, my_input.num_mfs,
                         msg='Test num_mfs')
        self.assertEqual('antecedent', my_input.var_type,
                         msg='Test input 1 var_type')

        self.assertEqual('Near', my_input.mfs.get(1).name,
                         msg='Test input 1 mf 1 name')
        self.assertEqual(Functions.gaussmf,
                         my_input.mfs.get(1).function,
                         msg='Test input 1 mf 1 function')
        self.assertEqual(0.2, my_input.mfs.get(1).sigma,
                         msg='Test input 1 mf 1 sigma')
        self.assertEqual(0, my_input.mfs.get(1).mean,
                         msg='Test input 1 mf 1 mean')

        self.assertEqual('Far', my_input.mfs.get(2).name,
                         msg='Test input 1 mf 2 name')
        self.assertEqual(Functions.gaussmf,
                         my_input.mfs.get(2).function,
                         msg='Test input 1 mf 2 function')
        self.assertEqual(0.42, my_input.mfs.get(2).sigma,
                         msg='Test input 1 mf 2 sigma')
        self.assertEqual(1, my_input.mfs.get(2).mean,
                         msg='Test input 1 mf 2 mean')

    def test_create_from_fis_block_exception_1(self):
        my_variable = InputService()

        my_entries = ['Range=[0 1]',
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_exception = "O nome da variável não foi informado!"

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 1')

    def test_create_from_fis_block_exception_2(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'NumMFs=2',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_exception = (
            "A amplitude do conjunto da variável não foi informada!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 2')

    def test_create_from_fis_block_exception_3(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      "MF1='Near':'gaussmf',[0.2 0]",
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_exception = (
            "O número de funções de pertinência da variável não foi informado!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 3')

    def test_create_from_fis_block_exception_4(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_exception = ("Quantidade de funções de pertinência para "
                        f"a variável Distance é diferente do número "
                        "de funções de pertinência informado no bloco!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 4')

    def test_create_from_fis_block_exception_5(self):
        my_variable = InputService()

        my_entries = [{1: [1, 2, 3]},
                      'Range=[0 1]',
                      'NumMFs=2',
                      "MF2='Far':'gaussmf',[0.42 1]"]

        my_exception = ("A lista de informações do arquivo .fis possui um "
                        "valor que não é do tipo String!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 5')

    def test_create_from_fis_block_exception_6(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=1',
                      "MF1='Far':'linear',[0.42 1]"]

        my_exception = ("Função de pertinência linear, não implementada "
                        "para Mamdani!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 6')

    def test_create_from_fis_block_exception_7(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=1',
                      "MF1='Far':'trimf',[0.42 1 'a']"]

        my_exception = "Um dos valores não é do tipo float!"

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.mamdani,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 7')

    def test_create_from_fis_block_exception_8(self):
        my_variable = InputService()

        my_entries = ["Name='Distance'",
                      'Range=[0 1]',
                      'NumMFs=1',
                      "MF1='Far':'linear',[0.42 1]"]

        my_exception = ("Função de pertinência linear, não implementada "
                        "para Sugeno!")

        with self.assertRaises(Exception) as context:
            my_variable.create_from_fis_block(ControllerType.sugeno,
                                              my_entries)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create from fis block exception 8')