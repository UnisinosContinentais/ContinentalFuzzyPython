"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class SugenoOutputFunctions(Enum):
    """
    Enum com as funções de pertinência implementadas para os consequentes
    Takagi-Sugeno.
    """
    linear = auto()
    constant = auto()
