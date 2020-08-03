"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.service.MembershipFunctionService import \
    MembershipFunctionService


class MembershipFunctionServiceTest(unittest.TestCase):
    def test_create_membership_function_service_1(self):
        my_mf_service = MembershipFunctionService()

        self.assertTrue(
            isinstance(my_mf_service.membership_function, MembershipFunction),
            msg='Test create  membership function')

    def test_property_membership_function(self):
        my_mf_service = MembershipFunctionService()
        my_mf = TriMF()
        my_mf_service.membership_function = my_mf

        self.assertEqual(my_mf,
                         my_mf_service.membership_function,
                         msg='Test membership_function')

    def test_property_membership_function_exception_1(self):
        my_mf_service = MembershipFunctionService()
        my_mf = 10

        my_exception = ("O valor não é uma instância da classe "
                        "MembershipFunction!")
        with self.assertRaises(Exception) as context:
            my_mf_service.membership_function = my_mf

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property membership_function exception 1')

    def test_create_membership_function_trimf(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.trimf
        mf_name = 'Termo'
        values_list = [0, 1, 2]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list)

        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')
        self.assertEqual(values_list,
                         my_mf_service.membership_function.abc,
                         msg='Test abc')

    def test_create_membership_function_trimf_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.trimf
        mf_name = 'Termo'
        values_list = [0, 2]

        my_exception = ("Número de parâmetros incorretos para a função de "
                        "pertinência triangular!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function trimf exception 1')

    def test_create_membership_function_trapmf(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.trapmf
        mf_name = 'Termo'
        values_list = [0, 1, 2, 4]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list)

        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')
        self.assertEqual(values_list,
                         my_mf_service.membership_function.abcd,
                         msg='Test abcd')

    def test_create_membership_function_trapmf_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.trapmf
        mf_name = 'Termo'
        values_list = [0, 1, 2]

        my_exception = ("Número de parâmetros incorretos para a função de "
                        "pertinência trapezoidal!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function trapmf exception 1')

    def test_create_membership_function_gaussmf(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.gaussmf
        mf_name = 'Termo'
        values_list = [0, 1]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list)

        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')
        self.assertEqual(values_list[0],
                         my_mf_service.membership_function.sigma,
                         msg='Test sigma')
        self.assertEqual(values_list[1],
                         my_mf_service.membership_function.mean,
                         msg='Test mean')

    def test_create_membership_function_gaussmf_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.gaussmf
        mf_name = 'Termo'
        values_list = [0, 1, 2]

        my_exception = ("Número de parâmetros incorretos para a função de "
                        "pertinência gaussiana!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function gaussmf exception 1')

    def test_create_membership_function_gauss2mf(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.gauss2mf
        mf_name = 'Termo'
        values_list = [0, 1, 2, 3]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list)

        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')
        self.assertEqual(values_list[0],
                         my_mf_service.membership_function.sigma1,
                         msg='Test sigma1')
        self.assertEqual(values_list[1],
                         my_mf_service.membership_function.mean1,
                         msg='Test mean1')
        self.assertEqual(values_list[2],
                         my_mf_service.membership_function.sigma2,
                         msg='Test sigma2')
        self.assertEqual(values_list[3],
                         my_mf_service.membership_function.mean2,
                         msg='Test mean2')

    def test_create_membership_function_gauss2mf_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.gauss2mf
        mf_name = 'Termo'
        values_list = [0, 1, 2]

        my_exception = ("Número de parâmetros incorretos para a função de "
                        "pertinência de duas gaussianas combinadas!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function gauss2mf exception 1')


    def test_create_membership_function_constant(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.constant
        mf_name = 'Termo'
        values_list = [10]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list)
        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')
        self.assertEqual(values_list[0],
                         my_mf_service.membership_function.value,
                         msg='Test value')

    def test_create_membership_function_constant_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.constant
        mf_name = 'Termo'
        values_list = [0, 1, 2]

        my_exception = ("Número de parâmetros incorretos para a função de "
                        "pertinência constante!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function constant exception 1')


    def test_create_membership_function_linear(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.linear
        mf_name = 'Termo'
        mf_num_inputs = 3
        values_list = [0, 1, 2, 3]

        my_mf_service.create_membership_function(mf_function,
                                                 mf_name,
                                                 values_list,
                                                 mf_num_inputs)

        self.assertEqual(mf_function,
                         my_mf_service.membership_function.function,
                         msg='Test function')
        self.assertEqual(mf_name,
                         my_mf_service.membership_function.name,
                         msg='Test name')

        self.assertEqual(mf_num_inputs,
                         my_mf_service.membership_function.num_inputs,
                         msg='Test num_inputs')
        self.assertEqual(values_list,
                         my_mf_service.membership_function.params,
                         msg='Test params')

    def test_create_membership_function_linear_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.linear
        mf_name = 'Termo'
        mf_num_inputs = 3
        values_list = [0, 1, 2]

        my_exception = ("A lista possui tamanho diferente do número de "
                        "antecedentes mais uma constante!")
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list,
                                                     mf_num_inputs)

        self.assertEqual(
            my_exception, context.exception.args[0],
            msg='Test create membership_function linear exception 1')


    def test_create_membership_function_exception_1(self):
        my_mf_service = MembershipFunctionService()
        mf_function = 10
        mf_name = 'Termo'
        values_list = [10]

        my_exception = "O parâmetro não é uma Functions!"
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership_function exception 1')

    def test_create_membership_function_exception_2(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.constant
        mf_name = ['Termo']
        values_list = [10]

        my_exception = "O parâmetro não é uma string!"
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership_function exception 2')

    def test_create_membership_function_exception_3(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.constant
        mf_name = 'Termo'
        values_list = 10

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership_function exception 3')

    def test_create_membership_function_exception_4(self):
        my_mf_service = MembershipFunctionService()
        mf_function = Functions.constant
        mf_name = 'Termo'
        values_list = ['a']

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_mf_service.create_membership_function(mf_function,
                                                     mf_name,
                                                     values_list)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership_function exception 4')