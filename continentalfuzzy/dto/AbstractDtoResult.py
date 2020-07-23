"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
from typing import List
from continentalfuzzy.dto.ProcessResult import ProcessResult


class AbstractDtoResult:
    def __init__(self):
        self.__status = ProcessResult.RESULT_ERROR
        self.__messages = list()

    @property
    def status(self) -> ProcessResult:
        return self.__status

    @status.setter
    def status(self, p_status: ProcessResult):
        self.__status = p_status

    @property
    def messages(self) -> List[str]:
        return self.__messages

    def add_message(self, p_message: str):
        self.__messages.append(p_message)
