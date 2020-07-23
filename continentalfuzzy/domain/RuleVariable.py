"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional


class RuleVariable:
    """
    Classe usada para representar uma variável de uma regra.

    """
    def __init__(self,
                 r_var_name: Optional[str] = None,
                 r_var_mf: Optional[str] = None):
        """
        Inicializador da classe FISRuleVariable

        Parâmetros
        ----------
        r_var_name : str
            String contendo o nome da variável da regra.

        r_var_mf : str
            String contendo  o nome da função de pertinência da variável
            da regra.
        """

        self.__name = None
        self.__mf = None

        if r_var_name is not None:
            self.name = r_var_name

        if r_var_mf is not None:
            self.mf = r_var_mf

    @property
    def name(self) -> str:
        """
        Nome da variável da regra.

        Retorna
        -------
        str
            Retorna uma string com o nome da variável da regra.
        """
        return self.__name

    @name.setter
    def name(self, var_rule_name: str):
        """
        Altera o nome da variável da regra.

        Parâmetros
        ----------
        var_rule_name : str
            String contendo o nome da variável da regra.
        """

        if not isinstance(var_rule_name, str):
            raise Exception(f"O nome não é uma string!")

        self.__name = var_rule_name

    @property
    def mf(self) -> str:
        """
        Nome da função de pertinência da variável da regra.

        Retorna
        -------
        str
            Retorna uma string com o nome da função de pertinência da variável
            da regra.
        """
        return self.__mf

    @mf.setter
    def mf(self, mf_var_rule_name: str):
        """
        Altera o nome da função de pertinência da variável da regra.

        Parâmetros
        ----------
        mf_var_rule_name : str
            String contendo o nome da função de pertinência da variável da
            regra.
        """
        if not isinstance(mf_var_rule_name, str):
            raise Exception(f"O nome não é uma string!")

        self.__mf = mf_var_rule_name
