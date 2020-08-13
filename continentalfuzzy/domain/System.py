"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import Optional, List, Dict
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.domain.variable.Output import Output
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.AggMethods import AggMethods
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.ImpMethods import ImpMethods
from continentalfuzzy.domain.definition.OrMethods import OrMethods


class System:
    """
    Classe usada para armazenar todos os componentes de um arquivo (.fis).
    """
    # Constante com o número máximo de consequentes
    MAX_NUM_OUTPUTS = 1

    # Dicionário com os conectores implementados e a equivalência com
    # relação ao arquivo .fis
    DICT_CONNECTORS = {'1': 'AND', '2': 'OR'}

    def __init__(self,
                 sys_name: Optional[str] = None,
                 sys_filename: Optional[str] = None,
                 sys_type: Optional[ControllerType] = None,
                 sys_version: Optional[str] = None,
                 sys_num_inputs: Optional[int] = None,
                 sys_num_outputs: Optional[int] = None,
                 sys_num_rules: Optional[int] = None,
                 sys_and_method: Optional[AndMethods] = None,
                 sys_or_method: Optional[OrMethods] = None,
                 sys_imp_method: Optional[ImpMethods] = None,
                 sys_agg_method: Optional[AggMethods] = None,
                 sys_defuzz_method: Optional[DefuzzMethods] = None,
                 sys_inputs: Optional[Dict[int, Input]] = None,
                 sys_outputs: Optional[Dict[int, Output]] = None,
                 sys_rules: Optional[List[Rule]] = None,
                 sys_facies_association: Optional[Dict[int, int]] = None,
                 sys_use_dict_facies_association: Optional[bool] = None):
        """
        Inicializador da classe System

        Parâmetros
        ----------
        sys_name : str
            String contendo o nome da regra.

        sys_filename : str
            Caminho do arquivo .fis.

        sys_type : ControllerType
            Instância da classe ControllerType.

        sys_version : str
            String contendo a versão da biblioteca fuzzy do Matlab.

        sys_num_inputs : int
            Número de antecedentes do Sistema Fuzzy.

        sys_num_outputs : int
            Número de consequentes do Sistema Fuzzy.

        sys_num_rules : int
            Número de regras do Sistema Fuzzy.

        sys_and_method : ANDMethods
            Instância da classe ANDMethods.

        sys_or_method : ORMethods
            Instância da classe ORMethods.

        sys_imp_method : ImpMethods
            Instância da classe ImpMethods.

        sys_agg_method : AggMethods
            Instância da classe AggMethods.

        sys_defuzz_method : DefuzzMethods
            Instância da classe DefuzzMethods.

        sys_inputs : dict
            Dicionário contendo os antecedentes do sistema fuzzy.

        sys_outputs : dict
            Dicionário contendo os consequentes do sistema fuzzy.

        sys_rules : list
            Lista contendo as regras do sistema fuzzy.


        """
        self.__name = None
        self.__filename = None
        self.__type = None
        self.__version = None
        self.__num_inputs = None
        self.__num_outputs = None
        self.__num_rules = None
        self.__and_method = None
        self.__or_method = None
        self.__imp_method = None
        self.__agg_method = None
        self.__defuzz_method = None
        self.__inputs = dict()
        self.__outputs = dict()
        self.__rules = list()
        self.__facies_association = dict()
        self.__use_dict_facies_association = None

        if sys_name is not None:
            self.name = sys_name

        if sys_filename is not None:
            self.filename = sys_filename

        if sys_type is not None:
            self.type = sys_type

        if sys_version is not None:
            self.version = sys_version

        if sys_num_inputs is not None:
            self.num_inputs = sys_num_inputs

        if sys_num_outputs is not None:
            self.num_outputs = sys_num_outputs

        if sys_num_rules is not None:
            self.num_rules = sys_num_rules

        if sys_and_method is not None:
            self.and_method = sys_and_method

        if sys_or_method is not None:
            self.or_method = sys_or_method

        if sys_imp_method is not None:
            self.imp_method = sys_imp_method

        if sys_agg_method is not None:
            self.agg_method = sys_agg_method

        if sys_agg_method is not None:
            self.agg_method = sys_agg_method

        if sys_defuzz_method is not None:
            self.defuzz_method = sys_defuzz_method

        if sys_inputs is not None:
            self.inputs = sys_inputs

        if sys_outputs is not None:
            self.outputs = sys_outputs

        if sys_rules is not None:
            self.rules = sys_rules

        if sys_facies_association:
            self.__facies_association = sys_facies_association

        if sys_use_dict_facies_association:
            self.__use_dict_facies_association = sys_use_dict_facies_association

    @property
    def name(self) -> str:
        """
        Nome do sistema fuzzy.

        Retorna
        -------
        str
            Retorna uma string com o nome do sistema fuzzy.
        """
        return self.__name

    @name.setter
    def name(self, sys_name: str):
        """
        Altera o nome do sistema fuzzy.

        Parâmetros
        ----------
        sys_name : str
            String contendo o nome do sistema fuzzy.
        """

        if not isinstance(sys_name, str):
            raise Exception(f"O nome não é uma String!")

        self.__name = sys_name

    @property
    def filename(self) -> str:
        """
        Caminho do arquivo .fis.

        Retorna
        -------
        str
            Retorna uma string com o caminho do arquivo .fis.
        """
        return self.__filename

    @filename.setter
    def filename(self, sys_filename: str):
        """
        Altera o caminho do arquivo .fis.

        Parâmetros
        ----------
        sys_filename : str
            String contendo o caminho do arquivo .fis.
        """

        if not isinstance(sys_filename, str):
            raise Exception(f"O caminho do arquivo .fis. não é uma String!")

        self.__filename = sys_filename

    @property
    def type(self) -> ControllerType:
        """
        Tipo de inferência.

        Retorna
        -------
        ControllerType
            Retorna uma instância da classe ControllerType.
        """
        return self.__type

    @type.setter
    def type(self, sys_type: ControllerType):
        """
        Altera o tipo de inferência.

        Parâmetros
        ----------
        sys_type : ControllerType
            Instância da classe ControllerType.
        """

        if not isinstance(sys_type, ControllerType):
            raise Exception("O tipo de inferência não é uma instância da "
                            "classe ControllerType!")

        self.__type = sys_type

    @property
    def version(self) -> str:
        """
        Versão da biblioteca fuzzy do Matlab.

        Retorna
        -------
        str
            Retorna uma string com a versão da biblioteca fuzzy do Matlab.
        """
        return self.__version

    @version.setter
    def version(self, sys_version: str):
        """
        Altera a versão da biblioteca fuzzy do Matlab.

        Parâmetros
        ----------
        sys_version : str
            String contendo a versão da biblioteca fuzzy do Matlab.
        """

        if not isinstance(sys_version, str):
            raise Exception("A versão da biblioteca fuzzy do Matlab não é "
                            "uma String!")

        self.__version = sys_version

    @property
    def num_inputs(self) -> int:
        """
        Número de antecedentes do Sistema Fuzzy.

        Retorna
        -------
        int
            Retorna um inteiro com o número de antecedentes.
        """
        return self.__num_inputs

    @num_inputs.setter
    def num_inputs(self, sys_num_inputs: int):
        """
        Altera o número de antecedentes do Sistema Fuzzy.

        Parâmetros
        ----------
        sys_num_inputs : int
            Inteiro contendo o número de antecedentes.
        """

        if not isinstance(sys_num_inputs, int):
            raise Exception("O número de antecedentes do Sistema Fuzzy não é "
                            "um número inteiro!")

        self.__num_inputs = sys_num_inputs

    @property
    def num_outputs(self) -> int:
        """
        Número de consequentes do Sistema Fuzzy.

        Retorna
        -------
        int
            Retorna um inteiro com o número de consequentes.
        """
        return self.__num_outputs

    @num_outputs.setter
    def num_outputs(self, sys_num_outputs: int):
        """
        Altera o número de consequentes do Sistema Fuzzy.

        Parâmetros
        ----------
        sys_num_outputs : int
            Inteiro contendo o número de consequentes.
        """

        if not isinstance(sys_num_outputs, int):
            raise Exception("O número de consequentes do Sistema Fuzzy não é "
                            "um número inteiro!")

        # Verifica se o número de consequentes é menor igual ao máximo definido
        if sys_num_outputs > self.MAX_NUM_OUTPUTS:
            raise Exception(
                f"Número máximo de consequentes é {self.MAX_NUM_OUTPUTS}"
                f", número informado é {sys_num_outputs}!")

        self.__num_outputs = sys_num_outputs

    @property
    def num_rules(self) -> int:
        """
        Número de regras do Sistema Fuzzy.

        Retorna
        -------
        int
            Retorna um inteiro com o número de regras.
        """
        return self.__num_rules

    @num_rules.setter
    def num_rules(self, sys_num_rules: int):
        """
        Altera o número de regras do Sistema Fuzzy.

        Parâmetros
        ----------
        sys_num_rules : int
            Inteiro contendo o número de regras.
        """

        if not isinstance(sys_num_rules, int):
            raise Exception("O número de regras do Sistema Fuzzy não é "
                            "um número inteiro!")

        self.__num_rules = sys_num_rules

    @property
    def and_method(self) -> AndMethods:
        """
        Método usado para o "AND" fuzzy.

        Retorna
        -------
        ANDMethods
            Retorna uma instância da classe ANDMethods.
        """
        return self.__and_method

    @and_method.setter
    def and_method(self, sys_and_method: AndMethods):
        """
        Altera o método usado para o "AND" fuzzy.

        Parâmetros
        ----------
        sys_and_method : ANDMethods
            Instância da classe ANDMethods.
        """

        if not isinstance(sys_and_method, AndMethods):
            raise Exception("O método AND fuzzy não é uma instância da "
                            "classe ANDMethods!")

        self.__and_method = sys_and_method

    @property
    def or_method(self) -> OrMethods:
        """
        Método usado para o "OR" fuzzy.

        Retorna
        -------
        ORMethods
            Retorna uma instância da classe ORMethods.
        """
        return self.__or_method

    @or_method.setter
    def or_method(self, sys_or_method: OrMethods):
        """
        Altera o método usado para o "OR" fuzzy.

        Parâmetros
        ----------
        sys_or_method : ORMethods
            Instância da classe ORMethods.
        """

        if not isinstance(sys_or_method, OrMethods):
            raise Exception("O método OR fuzzy não é uma instância da "
                            "classe ORMethods!")

        self.__or_method = sys_or_method

    @property
    def imp_method(self) -> ImpMethods:
        """
        Método de implicação do sistema fuzzy.

        Retorna
        -------
        ImpMethods
            Retorna uma instância da classe ImpMethods.
        """
        return self.__imp_method

    @imp_method.setter
    def imp_method(self, sys_imp_method: ImpMethods):
        """
        Altera o método de implicação do sistema fuzzy.

        Parâmetros
        ----------
        sys_imp_method : ImpMethods
            Instância da classe ImpMethods.
        """

        if not isinstance(sys_imp_method, ImpMethods):
            raise Exception("O método de implicação não é uma instância da "
                            "classe ImpMethods!")

        self.__imp_method = sys_imp_method

    @property
    def agg_method(self) -> AggMethods:
        """
        Método de agregação do sistema fuzzy.

        Retorna
        -------
        AggMethods
            Retorna uma instância da classe AggMethods.
        """
        return self.__agg_method

    @agg_method.setter
    def agg_method(self, sys_agg_method: str):
        """
        Altera o método de agregação do sistema fuzzy.

        Parâmetros
        ----------
        sys_agg_method : AggMethods
            Instância da classe AggMethods.
        """

        if not isinstance(sys_agg_method, AggMethods):
            raise Exception("O método de agregação não é uma instância da "
                            "classe AggMethods!")

        self.__agg_method = sys_agg_method

    @property
    def defuzz_method(self) -> DefuzzMethods:
        """
        Método de defuzzificação do sistema fuzzy.

        Retorna
        -------
        DefuzzMethods
            Retorna uma instância da classe DefuzzMethods.
        """
        return self.__defuzz_method

    @defuzz_method.setter
    def defuzz_method(self, sys_defuzz_method: DefuzzMethods):
        """
        Altera o método de defuzzificação do sistema fuzzy.

        Parâmetros
        ----------
        sys_defuzz_method : DefuzzMethods
            Instância da classe DefuzzMethods.
        """

        if not isinstance(sys_defuzz_method, DefuzzMethods):
            raise Exception("O método de defuzzificação não é uma instância "
                            "da classe DefuzzMethods!")

        self.__defuzz_method = sys_defuzz_method

    @property
    def inputs(self) -> Dict[int, Input]:
        """
        Dicionário contendo os antecedentes do sistema fuzzy.

        A chave do dicionário é o número do antecedente.
        O valor é uma instância da classe Input.

        Retorna
        -------
        Dict [int, Input]
            Retorna um dicionário onde a chave é o número do antecedente e o
            valor é uma instância da classe Input.
        """
        return self.__inputs

    @inputs.setter
    def inputs(self, sys_inputs: Dict[int, Input]):
        """
        Altera o dicionário contendo os antecedentes do sistema fuzzy.

        Parâmetros
        ----------
        sys_inputs : Dict[int, Input]
            Dicionário contendo os antecedentes do sistema fuzzy.
        """

        # Verifica se o número de inputs já foi informado
        if self.num_inputs is None:
            raise Exception(f"O número de antecedentes não foi informado!")

        # Verifica se a quantidade de antecedentes está correta
        if len(sys_inputs) != self.num_inputs:
            raise Exception("Quantidade de antecedentes é diferente da "
                            "informada no bloco do sistema!")

        # # Verifica se o dicionário possui os tipos corretos
        for k_input, k_value in sys_inputs.items():
            if not isinstance(k_input, int):
                raise Exception(
                    "A chave não é uma número inteiro!")
            if not isinstance(k_value, Input):
                raise Exception(
                    "O valor não é uma instância da classe Input!")

        self.__inputs = sys_inputs

    def add_input(self, sys_num: int, sys_value: Input):
        """
        Adiciona uma nova entrada no dicionário contendo os antecedentes do
        sistema fuzzy.

        Parâmetros
        ----------
        sys_num : int
            Inteiro com o número do antecedente.

        sys_value : Input
            Instância da classe Input.
        """

        # Verifica se o número do antecedente é um número inteiro
        if not isinstance(sys_num, int):
            raise Exception(
                "O número do antecedente não é um número inteiro!")

        # Verifica se o número de inputs já foi informado
        if self.num_inputs is None:
            raise Exception(f"O número de antecedentes não foi informado!")

        # Verifica se o número do antecedente já foi cadastrado
        if self.__inputs.get(sys_num) is not None:
            raise Exception(f"Número do antecedente {sys_num} já cadastrado!")

        # Verifica se a quantidade de antecedentes está correta
        if len(self.__inputs) >= self.num_inputs:
            raise Exception("Não é possível adicionar mais antecedentes!")

        # Verifica se o valor do dicionário é instância da classe Input
        if not isinstance(sys_value, Input):
            raise Exception(f"O valor não é uma instância da classe Input!")

        self.__inputs[sys_num] = sys_value

    @property
    def outputs(self) -> Dict[int, Output]:
        """
        Dicionário contendo os consequentes do sistema fuzzy.

        A chave do dicionário é o número do consequente.
        O valor é uma instância da classe Output.

        Retorna
        -------
        Dict [int, Output]
            Retorna um dicionário onde a chave é o número do consequente e o
            valor é uma instância da classe Output.
        """
        return self.__outputs

    @outputs.setter
    def outputs(self, sys_outputs: Dict[int, Output]):
        """
        Altera o dicionário contendo os consequentes do sistema fuzzy.

        Parâmetros
        ----------
        sys_outputs : Dict[int, Output]
            Dicionário contendo os consequentes do sistema fuzzy.
        """

        # Verifica se o número de outputs já foi informado
        if self.num_outputs is None:
            raise Exception(f"O número de consequentes não foi informado!")

        # Verifica se a quantidade de consequentes está correta
        if len(sys_outputs) != self.num_outputs:
            raise Exception("Quantidade de consequentes é diferente da "
                            "informada no bloco do sistema!")

        # Verifica se o dicionário possui os tipos corretos
        for k_output, k_value in sys_outputs.items():
            if not isinstance(k_output, int):
                raise Exception(
                    "A chave não é uma número inteiro!")
            if not isinstance(k_value, Output):
                raise Exception(
                    "O valor não é uma instância da classe Output!")

        self.__outputs = sys_outputs

    def add_output(self, sys_num: int, sys_value: Output):
        """
        Adiciona uma nova entrada no dicionário contendo os consequentes do
        sistema fuzzy.

        Parâmetros
        ----------
        sys_num : int
            Inteiro com o número do consequente.

        sys_value : Output
            Instância da classe Output.
        """

        # Verifica se o número do consequente é um número inteiro
        if not isinstance(sys_num, int):
            raise Exception(
                "O número do consequente não é um número inteiro!")

        # Verifica se o número de inputs já foi informado
        if self.num_outputs is None:
            raise Exception(f"O número de consequentes não foi informado!")

        # Verifica se a quantidade de consequentes está correta
        if len(self.__outputs) >= self.num_outputs:
            raise Exception("Não é possível adicionar mais consequentes!")

        # Verifica se o número do consequente já foi cadastrado
        if self.__outputs.get(sys_num) is not None:
            raise Exception(f"Número do consequente {sys_num} já cadastrado!")

        # Verifica se os valor do dicionário é instância da classe Output
        if not isinstance(sys_value, Output):
            raise Exception(
                f"O valor não é uma instância da classe Output!")

        self.__outputs[sys_num] = sys_value

    @property
    def rules(self) -> List[Rule]:
        """
        Lista contendo as regras do sistema fuzzy.

        Os valores da lista são instâncias da classe Rule.

        Retorna
        -------
        List[Rule]
            Retorna uma lista com as instâncias da classe Rule.
        """

        return self.__rules

    @rules.setter
    def rules(self, sys_rules: List[Rule]):
        """
        Altera a lista contendo as regras do sistema fuzzy.

        Parâmetros
        ----------
        sys_rules : List[Rule]
            Lista contendo as regras do sistema fuzzy.
        """

        # Verifica se o número de regras já foi informado
        if self.num_rules is None:
            raise Exception(f"O número de regras não foi informado!")

        # Verifica se a quantidade de regras está correta
        if len(sys_rules) != self.num_rules:
            raise Exception("Quantidade de regras é diferente da informada no "
                            "bloco do sistema!")

        # Verifica se os valores da lista são instâncias da classe Rule
        for value in sys_rules:
            if not isinstance(value, Rule):
                raise Exception(
                    f"O valor não é uma instância da classe Rule!")

        self.__rules = sys_rules

    def add_rule(self, sys_rule: Rule):
        """
        Adiciona uma nova entrada na lista contendo as regras do
        sistema fuzzy.

        Parâmetros
        ----------
        sys_rule : Rule
            Instância da classe Rule.
        """

        # Verifica se o número de regras já foi informado
        if self.num_rules is None:
            raise Exception(f"O número de regras não foi informado!")

        # Verifica se a quantidade de regras está correta
        if len(self.rules) >= self.num_rules:
            raise Exception("Não é possível adicionar mais regras!")

        if not isinstance(sys_rule, Rule):
            raise Exception(
                f"O valor não é uma instância da classe Rule!")

        self.__rules.append(sys_rule)

    @property
    def facies_association(self) -> Dict[int, int]:
        return self.__facies_association

    @facies_association.setter
    def facies_association(self, sys_facies_association: Dict[int, int]):
        # Verifica se o dicionário possui os tipos corretos
        for k_output, k_value in sys_facies_association.items():
            if not isinstance(k_output, int):
                raise Exception(
                    "A chave não é uma número inteiro!")
            if not isinstance(k_value, int):
                raise Exception(
                    "O valor não é uma número inteiro!")

        self.__facies_association = sys_facies_association

    def add_facies_association(self, sys_num: int, sys_value: Output):
        # Verifica se a associação de fácies já foi cadastrada
        if self.__facies_association.get(sys_num) is not None:
            raise Exception(f"Associação de Fácies {sys_num} já cadastrada!")

        # Verifica se a chave do dicionário é um inteiro
        if not isinstance(sys_num, int):
            raise Exception(
                "A chave não é uma número inteiro!")

        # Verifica se o valor do dicionário é um inteiro
        if not isinstance(sys_value, int):
            raise Exception(
                "O valor não é uma número inteiro!")

        self.__facies_association[sys_num] = sys_value

    @property
    def use_dict_facies_association(self) -> bool:
        return self.__use_dict_facies_association

    @use_dict_facies_association.setter
    def use_dict_facies_association(self,
                                    sys_use_dict_facies_association: bool):
        if not isinstance(sys_use_dict_facies_association, bool):
            raise Exception(f"O nome não é um booleano!")

        self.__use_dict_facies_association = sys_use_dict_facies_association