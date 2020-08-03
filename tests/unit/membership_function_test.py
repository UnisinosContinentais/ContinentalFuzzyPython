"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.membership_function.ConstantMF import ConstantMF
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.LinearMF import LinearMF
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF


class MembershipFunctionTest(unittest.TestCase):
    def test_create_membership_1(self):
        my_mf = MembershipFunction()

        self.assertIsNone(my_mf.name, msg='Test name')
        self.assertIsNone(my_mf.function, msg='Test function')

    def test_create_membership_2(self):
        my_name = "Test Name"
        my_func = Functions.trimf
        my_mf = MembershipFunction(my_name, my_func)

        self.assertEqual(my_name, my_mf.name, msg='Test name')
        self.assertEqual(my_func, my_mf.function, msg='Test function')

    def test_create_membership_exception_1(self):
        my_name = [10]

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            _ = MembershipFunction(my_name)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership exception 1')

    def test_create_membership_exception_2(self):
        my_name = "Test Name"
        my_func = 10

        my_exception = (f"Função de pertinência {my_func} não é uma instância "
                        "da classe MembershipFunction!")
        with self.assertRaises(Exception) as context:
            _ = MembershipFunction(my_name, my_func)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create membership exception 2')

    def test_property_name(self):
        my_mf = MembershipFunction()
        my_name = 'test name'
        my_mf.name = my_name
        self.assertEqual(my_name, my_mf.name, msg='Test name')

    def test_property_name_exception_1(self):
        my_mf = MembershipFunction()
        my_name = {'sigmf': 10}

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            my_mf.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception 1')

    def test_property_function(self):
        my_mf = MembershipFunction()
        my_func = Functions.gauss2mf
        my_mf.function = my_func

        self.assertEqual(my_func, my_mf.function, msg='Test function')

    def test_property_function_exception_1(self):
        my_mf = MembershipFunction()
        my_func = 'sigmf'

        my_exception = (f"Função de pertinência {my_func} não é uma instância "
                        "da classe MembershipFunction!")
        with self.assertRaises(Exception) as context:
            my_mf.function = my_func

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property function exception 1')


class TriMFTest(unittest.TestCase):
    def test_create_trimf_1(self):
        my_trimf = TriMF()

        self.assertIsNone(my_trimf.name, msg='Test name')
        self.assertEqual(Functions.trimf, my_trimf.function,
                         msg='Test function')
        self.assertEqual([0, 1, 2], my_trimf.abc, msg='Test abc')

    def test_create_trimf_2(self):
        my_name = "Test Name"
        my_abc = [1, 2, 3]
        my_trimf = TriMF(my_name, my_abc)

        self.assertEqual(my_name, my_trimf.name, msg='Test name')
        self.assertEqual(Functions.trimf, my_trimf.function,
                         msg='Test function')
        self.assertEqual(my_abc, my_trimf.abc, msg='Test abc')

    def test_create_trimf_exception_1(self):
        my_name = "Test Name"
        my_abc = [1, 2]

        my_exception = "A lista possui um tamanho diferente de 3 pontos!"
        with self.assertRaises(Exception) as context:
            _ = TriMF(my_name, my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create trimf exception 1')

    def test_create_trimf_exception_2(self):
        my_name = "Test Name"
        my_abc = ['a', 2, 3]

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            _ = TriMF(my_name, my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create trimf exception 2')

    def test_create_trimf_exception_3(self):
        my_name = "Test Name"
        my_abc = 10

        my_exception = f"O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            _ = TriMF(my_name, my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create trimf exception 3')

    def test_property_abc(self):
        my_trimf = TriMF()
        my_abc = [1.3, 2.1, 4.7]

        my_trimf.abc = my_abc
        self.assertEqual(my_abc, my_trimf.abc, msg='Test abc')

    def test_property_abc_exception_1(self):
        my_trimf = TriMF()
        my_abc = [1, 2]

        my_exception = "A lista possui um tamanho diferente de 3 pontos!"
        with self.assertRaises(Exception) as context:
            my_trimf.abc = my_abc

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abc exception 1')

    def test_property_abc_exception_2(self):
        my_trimf = TriMF()
        my_abc = ['a', 2, 3]

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_trimf.abc = my_abc

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abc exception 2')

    def test_property_abc_exception_3(self):
        my_trimf = TriMF()
        my_abc = 10

        my_exception = f"O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_trimf.abc = my_abc

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abc exception 3')


class TrapMFTest(unittest.TestCase):
    def test_create_trapmf_1(self):
        my_trapmf = TrapMF()

        self.assertIsNone(my_trapmf.name, msg='Test name')
        self.assertEqual(Functions.trapmf, my_trapmf.function,
                         msg='Test function')
        self.assertEqual([0, 1, 2, 4], my_trapmf.abcd, msg='Test abcd')

    def test_create_trapmf_2(self):
        my_name = "Test Name"
        my_abcd = [1, 2, 3, 4]
        my_trapmf = TrapMF(my_name, my_abcd)

        self.assertEqual(my_name, my_trapmf.name, msg='Test name')
        self.assertEqual(Functions.trapmf, my_trapmf.function,
                         msg='Test function')
        self.assertEqual(my_abcd, my_trapmf.abcd, msg='Test abcd')

    def test_create_trapmf_exception_1(self):
        my_name = "Test Name"
        my_abcd = [1, 2]

        my_exception = "A lista possui um tamanho diferente de 4 pontos!"
        with self.assertRaises(Exception) as context:
            _ = TrapMF(my_name, my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test create trapmf exception 1")

    def test_create_trapmf_exception_2(self):
        my_name = "Test Name"
        my_abcd = ['a', 2, 3, 4]

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            _ = TrapMF(my_name, my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test create trapmf exception 2")

    def test_create_trapmf_exception_3(self):
        my_name = "Test Name"
        my_abcd = 10

        my_exception = f"O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            _ = TrapMF(my_name, my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test create trapmf exception 3")

    def test_property_abcd(self):
        my_trapmf = TrapMF()
        my_abcd = [1.3, 2.1, 4.7, 5.4]

        my_trapmf.abcd = my_abcd
        self.assertEqual(my_abcd, my_trapmf.abcd, msg='Test abcd')

    def test_property_abcd_exception_1(self):
        my_trapmf = TrapMF()
        my_abcd = [1, 2]

        my_exception = "A lista possui um tamanho diferente de 4 pontos!"
        with self.assertRaises(Exception) as context:
            my_trapmf.abcd = my_abcd

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abcd exception 1')

    def test_property_abcd_exception_2(self):
        my_trapmf = TrapMF()
        my_abcd = ['a', 2, 3, 4]

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_trapmf.abcd = my_abcd

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abcd exception 2')

    def test_property_abcd_exception_3(self):
        my_trapmf = TrapMF()
        my_abcd = 10

        my_exception = f"O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_trapmf.abcd = my_abcd

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property abcd exception 3')


class GaussMFTest(unittest.TestCase):
    def test_create_gaussmf_1(self):
        my_gaussmf = GaussMF()

        self.assertIsNone(my_gaussmf.name, msg='Test name')
        self.assertEqual(Functions.gaussmf, my_gaussmf.function,
                         msg='Test function')
        self.assertIsNone(my_gaussmf.sigma, msg='Test sigma')
        self.assertIsNone(my_gaussmf.mean, msg='Test mean')

    def test_create_gaussmf_2(self):
        my_name = "Test Name"
        my_sigma = 1
        my_mean = 0
        my_gaussmf = GaussMF(my_name, my_sigma, my_mean)

        self.assertEqual(my_name, my_gaussmf.name, msg='Test name')
        self.assertEqual(Functions.gaussmf, my_gaussmf.function,
                         msg='Test function')
        self.assertEqual(my_sigma, my_gaussmf.sigma, msg='Test sigma')
        self.assertEqual(my_mean, my_gaussmf.mean, msg='Test mean')

    def test_create_gaussmf_exception_1(self):
        my_name = "Test Name"
        my_sigma = 'a'
        my_mean = 0

        my_exception = "O parâmetro desvio padrão não é do tipo float!"
        with self.assertRaises(Exception) as context:
            _ = GaussMF(my_name, my_sigma, my_mean)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf exception 1')

    def test_create_gaussmf_exception_2(self):
        my_name = "Test Name"
        my_sigma = 0
        my_mean = 'a'

        my_exception = "O parâmetro média não é do tipo float!"
        with self.assertRaises(Exception) as context:
            _ = GaussMF(my_name, my_sigma, my_mean)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf exception 2')

    def test_property_sigma(self):
        my_gaussmf = GaussMF()
        my_sigma = 1.3

        my_gaussmf.sigma = my_sigma
        self.assertEqual(my_sigma, my_gaussmf.sigma, msg='Test sigma')

    def test_property_sigma_exception_1(self):
        my_gaussmf = GaussMF()
        my_sigma = 'a'

        my_exception = "O parâmetro desvio padrão não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_gaussmf.sigma = my_sigma

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property sigma exception 1')

    def test_property_mean(self):
        my_gaussmf = GaussMF()
        my_mean = 2.7

        my_gaussmf.mean = my_mean
        self.assertEqual(my_mean, my_gaussmf.mean, msg='Test mean')

    def test_property_mean_exception_1(self):
        my_gaussmf = GaussMF()
        my_mean = 'b'

        my_exception = "O parâmetro média não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_gaussmf.mean = my_mean

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mean exception 1')


class GaussMF2Test(unittest.TestCase):
    def test_create_gaussmf2_1(self):
        my_gaussmf2 = Gauss2MF()

        self.assertIsNone(my_gaussmf2.name, msg='Test name')
        self.assertEqual(Functions.gauss2mf, my_gaussmf2.function,
                         msg='Test function')
        self.assertIsNone(my_gaussmf2.sigma1, msg='Test sigma1')
        self.assertIsNone(my_gaussmf2.mean1, msg='Test mean1')
        self.assertIsNone(my_gaussmf2.sigma2, msg='Test sigma2')
        self.assertIsNone(my_gaussmf2.mean2, msg='Test mean2')

    def test_create_gaussmf2_2(self):
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

        self.assertEqual(my_name, my_gaussmf2.name, msg='Test name')
        self.assertEqual(Functions.gauss2mf, my_gaussmf2.function,
                         msg='Test function')
        self.assertEqual(my_sigma1, my_gaussmf2.sigma1, msg='Test sigma1')
        self.assertEqual(my_mean1, my_gaussmf2.mean1, msg='Test mean1')
        self.assertEqual(my_sigma2, my_gaussmf2.sigma2, msg='Test sigma2')
        self.assertEqual(my_mean2, my_gaussmf2.mean2, msg='Test mean2')

    def test_create_gaussmf2_exception_1(self):
        my_name = "Test Name"
        my_sigma1 = 'a'
        my_mean1 = 0
        my_sigma2 = 10
        my_mean2 = 5

        my_exception = ("O parâmetro desvio padrão da primeira gaussiana não é "
                        "do tipo float!")
        with self.assertRaises(Exception) as context:
            _ = Gauss2MF(my_name,
                         my_sigma1,
                         my_mean1,
                         my_sigma2,
                         my_mean2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf2 exception 1')

    def test_create_gaussmf2_exception_2(self):
        my_name = "Test Name"
        my_sigma1 = 1
        my_mean1 = 'a'
        my_sigma2 = 10
        my_mean2 = 5

        my_exception = ("O parâmetro média da primeira gaussiana não é do "
                        "tipo float!")
        with self.assertRaises(Exception) as context:
            _ = Gauss2MF(my_name,
                         my_sigma1,
                         my_mean1,
                         my_sigma2,
                         my_mean2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf2 exception 2')

    def test_create_gaussmf2_exception_3(self):
        my_name = "Test Name"
        my_sigma1 = 1
        my_mean1 = 0
        my_sigma2 = []
        my_mean2 = 5

        my_exception = ("O parâmetro desvio padrão da segunda gaussiana não "
                        "é do tipo float!")
        with self.assertRaises(Exception) as context:
            _ = Gauss2MF(my_name,
                         my_sigma1,
                         my_mean1,
                         my_sigma2,
                         my_mean2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf2 exception 3')

    def test_create_gaussmf2_exception_4(self):
        my_name = "Test Name"
        my_sigma1 = 1
        my_mean1 = 0
        my_sigma2 = 10
        my_mean2 = {}

        my_exception = ("O parâmetro média da segunda gaussiana não é do "
                        "tipo float!")
        with self.assertRaises(Exception) as context:
            _ = Gauss2MF(my_name,
                         my_sigma1,
                         my_mean1,
                         my_sigma2,
                         my_mean2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test create gaussmf2 exception 4')

    def test_property_sigma1(self):
        my_gauss2mf = Gauss2MF()
        my_sigma1 = 1.3

        my_gauss2mf.sigma1 = my_sigma1
        self.assertEqual(my_sigma1, my_gauss2mf.sigma1, msg='Test sigma1')

    def test_property_sigma1_exception_1(self):
        my_gauss2mf = Gauss2MF()
        my_sigma1 = 'a'

        my_exception = ("O parâmetro desvio padrão da primeira gaussiana não "
                        "é do tipo float!")
        with self.assertRaises(Exception) as context:
            my_gauss2mf.sigma1 = my_sigma1

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property sigma1 exception 1")

    def test_property_mean1(self):
        my_gauss2mf = Gauss2MF()
        my_mean1 = 1.3

        my_gauss2mf.mean1 = my_mean1
        self.assertEqual(my_mean1, my_gauss2mf.mean1, msg='Test mean1')

    def test_property_mean1_exception_1(self):
        my_gauss2mf = Gauss2MF()
        my_mean1 = 'a'

        my_exception = ("O parâmetro média da primeira gaussiana não é "
                        "do tipo float!")
        with self.assertRaises(Exception) as context:
            my_gauss2mf.mean1 = my_mean1

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property mean1 exception 1")

    def test_property_sigma2(self):
        my_gauss2mf = Gauss2MF()
        my_sigma2 = 1.3

        my_gauss2mf.sigma2 = my_sigma2
        self.assertEqual(my_sigma2, my_gauss2mf.sigma2, msg='Test sigma2')

    def test_property_sigma2_exception_1(self):
        my_gauss2mf = Gauss2MF()
        my_sigma2 = 'a'

        my_exception = ("O parâmetro desvio padrão da segunda gaussiana não "
                        "é do tipo float!")
        with self.assertRaises(Exception) as context:
            my_gauss2mf.sigma2 = my_sigma2

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property sigma2 exception 1")

    def test_property_mean2(self):
        my_gauss2mf = Gauss2MF()
        my_mean2 = 1.3

        my_gauss2mf.mean2 = my_mean2
        self.assertEqual(my_mean2, my_gauss2mf.mean2, msg='Test sigma2')

    def test_property_mean2_exception_1(self):
        my_gauss2mf = Gauss2MF()
        my_mean2 = 'a'

        my_exception = ("O parâmetro média da segunda gaussiana não é do "
                        "tipo float!")
        with self.assertRaises(Exception) as context:
            my_gauss2mf.mean2 = my_mean2

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property mean2 exception 1")


class ConstantMFTest(unittest.TestCase):
    def test_create_constant_1(self):
        my_constant = ConstantMF()

        self.assertIsNone(my_constant.name, msg='Test name')
        self.assertEqual(Functions.constant, my_constant.function,
                         msg='Test function')
        self.assertEqual(0, my_constant.value, msg='Test value')

    def test_create_constant_2(self):
        my_name = "Test name"
        my_value = 15
        my_constant = ConstantMF(my_name, my_value)

        self.assertEqual(my_name, my_constant.name, msg='Test name')
        self.assertEqual(Functions.constant, my_constant.function,
                         msg='Test function')
        self.assertEqual(15, my_constant.value, msg='Test value')

    def test_create_constant_exception_1(self):
        my_name = "Test Name"
        my_value = 'a'

        my_exception = "O valor não é do tipo float!"
        with self.assertRaises(Exception) as context:
            _ = ConstantMF(my_name, my_value)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test create constant exception 1")

    def test_property_value(self):
        my_constant = ConstantMF()
        my_value = 1.3

        my_constant.value = my_value
        self.assertEqual(my_value, my_constant.value, msg='Test value')

    def test_property_value_exception_1(self):
        my_constant = ConstantMF()
        my_value = 'a'

        my_exception = "O valor não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_constant.value = my_value

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property sigma1 exception 1")


class LinearMFTest(unittest.TestCase):
    def test_create_linear_1(self):
        my_linear = LinearMF()

        self.assertIsNone(my_linear.name, msg='Test name')
        self.assertEqual(Functions.linear, my_linear.function,
                         msg='Test function')
        self.assertEqual(1, my_linear.num_inputs, msg='Test num_inputs')
        self.assertIsNone(my_linear.params, msg='Test params')

    def test_create_linear_2(self):
        my_name = "Test name"
        my_num_inputs = 3
        my_params = [0, 0, 0, 1]
        my_linear = LinearMF(my_name, my_num_inputs, my_params)

        self.assertEqual(my_name, my_linear.name, msg='Test name')
        self.assertEqual(Functions.linear, my_linear.function,
                         msg='Test function')
        self.assertEqual(3, my_linear.num_inputs, msg='Test num_inputs')
        self.assertEqual(my_params, my_linear.params, msg='Test params')

    def test_create_linear_exception_1(self):
        my_name = "Test Name"
        my_num_inputs = 'a'
        my_params = [0, 0, 0, 1]

        my_exception = "O número de antecedentes não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            _ = LinearMF(my_name, my_num_inputs, my_params)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test create linear exception 1")

    def test_property_num_inputs(self):
        my_linear = LinearMF()
        my_num_inputs = 3

        my_linear.num_inputs = my_num_inputs
        self.assertEqual(my_num_inputs,
                         my_linear.num_inputs,
                         msg='Test num_inputs')

    def test_property_num_inputs_exception_1(self):
        my_linear = LinearMF()
        my_num_inputs = 'a'

        my_exception = "O número de antecedentes não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_linear.num_inputs = my_num_inputs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property num_inputs exception 1")

    def test_property_params(self):
        my_linear = LinearMF()
        my_num_inputs = 3
        my_params = [0, 0, 0, 1]

        my_linear.num_inputs = my_num_inputs
        my_linear.params = my_params
        self.assertEqual(my_params,
                         my_linear.params,
                         msg='Test params')

    def test_property_params_exception_1(self):
        my_linear = LinearMF()
        my_num_inputs = 3
        my_params = 10

        my_linear.num_inputs = my_num_inputs

        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_linear.params = my_params

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property params exception 1")

    def test_property_params_exception_2(self):
        my_linear = LinearMF()
        my_num_inputs = 3
        my_params = [0, 0, 0]

        my_linear.num_inputs = my_num_inputs

        my_exception = ("A lista possui tamanho diferente do número de "
                        "antecedentes mais uma constante!")
        with self.assertRaises(Exception) as context:
            my_linear.params = my_params

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property params exception 2")

    def test_property_params_exception_3(self):
        my_linear = LinearMF()
        my_num_inputs = 3
        my_params = ['a', 0, 0, 1]

        my_linear.num_inputs = my_num_inputs

        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_linear.params = my_params

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test property params exception 3")
