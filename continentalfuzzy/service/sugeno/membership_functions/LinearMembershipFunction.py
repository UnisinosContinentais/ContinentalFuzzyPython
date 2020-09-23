"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List, Dict


class LinearMembershipFunction:
    @staticmethod
    def calculate_linear(params: Dict[str, float],
                         inputs: Dict[str, float]):

        result = 0
        for key, value in inputs.items():
            result += (params[key] * inputs[key])
        result += params['__constant__']

        return result
