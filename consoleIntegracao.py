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
