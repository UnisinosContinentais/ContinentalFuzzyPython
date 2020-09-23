"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Dict
import numpy as np


class FuzzyControlCommandInput:
    def __init__(self):
        self.__filename = None
        self.__num_rows = 0
        self.__num_cols = 0
        self.__matrix = None
        self.__fuzzy_inputs = dict()
        self.__fuzzy_inputs_matrix = dict()
        self.__fuzzy_output = None
        self.__use_dict_facies_association = True

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, p_filename: str):
        self.__filename = p_filename

    def set_filename(self, p_filename: str):
        self.__filename = p_filename

    def set_matrix_dimension(self, p_num_rows: int, p_num_cols: int):
        self.__num_rows = p_num_rows
        self.__num_cols = p_num_cols

    @property
    def fuzzy_inputs(self) -> Dict[str, float]:
        return self.__fuzzy_inputs

    @fuzzy_inputs.setter
    def fuzzy_inputs(self, p_fuzzy_inputs: Dict[str, float]):
        self.__fuzzy_inputs = p_fuzzy_inputs

    def add_fuzzy_inputs(self, p_name, p_value):
        self.__fuzzy_inputs[p_name] = p_value

    def get_num_rows(self):
        self.__num_rows

    def get_num_cols(self):
        self.__num_cols

    def add_fuzzy_inputs_matrix(self, p_row, p_column, p_name, p_value):
        if self.__fuzzy_inputs_matrix.get(p_name) is None:
            self.__fuzzy_inputs_matrix[p_name] = np.zeros((self.__num_rows, self.__num_cols))
        self.__fuzzy_inputs_matrix[p_name][p_row][p_column] = p_value

    def get_fuzzy_inputs_matrix(self):
        return self.__fuzzy_inputs_matrix

    @property
    def fuzzy_output(self) -> str:
        return self.__fuzzy_output

    @fuzzy_output.setter
    def fuzzy_output(self, p_fuzzy_output: str):
        self.__fuzzy_output = p_fuzzy_output

    def set_fuzzy_output(self, p_fuzzy_output: str):
        self.__fuzzy_output = p_fuzzy_output

    @property
    def use_dict_facies_association(self) -> bool:
        return self.__use_dict_facies_association

    @use_dict_facies_association.setter
    def use_dict_facies_association(self, p_use_dict_facies_association: bool):
        self.__use_dict_facies_association = p_use_dict_facies_association

    def set_use_dict_facies_association(self, p_use_dict_facies_association: bool):
        self.__use_dict_facies_association = p_use_dict_facies_association