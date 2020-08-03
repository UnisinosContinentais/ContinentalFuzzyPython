"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.service.sugeno.operators.NotMethod import NotMethod


class ProborOrMethod:
    @classmethod
    def calculate_probor_or(cls, inputs, values):
        final_result = 0
        first_element = True
        for r_input in inputs:
            result = r_input.rule_func(values[r_input.name],
                                       **r_input.params)

            if r_input.var_not:
                result = NotMethod.calculate_not(result)

            if first_element:
                first_element = False
                final_result = result
            else:
                final_result = (final_result + result) - (final_result * result)

        return final_result
