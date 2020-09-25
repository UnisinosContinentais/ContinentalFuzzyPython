"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.service.sugeno.membership_functions.membership_functions import c_calculate_gaussmf

class GaussMembershipFunction:
    @staticmethod
    def calculate_gaussmf(x: float, mean: float, sigma: float):
        return c_calculate_gaussmf(x, mean, sigma)
