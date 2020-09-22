"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import sys
try:
    sys.path.append(basePath)

except NameError:
    pass

import os
from continentalfuzzy.applicationservice.FuzzyControlApplicationService import FuzzyControlApplicationService
from continentalfuzzy.dto.FuzzyControlCommandInput import FuzzyControlCommandInput


print("==========RODANDO O CONSOLE INTEGRACAO RAMP_ARID ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("Ramp_Arid.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 120)
fuzzyControlCommandInput.add_fuzzy_inputs("EnergyDissipation", 0.7)
fuzzyControlCommandInput.set_use_dict_facies_association(True)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO RAMP_ARID ============")

print("==========RODANDO O CONSOLE INTEGRACAO RAMP_HUMID ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("Ramp_Humid.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 120)
fuzzyControlCommandInput.add_fuzzy_inputs("EnergyDissipation", 0.7)
fuzzyControlCommandInput.set_use_dict_facies_association(True)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO RAMP_HUMID ============")

print("==========RODANDO O CONSOLE INTEGRACAO SHELF_ARID ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("Shelf_Arid.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 120)
fuzzyControlCommandInput.add_fuzzy_inputs("EnergyDissipation", 0.7)
fuzzyControlCommandInput.set_use_dict_facies_association(True)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO SHELF_ARID ============")

print("==========RODANDO O CONSOLE INTEGRACAO SHELF_HUMID ============")

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.set_filename("Shelf_Humid.fis")
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 120)
fuzzyControlCommandInput.add_fuzzy_inputs("EnergyDissipation", 0.7)
fuzzyControlCommandInput.set_use_dict_facies_association(True)

fuzzyControlCommandInput.set_fuzzy_output("output1")

fuzzyControlApplicationService = FuzzyControlApplicationService()
result = fuzzyControlApplicationService.process_fuzzy_control(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU O CONSOLE INTEGRACAO SHELF_HUMID ============")


print("==========RODANDO INIT E PROCESS ============")

filename = "Shelf_Humid.fis"
fuzzyControlApplicationService = FuzzyControlApplicationService()
fuzzyControlApplicationService.init_fuzzy_control(filename)

fuzzyControlCommandInput = FuzzyControlCommandInput()
fuzzyControlCommandInput.add_fuzzy_inputs("Depth", 120)
fuzzyControlCommandInput.add_fuzzy_inputs("EnergyDissipation", 0.7)

fuzzyControlCommandInput.set_fuzzy_output("output1")

result = fuzzyControlApplicationService.process_fuzzy_item(fuzzyControlCommandInput)

print(result)
print("==========FINALIZOU INIT E PROCESS============")
