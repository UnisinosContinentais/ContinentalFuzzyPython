"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Dict


class FuzzyControlCommandInput:
    def __init__(self):
        self.__filename = None
        self.__fuzzy_inputs = None
        self.__fuzzy_output = None

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, p_filename: str):
        self.__filename = p_filename

    @property
    def fuzzy_inputs(self) -> Dict[str, float]:
        return self.__fuzzy_inputs

    @fuzzy_inputs.setter
    def fuzzy_inputs(self, p_fuzzy_inputs: Dict[str, float]):
        self.__fuzzy_inputs = p_fuzzy_inputs

    @property
    def fuzzy_output(self) -> str:
        return self.__fuzzy_output

    @fuzzy_output.setter
    def fuzzy_output(self, p_fuzzy_output: str):
        self.__fuzzy_output = p_fuzzy_output
