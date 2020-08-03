"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.Variable import Variable
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.domain.variable.Output import Output


class VariableTest(unittest.TestCase):
    def test_create_variable_1(self):
        my_variable = Variable()

        self.assertIsNone(my_variable.name, msg='Test name')
        self.assertEqual(list(), my_variable.range, msg='Test range')
        self.assertIsNone(my_variable.num_mfs, msg='Test num_mfs')
        self.assertEqual(dict(), my_variable.mfs, msg='Test mfs')

    def test_property_name(self):
        my_variable = Variable()
        my_name = 'test name'
        my_variable.name = my_name

        self.assertEqual(my_name, my_variable.name, msg='Test name')

    def test_property_name_exception_1(self):
        my_variable = Variable()
        my_name = [10, 20]

        my_exception = "O nome não é uma string!"
        with self.assertRaises(Exception) as context:
            my_variable.name = my_name

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property name exception 1')

    def test_property_range(self):
        my_variable = Variable()
        my_range = [0, 1.7]
        my_variable.range = my_range

        self.assertEqual(my_range, my_variable.range, msg='Test range')

    def test_property_range_exception_1_value(self):
        my_variable = Variable()
        my_range = [0]
        my_exception = ("A lista com a amplitude do conjunto da variável "
                        "precisa ter dois números!")
        with self.assertRaises(Exception) as context:
            my_variable.range = my_range

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property range exception 1 value')

    def test_property_range_exception_3_values(self):
        my_variable = Variable()
        my_range = [0, 1, 2]
        my_exception = ("A lista com a amplitude do conjunto da variável "
                        "precisa ter dois números!")
        with self.assertRaises(Exception) as context:
            my_variable.range = my_range

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property range exception 3 values')

    def test_property_range_exception_1(self):
        my_variable = Variable()
        my_range = {1: 'var'}
        my_exception = "O parâmetro não é uma lista!"
        with self.assertRaises(Exception) as context:
            my_variable.range = my_range

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property range exception 1')

    def test_property_range_exception_2(self):
        my_variable = Variable()
        my_range = [1, 'var']
        my_exception = "Um dos valores não é do tipo float!"
        with self.assertRaises(Exception) as context:
            my_variable.range = my_range

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property range exception 2')

    def test_property_num_mfs_exception_1(self):
        my_variable = Variable()
        my_num_mfs = '45'
        my_exception = "O parâmetro não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_variable.num_mfs = my_num_mfs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property num_mfs exception 1')

    def test_property_num_mfs(self):
        my_variable = Variable()
        my_num_mfs = 45
        my_variable.num_mfs = my_num_mfs

        self.assertEqual(my_num_mfs, my_variable.num_mfs, msg='Test num_mfs')

    def test_create_variable_2(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2
        my_mfs = mf_dict

        my_variable = Variable(my_name, my_range, my_num_mfs, my_mfs)

        self.assertEqual(my_name, my_variable.name, msg='Test name')
        self.assertEqual(my_range, my_variable.range, msg='Test range')
        self.assertEqual(my_num_mfs, my_variable.num_mfs, msg='Test num_mfs')
        self.assertEqual(mf_dict, my_variable.mfs, msg='Test mfs')

        self.assertEqual(my_trimf_name, my_variable.mfs.get(1).name,
                         msg='Test mfs 1 name')
        self.assertEqual(Functions.trimf, my_variable.mfs.get(1).function,
                         msg='Test mfs 1 function')
        self.assertEqual(my_trimf_abc, my_variable.mfs.get(1).abc,
                         msg='Test mfs 1 abc')

        self.assertEqual(my_gaussmf_name, my_variable.mfs.get(2).name,
                         msg='Test mfs 2 name')
        self.assertEqual(Functions.gaussmf, my_variable.mfs.get(2).function,
                         msg='Test mfs 2 function')
        self.assertEqual(my_gaussmf_sigma, my_variable.mfs.get(2).sigma,
                         msg='Test mfs 2 sigma')
        self.assertEqual(my_gaussmf_mean, my_variable.mfs.get(2).mean,
                         msg='Test mfs 2 mean')

    def test_property_mfs(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2
        my_mfs = mf_dict

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs
        my_variable.mfs = my_mfs

        self.assertEqual(mf_dict, my_variable.mfs, msg='Test mfs')

        self.assertEqual(my_trimf_name, my_variable.mfs.get(1).name,
                         msg='Test mfs 1 name')
        self.assertEqual(Functions.trimf, my_variable.mfs.get(1).function,
                         msg='Test mfs 1 function')
        self.assertEqual(my_trimf_abc, my_variable.mfs.get(1).abc,
                         msg='Test mfs 1 abc')

        self.assertEqual(my_gaussmf_name, my_variable.mfs.get(2).name,
                         msg='Test mfs 2 name')
        self.assertEqual(Functions.gaussmf, my_variable.mfs.get(2).function,
                         msg='Test mfs 2 function')
        self.assertEqual(my_gaussmf_sigma, my_variable.mfs.get(2).sigma,
                         msg='Test mfs 2 sigma')
        self.assertEqual(my_gaussmf_mean, my_variable.mfs.get(2).mean,
                         msg='Test mfs 2 mean')

    def test_property_mfs_exception_1(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_mfs = mf_dict

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range

        my_exception = ("O número de funções de pertinências não foi "
                        "informado!")
        with self.assertRaises(Exception) as context:
            my_variable.mfs = my_mfs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mfs exception 1')

    def test_property_mfs_exception_2(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_mfs = mf_dict
        my_num_mfs = 7

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_exception = ("A quantidade de funções de pertinência é diferente "
                        "da informada!")
        with self.assertRaises(Exception) as context:
            my_variable.mfs = my_mfs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mfs exception 2')

    def test_property_mfs_exception_3(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {'a': my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_mfs = mf_dict
        my_num_mfs = 2

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_exception = "A chave do dicionário não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_variable.mfs = my_mfs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mfs exception 3')

    def test_property_mfs_exception_4(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        mf_dict = {1: my_trimf,
                   2: [1, 2, 3]}

        my_name = "Test Name"
        my_range = [0, 10]
        my_mfs = mf_dict
        my_num_mfs = 2

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_exception = ("O valor não é uma instância da classe "
                        "FISMembershipFunc!")
        with self.assertRaises(Exception) as context:
            my_variable.mfs = my_mfs

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property mfs exception 4')

    def test_property_add_mfs(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs
        my_variable.add_mfs(1, my_trimf)
        my_variable.add_mfs(2, my_gaussmf)

        self.assertEqual(mf_dict, my_variable.mfs, msg='Test mfs')

        self.assertEqual(my_trimf_name, my_variable.mfs.get(1).name,
                         msg='Test mfs 1 name')
        self.assertEqual(Functions.trimf, my_variable.mfs.get(1).function,
                         msg='Test mfs 1 function')
        self.assertEqual(my_trimf_abc, my_variable.mfs.get(1).abc,
                         msg='Test mfs 1 abc')

        self.assertEqual(my_gaussmf_name, my_variable.mfs.get(2).name,
                         msg='Test mfs 2 name')
        self.assertEqual(Functions.gaussmf, my_variable.mfs.get(2).function,
                         msg='Test mfs 2 function')
        self.assertEqual(my_gaussmf_sigma, my_variable.mfs.get(2).sigma,
                         msg='Test mfs 2 sigma')
        self.assertEqual(my_gaussmf_mean, my_variable.mfs.get(2).mean,
                         msg='Test mfs 2 mean')

    def test_property_add_mfs_exception_1(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        my_name = "Test Name"
        my_range = [0, 10]

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range

        my_exception = ("O número de funções de pertinências não foi "
                        "informado!")
        with self.assertRaises(Exception) as context:
            my_variable.add_mfs(1, my_trimf)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property add_mfs exception 1')

    def test_property_add_mfs_exception_2(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 1

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_variable.add_mfs(1, my_trimf)

        my_exception = ("Não é possível cadastrar mais funções de "
                        "pertinências!")
        with self.assertRaises(Exception) as context:
            my_variable.add_mfs(2, my_gaussmf)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property add_mfs exception 2')

    def test_property_add_mfs_exception_3(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_exception = "A variável número não é um número inteiro!"
        with self.assertRaises(Exception) as context:
            my_variable.add_mfs('a', my_trimf)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property add_mfs exception 3')

    def test_property_add_mfs_exception_4(self):

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2

        my_variable = Variable()
        my_variable.name = my_name
        my_variable.range = my_range
        my_variable.num_mfs = my_num_mfs

        my_exception = ("O valor não é uma instância da classe "
                        "FISMembershipFunc!")
        with self.assertRaises(Exception) as context:
            my_variable.add_mfs(1, [16, 23])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test property add_mfs exception 4')


class InputTest(unittest.TestCase):
    def test_create_input_1(self):
        my_input = Input()

        self.assertIsNone(my_input.name, msg='Test name')
        self.assertEqual('antecedent', my_input.var_type, msg='Test var_type')
        self.assertEqual(list(), my_input.range, msg='Test range')
        self.assertIsNone(my_input.num_mfs, msg='Test num_mfs')
        self.assertEqual(dict(), my_input.mfs, msg='Test mfs')

    def test_create_input_2(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2
        my_mfs = mf_dict

        my_variable = Input(my_name, my_range, my_num_mfs, my_mfs)

        self.assertEqual(my_name, my_variable.name, msg='Test name')
        self.assertEqual('antecedent', my_variable.var_type,
                         msg='Test var_type')
        self.assertEqual(my_range, my_variable.range, msg='Test range')
        self.assertEqual(my_num_mfs, my_variable.num_mfs, msg='Test num_mfs')
        self.assertEqual(mf_dict, my_variable.mfs, msg='Test mfs')

        self.assertEqual(my_trimf_name, my_variable.mfs.get(1).name,
                         msg='Test mfs 1 name')
        self.assertEqual(Functions.trimf, my_variable.mfs.get(1).function,
                         msg='Test mfs 1 function')
        self.assertEqual(my_trimf_abc, my_variable.mfs.get(1).abc,
                         msg='Test mfs 1 abc')

        self.assertEqual(my_gaussmf_name, my_variable.mfs.get(2).name,
                         msg='Test mfs 2 name')
        self.assertEqual(Functions.gaussmf, my_variable.mfs.get(2).function,
                         msg='Test mfs 2 function')
        self.assertEqual(my_gaussmf_sigma, my_variable.mfs.get(2).sigma,
                         msg='Test mfs 2 sigma')
        self.assertEqual(my_gaussmf_mean, my_variable.mfs.get(2).mean,
                         msg='Test mfs 2 mean')

    def test_property_var_type(self):
        my_input = Input()
        my_var_type = 'antecedent'

        self.assertEqual(my_var_type, my_input.var_type, msg='Test var_type')


class OutputTest(unittest.TestCase):
    def test_create_output_1(self):
        my_output = Output()

        self.assertIsNone(my_output.name, msg='Test name')
        self.assertEqual('consequent', my_output.var_type, msg='Test var_type')
        self.assertEqual(list(), my_output.range, msg='Test range')
        self.assertIsNone(my_output.num_mfs, msg='Test num_mfs')
        self.assertEqual(dict(), my_output.mfs, msg='Test mfs')

    def test_create_output_2(self):
        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        # MF 2
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        mf_dict = {1: my_trimf,
                   2: my_gaussmf}

        my_name = "Test Name"
        my_range = [0, 10]
        my_num_mfs = 2
        my_mfs = mf_dict

        my_variable = Output(my_name, my_range, my_num_mfs, my_mfs)

        self.assertEqual(my_name, my_variable.name, msg='Test name')
        self.assertEqual('consequent', my_variable.var_type,
                         msg='Test var_type')
        self.assertEqual(my_range, my_variable.range, msg='Test range')
        self.assertEqual(my_num_mfs, my_variable.num_mfs, msg='Test num_mfs')
        self.assertEqual(mf_dict, my_variable.mfs, msg='Test mfs')

        self.assertEqual(my_trimf_name, my_variable.mfs.get(1).name,
                         msg='Test mfs 1 name')
        self.assertEqual(Functions.trimf, my_variable.mfs.get(1).function,
                         msg='Test mfs 1 function')
        self.assertEqual(my_trimf_abc, my_variable.mfs.get(1).abc,
                         msg='Test mfs 1 abc')

        self.assertEqual(my_gaussmf_name, my_variable.mfs.get(2).name,
                         msg='Test mfs 2 name')
        self.assertEqual(Functions.gaussmf, my_variable.mfs.get(2).function,
                         msg='Test mfs 2 function')
        self.assertEqual(my_gaussmf_sigma, my_variable.mfs.get(2).sigma,
                         msg='Test mfs 2 sigma')
        self.assertEqual(my_gaussmf_mean, my_variable.mfs.get(2).mean,
                         msg='Test mfs 2 mean')

    def test_property_var_type(self):
        my_output = Output()
        my_var_type = 'consequent'

        self.assertEqual(my_var_type, my_output.var_type, msg='Test var_type')
