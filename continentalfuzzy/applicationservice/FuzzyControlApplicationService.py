"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.service.MamdaniControllerService import MamdaniControllerService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput
from continentalfuzzy.dto.FuzzyControlCommandOutput import FuzzyControlCommandOutput
from continentalfuzzy.dto.ProcessResult import ProcessResult
from continentalfuzzy.service.SugenoControllerService import \
    SugenoControllerService
from continentalfuzzy.service.SystemService import SystemService


class FuzzyControlApplicationService:
    def __init__(self):
        self.__fisSystem = None
        self.__fuzzy_controller = None

    @property
    def fisSystem(self):
        return self.__fisSystem

    @fisSystem.setter
    def fisSystem(self, p_fisSystem):
        self.__fisSystem = p_fisSystem

    @property
    def fuzzyController(self):
        return self.__fuzzy_controller

    @fuzzyController.setter
    def fuzzyController(self, p_fuzzyController):
        self.__fuzzy_controller = p_fuzzyController

    @classmethod
    def process_fuzzy_control(cls, fuzzyControlCommandInput: FuzzyControlCommandInput):

        result = FuzzyControlCommandOutput()
        result.status = ProcessResult.RESULT_ERROR

        try:
            fisSystemService = SystemService()
            fisSystem = fisSystemService.import_file(
                fuzzyControlCommandInput.filename,
                fuzzyControlCommandInput.use_dict_facies_association)

            if fisSystem.type == ControllerType.mamdani:
                mamdaniController = MamdaniControllerService()
                mamdaniController.create_from_fis_system(fisSystem)

                fuzzy_result = mamdaniController.fuzzy_calc_single_value(
                    fuzzyControlCommandInput.fuzzy_inputs,
                    fuzzyControlCommandInput.fuzzy_output)
            elif fisSystem.type == ControllerType.sugeno:
                sugenoController = SugenoControllerService()
                sugenoController.create_from_fis_system(fisSystem)

                fuzzy_result = sugenoController.sugeno_calc_single_value(
                    fuzzyControlCommandInput.fuzzy_inputs)

            result.add_message("Processo executado com sucesso!")
            result.status = ProcessResult.RESULT_SUCCESS
            result.result = fuzzy_result

        except Exception as ex:
            result.add_message("Não foi possível executar o processo do fuzzy!")
            result.add_message(ex.args[0])

        return result.result

    def init_fuzzy_control(self, filename: str):

        result = FuzzyControlCommandOutput()
        result.status = ProcessResult.RESULT_ERROR

        try:
            fisSystemService = SystemService()
            self.fisSystem = fisSystemService.import_file(filename, True)

            if self.fisSystem.type == ControllerType.mamdani:
                self.fuzzyController = MamdaniControllerService()
                self.fuzzyController.create_from_fis_system(self.fisSystem)

            elif self.fisSystem.type == ControllerType.sugeno:
                self.fuzzyController = SugenoControllerService()
                self.fuzzyController.create_from_fis_system(self.fisSystem)

            result.add_message("Processo executado com sucesso!")
            result.status = ProcessResult.RESULT_SUCCESS

        except Exception as ex:
            result.add_message("Não foi possível executar o processo do fuzzy!")
            result.add_message(ex.args[0])

        return result.result

    def process_fuzzy_item(self, fuzzyControlCommandInput: FuzzyControlCommandInput):

        result = FuzzyControlCommandOutput()
        result.status = ProcessResult.RESULT_ERROR

        try:
            if self.fisSystem.type == ControllerType.mamdani:
                fuzzy_result = self.fuzzyController.fuzzy_calc_single_value(
                    fuzzyControlCommandInput.fuzzy_inputs,
                    fuzzyControlCommandInput.fuzzy_output)

            elif self.fisSystem.type == ControllerType.sugeno:
                fuzzy_result = self.fuzzyController.sugeno_calc_single_value(
                    fuzzyControlCommandInput.fuzzy_inputs)

            result.add_message("Processo executado com sucesso!")
            result.status = ProcessResult.RESULT_SUCCESS
            result.result = fuzzy_result

        except Exception as ex:
            result.add_message("Não foi possível executar o processo do fuzzy!")
            result.add_message(ex.args[0])

        return result.result
