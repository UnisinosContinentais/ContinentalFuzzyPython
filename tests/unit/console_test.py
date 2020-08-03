"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from io import StringIO
import unittest
from unittest.mock import patch
from continentalfuzzy.console.console import TestFuzzy

class TestFuzzyTest(unittest.TestCase):
    def test_validate_args(self):
        TestFuzzy.validate_args(["tests/test_data/EnvironmentMamdani.fis",
                                 0.1,
                                 0.2,
                                 0.3])

    def test_validate_args_exception_1(self):
        my_exception = "É necessário informar 4 argumentos!"
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/EnvironmentMamdani.fis",
                                     0.2,
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 1')

    def test_validate_args_exception_2(self):
        my_exception = "O primeiro argumento precisa ser o nome do arquivo!"
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args([[1, 2, 3],
                                     0.1,
                                     0.2,
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 2')

    def test_validate_args_exception_3(self):
        my_exception = ("O arquivo tests/test_data/EnvironmntMamdani.fis não "
                        "foi encontrado!")
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/EnvironmntMamdani.fis",
                                     0.1,
                                     0.2,
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 3')

    def test_validate_args_exception_4(self):
        my_exception = ("O arquivo a ser importado precisar ter a extensão "
                        ".fis!")
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/test.txt",
                                     0.1,
                                     0.2,
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 4')

    def test_validate_args_exception_5(self):
        my_exception = "O argumento da distância não é do tipo float!"
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/EnvironmentMamdani.fis",
                                     'a',
                                     0.2,
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 5')

    def test_validate_args_exception_6(self):
        my_exception = "O argumento da declividade não é do tipo float!"
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/EnvironmentMamdani.fis",
                                     0.1,
                                     'a',
                                     0.3])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 6')

    def test_validate_args_exception_7(self):
        my_exception = "O argumento da paleobatimetria não é do tipo float!"
        with self.assertRaises(Exception) as context:
            TestFuzzy.validate_args(["tests/test_data/EnvironmentMamdani.fis",
                                     0.1,
                                     0.2,
                                     'a'])

        self.assertEqual(my_exception, context.exception.args[0],
                         msg='Test validate_args exception 7')

    def test_execute(self):
        testFuzzy = TestFuzzy()
        with patch('sys.stdout', new_callable=StringIO) as buffer:
            testFuzzy.execute(["tests/test_data/EnvironmentMamdani.fis",
                               0.1,
                               0.2,
                               0.3])
        my_output = buffer.getvalue()
        correct_output = ("['Processo executado com sucesso!']\nProcessResult."
                          "RESULT_SUCCESS\n1.801431957597389\n")

        self.assertEqual(my_output, correct_output,
                         msg='Test execute')

    def test_main(self):
        pass

