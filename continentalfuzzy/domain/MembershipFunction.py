"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional
from continentalfuzzy.domain.definition.Functions import Functions


class MembershipFunction:
    """
    Classe usada para representar uma função de pertinência.
    """

    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_function: Optional[Functions] = None):
        """
        Inicializador da classe FISMembershipFunc

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_function : FISFunction
            Nome da função de pertinência.

        """

        self.__name = None
        self.__function = None
        if mf_name is not None:
            self.name = mf_name
        if mf_function is not None:
            self.function = mf_function

    @property
    def name(self) -> str:
        """
        Nome para identificação da função de pertinência.

        Retorna
        -------
        str
            Retorna uma string com o nome para identificação da função de
            pertinência.
        """
        return self.__name

    @name.setter
    def name(self, mf_name: str):
        """
        Altera o nome para identificação da função de pertinência.

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.
        """

        if not isinstance(mf_name, str):
            raise Exception(f"O nome não é uma string!")

        self.__name = mf_name

    @property
    def function(self) -> Functions:
        """
        Nome da função de pertinência.

        Retorna
        -------
        str
            Retorna uma instância da classe MembershipFunction com o nome da
            função de pertinência.
        """
        return self.__function

    @function.setter
    def function(self, mf_function: Functions):
        """
        Altera o nome da função de pertinência.

        Parâmetros
        ----------
        mf_function : FISFunctions
            FISFunctions contendo o nome da função de pertinência.
        """

        if not isinstance(mf_function, Functions):
            raise Exception(f"Função de pertinência {mf_function} não é uma "
                            f"instância da classe MembershipFunction!")

        self.__function = mf_function
