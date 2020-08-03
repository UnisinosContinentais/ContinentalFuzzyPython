"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List

from continentalfuzzy.domain.definition.AggMethods import AggMethods
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.ImpMethods import ImpMethods
from continentalfuzzy.domain.definition.OrMethods import OrMethods
from continentalfuzzy.domain.definition.sugeno.SugenoAggMethods import SugenoAggMethods
from continentalfuzzy.domain.definition.sugeno.SugenoAndMethods import SugenoAndMethods
from continentalfuzzy.domain.definition.sugeno.SugenoDefuzzMethods import \
    SugenoDefuzzMethods
from continentalfuzzy.domain.definition.sugeno.SugenoImpMethods import SugenoImpMethods
from continentalfuzzy.domain.definition.sugeno.SugenoOrMethods import SugenoOrMethods
from continentalfuzzy.service.InputService import InputService
from continentalfuzzy.service.OutputService import OutputService
from continentalfuzzy.domain.Rule import Rule
from continentalfuzzy.domain.System import System
from continentalfuzzy.domain.rule_variable.RuleInput import RuleInput
from continentalfuzzy.domain.rule_variable.RuleOutput import RuleOutput
from continentalfuzzy.domain.definition.mamdani.MamdaniAndMethods import MamdaniAndMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniAggMethods import MamdaniAggMethods
from continentalfuzzy.domain.definition.Blocks import Blocks
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.ControllerType import \
    ControllerType
from continentalfuzzy.domain.definition.mamdani.MamdaniDefuzzMethods import \
    MamdaniDefuzzMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniImpMethods import MamdaniImpMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniOrMethods import MamdaniOrMethods


class SystemService:
    def __init__(self):
        self.__system = System()

    @property
    def system(self) -> System:
        return self.__system

    def create_system_from_list(self, s_list: List[str]):
        """
        Preenche as informações do bloco sistema a partir das informações de
        um arquivo .fis.

        Parâmetros
        ----------
        s_list : List[str]
            Lista com as entradas de um arquivo .fis com as informações do
            bloco sistema.
        """
        for entry in s_list:
            # Divide a string das entradas no sinal de "=" em nome
            # e valor
            l_attr = entry.split(sep='=')

            # Preenche os atributos da classe baseado nas
            # entradas do arquivo .fis
            if l_attr[0] == 'Name':
                self.system.name = l_attr[1][:-1].replace("'", "")
            if l_attr[0] == 'Type':
                control_type = l_attr[1][:-1].replace("'", "")
                try:
                    self.system.type = ControllerType[control_type]
                except Exception:
                    raise Exception(f"O controlador {control_type} não foi "
                                    f"implementado!")
            if l_attr[0] == 'Version':
                self.system.version = l_attr[1].replace("'", "")
            if l_attr[0] == 'NumInputs':
                self.system.num_inputs = int(l_attr[1])
            if l_attr[0] == 'NumOutputs':
                self.system.num_outputs = int(l_attr[1])
            if l_attr[0] == 'NumRules':
                self.system.num_rules = int(l_attr[1])

            if self.system.type == ControllerType.mamdani:
                if l_attr[0] == 'AndMethod':
                    and_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = MamdaniAndMethods[and_meth_name]
                    except Exception:
                        raise Exception(f"O método AND {and_meth_name} não foi "
                                        f"implementado para inferência "
                                        f"Mamdani!")
                    self.system.and_method = AndMethods[and_meth_name]

                if l_attr[0] == 'OrMethod':
                    or_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = MamdaniOrMethods[or_meth_name]
                    except Exception:
                        raise Exception(f"O método OR {or_meth_name} não foi "
                                        f"implementado para inferência "
                                        f"Mamdani!")
                    self.system.or_method = OrMethods[or_meth_name]

                if l_attr[0] == 'ImpMethod':
                    imp_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = MamdaniImpMethods[imp_meth_name]
                    except Exception:
                        raise Exception(
                            f"O método de implicação {imp_meth_name} "
                            f"não foi implementado para inferência "
                            f"Mamdani!")
                    self.system.imp_method = ImpMethods[imp_meth_name]

                if l_attr[0] == 'AggMethod':
                    agg_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = MamdaniAggMethods[agg_meth_name]
                    except Exception:
                        raise Exception(
                            f"O método de agregação {agg_meth_name} "
                            f"não foi implementado para inferência "
                            f"Mamdani!")
                    self.system.agg_method = AggMethods[agg_meth_name]

                if l_attr[0] == 'DefuzzMethod':
                    defuzz_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = MamdaniDefuzzMethods[defuzz_name]
                    except Exception:
                        raise Exception(
                            f"O método de defuzzificação {defuzz_name} "
                            f"não foi implementado para inferência "
                            f"Mamdani!")
                    self.system.defuzz_method = DefuzzMethods[defuzz_name]

            elif self.system.type == ControllerType.sugeno:
                if l_attr[0] == 'AndMethod':
                    and_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = SugenoAndMethods[and_meth_name]
                    except Exception:
                        raise Exception(f"O método AND {and_meth_name} não foi "
                                        f"implementado para inferência Sugeno!")
                    self.system.and_method = AndMethods[and_meth_name]

                if l_attr[0] == 'OrMethod':
                    or_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = SugenoOrMethods[or_meth_name]
                    except Exception:
                        raise Exception(f"O método OR {or_meth_name} não foi "
                                        f"implementado para inferência Sugeno!")
                    self.system.or_method = OrMethods[or_meth_name]

                if l_attr[0] == 'ImpMethod':
                    imp_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = SugenoImpMethods[imp_meth_name]
                    except Exception:
                        raise Exception(
                            f"O método de implicação {imp_meth_name} "
                            f"não foi implementado para inferência Sugeno!")
                    self.system.imp_method = ImpMethods[imp_meth_name]

                if l_attr[0] == 'AggMethod':
                    agg_meth_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = SugenoAggMethods[agg_meth_name]
                    except Exception:
                        raise Exception(
                            f"O método de agregação {agg_meth_name} "
                            f"não foi implementado para inferência Sugeno!")
                    self.system.agg_method = AggMethods[agg_meth_name]

                if l_attr[0] == 'DefuzzMethod':
                    defuzz_name = l_attr[1][:-1].replace("'", "")
                    try:
                        _ = SugenoDefuzzMethods[defuzz_name]
                    except Exception:
                        raise Exception(
                            f"O método de defuzzificação {defuzz_name} "
                            f"não foi implementado para inferência Sugeno!")
                    self.system.defuzz_method = DefuzzMethods[defuzz_name]

    def valid_system(self):
        """
        Verifica se todos os atributos do sistema foram preechidos.
        """

        if self.system.name is None:
            raise Exception(f"O nome não foi informado!")
        if self.system.filename is None:
            raise Exception(f"O nome do arquivo não foi informado!")
        if self.system.type is None:
            raise Exception(f"O tipo não foi informado!")
        if self.system.version is None:
            raise Exception(f"A versão não foi informada!")
        if self.system.num_inputs is None:
            raise Exception(f"O número de antecedentes não foi informado!")
        if self.system.num_outputs is None:
            raise Exception(f"O número de consequentes não foi informado!")
        if self.system.num_rules is None:
            raise Exception(f"O número de regras não foi informado!")
        if self.system.and_method is None:
            raise Exception(f"O método AND fuzzy não foi informado!")
        if self.system.or_method is None:
            raise Exception(f"O método OR fuzzy não foi informado!")
        if self.system. imp_method is None:
            raise Exception(f"O método de implicação não foi informado!")
        if self.system.agg_method is None:
            raise Exception(f"O método de agregação não foi informado!")
        if self.system.defuzz_method is None:
            raise Exception(f"O método de defuzzificação não foi informado!")

    def create_inputs_from_list(self, i_list: List[List[str]]):
        """
        Cria os antecedentes com as informações dos blocos de inputs do
        arquivo .fis.

        Parâmetros
        ----------
        i_list : List[List{str]]
            Lista de listas com as entradas de um arquivo .fis com as
            informações sobre os antecedentes.

            Cada lista interna tem as informações sobre um antecedente.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(i_list, list):
            raise Exception(
                "O parâmetro não é um lista!")

        # Verifica se a quantidade de antecedentes está correta
        if len(i_list) == self.system.num_inputs:
            for item_index, i_item_list in enumerate(i_list):

                # Verifica se o parâmetro é uma lista
                if not isinstance(i_item_list, list):
                    raise Exception(
                        "Um dos itens não é um lista!")

                # Verifica se os items da lista são strings
                for line in i_item_list:
                    if not isinstance(line, str):
                        raise Exception(
                            "Um dos items da lista não é uma string!")

                fisInputService = InputService()
                fisInputService.create_from_fis_block(self.system.type,
                                                      i_item_list)
                new_input = fisInputService.input
                self.system.add_input((item_index + 1), new_input)

        else:
            raise Exception(f"Quantidade de antecedentes é diferente do número "
                            "de antecedentes informado no bloco System!")

    def create_outputs_from_list(self, o_list: List[List[str]]):
        """
        Cria os consequentes com as informações dos blocos de inputs do
        arquivo .fis.

        Parâmetros
        ----------
        o_list : List[List{str]]
            Lista de listas com as entradas de um arquivo .fis com as
            informações sobre os consequentes.

            Cada lista interna tem as informações sobre um consequente.
        """

        # Verifica se o parâmetro é uma lista
        if not isinstance(o_list, list):
            raise Exception(
                "O parâmetro não é um lista!")

        # Verifica se a quantidade de consequentes está correta
        if len(o_list) == self.system.num_outputs:
            for item_index, o_item_list in enumerate(o_list):

                # Verifica se o parâmetro é uma lista
                if not isinstance(o_item_list, list):
                    raise Exception(
                        "Um dos itens não é um lista!")

                # Verifica se os items da lista são strings
                for line in o_item_list:
                    if not isinstance(line, str):
                        raise Exception(
                            "Um dos items da lista não é uma string!")

                fisOutputService = OutputService()
                fisOutputService.create_from_fis_block(self.system.type,
                                                       o_item_list,
                                                       self.system.num_inputs)
                new_output = fisOutputService.output

                self.system.add_output((item_index + 1), new_output)

        else:
            raise Exception(f"Quantidade de consequentes é diferente do número "
                            "de consequentes informado no bloco System!")

    def create_inputs_rule(self, i_r_list: List[str]) -> List[RuleInput]:
        """
        Cria os antededentes das regras com as informações do bloco de rules do
        arquivo .fis.

        Parâmetros
        ----------
        i_r_list : List[str]
            Lista com as entradas de um arquivo .fis com as informações sobre
            os antecedentes das regras.

        Retorna
        -------
        List[RuleInput]
            Retorna uma lista com as instâncias da classe RuleInput.
        """

        # Lista com os antecedentes das regras
        list_rule_inputs = []

        # Percorre todos os antecedentes da regra
        for n_input, r_input in enumerate(i_r_list):

            # Verifica se o antecedente é um número inteiro
            try:
                r_input = int(r_input)
            except Exception:
                raise Exception("O antecedente da regra não é um número "
                                "inteiro!")

            # Se o valor do antecedente for zero pula para o próximo
            if r_input == 0:
                continue

            # Cria um novo antecedente da regra
            new_rule_input = RuleInput()

            # Busca o nome de identificação do antecedente
            class_input = self.system.inputs.get(n_input + 1)

            # Verifica se o antecedente foi cadastrado
            if class_input is None:
                raise Exception(f"O antecedente número: {n_input + 1}, "
                                f"não foi cadastrado!")

            new_rule_input.name = class_input.name

            # Busca a função de pertinência do antecedente
            class_input_mf = class_input.mfs.get(abs(r_input))

            # Verifica se a função de pertinência do antecedente foi
            # cadastrada
            if class_input_mf is None:
                raise Exception(f"A função de pertinência {r_input} do "
                                f"antecedente {new_rule_input.name}, "
                                f"não foi cadastrada!")

            new_rule_input.mf = class_input_mf.name

            # Verificar o operador NOT
            if int(r_input) < 0:
                new_rule_input.var_not = True
            else:
                new_rule_input.var_not = False

            list_rule_inputs.append(new_rule_input)

        return list_rule_inputs

    def create_outputs_rule(self, o_r_list: List[str]) -> List[RuleOutput]:
        """
        Cria os consequentes das regras com as informações do bloco de rules do
        arquivo .fis.

        Parâmetros
        ----------
        o_r_list : List[str]
            Lista com as entradas de um arquivo .fis com as informações sobre
            os consequentes das regras.

        Retorna
        -------
        List[RuleOutput]
            Retorna uma lista com as instâncias da classe RuleOutput.
        """

        # Lista com os consequentes das regras
        list_rule_outputs = []

        # Percorre todos os consequentes da regra
        for n_output, r_output in enumerate(o_r_list):

            # Verifica se o consequente é um número inteiro
            try:
                r_output = int(r_output)
            except Exception:
                raise Exception(
                    "O consequente da regra não é um número inteiro!")

            # Se o valor do antecedente for zero pula para o próximo
            if r_output == 0:
                continue

            # Verificar o operador NOT
            if int(r_output) < 0:
                raise Exception(
                    "O consequente da regra não pode ser negado!")

            # Cria um novo antecedente da regra
            new_rule_output = RuleOutput()

            # Busca o nome de identificação do consequente
            class_output = self.system.outputs.get(n_output + 1)

            # Verifica se o consequente foi cadastrado
            if class_output is None:
                raise Exception(f"O consequente número: {n_output + 1}, "
                                f"não foi cadastrado!")

            new_rule_output.name = class_output.name

            # Busca a função de pertinência do consequente
            class_output_mf = class_output.mfs.get(abs(int(r_output)))

            # Verifica se a função de pertinência do consequente foi
            # cadastrada
            if class_output_mf is None:
                raise Exception(f"A função de pertinência {r_output} do "
                                f"consequente {new_rule_output.name}, "
                                f"não foi cadastrada!")

            new_rule_output.mf = class_output_mf.name

            list_rule_outputs.append(new_rule_output)

        return list_rule_outputs

    def create_rules_from_list(self, r_list: List[str]):
        """
        Cria as regras com as informações do bloco de rules do arquivo .fis.

        Parâmetros
        ----------
        r_list : List[str]
            Lista com as entradas de um arquivo .fis com as informações sobre
            as regras.
        """

        # Verifica se a quantidade de regras está correta
        if len(r_list) == self.system.num_rules:

            # Percorre cada uma das regras
            for rule_number, entry in enumerate(r_list):

                # Cria uma nova regra
                new_rule = Rule()
                new_rule.name = f"rule_{rule_number + 1}"

                # Separa a string em antecedentes e o restante
                inputs_other = entry.split(sep=',')

                # Separa os antecedentes da regra
                r_inputs = inputs_other[0].split()

                # Verifica se a quantidade de antecedentes está correta
                if len(r_inputs) != self.system.num_inputs:
                    raise Exception(
                        "Quantidade de antecedentes da regra é diferente do "
                        "número de antecedentes informado no bloco System!")

                # Cria os antededentes das regras
                new_rule.inputs = self.create_inputs_rule(r_inputs)

                # Separa o consequentes do tipo de conector
                output_conn = inputs_other[1].split(':')

                # Separa o consequentes do peso
                output_weight = output_conn[0].strip().split()

                # Separa os consequentes da regra
                r_outputs = output_weight[:-1]

                # Verifica se a quantidade de consequentes está correta
                if len(r_outputs) != self.system.num_outputs:
                    raise Exception(
                        "Quantidade de consequentes da regra é diferente do "
                        "número de consequentes informado no bloco System!")

                # Cria os consequentes das regras
                new_rule.outputs = self.create_outputs_rule(r_outputs)

                # Verifica se o peso do consequente é um número float
                try:
                    # Salva o peso do consequente
                    new_rule.weight = float(output_weight[-1][1:-1])
                except Exception:
                    raise Exception("O peso do consequente da regra não é um "
                                    "número float!")

                r_connection = self.system.DICT_CONNECTORS.get(
                    output_conn[1].strip())

                # Verifica se o conector informado foi implementado
                if r_connection is None:
                    raise Exception(f"O conector {output_conn[1].strip()} da "
                                    f"regra {new_rule.name}, não foi "
                                    f"implementado!")

                # Salva os conectores dos antecedentes
                new_rule.connection = Connections[r_connection]

                self.system.add_rule(new_rule)
        else:
            raise Exception(f"Quantidade de regras é diferente do número "
                            "de regras informado no bloco System!")

    def valid_import(self):
        """
        Verifica se a importação preencheu todas as informações.
        """
        if self.system.filename is None:
            raise Exception(f"O caminho do arquivo não foi informado!")
        if len(self.system.inputs) != self.system.num_inputs:
            raise Exception(f"Não foi importada a quantidade correta de "
                            f"antecedentes!")
        if len(self.system.outputs) != self.system.num_outputs:
            raise Exception(f"Não foi importada a quantidade correta de "
                            f"consequentes!")
        if len(self.system.rules) != self.system.num_rules:
            raise Exception(f"Não foi importada a quantidade correta de "
                            f"regras!")

    def import_file(self, filename: str):
        """
        Importa um arquivo .fis e cria todos os componentes de um sistema fuzzy.

        Parâmetros
        ----------
        filename : str
            Caminho do arquivo .fis a ser importado
        """
        # Armazena o caminho do arquivo .fis
        self.system.filename = filename

        # Armazena o bloco que está sendo lido do arquivo .fis
        block = ''

        # Armazena as informações sobre o sistema
        system_list = []

        # Armazena as informações sobre os antecedentes
        inputs_list = []

        # Armazena as informações sobre os consequentes
        outputs_list = []

        # Armazena as informações sobre as regras
        rules_list = []

        # Abre o aquivo .fis para a leitura
        with open(filename) as file:

            # Faz a leitura de todas as linhas do arquivo .fis
            for line in file:
                if line[0] == '[':

                    # Verifica se está no bloco principal do sistema.
                    if line[: 8] == '[System]':
                        block = Blocks.system

                    # Verifica se está nos blocos de antecedentes
                    elif line[: 6] == '[Input':
                        block = Blocks.inputs
                        input_number = int(line[6: -1].replace(']', ''))
                        if input_number != (len(inputs_list) + 1):
                            raise Exception("Os inputs não estão ordenados!")
                        inputs_list.append([])

                    # Verifica se está no bloco de consequentes
                    elif line[:7] == '[Output':
                        block = Blocks.outputs
                        output_number = int(line[7: -1].replace(']', ''))
                        if output_number != (len(outputs_list) + 1):
                            raise Exception("Os outputs não estão ordenados!")
                        outputs_list.append([])

                    # Verifica se está nos bloco de regras
                    elif line[:7] == '[Rules]':
                        block = Blocks.rules

                    else:
                        raise Exception(f"Bloco {line[:-1]} não é válido!")
                else:
                    # Armazena entradas que não sejam vazias
                    if line[:-1].strip():

                        if block == Blocks.system:
                            system_list.append(line[:-1])

                        elif block == Blocks.inputs:
                            inputs_list[-1].append(line[:-1])

                        elif block == Blocks.outputs:
                            outputs_list[-1].append(line[:-1])

                        elif block == Blocks.rules:
                            rules_list.append(line[:-1])

        # Criar os atributos do sistema
        self.create_system_from_list(system_list)

        # Verificar se todos os atributos do sistema foram preenchidos
        self.valid_system()

        # Criar os inputs
        self.create_inputs_from_list(inputs_list)

        # Criar os outputs
        self.create_outputs_from_list(outputs_list)

        # Criar as regras
        self.create_rules_from_list(rules_list)

        # Valida a importação
        self.valid_import()

        return self.system
