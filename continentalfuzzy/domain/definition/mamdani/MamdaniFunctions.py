"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class MamdaniFunctions(Enum):
    """
    Enum com as funções de pertinência implementadas para o Mamdani.
    """
    trimf = auto()
    trapmf = auto()
    gaussmf = auto()
    gauss2mf = auto()
