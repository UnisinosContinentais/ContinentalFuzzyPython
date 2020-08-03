"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Dict, List, Optional
from continentalfuzzy.domain.System import System
from continentalfuzzy.domain.sugeno.variable.SugenoInput import SugenoInput
from continentalfuzzy.domain.sugeno.variable.SugenoOutput import SugenoOutput
from continentalfuzzy.domain.sugeno.SugenoRule import SugenoRule


class SugenoController:
    """
    Sugeno Controller
    """
    def __init__(self,
                 sugeno_fis_system: Optional[System] = None,
                 sugeno_inputs: Optional[Dict[str, SugenoInput]] = None,
                 sugeno_outputs: Optional[Dict[str, SugenoOutput]] = None,
                 sugeno_rules: Optional[List[SugenoRule]] = None):
        self.__fis_system = None
        self.__inputs = dict()
        self.__outputs = dict()
        self.__rules = list()

        if sugeno_fis_system is not None:
            self.fis_system = sugeno_fis_system

        if sugeno_inputs is not None:
            self.inputs = sugeno_inputs

        if sugeno_outputs is not None:
            self.outputs = sugeno_outputs

        if sugeno_rules is not None:
            self.rules = sugeno_rules

    @property
    def fis_system(self) -> System:
        return self.__fis_system

    @fis_system.setter
    def fis_system(self, p_fis_system: System):
        if not isinstance(p_fis_system, System):
            raise Exception("O parâmetro não é uma instância da classe System!")
        self.__fis_system = p_fis_system

    @property
    def inputs(self) -> Dict[str, SugenoInput]:
        return self.__inputs

    @inputs.setter
    def inputs(self, p_inputs: Dict[str, SugenoInput]):
        # Verifica se o inputs é um dicionário
        if not isinstance(p_inputs, dict):
            raise Exception(f"O input não é um dicionário!")

        # Verifica se o dicionário possui os tipos corretos
        for k_input, v_input in p_inputs.items():
            if not isinstance(k_input, str):
                raise Exception("A chave não é uma string!")
            if not isinstance(v_input, SugenoInput):
                raise Exception(
                    "O valor não é uma instância da classe SugenoInput!")
        self.__inputs = p_inputs

    def add_input(self, p_input_name: str, p_input: SugenoInput):
        if not isinstance(p_input_name, str):
            raise Exception("A chave não é uma string!")
        if not isinstance(p_input, SugenoInput):
            raise Exception(
                "O valor não é uma instância da classe SugenoInput!")
        self.__inputs[p_input_name] = p_input

    @property
    def outputs(self) -> Dict[str, SugenoOutput]:
        return self.__outputs

    @outputs.setter
    def outputs(self, p_outputs: Dict[str, SugenoOutput]):
        # Verifica se o outputs é um dicionário
        if not isinstance(p_outputs, dict):
            raise Exception(f"O output não é um dicionário!")

        # Verifica se o dicionário possui os tipos corretos
        for k_output, v_output in p_outputs.items():
            if not isinstance(k_output, str):
                raise Exception("A chave não é uma string!")
            if not isinstance(v_output, SugenoOutput):
                raise Exception(
                    "O valor não é uma instância da classe SugenoOutput!")
        self.__outputs = p_outputs

    def add_output(self, p_output_name: str, p_output: SugenoOutput):
        if not isinstance(p_output_name, str):
            raise Exception("A chave não é uma string!")
        if not isinstance(p_output, SugenoOutput):
            raise Exception(
                "O valor não é uma instância da classe SugenoOutput!")
        self.__outputs[p_output_name] = p_output

    @property
    def rules(self) -> List[SugenoRule]:
        return self.__rules

    @rules.setter
    def rules(self, p_rules: List[SugenoRule]):
        # Verifica se o rules é uma lista
        if not isinstance(p_rules, list):
            raise Exception(f"O rule não é um dicionário!")

        # Verifica se os valores da lista são instâncias da classe SugenoRule
        for value in p_rules:
            if not isinstance(value, SugenoRule):
                raise Exception(
                    f"O valor não é uma instância da classe SugenoRule!")
        self.__rules = p_rules

    def add_rule(self, p_rule: SugenoRule):
        if not isinstance(p_rule, SugenoRule):
            raise Exception(
                f"O valor não é uma instância da classe SugenoRule!")
        self.__rules.append(p_rule)
