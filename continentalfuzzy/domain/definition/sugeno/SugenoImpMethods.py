"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class SugenoImpMethods(Enum):
    """
    Enum com os métodos de implicação implementados para o Takagi-Sugeno.
    """
    prod = auto()
