"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class Connections(Enum):
    """
    Enum com os conectores implementados.
    """
    AND = auto()
    OR = auto()
