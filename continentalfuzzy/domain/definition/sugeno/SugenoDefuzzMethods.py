"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class SugenoDefuzzMethods(Enum):
    """
    Enum com os métodos de defuzzificação implementados para o Takagi-Sugeno.
    """
    wtaver = auto()
    wtsum = auto()
