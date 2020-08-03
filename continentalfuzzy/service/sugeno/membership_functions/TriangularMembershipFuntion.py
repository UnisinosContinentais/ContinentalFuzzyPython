"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List
import numpy as np


class TriangularMembershipFunction:
    @staticmethod
    def calculate_trimf(x: float, abc: List[float]):
        try:
            x = np.array([x], dtype=np.float64)[0]
        except Exception:
            raise Exception("O parâmetro x precisa ser um número!")

        # Verifica se a lista possui os tipos corretos
        for val in abc:
            try:
                _ = float(val)
            except Exception:
                raise Exception("O parâmetro não é um número!")

        abc = np.array(abc)
        if np.shape(abc)[0] != 3:
            raise Exception("O parâmetro abc necessita de 3 valores!")

        a = abc[0]
        b = abc[1]
        c = abc[2]

        if (a > b) or (b > c):
            raise Exception("Os parâmetros não estão em ordem crescente!")

        if a == b == c == x:
            return 1
        elif a < x <= b:
            return (x - a)/(b - a)
        elif b < x < c:
            return (c - x)/(c - b)
        else:
            return 0
