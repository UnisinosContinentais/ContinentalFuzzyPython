"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np
from continentalfuzzy.service.sugeno.membership_functions.GaussMembershipFunction import \
    GaussMembershipFunction


class GaussTwoMembershipFunction:
    @staticmethod
    def calculate_gauss2mf(x: float, mean1: float, sigma1: float,
                           mean2: float, sigma2: float):

        try:
            x = np.array([x], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro x precisa ser um número!")

        try:
            mean = np.array([mean1], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro média 1 precisa ser um número!")

        try:
            sigma = np.array([sigma1], dtype=np.float64)[0]
        except Exception:
            raise Exception(
                "O parâmetro desvio padrão 1 precisa ser um número!")

        try:
            mean = np.array([mean2], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro média 2 precisa ser um número!")

        try:
            sigma = np.array([sigma2], dtype=np.float64)[0]
        except Exception:
            raise Exception(
                "O parâmetro desvio padrão 2 precisa ser um número!")

        if (x >= mean1) and (x <= mean2):
            return 1
        left_gauss = 1
        right_gauss = 1

        gaussmf = GaussMembershipFunction()

        if x < mean1:
            left_gauss = gaussmf.calculate_gaussmf(x, mean1, sigma1)

        if x > mean2:
            right_gauss = gaussmf.calculate_gaussmf(x, mean2, sigma2)

        return left_gauss * right_gauss
