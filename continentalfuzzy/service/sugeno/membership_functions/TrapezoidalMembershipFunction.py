"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List
import numpy as np
from continentalfuzzy.service.sugeno.membership_functions.TriangularMembershipFuntion import \
    TriangularMembershipFunction


class TrapezoidalMembershipFunction:
    @staticmethod
    def calculate_trapmf(x: float, abcd: List[float]):
        try:
            x = np.array([x], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro x precisa ser um número!")

        abcd = np.array(abcd)
        if np.shape(abcd)[0] != 4:
            raise Exception("O parâmetro abc necessita de 4 valores!")

        a = abcd[0]
        b = abcd[1]
        c = abcd[2]
        d = abcd[3]

        if (a > b) or (b > c) or (c > d):
            raise Exception("Os parâmetros não estão em ordem crescente!")

        trimf = TriangularMembershipFunction()

        if a == b == c == d == x:
            return 1

        elif (x >= b) and (x <= c):
            return 1

        elif (x > a) and (x < b):
            return trimf.calculate_trimf(x, [a, b, c])

        elif (x > c) and (x < d):
            return trimf.calculate_trimf(x, [b, c, d])

        else:
            return 0
