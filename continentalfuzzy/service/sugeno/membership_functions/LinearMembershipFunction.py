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
        if len(params) != (len(inputs) + 1):
            raise Exception("O número de parâmetros está incorreto!")

        # Verifica se o dicionário possui os tipos corretos
        for k_param, v_param in params.items():
            if not isinstance(k_param, str):
                raise Exception(
                    "A chave do parâmetro não é uma string!")
            try:
                _ = float(v_param)
            except Exception:
                raise Exception("O valor do parâmetro não é um número!")

        # Verifica se o dicionário possui os tipos corretos
        for k_input, v_input in inputs.items():
            if not isinstance(k_input, str):
                raise Exception(
                    "A chave do valor não é uma string!")
            try:
                _ = float(v_input)
            except Exception:
                raise Exception("O valor não é um número!")

        result = 0
        for key, value in inputs.items():
            result += (params[key] * inputs[key])
        result += params['__constant__']

        return result
