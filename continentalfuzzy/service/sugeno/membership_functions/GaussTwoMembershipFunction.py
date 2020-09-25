"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.service.sugeno.membership_functions.membership_functions import c_calculate_gaussmf

class GaussTwoMembershipFunction:
    @staticmethod
    def calculate_gauss2mf(x: float, mean1: float, sigma1: float,
                           mean2: float, sigma2: float):

        if (x >= mean1) and (x <= mean2):
            return 1
        left_gauss = 1
        right_gauss = 1

        if x < mean1:
            left_gauss = c_calculate_gaussmf(x, mean1, sigma1)

        if x > mean2:
            right_gauss = c_calculate_gaussmf(x, mean2, sigma2)

        return left_gauss * right_gauss
