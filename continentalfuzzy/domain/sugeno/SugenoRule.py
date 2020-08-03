"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import types
from typing import Optional, List
from continentalfuzzy.domain.sugeno.rule_variable.SugenoRuleInput import \
    SugenoRuleInput
from continentalfuzzy.domain.sugeno.rule_variable.SugenoRuleOutput import \
    SugenoRuleOutput


class SugenoRule:
    """
    Sugeno Rule
    """
    def __init__(self,
                 r_weight: Optional[float] = None,
                 r_connection_func = None,
                 r_inputs: Optional[List[SugenoRuleInput]] = None,
                 r_outputs=None): #: Optional[List[SugenoRuleOutput]] = None):
        self.__weight = None
        self.__connection_func = None
        self.__inputs = list()
        self.__outputs = list()

        if r_weight is not None:
            self.weight = r_weight

        if r_connection_func is not None:
            self.connection_func = r_connection_func

        if r_inputs is not None:
            self.inputs = r_inputs

        if r_outputs is not None:
            self.outputs = r_outputs

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, p_weight):
        # Verifica se o parâmetro é um número float
        try:
            self.__weight = float(p_weight)
        except Exception:
            raise Exception("O parâmetro peso não é do tipo float!")

        if p_weight < 0 or p_weight > 1:
            raise Exception("O peso precisa estar no intervalo 0 e 1!")

    @property
    def connection_func(self):
        return self.__connection_func

    @connection_func.setter
    def connection_func(self, p_connection_func):
        # Verifica se o parâmetro é uma lista
        if not isinstance(p_connection_func, types.MethodType):
            raise Exception(f"O parâmetro não é um método!")
        self.__connection_func = p_connection_func

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, p_inputs):
        # Verifica se o parâmetro é uma lista
        if not isinstance(p_inputs, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se os itens da lista são instâncias SugenoRuleInput
        for value in p_inputs:
            if not isinstance(value, SugenoRuleInput):
                raise Exception(
                    "O valor não é uma instância da classe SugenoRuleInput!")
        self.__inputs = p_inputs

    def add_input(self, p_input):
        # Verifica se o valor é instância da classe SugenoRuleInput
        if not isinstance(p_input, SugenoRuleInput):
            raise Exception("O valor não é uma instância da classe "
                            "SugenoRuleInput!")
        self.__inputs.append(p_input)

    @property
    def outputs(self):
        return self.__outputs

    @outputs.setter
    def outputs(self, p_outputs):
        # Verifica se o parâmetro é uma lista
        if not isinstance(p_outputs, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se os itens da lista são instâncias SugenoRuleOutput
        for value in p_outputs:
            if not isinstance(value, SugenoRuleOutput):
                raise Exception(
                    "O valor não é uma instância da classe SugenoRuleOutput!")
        self.__outputs = p_outputs

    def add_output(self, p_output):
        # Verifica se o valor é instância da classe SugenoRuleOutput
        if not isinstance(p_output, SugenoRuleOutput):
            raise Exception("O valor não é uma instância da classe "
                            "SugenoRuleOutput!")
        self.__outputs.append(p_output)
