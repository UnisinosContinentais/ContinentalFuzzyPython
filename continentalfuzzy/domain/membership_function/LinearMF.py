"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.Functions import Functions


class LinearMF(MembershipFunction):
    """
    Classe usada para representar uma função de pertinência linear.

    Esta classe é filha da classe FISMembershipFunc.
    """
    def __init__(self,
                 mf_name: Optional[str] = None,
                 mf_num_inputs: int = 1,
                 mf_params: Optional[List[float]] = None):
        """
        Inicializador da classe LinearMF

        Parâmetros
        ----------
        mf_name : str
            String contendo o nome para identificação da função de pertinência.

        mf_abc : List[float]
            Lista contendo os parâmetros da funçõo linear.

        """

        super().__init__(mf_name, Functions.linear)
        self.__params = None
        self.___num_inputs = None

        if mf_num_inputs is not None:
            self.num_inputs = mf_num_inputs

        if mf_params is not None:
            self.params = mf_params

    @property
    def num_inputs(self) -> int:
        return self.___num_inputs

    @num_inputs.setter
    def num_inputs(self, mf_num_inputs: int):
        # Verifica se o parâmetro é um inteiro
        if not isinstance(mf_num_inputs, int):
            raise Exception("O número de antecedentes não é "
                            "um número inteiro!")
        self.___num_inputs = mf_num_inputs

    @property
    def params(self) -> List[float]:
        """
        Lista contendo os parâmetros da funçõo linear.

        Retorna
        -------
        List[float]
            Retorna uma lista contendo os parâmetros da funçõo linear.
        """
        return self.__params

    @params.setter
    def params(self, mf_params: List[float]):
        """
        Altera a lista contendo os parâmetros da funçõo linear.

        Parâmetros
        ----------
        mf_abc : List[float]
            Lista contendo os parâmetros da funçõo linear.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(mf_params, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se a lista possui o tamanho correto
        if len(mf_params) != (self.num_inputs + 1):
            raise Exception(f"A lista possui tamanho diferente do número de "
                            f"antecedentes mais uma constante!")

        # Verifica se os valores da lista são do tipo float
        try:
            self.__params = [float(val) for val in mf_params]
        except Exception:
            raise Exception("Um dos valores não é do tipo float!")
