"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.domain.SugenoRuleVariable import SugenoRuleVariable


class SugenoRuleInput(SugenoRuleVariable):
    """
    Sugeno Rule Input
    """
    def __init__(self,
                 p_name=None,
                 p_rule_func=None,
                 p_params=None,
                 p_var_not=None):

        super().__init__(p_name, p_rule_func, p_params)
        self.__var_type = 'antecedent'
        self.__var_not = None

        if p_var_not is not None:
            self.var_not = p_var_not

    @property
    def var_type(self):
        return self.__var_type

    @property
    def var_not(self):
        return self.__var_not

    @var_not.setter
    def var_not(self, p_var_not):
        if not isinstance(p_var_not, bool):
            raise Exception("O operador lógico NOT não é um booleano!")
        self.__var_not = p_var_not
