"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import sys
import time

import os
from continentalfuzzy.applicationservice.FuzzyControlApplicationService import FuzzyControlApplicationService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput

print("==========RODANDO INIT E PROCESS ============")

filename = "Shelf_Humid.fis"
fuzzyControlApplicationService = FuzzyControlApplicationService()
fuzzyControlApplicationService.init_fuzzy_control(filename)

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_fuzzy_output("output1")
fuzzyControlCommandInput.set_matrix_dimension(100, 90)

for row in range(100):
    for col in range(90):
        fuzzyControlCommandInput.add_fuzzy_inputs_matrix(row, col, "Depth", 120 + row / 100)
        fuzzyControlCommandInput.add_fuzzy_inputs_matrix(row, col, "EnergyDissipation", 0.7 + col / 90)

a = time.time()
print(a)
fuzzyControlApplicationService.process_fuzzy_matrix(fuzzyControlCommandInput)
'''
for row in range(100):
    for col in range(90):
        print(fuzzyControlApplicationService.get_fuzzy_output_matrix(row, col))
'''
b = time.time()
print(b)
print((b - a) * 10000)

print("==========FINALIZOU INIT E PROCESS============")
