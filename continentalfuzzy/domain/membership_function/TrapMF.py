"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List, Optional

from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions


class TrapMF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência trapezoidal.

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_abcd: Optional[List[float]] = None):
        """
        Inicializador da classe FISTrapMF

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_abc : List[float]
            Lista contendo os três pontos que representam a função trapezoidal.

        """

        super().__init__(mf_name, MamdaniFunctions.trapmf)
        self.__abcd = [0, 1, 2, 4]

        if mf_abcd is not None:
            self.abcd = mf_abcd

    @property
    def abcd(self) -> List[float]:
        """
        Lista contendo os quatro pontos que representam a função trapezoidal.

        Retorna
        -------
        List[float]
            Retorna uma Lista contendo os quatro pontos que representam a
            função trapezoidal.
        """
        return self.__abcd

    @abcd.setter
    def abcd(self, mf_abcd: List[float]):
        """
        Altera a lista contendo os quatro pontos que representam a função
        trapezoidal.

        Parâmetros
        ----------
        mf_abc : List[float]
            lista contendo os quatro pontos que representam a função
            trapezoidal.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(mf_abcd, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se a lista de parâmetro possui 4 valores
        if len(mf_abcd) != 4:
            raise Exception(f"A lista possui um tamanho diferente de 4 pontos!")

        # Verifica se os valores da lista são do tipo float
        try:
            self.__abcd = [float(val) for val in mf_abcd]
        except Exception:
            raise Exception("Um dos valores não é do tipo float!")
