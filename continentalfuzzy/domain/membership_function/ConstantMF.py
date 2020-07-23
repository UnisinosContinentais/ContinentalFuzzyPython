"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions
from continentalfuzzy.domain.MembershipFunction import MembershipFunction


class ConstantMF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência constante.

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_value: Optional[float] = None):
        """
        Inicializador da classe v

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_value : float
            Valor constante da função.

        """

        super().__init__(mf_name, MamdaniFunctions.constant)
        self.__value = 0

        if mf_value is not None:
            self.value = mf_value

    @property
    def value(self) -> float:
        """
        Valor constante da função.

        Retorna
        -------
        float
            Valor constante da função.
        """
        return self.__value

    @value.setter
    def value(self, mf_value: float):
        """
        Altera o valor constante da função.

        Parâmetros
        ----------
        mf_value : float
            Valor constante da função.
        """

        # Verifica se o valor é do tipo float
        try:
            self.__value = float(mf_value)
        except Exception:
            raise Exception("O valor não é do tipo float!")
