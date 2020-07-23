"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np
from skfuzzy.control.antecedent_consequent import Antecedent
from skfuzzy.control.antecedent_consequent import Consequent
from skfuzzy.control.rule import Rule as SkRule
from skfuzzy.control.controlsystem import ControlSystem
from skfuzzy.control.controlsystem import ControlSystemSimulation
from typing import Dict, List, Optional
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.definition.MamdaniAndMethods import AndMethods
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.MamdaniOrMethods import OrMethods


class FuzzyMachine:
    """
    Classe usada para criar um controlador fuzzy da biblioteca scikit-fuzzy.
    """

    # Dicionário com os métodos AND implementadas
    DICT_AND_METHODS = {AndMethods.min: np.min}

    # Dicionário com os métodos OR implementadas
    DICT_OR_METHODS = {OrMethods.max: np.max}

    # Dicionário com os conectores implementados
    DICT_CONNECTORS = {Connections.AND: '&', Connections.OR: '|'}

    def __init__(self,
                 cont_inputs: Optional[Dict[str, Antecedent]] = None,
                 cont_outputs: Optional[Dict[str, Consequent]] = None,
                 cont_rules: Optional[List[Rule]] = None,
                 cont_controller: Optional[ControlSystem] = None,
                 cont_simulator: Optional[ControlSystemSimulation] = None):
        """ Inicializador da classe FISVariable"""

        self.__inputs = dict()
        self.__outputs = dict()
        self.__rules = list()
        self.__controller = None
        self.__simulator = None

        if cont_inputs is not None:
            self.inputs = cont_inputs

        if cont_outputs is not None:
            self.outputs = cont_outputs

        if cont_rules is not None:
            self.rules = cont_rules

        if cont_controller is not None:
            self.controller = cont_controller

        if cont_simulator is not None:
            self.simulator = cont_simulator

    @property
    def inputs(self) -> Dict[str, Antecedent]:
        """
        Antecedentes do controlador fuzzy.

        Retorna
        -------
        Dict[str, Antecedent]
            Retorna um dicionário com as chaves sendo o nome dos antecedentes
            e os valores sendo instâncias da classe
            skfuzzy.control.antecedent_consequent.Antecedent.
        """
        return self.__inputs

    @inputs.setter
    def inputs(self, fis_inputs: Dict[str, Antecedent]):
        """
        Altera os antecedentes do controlador fuzzy.

        Parâmetros
        ----------
        fis_inputs : Dict[str, Antecedent]
            Dicionário com as chaves sendo o nome dos antecedentes e os valores
            sendo instâncias da classe
            skfuzzy.control.antecedent_consequent.Antecedent.
        """

        # Verifica o parâmetro é um dicionário
        if not isinstance(fis_inputs, dict):
            raise Exception(
                "O parâmetro não é um dicionário!")

        # Verifica se o dicionário possui os tipos corretos
        for k_input, k_value in fis_inputs.items():
            # Verifica se o nome do antecedente é uma string
            if not isinstance(k_input, str):
                raise Exception(
                    "O nome do antecedente não é uma string!")

            # Verifica se o valor é instância da classe Antecedent
            if not isinstance(k_value, Antecedent):
                raise Exception(
                    f"O valor não é uma instância da classe Antecedent!")

        self.__inputs = fis_inputs

    def add_input(self, input_name: str, input_value: Antecedent):
        """
        Adiciona uma nova entrada no dicionário dos antecedentes do
        controlador fuzzy.

        Parâmetros
        ----------
        input_name: str
            Nome do antecedente

        input_value : Antecedent
            Instância da classe
            skfuzzy.control.antecedent_consequent.Antecedent.
        """

        # Verifica se o nome do antecedente é uma string
        if not isinstance(input_name, str):
            raise Exception(
                "O nome do antecedente não é uma string!")

        # Verifica se o valor do antecedente é instância da classe Antecedent
        if not isinstance(input_value, Antecedent):
            raise Exception(
                f"O valor não é uma instância da classe Antecedent!")

        self.__inputs[input_name] = input_value

    @property
    def outputs(self) -> Dict[str, Consequent]:
        """
        Consequentes do controlador fuzzy.

        Retorna
        -------
        Dict[str, Consequent]
            Retorna um dicionário com as chaves sendo o nome dos consequentes
            e os valores sendo instâncias da classe
            skfuzzy.control.antecedent_consequent.Consequent.
        """
        return self.__outputs

    @outputs.setter
    def outputs(self, fis_outputs: Dict[str, Consequent]):
        """
        Altera os consequentes do controlador fuzzy.

        Parâmetros
        ----------
        fis_inputs : Dict[str, Consequent]
            Dicionário com as chaves sendo o nome dos consequentes e os valores
            sendo instâncias da classe
            skfuzzy.control.antecedent_consequent.Consequent.
        """

        # Verifica o parâmetro é um dicionário
        if not isinstance(fis_outputs, dict):
            raise Exception(
                "O parâmetro não é um dicionário!")

        # Verifica se o dicionário possui os tipos corretos
        for k_input, k_value in fis_outputs.items():
            # Verifica se o nome do consequente é uma string
            if not isinstance(k_input, str):
                raise Exception(
                    "O nome do consequente não é uma string!")

            # Verifica se o valor é instância da classe Antecedent
            if not isinstance(k_value, Consequent):
                raise Exception(
                    f"O valor não é uma instância da classe Consequent!")

        self.__outputs = fis_outputs

    def add_output(self, output_name: str, output_value: Consequent):
        """
        Adiciona uma nova entrada no dicionário dos consequentes do
        controlador fuzzy.

        Parâmetros
        ----------
        output_name: str
            Nome do consequente

        output_value : Consequent
            Instância da classe
            skfuzzy.control.antecedent_consequent.Consequent.
        """
        # Verifica se o nome do consequente é uma string
        if not isinstance(output_name, str):
            raise Exception(
                "O nome do consequente não é uma string!")

        # Verifica se o valor do consequente é instância da classe Consequent
        if not isinstance(output_value, Consequent):
            raise Exception(
                f"O valor não é uma instância da classe Consequent!")

        self.__outputs[output_name] = output_value

    @property
    def rules(self) -> List[Rule]:
        """
        Regras do controlador fuzzy.

        Retorna
        -------
        List[Rule]
            Retorna lista com instâncias da classe skfuzzy.control.rule.Rule.
        """
        return self.__rules

    @rules.setter
    def rules(self, fis_rules: List[SkRule]):
        """
        Altera as regras do controlador fuzzy.

        Parâmetros
        ----------
        fis_rules : List[Rule]
            lista com instâncias da classe skfuzzy.control.rule.Rule.
        """
        # Verifica o parâmetro é uma lista
        if not isinstance(fis_rules, list):
            raise Exception(
                "O parâmetro não é uma lista!")

        # Verifica se os itens são instância da classe Rule
        for value in fis_rules:
            if not isinstance(value, SkRule):
                raise Exception(
                    "O valor não é uma instância da classe Rule!")

        self.__rules = fis_rules

    def add_rule(self, rule_value: SkRule):
        """
        Altera as regras do controlador fuzzy.

        Parâmetros
        ----------
        rule_value : Rule
            Instância da classe skfuzzy.control.rule.Rule.
        """
        # Verifica se o valor é instância da classe Rule
        if not isinstance(rule_value, SkRule):
            raise Exception(
                "O valor não é uma instância da classe Rule!")

        self.__rules = rule_value

    @property
    def controller(self) -> ControlSystem:
        """
        Controlador fuzzy.

        Retorna
        -------
        ControlSystem
            Retorna uma instância da classe ControlSystem.
        """
        return self.__controller

    @controller.setter
    def controller(self, f_controller: ControlSystem):
        """
        Altera o controlador fuzzy.

        Parâmetros
        ----------
        f_controller : ControlSystem
            Instância da classe ControlSystem.
        """
        if not isinstance(f_controller, ControlSystem):
            raise Exception("O parâmetro não é uma instância da classe "
                            "ControlSystem!")

        self.__controller = f_controller

    @property
    def simulator(self) -> ControlSystemSimulation:
        """
        Simulador fuzzy.

        Retorna
        -------
        ControlSystemSimulation
            Retorna uma instância da classe ControlSystemSimulation.
        """
        return self.__simulator

    @simulator.setter
    def simulator(self, f_simulator: ControlSystemSimulation):
        """
        Altera o simulador fuzzy.

        Parâmetros
        ----------
        f_simulator : ControlSystemSimulation
            Instância da classe ControlSystemSimulation.
        """
        if not isinstance(f_simulator, ControlSystemSimulation):
            raise Exception("O parâmetro não é uma instância da classe "
                            "ControlSystemSimulation!")

        self.__simulator = f_simulator
