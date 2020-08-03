"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class SugenoAndMethods(Enum):
    """
    Enum com os métodos AND implementados para o Takagi-Sugeno.
    """
    min = auto()
    prod = auto()
