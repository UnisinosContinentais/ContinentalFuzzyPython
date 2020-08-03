"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class SugenoOrMethods(Enum):
    """
    Enum com os métodos OR implementados para os Takagi-Sugeno.
    """
    max = auto()
    probor = auto()
