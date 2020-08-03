"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.definition.sugeno.SugenoInputFunctions import \
    SugenoInputFunctions
from continentalfuzzy.domain.definition.mamdani.MamdaniFunctions import MamdaniFunctions
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.service.MembershipFunctionService import \
    MembershipFunctionService


class InputService:
    def __init__(self):
        self.__input = Input()

    @property
    def input(self) -> Input:
        return self.__input

    def create_from_fis_block(self,
                              inference_type: ControllerType,
                              fis_lines: List[str]):
        """
        Cria uma variável a partir das informações de um arquivo .fis.

        Parâmetros
        ----------
        entries : List[str]
            Lista com as entradas de um arquivo .fis utilizadas para a criação
            de uma variável.
        """

        for f_line in fis_lines:
            if not isinstance(f_line, str):
                raise Exception("A lista de informações do arquivo .fis possui "
                                "um valor que não é do tipo String!")

        # Armazena as informações sobre as funções de pertinência
        mfs_list = []

        for f_line in fis_lines:
            # Divide a string das linhas no sinal de "=" em nome e valor
            l_attr = f_line.split(sep='=')

            # Preenche os atributos da classe baseado nas  entradas do
            # arquivo .fis
            if l_attr[0] == 'Name':
                self.input.name = l_attr[1][:-1].replace("'", "")
            if l_attr[0] == 'Range':
                range_list = (l_attr[1][1:-1].split())
                self.input.range = [float(range_list[0]),
                                       float(range_list[1])]
            if l_attr[0] == 'NumMFs':
                self.input.num_mfs = int(l_attr[1])
            if l_attr[0][:2] == 'MF':
                mf_number = int(l_attr[0][2:])
                mfs_list.append({'num': mf_number, 'entries': l_attr[1]})

        # Verifica se todos os atributos da variável foram preenchidos
        if self.input.name is None:
            raise Exception(f"O nome da variável não foi informado!")
        if self.input.range == list():
            raise Exception(f"A amplitude do conjunto da variável "
                            "não foi informada!")
        if self.input.num_mfs is None:
            raise Exception(f"O número de funções de pertinência da "
                            "variável não foi informado!")

        # Verifica se a quantidade de funções de pertinência está correta
        if len(mfs_list) == self.input.num_mfs:
            for mf in mfs_list:
                # Remover aspas e extrair nome de identificação
                line_list = mf['entries'].replace("'", '').split(':')
                mf_name = line_list[0]

                # Atribui o nome da função
                func_list = line_list[1].split(',')

                if inference_type == ControllerType.mamdani:
                    try:
                        _ = MamdaniFunctions[func_list[0]]
                    except Exception:
                        raise Exception(
                            f"Função de pertinência {func_list[0]}, "
                            "não implementada para Mamdani!")

                elif inference_type == ControllerType.sugeno:
                    try:
                        _ = SugenoInputFunctions[func_list[0]]
                    except Exception:
                        raise Exception(
                            f"Função de pertinência {func_list[0]}, "
                            "não implementada para Sugeno!")

                mf_function = Functions[func_list[0]]

                # Verifica se os valores da lista são do tipo float
                try:
                    values_list = [float(x) for x in func_list[1][1:-1].split()]
                except Exception:
                    raise Exception("Um dos valores não é do tipo float!")

                mf_service = MembershipFunctionService()
                mf_service.create_membership_function(mf_function,
                                                      mf_name,
                                                      values_list)
                self.input.add_mfs(mf['num'], mf_service.membership_function)

        else:
            raise Exception("Quantidade de funções de pertinência para "
                            f"a variável {self.input.name} é diferente "
                            f"do número de funções de pertinência informado "
                            f"no bloco!")
