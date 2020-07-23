"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional
from continentalfuzzy.domain.RuleVariable import RuleVariable


class RuleOutput(RuleVariable):
    """
    Classe usada para representar um consequente de uma regra.

    Esta classe é filha da classe FISRuleVariable.
    """
    def __init__(self,
                 r_output_name: Optional[str] = None,
                 r_output_mf: Optional[str] = None):
        """
        Inicializador da classe FISRuleOutput

        Parâmetros
        ----------
        r_output_name : str
            String contendo o nome da variável da regra.

        r_output_mf : str
            String contendo o nome da função de pertinência da variável
            da regra.
        """
        super().__init__(r_output_name, r_output_mf)
        self.__var_type = 'consequent'

    @property
    def var_type(self) -> str:
        """
        Tipo da variável - consequent.

        Retorna
        -------
        str
            Retorna uma string com o tipo da variável - consequent.
        """
        return self.__var_type
