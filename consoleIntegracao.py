"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import sys
#sys.path.append('C:\\Git\\CONTINENTAIS_skfuzzy')
sys.path.append('R:\continentais\repos\CONTINENTAIS_skfuzzy')
import os
from continentalfuzzy.applicationservice.FuzzyControlApplicationService import FuzzyControlApplicationService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput


print("==========RODANDO O CONSOLE INTEGRACAO MAMDANI ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("test_mamdani.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Distance", 0.5)
fuzzyControlCommandInput.add_fuzzy_inputs("Slope", 0.01)
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 30.0)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO MAMDANI ============")

print("==========RODANDO O CONSOLE INTEGRACAO SUGENO ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("test_sugeno.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Distance", 0.5)
fuzzyControlCommandInput.add_fuzzy_inputs("Slope", 0.01)
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 30.0)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO SUGENO ============")
