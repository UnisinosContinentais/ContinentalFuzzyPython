"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.dto.FuzzyControlCommandInput import \
    FuzzyControlCommandInput


class FuzzyControlCommandInputTest(unittest.TestCase):
    def test_create_fuzzy_control_command_input(self):
        my_command_input = FuzzyControlCommandInput()

        self.assertIsNone(my_command_input.filename, msg='Test filename')
        self.assertEqual(dict(),my_command_input.fuzzy_inputs, msg='Test inputs')
        self.assertIsNone(my_command_input.fuzzy_output, msg='Test outputs')

    def test_property_filename(self):
        my_command_input = FuzzyControlCommandInput()
        my_filename = 'teste.fis'
        my_command_input.filename = my_filename

        self.assertEqual(my_filename,
                         my_command_input.filename,
                         msg='Test filename')

    def test_set_filename(self):
        my_command_input = FuzzyControlCommandInput()
        my_filename = 'teste.fis'
        my_command_input.set_filename(my_filename)

        self.assertEqual(my_filename,
                         my_command_input.filename,
                         msg='Test set_filename')

    def test_property_fuzzy_inputs(self):
        my_command_input = FuzzyControlCommandInput()
        my_inputs = {'Distance': 1,
                     'Slope': 2,
                     'Depth': 3}
        my_command_input.fuzzy_inputs = my_inputs

        self.assertEqual(my_inputs,
                         my_command_input.fuzzy_inputs,
                         msg='Test fuzzy_inputs')

    def test_add_fuzzy_inputs(self):
        my_command_input = FuzzyControlCommandInput()
        my_inputs = {'Distance': 1}
        my_command_input.add_fuzzy_inputs('Distance', 1)

        self.assertEqual(my_inputs,
                         my_command_input.fuzzy_inputs,
                         msg='Test add_fuzzy_inputs')

    def test_property_outputs(self):
        my_command_input = FuzzyControlCommandInput()
        my_outputs = 'output1'
        my_command_input.fuzzy_output = my_outputs

        self.assertEqual(my_outputs,
                         my_command_input.fuzzy_output,
                         msg='Test outputs')

    def test_set_fuzzy_output(self):
        my_command_input = FuzzyControlCommandInput()
        my_output = 'output1'
        my_command_input.set_fuzzy_output(my_output)

        self.assertEqual(my_output,
                         my_command_input.fuzzy_output,
                         msg='Test set_fuzzy_output')

    def test_property_use_dict_facies_association(self):
        my_command_input = FuzzyControlCommandInput()
        my_use_dict_facies_association = True
        my_command_input.use_dict_facies_association = my_use_dict_facies_association

        self.assertEqual(my_use_dict_facies_association,
                         my_command_input.use_dict_facies_association,
                         msg='Test use_dict_facies_association')

    def test_set_use_dict_facies_association(self):
        my_command_input = FuzzyControlCommandInput()
        my_use_dict_facies_association = True
        my_command_input.set_use_dict_facies_association(my_use_dict_facies_association)

        self.assertEqual(my_use_dict_facies_association,
                         my_command_input.use_dict_facies_association,
                         msg='Test set_use_dict_facies_association')