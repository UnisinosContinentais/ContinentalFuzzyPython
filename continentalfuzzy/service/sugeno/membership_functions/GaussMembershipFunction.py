"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np


class GaussMembershipFunction:
    @staticmethod
    def calculate_gaussmf(x: float, mean: float, sigma: float):
        try:
            x = np.array([x], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro x precisa ser um número!")

        try:
            mean = np.array([mean], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro média precisa ser um número!")

        try:
            sigma = np.array([sigma], dtype=np.float64)[0]
        except Exception:
            raise Exception(
                "O parâmetro desvio padrão precisa ser um número!")

        return np.exp(-((x - mean) ** 2.0) / (2.0 * sigma ** 2.0))
