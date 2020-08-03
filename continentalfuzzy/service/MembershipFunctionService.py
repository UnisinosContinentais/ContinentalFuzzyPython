"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.membership_function.ConstantMF import ConstantMF
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.LinearMF import LinearMF
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF


class MembershipFunctionService:
    def __init__(self):
        self.__membership_function = MembershipFunction()

    @property
    def membership_function(self) -> MembershipFunction:
        return self.__membership_function

    @membership_function.setter
    def membership_function(self, p_membership_function: MembershipFunction):
        if not isinstance(p_membership_function, MembershipFunction):
            raise Exception(
                "O valor não é uma instância da classe MembershipFunction!")

        self.__membership_function = p_membership_function

    def create_membership_function(
            self,
            p_membership_function: Functions,
            mf_name: str,
            values_list: List[float],
            num_inputs=1):

        # Verifica se o parâmetro é uma Function
        if not isinstance(p_membership_function, Functions):
            raise Exception(f"O parâmetro não é uma Functions!")

        # Verifica se o parâmetro é uma string
        if not isinstance(mf_name, str):
            raise Exception(f"O parâmetro não é uma string!")

        # Verifica se o parâmetro é uma lista
        if not isinstance(values_list, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se os valores da lista são do tipo float
        try:
            _ = [float(val) for val in values_list]
        except Exception:
            raise Exception("Um dos valores não é do tipo float!")

        # Ajusta os valores para cada tipo de função
        if p_membership_function == Functions.trimf:
            # Verifica se o tamanho dos parâmetros está correto
            if len(values_list) != 3:
                raise Exception("Número de parâmetros incorretos para "
                                "a função de pertinência triangular!")

            self.membership_function = TriMF(mf_name=mf_name,
                                             mf_abc=values_list)

        elif p_membership_function == Functions.trapmf:
            # Verifica se o tamanho dos parâmetros está correto
            if len(values_list) != 4:
                raise Exception("Número de parâmetros incorretos para "
                                "a função de pertinência trapezoidal!")

            self.membership_function = TrapMF(mf_name=mf_name,
                                              mf_abcd=values_list)

        elif p_membership_function == Functions.gaussmf:
            # Verifica se o tamanho dos parâmetros está correto
            if len(values_list) != 2:
                raise Exception("Número de parâmetros incorretos para "
                                "a função de pertinência gaussiana!")

            self.membership_function = GaussMF(mf_name=mf_name,
                                               mf_sigma=values_list[0],
                                               mf_mean=values_list[1])

        elif p_membership_function == Functions.gauss2mf:
            # Verifica se o tamanho dos parâmetros está correto
            if len(values_list) != 4:
                raise Exception("Número de parâmetros incorretos para "
                                "a função de pertinência de duas "
                                "gaussianas combinadas!")

            self.membership_function = Gauss2MF(mf_name=mf_name,
                                                mf_sigma1=values_list[0],
                                                mf_mean1=values_list[1],
                                                mf_sigma2=values_list[2],
                                                mf_mean2=values_list[3])

        elif p_membership_function == Functions.constant:
            # Verifica se o tamanho dos parâmetros está correto
            if len(values_list) != 1:
                raise Exception("Número de parâmetros incorretos para "
                                "a função de pertinência constante!")

            self.membership_function = ConstantMF(mf_name=mf_name,
                                                  mf_value=values_list[0])

        elif p_membership_function == Functions.linear:
            # Verifica se a lista possui o tamanho correto
            if len(values_list) != (num_inputs + 1):
                raise Exception(
                    f"A lista possui tamanho diferente do número de "
                    f"antecedentes mais uma constante!")

            self.membership_function = LinearMF(mf_name=mf_name,
                                                mf_num_inputs=num_inputs,
                                                mf_params=values_list)
