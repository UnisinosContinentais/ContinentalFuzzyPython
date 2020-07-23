"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import sys
import os
from typing import List
from continentalfuzzy.applicationservice.FuzzyControlApplicationService import FuzzyControlApplicationService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput


class TestFuzzy:
    @staticmethod
    def validate_args(args: List):
        if len(args) != 4:
            raise Exception(f"É necessário informar 4 argumentos!")

        if not isinstance(args[0], str):
            raise Exception(
                f"O primeiro argumento precisa ser o nome do arquivo!")

        if args[0][-4:] != ".fis":
            raise Exception(
                f"O arquivo a ser importado precisar ter a extensão .fis!")

        if not os.path.exists(args[0]):
            raise Exception(
                f"O arquivo {args[0]} não foi encontrado!")

        try:
            _ = float(args[1])
        except Exception:
            raise Exception("O argumento da distância não é do tipo float!")

        try:
            _ = float(args[2])
        except Exception:
            raise Exception("O argumento da declividade não é do tipo float!")

        try:
            _ = float(args[3])
        except Exception:
            raise Exception(
                "O argumento da paleobatimetria não é do tipo float!")

    def execute(self, args: List):
        self.validate_args(args)
        fuzzyControlCommandInput = FuzzyControlCommandInput()

        fuzzyControlCommandInput.filename = args[0]
        fuzzyControlCommandInput.fuzzy_inputs = {'Distance': float(args[1]),
                                                 'Slope': float(args[2]),
                                                 'Depth': float(args[3])}
        fuzzyControlCommandInput.fuzzy_output = 'output1'

        fuzzyControlApplicationService = FuzzyControlApplicationService()
        result = fuzzyControlApplicationService.process_fuzzy_control(
            fuzzyControlCommandInput)
        print(result.messages)
        print(result.status)
        print(result.result)


if __name__ == '__main__':
    testFuzzy = TestFuzzy()
    testFuzzy.execute(sys.argv[1:])
