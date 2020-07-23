"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum, auto


class Blocks(Enum):
    """
    Enum com os blocos de um arquivo .fis.
    """
    system = auto()
    inputs = auto()
    outputs = auto()
    rules = auto()
