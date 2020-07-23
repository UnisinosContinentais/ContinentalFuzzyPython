"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, Dict, List
from continentalfuzzy.domain.Variable import Variable
from continentalfuzzy.domain.MembershipFunction import MembershipFunction


class Input(Variable):
    """
    Classe usada para representar um antecedente de um sistema fuzzy.

    Esta classe é filha da classe FISVariable.
    """
    def __init__(self,
                 var_name: Optional[str] = None,
                 var_range: Optional[List[float]] = None,
                 var_num_mfs: Optional[int] = None,
                 var_mfs: Optional[Dict[int, MembershipFunction]] = None):
        """
        Inicializador da classe FISInput

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
        super().__init__(var_name,
                         var_range,
                         var_num_mfs,
                         var_mfs)
        self.__var_type = 'antecedent'

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
