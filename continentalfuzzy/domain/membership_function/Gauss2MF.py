"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""

from typing import Optional
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions


class Gauss2MF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência de duas gaussianas
    combinadas

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_sigma1: Optional[float] = None,
                 mf_mean1: Optional[float] = None,
                 mf_sigma2: Optional[float] = None,
                 mf_mean2: Optional[float] = None):
        """
        Inicializador da classe FISGauss2MF

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_sigma1 : float
            Número float contendo o desvio padrão da primeira gaussiana.

        mf_mean1 : float
            Número float contendo a média da primeira gaussiana.

        mf_sigma2 : float
            Número float contendo o desvio padrão da segunda gaussiana.

        mf_mean2 : float
            Número float contendo a média da segunda gaussiana.
        """

        super().__init__(mf_name, MamdaniFunctions.gauss2mf)
        self.__sigma1 = None
        self.__mean1 = None
        self.__sigma2 = None
        self.__mean2 = None

        if mf_sigma1 is not None:
            self.sigma1 = mf_sigma1

        if mf_mean1 is not None:
            self.mean1 = mf_mean1

        if mf_sigma2 is not None:
            self.sigma2 = mf_sigma2

        if mf_mean2 is not None:
            self.mean2 = mf_mean2

    @property
    def sigma1(self) -> float:
        """
        Número float representando o desvio padrão da primeira gaussiana.

        Retorna
        -------
        float
            Retorna um número float representando o desvio padrão da primeira
            gaussiana.
        """
        return self.__sigma1

    @sigma1.setter
    def sigma1(self, mf_sigma1: float):
        """
        Altera o número float representando o desvio padrão da primeira
        gaussiana.

        Parâmetros
        ----------
        mf_sigma1 : float
            Número float contendo o desvio padrão da primeira gaussiana.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__sigma1 = float(mf_sigma1)
        except Exception:
            raise Exception("O parâmetro desvio padrão da primeira gaussiana "
                            "não é do tipo float!")

    @property
    def mean1(self) -> float:
        """
        Número float representando a média da primeira gaussiana.

        Retorna
        -------
        float
            Retorna um número float representando a média da primeira gaussiana.
        """
        return self.__mean1

    @mean1.setter
    def mean1(self, mf_mean1: float):
        """
        Altera o número float representando a média da primeira gaussiana.

        Parâmetros
        ----------
        mf_mean1 : float
            Número float contendo a média da primeira gaussiana.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__mean1 = float(mf_mean1)
        except Exception:
            raise Exception("O parâmetro média da primeira gaussiana não é do "
                            "tipo float!")

    @property
    def sigma2(self) -> float:
        """
        Número float representando o desvio padrão da primeira gaussiana.

        Retorna
        -------
        float
            Retorna um número float representando o desvio padrão da primeira
            gaussiana.
        """
        return self.__sigma2

    @sigma2.setter
    def sigma2(self, mf_sigma2: float):
        """
        Altera o número float representando o desvio padrão da segunda
        gaussiana.

        Parâmetros
        ----------
        mf_sigma2 : float
            Número float contendo o desvio padrão da segunda gaussiana.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__sigma2 = float(mf_sigma2)
        except Exception:
            raise Exception("O parâmetro desvio padrão da segunda gaussiana "
                            "não é do tipo float!")

    @property
    def mean2(self) -> float:
        """
        Número float representando a média da segunda gaussiana.

        Retorna
        -------
        float
            Retorna um número float representando a média da segunda gaussiana.
        """
        return self.__mean2

    @mean2.setter
    def mean2(self, mf_mean2: float):
        """
        Altera o número float representando a média da segunda gaussiana.

        Parâmetros
        ----------
        mf_mean2 : float
            Número float contendo a média da segunda gaussiana.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__mean2 = float(mf_mean2)
        except Exception:
            raise Exception("O parâmetro média da segunda gaussiana não é "
                            "do tipo float!")
