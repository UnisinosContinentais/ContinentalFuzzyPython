"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest

from continentalfuzzy.dto.FuzzyControlCommandOutput import \
    FuzzyControlCommandOutput
from continentalfuzzy.dto.ProcessResult import ProcessResult


class FuzzyControlCommandOutputTest(unittest.TestCase):
    def test_create_fuzzy_control_command_output(self):
        my_command_output = FuzzyControlCommandOutput()

        self.assertEqual(ProcessResult.RESULT_ERROR,
                         my_command_output.status,
                         msg='Test status')
        self.assertEqual(list(),
                         my_command_output.messages,
                         msg='Test messages')

        self.assertEqual(my_command_output.result, 0.0,
                         msg='Test result')

    def test_property_status(self):
        my_command_output = FuzzyControlCommandOutput()
        my_result = 10.7
        my_command_output.result = my_result

        self.assertEqual(my_result,
                         my_command_output.result,
                         msg='Test result')
