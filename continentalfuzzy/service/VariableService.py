"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List, Union
from continentalfuzzy.domain.Variable import Variable
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.membership_function.LinearMF import LinearMF
from continentalfuzzy.domain.membership_function.ConstantMF import ConstantMF
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions
from continentalfuzzy.domain.variable.Input import Input
from continentalfuzzy.domain.variable.Output import Output


class VariableService:
    def __init__(self, p_variable: Union[Input, Output]):
        if (not isinstance(p_variable, Input)) \
                and (not isinstance(p_variable, Output)):
            raise Exception("É necessário informar uma instância de uma "
                            "variável de entrada ou de saída!")
        self.__variable = p_variable

    @property
    def variable(self) -> Variable:
        return self.__variable

    def create_from_fis_block(self, fis_lines: List[str]):
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
                self.variable.name = l_attr[1][:-1].replace("'", "")
            if l_attr[0] == 'Range':
                range_list = (l_attr[1][1:-1].split())
                self.variable.range = [float(range_list[0]),
                                       float(range_list[1])]
            if l_attr[0] == 'NumMFs':
                self.variable.num_mfs = int(l_attr[1])
            if l_attr[0][:2] == 'MF':
                mf_number = int(l_attr[0][2:])
                mfs_list.append({'num': mf_number, 'entries': l_attr[1]})

        # Verifica se todos os atributos da variável foram preenchidos
        if self.variable.name is None:
            raise Exception(f"O nome da variável não foi informado!")
        if self.variable.range == list():
            raise Exception(f"A amplitude do conjunto da variável "
                            "não foi informada!")
        if self.variable.num_mfs is None:
            raise Exception(f"O número de funções de pertinência da "
                            "variável não foi informado!")

        # Verifica se a quantidade de funções de pertinência está correta
        if len(mfs_list) == self.variable.num_mfs:
            for mf in mfs_list:
                # Remover aspas e extrair nome de identificação
                line_list = mf['entries'].replace("'", '').split(':')
                mf_name = line_list[0]

                # Atribui o nome da função
                func_list = line_list[1].split(',')

                try:
                    mf_function = MamdaniFunctions[func_list[0]]
                except Exception:
                    raise Exception(f"Função de pertinência {func_list[0]}, "
                                    "não cadastrada!")

                # Verifica se os valores da lista são do tipo float
                try:
                    values_list = [float(x) for x in func_list[1][1:-1].split()]
                except Exception:
                    raise Exception("Um dos valores não é do tipo float!")

                # Ajusta os valores para cada tipo de função
                if mf_function == MamdaniFunctions.trimf:
                    # Verifica se o tamanho dos parâmetros está correto
                    if len(values_list) != 3:
                        raise Exception("Número de parâmetros incorretos para "
                                        "a função de pertinência triangular!")
                    self.variable.add_mfs(mf['num'], TriMF(mf_name=mf_name,
                                                           mf_abc=values_list))

                elif mf_function == MamdaniFunctions.trapmf:
                    # Verifica se o tamanho dos parâmetros está correto
                    if len(values_list) != 4:
                        raise Exception("Número de parâmetros incorretos para "
                                        "a função de pertinência trapezoidal!")
                    self.variable.add_mfs(mf['num'],
                                          TrapMF(mf_name=mf_name,
                                                 mf_abcd=values_list))

                elif mf_function == MamdaniFunctions.gaussmf:
                    # Verifica se o tamanho dos parâmetros está correto
                    if len(values_list) != 2:
                        raise Exception("Número de parâmetros incorretos para "
                                        "a função de pertinência gaussiana!")
                    self.variable.add_mfs(mf['num'],
                                          GaussMF(mf_name=mf_name,
                                                  mf_sigma=values_list[0],
                                                  mf_mean=values_list[1]))

                elif mf_function == MamdaniFunctions.gauss2mf:
                    # Verifica se o tamanho dos parâmetros está correto
                    if len(values_list) != 4:
                        raise Exception("Número de parâmetros incorretos para "
                                        "a função de pertinência de duas "
                                        "gaussianas combinadas!")
                    self.variable.add_mfs(mf['num'],
                                          Gauss2MF(mf_name=mf_name,
                                                   mf_sigma1=values_list[0],
                                                   mf_mean1=values_list[1],
                                                   mf_sigma2=values_list[2],
                                                   mf_mean2=values_list[3]))

                elif mf_function == MamdaniFunctions.constant:
                    # Verifica se o tamanho dos parâmetros está correto
                    if len(values_list) != 1:
                        raise Exception("Número de parâmetros incorretos para "
                                        "a função de pertinência constante!")
                    self.variable.add_mfs(mf['num'],
                                          ConstantMF(mf_name=mf_name,
                                                     mf_value=values_list[0]))

                elif mf_function == MamdaniFunctions.linear:
                    # Verifica se o tamanho dos parâmetros está correto
                    self.variable.add_mfs(mf['num'],
                                          LinearMF(mf_name=mf_name,
                                                   mf_params=values_list))

        else:
            raise Exception("Quantidade de funções de pertinência para "
                            f"a variável {self.variable.name} é diferente "
                            f"do número de funções de pertinência informado "
                            f"no bloco!")
