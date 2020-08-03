"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Union, List, Dict, Optional, Callable
import types
from continentalfuzzy.service.MembershipFunctionService import \
    MembershipFunctionService


class SugenoRuleVariable(object):
    def __init__(self,
                 p_name: Optional[str] = None,
                 p_rule_func: Optional[Callable] = None,
                 p_params: Optional[Dict[str, Union[float, List[float]]]] = None):
        self.__name = None
        self.__rule_func = None
        self.__params = dict()

        if p_name is not None:
            self.name = p_name

        if p_rule_func is not None:
            self.rule_func = p_rule_func

        if p_params is not None:
            self.params = p_params

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, p_name):
        if not isinstance(p_name, str):
            raise Exception(f"O nome não é uma string!")
        self.__name = p_name

    @property
    def rule_func(self):
        return self.__rule_func

    @rule_func.setter
    def rule_func(self, p_rule_func):
        if not isinstance(p_rule_func, types.FunctionType):
            raise Exception(f"A função da regra não é uma função!")
        self.__rule_func = p_rule_func

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, p_params):
        if not isinstance(p_params, dict):
            raise Exception(f"Os parâmetros não são dicionários!")
        self.__params = p_params
