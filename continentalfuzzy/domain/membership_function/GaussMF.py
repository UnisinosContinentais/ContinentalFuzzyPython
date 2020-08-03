"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.Functions import Functions


class GaussMF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência gaussiana.

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_sigma: Optional[float] = None,
                 mf_mean: Optional[float] = None):
        """
        Inicializador da classe FISGaussMF

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_sigma : float
            Número float contendo o desvio padrão.

        mf_mean : float
            Número float contendo a média.
        """

        super().__init__(mf_name, Functions.gaussmf)
        self.__sigma = None
        self.__mean = None

        if mf_sigma is not None:
            self.sigma = mf_sigma

        if mf_mean is not None:
            self.mean = mf_mean

    @property
    def sigma(self) -> float:
        """
        Número float representando o desvio padrão.

        Retorna
        -------
        float
            Retorna um número float representando o desvio padrão.
        """
        return self.__sigma

    @sigma.setter
    def sigma(self, mf_sigma: float):
        """
        Altera o número float representando o desvio padrão.

        Parâmetros
        ----------
        mf_sigma : float
            Número float contendo o desvio padrão.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__sigma = float(mf_sigma)
        except Exception:
            raise Exception("O parâmetro desvio padrão não é do tipo float!")

    @property
    def mean(self) -> float:
        """
        Número float representando a média.

        Retorna
        -------
        float
            Retorna um número float representando a média.
        """
        return self.__mean

    @mean.setter
    def mean(self, mf_mean: float):
        """
        Altera o número float representando a média.

        Parâmetros
        ----------
        mf_mean : float
            Número float contendo a média.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__mean = float(mf_mean)
        except Exception:
            raise Exception("O parâmetro média não é do tipo float!")
