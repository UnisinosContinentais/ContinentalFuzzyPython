"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.dto.AbstractDtoResult import AbstractDtoResult


class FuzzyControlCommandOutput(AbstractDtoResult):
    def __init__(self):
        super().__init__()
        self.__result = 0.0

    @property
    def result(self) -> float:
        return self.__result

    @result.setter
    def result(self, p_result: float):
        self.__result = p_result
