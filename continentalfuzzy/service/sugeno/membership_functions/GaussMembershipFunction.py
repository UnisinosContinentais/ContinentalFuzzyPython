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
        x = np.array([x], dtype=np.float64)[0]
        mean = np.array([mean], dtype=np.float64)[0]
        sigma = np.array([sigma], dtype=np.float64)[0]
        return np.exp(-((x - mean) ** 2.0) / (2.0 * sigma ** 2.0))
