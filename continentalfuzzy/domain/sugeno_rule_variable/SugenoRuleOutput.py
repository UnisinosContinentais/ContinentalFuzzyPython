"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.domain.SugenoRuleVariable import SugenoRuleVariable


class SugenoRuleOutput(SugenoRuleVariable):
    """
    Sugeno Rule Output
    """
    def __init__(self,
                 p_name=None,
                 p_rule_func=None,
                 p_params=None):

        super().__init__(p_name, p_rule_func, p_params)
        self.__var_type = 'consequent'

    @property
    def var_type(self):
        return self.__var_type
