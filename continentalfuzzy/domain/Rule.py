"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, List
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput
from continentalfuzzy.domain.definition.Connections import Connections


class Rule:
    """
    Classe usada para representar uma regra de um sistema fuzzy.
    """
    def __init__(self,
                 r_name: Optional[str] = None,
                 r_weight: Optional[float] = None,
                 r_connection: Optional[Connections] = None,
                 r_inputs: Optional[List[RuleInput]] = None,
                 r_outputs: Optional[List[RuleOutput]] = None):
        """
        Inicializador da classe FISRule

        Parâmetros
        ----------
        r_name : str
            String contendo o nome da regra.

        r_weight : float
            Float contendo o peso da regra.

        r_connection : FISConnections
            Instância da classe FISConnections com o conector dos antecedentes.

        r_inputs : List[FISRuleInput]
            lista contendo os antecedentes de uma regra.

        r_outputs : List[FISRuleOutput]
            lista contendo os consequentes de uma regra.
        """
        self.__name = None
        self.__weight = None
        self.__connection = None
        self.__inputs = list()
        self.__outputs = list()

        if r_name is not None:
            self.name = r_name

        if r_weight is not None:
            self.weight = r_weight

        if r_connection is not None:
            self.connection = r_connection

        if r_inputs is not None:
            self.inputs = r_inputs

        if r_outputs is not None:
            self.outputs = r_outputs

    @property
    def name(self) -> str:
        """
        Nome da regra.

        Retorna
        -------
        str
            Retorna uma string com o nome da regra.
        """
        return self.__name

    @name.setter
    def name(self, rule_name: str):
        """
        Altera o nome da regra.

        Parâmetros
        ----------
        rule_name : str
            String contendo o nome da regra.
        """

        if not isinstance(rule_name, str):
            raise Exception(f"O nome não é uma String!")

        self.__name = rule_name

    @property
    def weight(self) -> float:
        """
        Peso do consequente da regra.

        Retorna
        -------
        str
            Retorna um float com o peso da regra.
        """
        return self.__weight

    @weight.setter
    def weight(self, rule_weight: float):
        """
        Altera o nome da regra.

        Parâmetros
        ----------
        rule_weight : float
            Float contendo o peso da regra.
        """

        # Verifica se o parâmetro é um número float
        try:
            self.__weight = float(rule_weight)
        except Exception:
            raise Exception("O parâmetro peso não é do tipo float!")

        if rule_weight < 0 or rule_weight > 1:
            raise Exception("O peso precisa estar no intervalo 0 e 1!")

    @property
    def connection(self) -> Connections:
        """
        Conector dos antecedentes.

        Retorna
        -------
        FISConnections
            Retorna uma instância da classe FISConnections com o conector dos
            antecedentes.
        """
        return self.__connection

    @connection.setter
    def connection(self, rule_connection: Connections):
        """
        Altera o conector dos antecedentes.

        Parâmetros
        ----------
        rule_connection : FISConnections
            Instância da classe FISConnections com o conector dos antecedentes.
        """

        if not isinstance(rule_connection, Connections):
            raise Exception(f"Conector {rule_connection} não é uma "
                            f"instância da classe FISConnections!")

        self.__connection = rule_connection

    @property
    def inputs(self) -> List[RuleInput]:
        """
        Lista contendo os antecedentes de uma regra.

        Retorna
        -------
        List [FISRuleInput]
            Retorna uma lista contendo os antecedentes de uma regra.
        """
        return self.__inputs

    @inputs.setter
    def inputs(self, rule_inputs: List[RuleInput]):
        """
        Altera a lista contendo os antecedentes de uma regra.

        Parâmetros
        ----------
        rule_inputs : List[FISRuleInput]
            lista contendo os antecedentes de uma regra.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(rule_inputs, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se os itens da lista são instâncias FISRuleInput
        for value in rule_inputs:
            if not isinstance(value, RuleInput):
                raise Exception(
                    "O valor não é uma instância da classe FISRuleInput!")

        self.__inputs = rule_inputs

    def add_input(self, rule_input: RuleInput):
        """
        Adiciona uma nova entrada na lista contendo os antecedentes de uma
        regra.

        Parâmetros
        ----------
        rule_input : FISRuleInput
            Instância da classe FISRuleInput.
        """

        # Verifica se o valor é instância da classe FISRuleInput
        if not isinstance(rule_input, RuleInput):
            raise Exception("O valor não é uma instância da classe "
                            "FISRuleInput!")

        self.__inputs.append(rule_input)

    @property
    def outputs(self) -> List[RuleOutput]:
        """
        Lista contendo os consequentes de uma regra.

        Retorna
        -------
        List [FISRuleOutput]
            Retorna uma lista contendo os consequentes de uma regra.
        """
        return self.__outputs

    @outputs.setter
    def outputs(self, rule_outputs: List[RuleOutput]):
        """
        Altera a lista contendo os consequentes de uma regra.

        Parâmetros
        ----------
        rule_outputs : List[FISRuleOutput]
            lista contendo os consequentes de uma regra.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(rule_outputs, list):
            raise Exception(f"O parâmetro não é uma lista!")

        # Verifica se os itens da lista são instâncias FISRuleInput
        for value in rule_outputs:
            if not isinstance(value, RuleOutput):
                raise Exception(
                    "O valor não é uma instância da classe FISRuleOutput!")

        self.__outputs = rule_outputs

    def add_output(self, rule_output: RuleOutput):
        """
        Adiciona uma nova entrada na lista contendo os consequentes de uma
        regra.

        Parâmetros
        ----------
        rule_output : FISRuleOutput
            Instância da classe FISRuleOutput.
        """

        # Verifica se o valor é instância da classe FISRuleOutput
        if not isinstance(rule_output, RuleOutput):
            raise Exception("O valor não é uma instância da classe "
                            "FISRuleOutput!")

        self.__outputs.append(rule_output)
