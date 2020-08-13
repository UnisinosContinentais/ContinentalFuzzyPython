"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: August, 2020
"""
from enum import Enum


class FaciesAssociation(Enum):
    """
    Enum com as Associações de Fácies do StratBR.
    """
    Cape = 0
    ShallowPlain = 1
    LowEnergyUnderwaterPlain = 2
    InterpatchesPlain = 3
    ClayeyEmbayment = 4
    StromatoliteEmbayment = 5
    LaminiteRamp = 6
    ModerateEnergyIntraclastic = 7
    HighEnergyIntraclastic = 8
    SubCoastal = 9
    Reef = 10
    ClayeyClasticDeposit = 11
    Undefined = 12
