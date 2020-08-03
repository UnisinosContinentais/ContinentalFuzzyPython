"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
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


class GaussMembershipFunctionTest(unittest.TestCase):
    def test_calculate_gaussmf(self):
        my_x = 4.9
        my_mean = 3
        my_sigma = 1.5
        my_result = 0.4483

        self.assertEqual(
            my_result,
            round(GaussMembershipFunction.calculate_gaussmf(my_x,
                                                            my_mean,
                                                            my_sigma), 4),
            msg='Test calculate_gaussmf')

    def test_calculate_gaussmf_exception_1(self):
        my_x = 'a'
        my_mean = 3
        my_sigma = 1.5

        my_exception = f"O parâmetro x precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussMembershipFunction.calculate_gaussmf(my_x,
                                                          my_mean,
                                                          my_sigma)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gaussmf exception 1')

    def test_calculate_gaussmf_exception_2(self):
        my_x = 4.9
        my_mean = 'a'
        my_sigma = 1.5

        my_exception = f"O parâmetro média precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussMembershipFunction.calculate_gaussmf(my_x,
                                                          my_mean,
                                                          my_sigma)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gaussmf exception 2')

    def test_calculate_gaussmf_exception_3(self):
        my_x = 4.9
        my_mean = 3
        my_sigma = 'a'

        my_exception = f"O parâmetro desvio padrão precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussMembershipFunction.calculate_gaussmf(my_x,
                                                          my_mean,
                                                          my_sigma)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gaussmf exception 3')


class GaussTwoMembershipFunctionTest(unittest.TestCase):
    def test_calculate_gauss2mf_1(self):
        my_x = 2.3
        my_mean1 = 3
        my_sigma1 = 1.5
        my_mean2 = 8
        my_sigma2 = 2.7
        my_result = 0.8968

        self.assertEqual(
            my_result,
            round(GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                                my_mean1,
                                                                my_sigma1,
                                                                my_mean2,
                                                                my_sigma2), 4),
            msg='Test calculate_gauss2mf 1')

    def test_calculate_gauss2mf_2(self):
        my_x = 9.1
        my_mean1 = 3
        my_sigma1 = 1.5
        my_mean2 = 8
        my_sigma2 = 2.7
        my_result = 0.9204

        self.assertEqual(
            my_result,
            round(GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                                my_mean1,
                                                                my_sigma1,
                                                                my_mean2,
                                                                my_sigma2), 4),
            msg='Test calculate_gauss2mf 2')

    def test_calculate_gauss2mf_3(self):
        my_x = 5
        my_mean1 = 3
        my_sigma1 = 1.5
        my_mean2 = 8
        my_sigma2 = 2.7
        my_result = 1

        self.assertEqual(
            my_result,
            round(GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                                my_mean1,
                                                                my_sigma1,
                                                                my_mean2,
                                                                my_sigma2), 4),
            msg='Test calculate_gauss2mf 3')

    def test_calculate_gauss2mf_4(self):
        my_x = 5
        my_mean1 = 8
        my_sigma1 = 2
        my_mean2 = 4
        my_sigma2 = 1
        my_result = 0.1969

        self.assertEqual(
            my_result,
            round(GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                                my_mean1,
                                                                my_sigma1,
                                                                my_mean2,
                                                                my_sigma2), 4),
            msg='Test calculate_gauss2mf 4')

    def test_calculate_gauss2mf_exception_1(self):
        my_x = 'a'
        my_mean1 = 8
        my_sigma1 = 2
        my_mean2 = 4
        my_sigma2 = 1

        my_exception = f"O parâmetro x precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                              my_mean1,
                                                              my_sigma1,
                                                              my_mean2,
                                                              my_sigma2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gauss2mf exception 1')

    def test_calculate_gauss2mf_exception_2(self):
        my_x = 5
        my_mean1 = 'a'
        my_sigma1 = 2
        my_mean2 = 4
        my_sigma2 = 1

        my_exception = f"O parâmetro média 1 precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                              my_mean1,
                                                              my_sigma1,
                                                              my_mean2,
                                                              my_sigma2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gauss2mf exception 2')

    def test_calculate_gauss2mf_exception_3(self):
        my_x = 5
        my_mean1 = 8
        my_sigma1 = 'a'
        my_mean2 = 4
        my_sigma2 = 1

        my_exception = f"O parâmetro desvio padrão 1 precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                              my_mean1,
                                                              my_sigma1,
                                                              my_mean2,
                                                              my_sigma2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gauss2mf exception 3')

    def test_calculate_gauss2mf_exception_4(self):
        my_x = 5
        my_mean1 = 8
        my_sigma1 = 2
        my_mean2 = 'a'
        my_sigma2 = 1

        my_exception = f"O parâmetro média 2 precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                              my_mean1,
                                                              my_sigma1,
                                                              my_mean2,
                                                              my_sigma2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gauss2mf exception 4')

    def test_calculate_gauss2mf_exception_5(self):
        my_x = 5
        my_mean1 = 8
        my_sigma1 = 2
        my_mean2 = 4
        my_sigma2 = 'a'

        my_exception = f"O parâmetro desvio padrão 2 precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = GaussTwoMembershipFunction.calculate_gauss2mf(my_x,
                                                              my_mean1,
                                                              my_sigma1,
                                                              my_mean2,
                                                              my_sigma2)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_gauss2mf exception 5')


class LinearMembershipFunctionTest(unittest.TestCase):
    def test_calculate_linear_1(self):
        my_params = {'Distance': 0.01,
                     'Depth': 0.02,
                     '__constant__': 2}
        my_inputs = {'Distance': 10,
                     'Depth': 20}
        my_result = 2.5

        self.assertEqual(
            my_result,
            round(LinearMembershipFunction.calculate_linear(my_params,
                                                            my_inputs), 4),
            msg='Test calculate_linear 1')

    def test_calculate_linear_exception_1(self):
        my_params = {'Distance': 0.01,
                     'Slope': 0.02,
                     'Depth': 0.03,
                     '__constant__': 2}
        my_inputs = {'Distance': 10,
                     'Depth': 20}

        my_exception = f"O número de parâmetros está incorreto!"
        with self.assertRaises(Exception) as context:
            _ = LinearMembershipFunction.calculate_linear(my_params,
                                                          my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_linear exception 1')

    def test_calculate_linear_exception_2(self):
        my_params = {10: 0.01,
                     'Depth': 0.02,
                     '__constant__': 2}
        my_inputs = {'Distance': 10,
                     'Depth': 20}

        my_exception = f"A chave do parâmetro não é uma string!"
        with self.assertRaises(Exception) as context:
            _ = LinearMembershipFunction.calculate_linear(my_params,
                                                          my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_linear exception 2')

    def test_calculate_linear_exception_3(self):
        my_params = {'Distance': 'a',
                     'Depth': 0.02,
                     '__constant__': 2}
        my_inputs = {'Distance': 10,
                     'Depth': 20}

        my_exception = f"O valor do parâmetro não é um número!"
        with self.assertRaises(Exception) as context:
            _ = LinearMembershipFunction.calculate_linear(my_params,
                                                          my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_linear exception 3')

    def test_calculate_linear_exception_4(self):
        my_params = {'Distance': 0.01,
                     'Depth': 0.02,
                     '__constant__': 2}
        my_inputs = {1: 10,
                     'Depth': 20}

        my_exception = f"A chave do valor não é uma string!"
        with self.assertRaises(Exception) as context:
            _ = LinearMembershipFunction.calculate_linear(my_params,
                                                          my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_linear exception 3')

    def test_calculate_linear_exception_5(self):
        my_params = {'Distance': 0.01,
                     'Depth': 0.02,
                     '__constant__': 2}
        my_inputs = {'Distance': 10,
                     'Depth': 'a'}

        my_exception = f"O valor não é um número!"
        with self.assertRaises(Exception) as context:
            _ = LinearMembershipFunction.calculate_linear(my_params,
                                                          my_inputs)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_linear exception 3')

class TrapezoidalMembershipFunctionTest(unittest.TestCase):
    def test_calculate_trapmf_1(self):
        my_x = 0
        my_abcd = [1, 2, 3, 4]
        my_result = 0

        self.assertEqual(
            my_result,
            round(TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                                 my_abcd), 4),
            msg='Test calculate_trapmf 1')

    def test_calculate_trapmf_2(self):
        my_x = 1.7
        my_abcd = [1, 2, 3, 4]
        my_result = 0.7

        self.assertEqual(
            my_result,
            round(TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                                 my_abcd), 4),
            msg='Test calculate_trapmf 2')

    def test_calculate_trapmf_3(self):
        my_x = 2.7
        my_abcd = [1, 2, 3, 4]
        my_result = 1

        self.assertEqual(
            my_result,
            round(TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                                 my_abcd), 4),
            msg='Test calculate_trapmf 3')

    def test_calculate_trapmf_4(self):
        my_x = 3.1
        my_abcd = [1, 2, 3, 4]
        my_result = 0.9

        self.assertEqual(
            my_result,
            round(TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                                 my_abcd), 4),
            msg='Test calculate_trapmf 4')

    def test_calculate_trapmf_5(self):
        my_x = 2
        my_abcd = [2, 2, 2, 2]
        my_result = 1

        self.assertEqual(
            my_result,
            round(TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                                 my_abcd), 4),
            msg='Test calculate_trapmf 5')

    def test_calculate_trapmf_exception_1(self):
        my_x = 'a'
        my_abcd = [2, 2, 2, 2]

        my_exception = f"O parâmetro x precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                               my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trapmf exception 1')

    def test_calculate_trapmf_exception_2(self):
        my_x = 2
        my_abcd = ['a', 2, 2, 2]

        my_exception = f"O parâmetro não é um número!"
        with self.assertRaises(Exception) as context:
            _ = TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                               my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trapmf exception 2')

    def test_calculate_trapmf_exception_3(self):
        my_x = 2
        my_abcd = [2, 2, 2]

        my_exception = f"O parâmetro abc necessita de 4 valores!"
        with self.assertRaises(Exception) as context:
            _ = TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                               my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trapmf exception 3')

    def test_calculate_trapmf_exception_4(self):
        my_x = 2
        my_abcd = [2, 1, 2, 2]

        my_exception = f"Os parâmetros não estão em ordem crescente!"
        with self.assertRaises(Exception) as context:
            _ = TrapezoidalMembershipFunction.calculate_trapmf(my_x,
                                                               my_abcd)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trapmf exception 4')

class TriangularMembershipFunctionTest(unittest.TestCase):
    def test_calculate_trimf_1(self):
        my_x = 2.7
        my_abc = [1, 2, 3]
        my_result = 0.3

        self.assertEqual(
            my_result,
            round(TriangularMembershipFunction.calculate_trimf(my_x,
                                                               my_abc), 4),
            msg='Test calculate_trimf 1')

    def test_calculate_trimf_2(self):
        my_x = 1.5
        my_abc = [1, 2, 3]
        my_result = 0.5

        self.assertEqual(
            my_result,
            round(TriangularMembershipFunction.calculate_trimf(my_x,
                                                               my_abc), 4),
            msg='Test calculate_trimf 2')

    def test_calculate_trimf_3(self):
        my_x = 2
        my_abc = [1, 2, 3]
        my_result = 1

        self.assertEqual(
            my_result,
            round(TriangularMembershipFunction.calculate_trimf(my_x,
                                                               my_abc), 4),
            msg='Test calculate_trimf 3')

    def test_calculate_trimf_4(self):
        my_x = 2
        my_abc = [2, 2, 2]
        my_result = 1

        self.assertEqual(
            my_result,
            round(TriangularMembershipFunction.calculate_trimf(my_x,
                                                               my_abc), 4),
            msg='Test calculate_trimf 4')

    def test_calculate_trimf_5(self):
        my_x = 7
        my_abc = [1, 2, 3]
        my_result = 0

        self.assertEqual(
            my_result,
            round(TriangularMembershipFunction.calculate_trimf(my_x,
                                                               my_abc), 4),
            msg='Test calculate_trimf 5')

    def test_calculate_trimf_exception_1(self):
        my_x = 'a'
        my_abc = [1, 2, 3]

        my_exception = f"O parâmetro x precisa ser um número!"
        with self.assertRaises(Exception) as context:
            _ = TriangularMembershipFunction.calculate_trimf(my_x,
                                                             my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trimf exception 1')

    def test_calculate_trimf_exception_2(self):
        my_x = 2
        my_abc = ['a', 2, 3]

        my_exception = f"O parâmetro não é um número!"
        with self.assertRaises(Exception) as context:
            _ = TriangularMembershipFunction.calculate_trimf(my_x,
                                                             my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trimf exception 2')


    def test_calculate_trimf_exception_3(self):
        my_x = 2
        my_abc = [2, 3]

        my_exception = f"O parâmetro abc necessita de 3 valores!"
        with self.assertRaises(Exception) as context:
            _ = TriangularMembershipFunction.calculate_trimf(my_x,
                                                             my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trimf exception 3')

    def test_calculate_trimf_exception_4(self):
        my_x = 2
        my_abc = [2, 3, 1]

        my_exception = f"Os parâmetros não estão em ordem crescente!"
        with self.assertRaises(Exception) as context:
            _ = TriangularMembershipFunction.calculate_trimf(my_x,
                                                             my_abc)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test calculate_trimf exception 4')