"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, Dict, List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.sugeno.SugenoVariable import SugenoVariable


class SugenoInput(SugenoVariable):
    def __init__(self,
                 var_range: Optional[List[float]] = None,
                 var_num_mfs: Optional[int] = None,
                 var_mfs: Optional[Dict[str, MembershipFunction]] = None):
        super().__init__(var_range,
                         var_num_mfs,
                         var_mfs)
        self.__var_type = 'antecedent'

    @property
    def var_type(self) -> str:
        return self.__var_type
