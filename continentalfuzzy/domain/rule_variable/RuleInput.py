"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional
from continentalfuzzy.domain.RuleVariable import RuleVariable


class RuleInput(RuleVariable):
    """
    Classe usada para representar um antecedente de uma regra.

    Esta classe é filha da classe FISRuleVariable.
    """

    def __init__(self,
                 r_input_name: Optional[str] = None,
                 r_input_mf: Optional[str] = None,
                 r_input_var_not: Optional[bool] = None):
        """
        Inicializador da classe FISRuleInput

        Parâmetros
        ----------
        r_input_name : str
            String contendo o nome da variável da regra.

        r_input_mf : str
            String contendo o nome da função de pertinência da variável
            da regra.

        r_input_var_not : bool
            Valor Lógico contendo o operador lógico NOT.
        """
        super().__init__(r_input_name, r_input_mf)
        self.__var_type = 'antecedent'
        self.__var_not = None

        if r_input_var_not is not None:
            self.var_not = r_input_var_not

    @property
    def var_type(self) -> str:
        """
        Tipo da variável - antecedent.

        Retorna
        -------
        str
            Retorna uma string com o tipo da variável - antecedent.
        """
        return self.__var_type

    @property
    def var_not(self) -> bool:
        """
        Operador lógico NOT.

        Retorna
        -------
        str
            Retorna um booleano se a variável possui o operador lógico NOT.
        """
        return self.__var_not

    @var_not.setter
    def var_not(self, mf_var_rule_not: bool):
        """
        Altera o operador lógico NOT.

        Parâmetros
        ----------
        mf_var_rule_not : bool
            Booleano se a variável possui o operador lógico NOT.
        """

        if not isinstance(mf_var_rule_not, bool):
            raise Exception(f"O operador lógico NOT não é um booleano!")

        self.__var_not = mf_var_rule_not
