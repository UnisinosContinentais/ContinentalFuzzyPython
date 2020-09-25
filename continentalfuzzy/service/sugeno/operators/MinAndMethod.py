"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.service.sugeno.operators.NotMethod import NotMethod


class MinAndMethod:
    @classmethod
    def calculate_min_and(cls, inputs, values):
        is_first = True
        min_value = 0
        for r_input in inputs:
            result = r_input.rule_func(values[r_input.name],
                                       **r_input.params)

            if r_input.var_not:
                result = NotMethod.calculate_not(result)
                if is_first:
                    min_value = result
                    is_first = False
                elif min_value > result:
                    min_value = result

            elif is_first:
                min_value = result
                is_first = False
            elif min_value > result:
                min_value = result

        return min_value
