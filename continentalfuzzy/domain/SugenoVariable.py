"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, Dict, List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction


class SugenoVariable(object):
    def __init__(self,
                 var_range: Optional[List[float]] = None,
                 var_num_mfs: Optional[int] = None,
                 var_mfs: Optional[Dict[str, MembershipFunction]] = None):
        self.__range = list()
        self.__num_mfs = None
        self.__mfs = dict()

        if var_range is not None:
            self.range = var_range

        if var_num_mfs is not None:
            self.num_mfs = var_num_mfs

        if var_mfs is not None:
            self.mfs = var_mfs

    @property
    def range(self) -> List[float]:
        return self.__range

    @range.setter
    def range(self, var_range: List[float]):
        # Verifica se o parâmetro é uma lista
        if not isinstance(var_range, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se a lista possui 2 itens
        if len(var_range) != 2:
            raise Exception("A lista com a amplitude do conjunto da variável "
                            "precisa ter dois números!")

        # Verifica se os valores da lista são do tipo float
        try:
            self.__range = [float(val) for val in var_range]
        except Exception:
            raise Exception("Um dos valores não é do tipo float!")

    @property
    def num_mfs(self) -> int:
        return self.__num_mfs

    @num_mfs.setter
    def num_mfs(self, var_num_mfs: int):
        if not isinstance(var_num_mfs, int):
            raise Exception(f"O parâmetro não é um número inteiro!")

        self.__num_mfs = var_num_mfs

    @property
    def mfs(self) -> Dict[str, MembershipFunction]:
        return self.__mfs

    @mfs.setter
    def mfs(self, var_mfs: Dict[str, MembershipFunction]):
        # Verifica se o número de funções de pertinência foi informado
        if self.num_mfs is None:
            raise Exception("O número de funções de pertinências não foi "
                            "informado!")

        # Verifica se o tamanho do dicionário está correto
        if len(var_mfs) != self.num_mfs:
            raise Exception("A quantidade de funções de pertinência é "
                            "diferente da informada!")

        # Verifica se o dicionário possui os tipos corretos
        for k_num, v_mfs in var_mfs.items():
            if not isinstance(k_num, str):
                raise Exception("A chave do dicionário não é uma string!")

            if not isinstance(v_mfs, MembershipFunction):
                raise Exception(
                    "O valor não é uma instância da classe FISMembershipFunc!")
        self.__mfs = var_mfs

    def add_mfs(self, mf_name, mf_value: Dict):
        # Verifica se o número de funções de pertinência foi informado
        if self.num_mfs is None:
            raise Exception("O número de funções de pertinências não foi "
                            "informado!")

        # Verifica se o tamanho do dicionário está correto
        if len(self.mfs) == self.num_mfs:
            raise Exception("Não é possível cadastrar mais funções de "
                            "pertinências!")

        if not isinstance(mf_name, str):
            raise Exception("A variável nome não é uma string!")

        if not isinstance(mf_value, dict):
            raise Exception(f"O valor não é um dicionário!")

        self.__mfs[mf_name] = mf_value
