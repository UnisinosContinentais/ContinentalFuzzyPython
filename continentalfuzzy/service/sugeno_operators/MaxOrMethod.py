"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.service.sugeno_operators.NotMethod import NotMethod


class MaxOrMethod:
    @classmethod
    def calculate_max_or(cls, inputs, values):
        results = list()
        for r_input in inputs:
            result = r_input.rule_func(values[r_input.name],
                                       **r_input.params)

            if r_input.var_not:
                results.append(NotMethod.calculate_not(result))

            else:
                results.append(result)

        return max(results)