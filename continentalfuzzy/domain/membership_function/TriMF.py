"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions


class TriMF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência triangular.

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_abc: Optional[List[float]] = None):
        """
        Inicializador da classe FISTriMF

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_abc : List[float]
            Lista contendo os três pontos que representam a função triangular.

        """

        super().__init__(mf_name, MamdaniFunctions.trimf)
        self.__abc = [0, 1, 2]

        if mf_abc is not None:
            self.abc = mf_abc

    @property
    def abc(self) -> List[float]:
        """
        Lista contendo os três pontos que representam a função triangular.

        Retorna
        -------
        List[float]
            Retorna uma Lista contendo os três pontos que representam a função
            triangular.
        """
        return self.__abc

    @abc.setter
    def abc(self, mf_abc: List[float]):
        """
        Altera a lista contendo os três pontos que representam a função
        triangular.

        Parâmetros
        ----------
        mf_abc : List[float]
            lista contendo os três pontos que representam a função triangular.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(mf_abc, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se a lista de parâmetro possui 3 valores
        if len(mf_abc) != 3:
            raise Exception(f"A lista possui um tamanho diferente de 3 pontos!")

        # Verifica se os valores da lista são do tipo float
        try:
            self.__abc = [float(val) for val in mf_abc]
        except Exception:
            raise Exception("Um dos valores não é do tipo float!")
