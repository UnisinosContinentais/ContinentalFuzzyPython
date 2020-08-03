"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.domain.sugeno.SugenoVariable import SugenoVariable


class SugenoOutput(SugenoVariable):
    def __init__(self,
                 var_range=None,
                 var_num_mfs=None,
                 var_mfs=None):
        super().__init__(var_range,
                         var_num_mfs,
                         var_mfs)
        self.__var_type = 'consequent'

    @property
    def var_type(self):
        return self.__var_type
