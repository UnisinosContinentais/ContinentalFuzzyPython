"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.applicationservice.FuzzyControlApplicationService import FuzzyControlApplicationService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput
from continentalfuzzy.dto.ProcessResult import ProcessResult


class FuzzyControlApplicationServiceTest(unittest.TestCase):
    def test_process_fuzzy_control_1(self):
        my_filename = "tests/test_data/EnvironmentMamdani.fis"

        fuzzyControlCommandInput = FuzzyControlCommandInput()

        fuzzyControlCommandInput.filename = my_filename
        fuzzyControlCommandInput.fuzzy_inputs = {'Distance': 0.3,
                                                 'Slope': 0.0015,
                                                 'Depth': 50}
        fuzzyControlCommandInput.fuzzy_output = 'output1'

        fuzzyControlApplicationService = FuzzyControlApplicationService()
        result = fuzzyControlApplicationService.process_fuzzy_control(
            fuzzyControlCommandInput)

        self.assertEqual(result.messages[0], 'Processo executado com sucesso!',
                         msg='Test messages')

        self.assertEqual(result.status, ProcessResult.RESULT_SUCCESS,
                         msg='Test status')

        self.assertEqual(round(result.result, 4), 1.6539,
                         msg='Test result')

    def test_process_fuzzy_control_2(self):
        my_filename = "tests/test_data/Tip_fuzzylite_2.fis"

        fuzzyControlCommandInput = FuzzyControlCommandInput()

        fuzzyControlCommandInput.filename = my_filename
        fuzzyControlCommandInput.fuzzy_inputs = {'service': 3,
                                                 'food': 7}
        fuzzyControlCommandInput.fuzzy_output = 'Tip'

        fuzzyControlApplicationService = FuzzyControlApplicationService()
        result = fuzzyControlApplicationService.process_fuzzy_control(
            fuzzyControlCommandInput)

        self.assertEqual(result.messages[0], 'Processo executado com sucesso!',
                         msg='Test messages')

        self.assertEqual(result.status, ProcessResult.RESULT_SUCCESS,
                         msg='Test status')

        self.assertEqual(round(result.result, 4), 18.35,
                         msg='Test result')

    def test_process_fuzzy_control_exception(self):
        my_filename = "tests/test_data/EnvironmentMamdani.fis"

        fuzzyControlCommandInput = FuzzyControlCommandInput()

        fuzzyControlCommandInput.filename = my_filename
        fuzzyControlCommandInput.fuzzy_output = 'output1'

        fuzzyControlApplicationService = FuzzyControlApplicationService()
        result = fuzzyControlApplicationService.process_fuzzy_control(
            fuzzyControlCommandInput)

        self.assertEqual(result.messages[0],
                         'Não foi possível executar o processo do fuzzy!',
                         msg='Test messages')

        self.assertEqual(result.status, ProcessResult.RESULT_ERROR,
                         msg='Test status')

        self.assertEqual(round(result.result, 4), 0.0,
                         msg='Test result')
