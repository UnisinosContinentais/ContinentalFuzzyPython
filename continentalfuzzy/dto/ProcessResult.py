"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from enum import Enum


class ProcessResult(Enum):
    """
    Enum com os resultados dos processos.
    """
    RESULT_ERROR = 0
    RESULT_SUCCESS = 1
