"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
import numpy as np
import skfuzzy as fuzz
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.service.SystemService import SystemService
from continentalfuzzy.util.FuzzyUtil import FuzzyUtil


class FuzzyUtilTest(unittest.TestCase):
    def test_create_universe_trimf(self):
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

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=1',
                    "MF1='trimf':'trimf',[0 0.1 0.2]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system

        my_input = my_system.inputs[1]
        my_range = my_input.range

        my_abc = [0, 0.1, 0.2, 1]

        # Cria o universo do antecedente
        my_universe = FuzzyUtil.create_universe(my_range, my_input.mfs)

        self.assertTrue((my_universe == my_abc).all(),
                        msg='Test create_universe trimf')

    def test_create_universe_trapmf(self):
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

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=1',
                    "MF1='trapmf':'trapmf',[0.1 0.2 0.25 0.3]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system

        my_input = my_system.inputs[1]
        my_range = my_input.range

        my_abcd = [0, 0.1, 0.2, 0.25, 0.3, 1]

        # Cria o universo do antecedente
        my_universe = FuzzyUtil.create_universe(my_range, my_input.mfs)

        self.assertTrue((my_universe == my_abcd).all(),
                        msg='Test create_universe trapmf')

    def test_create_universe_gaussmf(self):
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

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=1',
                    "MF1='gaussmf':'gaussmf',[0.42 0.3]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system

        my_input = my_system.inputs[1]
        my_range = my_input.range

        my_values = np.array([0., 0.01151515, 0.04545455, 0.07939394,
                              0.11333333, 0.14727273, 0.18121212, 0.21515152,
                              0.24909091, 0.2830303, 0.3169697, 0.35090909,
                              0.38484848, 0.41878788, 0.45272727, 0.48666667,
                              0.52060606, 0.55454545, 0.58848485, 0.62242424,
                              0.65636364, 0.69030303, 0.72424242, 0.75818182,
                              0.79212121, 0.82606061, 0.86, 0.89393939,
                              0.92787879, 0.96181818, 0.99575758, 1.])

        # Cria o universo do antecedente
        my_universe = (FuzzyUtil.create_universe(my_range, my_input.mfs))
        my_round_universe = np.round(my_universe, 8)

        self.assertTrue((my_round_universe == my_values).all(),
                        msg='Test create_universe gaussmf')

    def test_create_universe_gauss2mf(self):
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

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=1',
                    "MF1='gauss2mf':'gauss2mf',[0.1 0.4 0.1 0.6]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system

        my_input = my_system.inputs[1]
        my_range = my_input.range

        my_values = np.array([0., 0.00816327, 0.01632653, 0.0244898, 0.03265306,
                              0.04081633, 0.04897959, 0.05714286, 0.06530612,
                              0.07346939, 0.08163265, 0.08979592, 0.09795918,
                              0.10612245, 0.11428571, 0.12244898, 0.13061224,
                              0.13877551, 0.14693878, 0.15510204, 0.16326531,
                              0.17142857, 0.17959184, 0.1877551, 0.19591837,
                              0.20408163, 0.2122449, 0.22040816, 0.22857143,
                              0.23673469, 0.24489796, 0.25306122, 0.26122449,
                              0.26938776, 0.27755102, 0.28571429, 0.29387755,
                              0.30204082, 0.31020408, 0.31836735, 0.32653061,
                              0.33469388, 0.34285714, 0.35102041, 0.35918367,
                              0.36734694, 0.3755102, 0.38367347, 0.39183673,
                              0.4, 0.6, 0.60816327, 0.61632653, 0.6244898,
                              0.63265306, 0.64081633, 0.64897959, 0.65714286,
                              0.66530612, 0.67346939, 0.68163265, 0.68979592,
                              0.69795918, 0.70612245, 0.71428571, 0.72244898,
                              0.73061224, 0.73877551, 0.74693878, 0.75510204,
                              0.76326531, 0.77142857, 0.77959184, 0.7877551,
                              0.79591837, 0.80408163, 0.8122449, 0.82040816,
                              0.82857143, 0.83673469, 0.84489796, 0.85306122,
                              0.86122449, 0.86938776, 0.87755102, 0.88571429,
                              0.89387755, 0.90204082, 0.91020408, 0.91836735,
                              0.92653061, 0.93469388, 0.94285714, 0.95102041,
                              0.95918367, 0.96734694, 0.9755102, 0.98367347,
                              0.99183673, 1])

        # Cria o universo do antecedente
        my_universe = (FuzzyUtil.create_universe(my_range, my_input.mfs))
        my_round_universe = np.round(my_universe, 8)

        self.assertTrue((my_round_universe == my_values).all(),
                        msg='Test create_universe gauss2mf')

    def test_create_universe_all_mf(self):
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

        my_list = [["Name='Distance'", 'Range=[0 1]', 'NumMFs=4',
                    "MF1='trimf':'trimf',[0 0.1 0.2]",
                    "MF2='trapmf':'trapmf',[0.1 0.2 0.25 0.3]",
                    "MF3='gaussmf':'gaussmf',[0.42 0.3]",
                    "MF4='gauss2mf':'gauss2mf',[0.1 0.4 0.1 0.6]"]]

        systemService.create_inputs_from_list(my_list)
        my_system = systemService.system

        my_input = my_system.inputs[1]
        my_range = my_input.range

        my_values = np.array([0., 0.00816327, 0.01151515, 0.01632653, 0.0244898,
                              0.03265306, 0.04081633, 0.04545455, 0.04897959,
                              0.05714286, 0.06530612, 0.07346939, 0.07939394,
                              0.08163265, 0.08979592, 0.09795918, 0.1,
                              0.10612245, 0.11333333, 0.11428571, 0.12244898,
                              0.13061224, 0.13877551, 0.14693878, 0.14727273,
                              0.15510204, 0.16326531, 0.17142857, 0.17959184,
                              0.18121212, 0.1877551, 0.19591837, 0.2,
                              0.20408163, 0.2122449, 0.21515152, 0.22040816,
                              0.22857143, 0.23673469, 0.24489796, 0.24909091,
                              0.25, 0.25306122, 0.26122449, 0.26938776,
                              0.27755102, 0.2830303, 0.28571429, 0.29387755,
                              0.3, 0.30204082, 0.31020408, 0.3169697,
                              0.31836735, 0.32653061, 0.33469388, 0.34285714,
                              0.35090909, 0.35102041, 0.35918367, 0.36734694,
                              0.3755102, 0.38367347, 0.38484848, 0.39183673,
                              0.4, 0.41878788, 0.45272727, 0.48666667,
                              0.52060606, 0.55454545, 0.58848485, 0.6,
                              0.60816327, 0.61632653, 0.62242424, 0.6244898,
                              0.63265306, 0.64081633, 0.64897959, 0.65636364,
                              0.65714286, 0.66530612, 0.67346939, 0.68163265,
                              0.68979592, 0.69030303, 0.69795918, 0.70612245,
                              0.71428571, 0.72244898, 0.72424242, 0.73061224,
                              0.73877551, 0.74693878, 0.75510204, 0.75818182,
                              0.76326531, 0.77142857, 0.77959184, 0.7877551,
                              0.79212121, 0.79591837, 0.80408163, 0.8122449,
                              0.82040816, 0.82606061, 0.82857143, 0.83673469,
                              0.84489796, 0.85306122, 0.86, 0.86122449,
                              0.86938776, 0.87755102, 0.88571429, 0.89387755,
                              0.89393939, 0.90204082, 0.91020408, 0.91836735,
                              0.92653061, 0.92787879, 0.93469388, 0.94285714,
                              0.95102041, 0.95918367, 0.96181818, 0.96734694,
                              0.9755102, 0.98367347, 0.99183673, 0.99575758,
                              1])

        # Cria o universo do antecedente
        my_universe = FuzzyUtil.create_universe(my_range, my_input.mfs)
        my_round_universe = np.round(my_universe, 8)

        self.assertTrue((my_round_universe == my_values).all(),
                        msg='Test create_universe all mf')

    def test_get_trimf_values(self):
        my_name = "Test Name"
        my_abc = [1, 2, 3]
        my_trimf = TriMF(my_name, my_abc)
        my_trimf_values = FuzzyUtil.get_trimf_values(my_trimf)
        self.assertTrue((my_trimf_values == my_abc),
                        msg='Test get_trimf_values')

    def test_get_trapmf_values(self):
        my_name = "Test Name"
        my_abcd = [1, 2, 3, 4]
        my_trapmf = TrapMF(my_name, my_abcd)
        my_trapmf_values = FuzzyUtil.get_trapmf_values(my_trapmf)
        self.assertTrue((my_trapmf_values == my_abcd),
                        msg='Test get_trapmf_values')

    def test_get_gaussmf_values(self):
        my_name = "Test Name"
        my_sigma = 1
        my_mean = 0
        my_gaussmf = GaussMF(my_name, my_sigma, my_mean)
        my_gaussmf_values = FuzzyUtil.get_gaussmf_values(my_gaussmf)

        my_min = my_mean - (my_sigma * 4)
        my_max = my_mean + (my_sigma * 4)
        my_values = np.linspace(my_min,
                                my_max,
                                num=100,
                                endpoint=True)

        self.assertTrue((my_gaussmf_values == my_values).all(),
                        msg='Test get_gaussmf_values')

    def test_get_gauss2mf_values(self):
        my_name = "Test Name"
        my_sigma1 = 1
        my_mean1 = 0
        my_sigma2 = 10
        my_mean2 = 5
        my_gauss2mf = Gauss2MF(my_name,
                               my_sigma1,
                               my_mean1,
                               my_sigma2,
                               my_mean2)
        my_gaussmf2_values = FuzzyUtil.get_gauss2mf_values(my_gauss2mf)

        my_fist = np.linspace(my_mean1 - (my_sigma1 * 4),
                              my_mean1,
                              num=50,
                              endpoint=True)
        my_second = np.linspace(my_mean2,
                                my_mean2 + (my_sigma2 * 4),
                                num=50,
                                endpoint=True)
        my_values = np.concatenate((my_fist, my_second))

        self.assertTrue((my_gaussmf2_values == my_values).all(),
                        msg='Test get_gauss2mf_values')

    def test_membership_function_trimf(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        # MF 1
        my_trimf_name = "Test trimf"
        my_trimf_abc = [1, 2, 3]
        my_trimf = TriMF(my_trimf_name, my_trimf_abc)

        my_fuzzy_trimf = fuzz.trimf(x=my_universe, abc=my_trimf_abc)

        my_func_fuzzy = FuzzyUtil.membership_function(mf=my_trimf,
                                                      univ=my_universe)

        self.assertTrue((my_fuzzy_trimf == my_func_fuzzy).all(),
                        msg='Test membership_function trimf')

    def test_membership_function_trapmf(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        # MF 1
        my_trapmf_name = "Test trapmf"
        my_trapmf_abcd = [1, 2, 3, 4]
        my_trapmf = TrapMF(my_trapmf_name, my_trapmf_abcd)

        my_fuzzy_trapmf = fuzz.trapmf(x=my_universe, abcd=my_trapmf_abcd)

        my_func_fuzzy = FuzzyUtil.membership_function(mf=my_trapmf,
                                                      univ=my_universe)

        self.assertTrue((my_fuzzy_trapmf == my_func_fuzzy).all(),
                        msg='Test membership_function trapmf')

    def test_membership_function_gaussmf(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        # MF 1
        my_gaussmf_name = "Test gaussmf"
        my_gaussmf_sigma = 1
        my_gaussmf_mean = 0
        my_gaussmf = GaussMF(my_gaussmf_name,
                             my_gaussmf_sigma,
                             my_gaussmf_mean)

        my_fuzzy_gaussmf = fuzz.gaussmf(x=my_universe,
                                        sigma=my_gaussmf_sigma,
                                        mean=my_gaussmf_mean)

        my_func_fuzzy = FuzzyUtil.membership_function(mf=my_gaussmf,
                                                      univ=my_universe)

        self.assertTrue((my_fuzzy_gaussmf == my_func_fuzzy).all(),
                        msg='Test membership_function gaussmf')

    def test_membership_function_gaus2mf(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        # MF 1
        my_gauss2mf_name = "Test gauss2mf"
        my_gauss2mf_sigma1 = 1
        my_gauss2mf_mean1 = 0
        my_gauss2mf_sigma2 = 2
        my_gauss2mf_mean2 = 1
        my_gauss2mf = Gauss2MF(my_gauss2mf_name,
                               my_gauss2mf_sigma1,
                               my_gauss2mf_mean1,
                               my_gauss2mf_sigma2,
                               my_gauss2mf_mean2)

        my_fuzzy_gauss2mf = fuzz.gauss2mf(x=my_universe,
                                          sigma1=my_gauss2mf_sigma1,
                                          mean1=my_gauss2mf_mean1,
                                          sigma2=my_gauss2mf_sigma2,
                                          mean2=my_gauss2mf_mean2)

        my_func_fuzzy = FuzzyUtil.membership_function(mf=my_gauss2mf,
                                                      univ=my_universe)

        self.assertTrue((my_fuzzy_gauss2mf == my_func_fuzzy).all(),
                        msg='Test membership_function gauss2mf')

    def test_membership_function_exception_1(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        my_exception = ("O parâmetro não é uma instância da classe "
                        "FISMembershipFunc!")
        with self.assertRaises(Exception) as context:
            _ = FuzzyUtil.membership_function(mf=[10], univ=my_universe)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test membership_function exception 1')

    def test_membership_function_exception_2(self):
        my_universe = 'a'

        # MF 1
        my_gauss2mf_name = "Test gauss2mf"
        my_gauss2mf_sigma1 = 1
        my_gauss2mf_mean1 = 0
        my_gauss2mf_sigma2 = 2
        my_gauss2mf_mean2 = 1
        my_gauss2mf = Gauss2MF(my_gauss2mf_name,
                               my_gauss2mf_sigma1,
                               my_gauss2mf_mean1,
                               my_gauss2mf_sigma2,
                               my_gauss2mf_mean2)

        my_exception = "O parâmetro não é um numpy array!"
        with self.assertRaises(Exception) as context:
            _ = FuzzyUtil.membership_function(mf=my_gauss2mf, univ=my_universe)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test membership_function exception 2')

    def test_membership_function_exception_3(self):
        my_universe = np.linspace(0, 10, num=100, dtype=np.float64)

        # MF 1
        my_gauss2mf_name = "Test gauss2mf"
        my_gauss2mf_sigma1 = 1
        my_gauss2mf_mean1 = 0
        my_gauss2mf_sigma2 = 2
        my_gauss2mf_mean2 = 1
        my_gauss2mf = Gauss2MF(my_gauss2mf_name,
                               my_gauss2mf_sigma1,
                               my_gauss2mf_mean1,
                               my_gauss2mf_sigma2,
                               my_gauss2mf_mean2)
        my_gauss2mf._MembershipFunction__function = None

        my_exception = "Função de pertinência não implementada!"
        with self.assertRaises(Exception) as context:
            _ = FuzzyUtil.membership_function(mf=my_gauss2mf, univ=my_universe)

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test membership_function exception 3')
