"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.dto.AbstractDtoResult import AbstractDtoResult
from continentalfuzzy.dto.ProcessResult import ProcessResult


class AbstractDtoResultTest(unittest.TestCase):
    def test_create_abstract_dto_result(self):
        my_abs_dto_result = AbstractDtoResult()

        self.assertEqual(ProcessResult.RESULT_ERROR,
                         my_abs_dto_result.status,
                         msg='Test status')
        self.assertEqual(list(),
                         my_abs_dto_result.messages,
                         msg='Test messages')

    def test_property_status(self):
        my_abs_dto_result = AbstractDtoResult()
        my_result = ProcessResult.RESULT_SUCCESS
        my_abs_dto_result.status = my_result

        self.assertEqual(my_result,
                         my_abs_dto_result.status,
                         msg='Test status')

    def test_add_message(self):
        my_abs_dto_result = AbstractDtoResult()
        my_message = ['message']
        my_abs_dto_result.add_message(my_message[0])

        self.assertEqual(my_message,
                         my_abs_dto_result.messages,
                         msg='Test message')
