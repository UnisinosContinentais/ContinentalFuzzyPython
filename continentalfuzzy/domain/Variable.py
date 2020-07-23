"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, Dict, List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction


class Variable:
    """
    Classe usada para representar uma variável de um sistema fuzzy.
    """
    def __init__(self,
                 var_name: Optional[str] = None,
                 var_range: Optional[List[float]] = None,
                 var_num_mfs: Optional[int] = None,
                 var_mfs: Optional[Dict[int, MembershipFunction]] = None):
        """
        Inicializador da classe FISVariable

        Parâmetros
        ----------
        var_name : str
            String contendo o nome da variável.

        var_range : List[float]
            Lista contendo a amplitude do conjunto da variável.

        var_num_mfs : int
            Número inteiro contendo o número de funções de pertinência
            da variável.

        var_mfs : Dict[int, FISMembershipFunc]
            Dicionário contendo as funções de pertinência da variável.
        """

        self.__name = None
        self.__range = list()
        self.__num_mfs = None
        self.__mfs = dict()

        if var_name is not None:
            self.name = var_name

        if var_range is not None:
            self.range = var_range

        if var_num_mfs is not None:
            self.num_mfs = var_num_mfs

        if var_mfs is not None:
            self.mfs = var_mfs

    @property
    def name(self) -> str:
        """
        Nome da variável.

        Retorna
        -------
        str
            Retorna uma string com o nome da variável.
        """
        return self.__name

    @name.setter
    def name(self, var_name: str):
        """
        Altera o nome da variável.

        Parâmetros
        ----------
        var_name : str
            String contendo o nome da variável.
        """

        if not isinstance(var_name, str):
            raise Exception(f"O nome não é uma string!")

        self.__name = var_name

    @property
    def range(self) -> List[float]:
        """
        Amplitude do conjunto da variável.

        Retorna
        -------
        List[float]:
            Retorna uma lista com a amplitude do conjunto da variável.
        """
        return self.__range

    @range.setter
    def range(self, var_range: List[float]):
        """
        Altera a amplitude do conjunto da variável.

        Parâmetros
        ----------
        var_range : List[float]
            Lista contendo a amplitude do conjunto da variável.
        """

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
        """
        Número de funções de pertinência da variável.

        Retorna
        -------
        int
            Retorna um inteiro com o número de funções de pertinência da
            variável.
        """
        return self.__num_mfs

    @num_mfs.setter
    def num_mfs(self, var_num_mfs: int):
        """
        Altera o número de funções de pertinência da variável.

        Parâmetros
        ----------
        var_num_mfs : int
            Inteiro contendo o número de funções de pertinência da variável.
        """

        if not isinstance(var_num_mfs, int):
            raise Exception(f"O parâmetro não é um número inteiro!")

        self.__num_mfs = var_num_mfs

    @property
    def mfs(self) -> Dict[int, MembershipFunction]:
        """
        Dicionário contendo as funções de pertinência da variável.

        A chave do dicionário é o número da função de pertinência.
        O valor é uma instância da classe FISMembershipFunc.

        Retorna
        -------
        Dict[int, FISMembershipFunc]
            Retorna um dicionário onde a chave é o número da função de
            pertinência e o valor é uma instância da classe FISMembershipFunc.
        """
        return self.__mfs

    @mfs.setter
    def mfs(self, var_mfs: Dict[int, MembershipFunction]):
        """
        Altera o dicionário contendo as funções de pertinência da variável.

        Parâmetros
        ----------
        var_mfs : Dict[int, FISMembershipFunc]
            Dicionário contendo as funções de pertinência da variável.
        """

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
            if not isinstance(k_num, int):
                raise Exception("A chave do dicionário não é um número "
                                "inteiro!")

            if not isinstance(v_mfs, MembershipFunction):
                raise Exception(
                    "O valor não é uma instância da classe FISMembershipFunc!")

        self.__mfs = var_mfs

    def add_mfs(self, var_num: int, var_value: MembershipFunction):
        """
        Adiciona uma nova entrada no dicionário contendo as funções de
        pertinência da variável.

        Parâmetros
        ----------
        var_mfs : int
            Inteiro com o número da função de pertinência.

        var_value : FISMembershipFunc
            Instância da classe FISMembershipFunc.
        """

        # Verifica se o número de funções de pertinência foi informado
        if self.num_mfs is None:
            raise Exception("O número de funções de pertinências não foi "
                            "informado!")

        # Verifica se o tamanho do dicionário está correto
        if len(self.mfs) == self.num_mfs:
            raise Exception("Não é possível cadastrar mais funções de "
                            "pertinências!")

        if not isinstance(var_num, int):
            raise Exception("A variável número não é um número inteiro!")

        if not isinstance(var_value, MembershipFunction):
            raise Exception(f"O valor não é uma instância da classe "
                            "FISMembershipFunc!")

        self.__mfs[var_num] = var_value
