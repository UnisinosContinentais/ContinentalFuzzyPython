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
import numpy as np
import threading
import psutil

class FuzzyControlApplicationService:
    def __init__(self):
        self.__fisSystem = None
        self.__fuzzy_controller = None
        self.__fuzzy_output_matrix = None
        self.__number_of_cpus = psutil.cpu_count()

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

    def process_fuzzy_matrix(self, fuzzyControlCommandInput: FuzzyControlCommandInput):
        self.__fuzzy_output_matrix = np.zeros((fuzzyControlCommandInput.get_num_rows(), fuzzyControlCommandInput.get_num_cols()))
        for row in range(fuzzyControlCommandInput.get_num_rows()):
            for col in range(fuzzyControlCommandInput.get_num_cols()):
                self.process_fuzzy_matrix_item(col, fuzzyControlCommandInput, row)

    def process_fuzzy_matrix_multithread(self, fuzzyControlCommandInput: FuzzyControlCommandInput):
        self.__fuzzy_output_matrix = np.zeros((fuzzyControlCommandInput.get_num_rows(), fuzzyControlCommandInput.get_num_cols()))
        jobs = []
        step = int(fuzzyControlCommandInput.get_num_rows() / self.__number_of_cpus)
        for rowStart in range(0, fuzzyControlCommandInput.get_num_rows(), step):
            thread = threading.Thread(target=self.process_fuzzy_matrix_multithread_slice, args=(fuzzyControlCommandInput, rowStart, min(rowStart + step, fuzzyControlCommandInput.get_num_rows())))
            jobs.append(thread)

        # Start the threads (i.e. calculate the random number lists)
        for j in jobs:
            j.start()

        # Ensure all of the threads have finished
        for j in jobs:
            j.join()

    def process_fuzzy_matrix_multithread_slice(self, fuzzyControlCommandInput: FuzzyControlCommandInput, rowStart, rowEnd):
        for row in range(rowStart, rowEnd):
            for col in range(fuzzyControlCommandInput.get_num_cols()):
                self.process_fuzzy_matrix_item(col, fuzzyControlCommandInput, row)

    def process_fuzzy_matrix_item(self, col, fuzzyControlCommandInput, row):
        fuzzy_control_command_input_temp = FuzzyControlCommandInput()
        for name, matrix in fuzzyControlCommandInput.get_fuzzy_inputs_matrix().items():
            fuzzy_control_command_input_temp.add_fuzzy_inputs(name, matrix[row][col])
        fuzzy_control_command_input_temp.set_use_dict_facies_association(True)
        fuzzy_control_command_input_temp.set_fuzzy_output("output1")
        if self.fisSystem.type == ControllerType.mamdani:
            try:
                self.__fuzzy_output_matrix[row][col] = self.fuzzyController.fuzzy_calc_single_value(
                    fuzzy_control_command_input_temp.fuzzy_inputs,
                    fuzzy_control_command_input_temp.fuzzy_output)
            except Exception:
                pass

        elif self.fisSystem.type == ControllerType.sugeno:
            try:
                self.__fuzzy_output_matrix[row][col] = self.fuzzyController.sugeno_calc_single_value(
                    fuzzy_control_command_input_temp.fuzzy_inputs)
            except Exception:
                pass

    def get_fuzzy_output_matrix(self, row: int, col: int):
        return self.__fuzzy_output_matrix[row][col]

