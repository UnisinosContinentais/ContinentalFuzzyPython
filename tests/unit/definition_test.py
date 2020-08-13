"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import unittest
from continentalfuzzy.domain.definition.AggMethods import AggMethods
from continentalfuzzy.domain.definition.AndMethods import AndMethods
from continentalfuzzy.domain.definition.Blocks import Blocks
from continentalfuzzy.domain.definition.Connections import Connections
from continentalfuzzy.domain.definition.ControllerType import ControllerType
from continentalfuzzy.domain.definition.DefuzzMethods import DefuzzMethods
from continentalfuzzy.domain.definition.FaciesAssociation import \
    FaciesAssociation
from continentalfuzzy.domain.definition.Functions import Functions
from continentalfuzzy.domain.definition.ImpMethods import ImpMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniAggMethods import MamdaniAggMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniAndMethods import MamdaniAndMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniDefuzzMethods import MamdaniDefuzzMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniFunctions import MamdaniFunctions
from continentalfuzzy.domain.definition.mamdani.MamdaniImpMethods import MamdaniImpMethods
from continentalfuzzy.domain.definition.mamdani.MamdaniOrMethods import MamdaniOrMethods
from continentalfuzzy.domain.definition.OrMethods import OrMethods
from continentalfuzzy.domain.definition.sugeno.SugenoAggMethods import SugenoAggMethods
from continentalfuzzy.domain.definition.sugeno.SugenoAndMethods import SugenoAndMethods
from continentalfuzzy.domain.definition.sugeno.SugenoDefuzzMethods import \
    SugenoDefuzzMethods
from continentalfuzzy.domain.definition.sugeno.SugenoImpMethods import SugenoImpMethods
from continentalfuzzy.domain.definition.sugeno.SugenoInputFunctions import \
    SugenoInputFunctions
from continentalfuzzy.domain.definition.sugeno.SugenoOrMethods import SugenoOrMethods
from continentalfuzzy.domain.definition.sugeno.SugenoOutputFunctions import \
    SugenoOutputFunctions


class AggMethodsTest(unittest.TestCase):
    def test_AggMethods_max(self):
        self.assertEqual(AggMethods['max'],
                         AggMethods.max,
                         msg='Test max')

    def test_AggMethods_sum(self):
        self.assertEqual(AggMethods['sum'],
                         AggMethods.sum,
                         msg='Test sum')

    def test_AggMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = AggMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test AggMethods not found")


class AndMethodsTest(unittest.TestCase):
    def test_AndMethods_min(self):
        self.assertEqual(AndMethods['min'],
                         AndMethods.min,
                         msg='Test min')

    def test_AndMethods_prod(self):
        self.assertEqual(AndMethods['prod'],
                         AndMethods.prod,
                         msg='Test prod')

    def test_AndMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = AndMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test AndMethods not found")


class BlocksTest(unittest.TestCase):
    def test_Blocks_system(self):
        self.assertEqual(Blocks['system'],
                         Blocks.system,
                         msg='Test system')

    def test_Blocks_inputs(self):
        self.assertEqual(Blocks['inputs'],
                         Blocks.inputs,
                         msg='Test inputs')

    def test_Blocks_outputs(self):
        self.assertEqual(Blocks['outputs'],
                         Blocks.outputs,
                         msg='Test outputs')

    def test_Blocks_rules(self):
        self.assertEqual(Blocks['rules'],
                         Blocks.rules,
                         msg='Test rules')

    def test_Blocks_not_found(self):
        my_exception = "sugeno"
        with self.assertRaises(Exception) as context:
            _ = Blocks['sugeno']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test Blocks not found")


class ConnectionsTest(unittest.TestCase):
    def test_Connections_connection_and(self):
        self.assertEqual(Connections['AND'],
                         Connections.AND,
                         msg='Test AND')

    def test_Connections_connection_or(self):
        self.assertEqual(Connections['OR'],
                         Connections.OR,
                         msg='Test OR')

    def test_Connections_not_found(self):
        my_exception = "connection_maybe"
        with self.assertRaises(Exception) as context:
            _ = MamdaniFunctions['connection_maybe']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test Connections not found")


class ControllerTypeTest(unittest.TestCase):
    def test_ControllerType_mamdani(self):
        self.assertEqual(ControllerType['mamdani'],
                         ControllerType.mamdani,
                         msg='Test mamdani')

    def test_ControllerType_sugeno(self):
        self.assertEqual(ControllerType['sugeno'],
                         ControllerType.sugeno,
                         msg='Test sugeno')

    def test_ControllerType_not_found(self):
        my_exception = "tsukamoto"
        with self.assertRaises(Exception) as context:
            _ = ControllerType['tsukamoto']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test ControllerType not found")


class DefuzzMethodsTest(unittest.TestCase):
    def test_DefuzzMethods_centroid(self):
        self.assertEqual(DefuzzMethods['centroid'],
                         DefuzzMethods.centroid,
                         msg='Test centroid')

    def test_DefuzzMethods_wtaver(self):
        self.assertEqual(DefuzzMethods['wtaver'],
                         DefuzzMethods.wtaver,
                         msg='Test wtaver')

    def test_DefuzzMethods_wtsum(self):
        self.assertEqual(DefuzzMethods['wtsum'],
                         DefuzzMethods.wtsum,
                         msg='Test wtsum')

    def test_DefuzzMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = DefuzzMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test DefuzzMethods not found")


class FunctionsTest(unittest.TestCase):
    def test_Functions_trimf(self):
        self.assertEqual(Functions['trimf'],
                         Functions.trimf,
                         msg='Test trimf')

    def test_Functions_trapmf(self):
        self.assertEqual(Functions['trapmf'],
                         Functions.trapmf,
                         msg='Test trapmf')

    def test_Functions_gaussmf(self):
        self.assertEqual(Functions['gaussmf'],
                         Functions.gaussmf,
                         msg='Test gaussmf')

    def test_Functions_gauss2mf(self):
        self.assertEqual(Functions['gauss2mf'],
                         Functions.gauss2mf,
                         msg='Test gauss2mf')

    def test_Functions_linear(self):
        self.assertEqual(Functions['linear'],
                         Functions.linear,
                         msg='Test linear')

    def test_Functions_constant(self):
        self.assertEqual(Functions['constant'],
                         Functions.constant,
                         msg='Test constant')

    def test_Functions_not_found(self):
        my_exception = "bell"
        with self.assertRaises(Exception) as context:
            _ = Functions['bell']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test Functions not found")


class ImpMethodsTest(unittest.TestCase):
    def test_ImpMethods_max(self):
        self.assertEqual(ImpMethods['min'],
                         ImpMethods.min,
                         msg='Test min')

    def test_ImpMethods_prod(self):
        self.assertEqual(ImpMethods['prod'],
                         ImpMethods.prod,
                         msg='Test prod')

    def test_ImpMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = ImpMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test ImpMethods not found")


class MamdaniAggMethodsTest(unittest.TestCase):
    def test_MamdaniAggMethods_max(self):
        self.assertEqual(MamdaniAggMethods['max'],
                         MamdaniAggMethods.max,
                         msg='Test max')

    def test_MamdaniAggMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = MamdaniAggMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniAggMethods not found")


class MamdaniAndMethodsTest(unittest.TestCase):
    def testMamdaniAndMethods_min(self):
        self.assertEqual(MamdaniAndMethods['min'],
                         MamdaniAndMethods.min,
                         msg='Test min')

    def test_MamdaniAndMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = MamdaniAndMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniAndMethods not found")


class MamdaniDefuzzMethodsTest(unittest.TestCase):
    def test_MamdaniDefuzzMethods_centroid(self):
        self.assertEqual(MamdaniDefuzzMethods['centroid'],
                         MamdaniDefuzzMethods.centroid,
                         msg='Test centroid')

    def test_MamdaniDefuzzMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = MamdaniDefuzzMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniDefuzzMethods not found")


class MamdaniFunctionsTest(unittest.TestCase):
    def test_MamdaniFunctions_trimf(self):
        self.assertEqual(MamdaniFunctions['trimf'],
                         MamdaniFunctions.trimf,
                         msg='Test trimf')

    def test_MamdaniFunctions_tramf(self):
        self.assertEqual(MamdaniFunctions['trapmf'],
                         MamdaniFunctions.trapmf,
                         msg='Test trapmf')

    def test_MamdaniFunctions_gaussmf(self):
        self.assertEqual(MamdaniFunctions['gaussmf'],
                         MamdaniFunctions.gaussmf,
                         msg='Test gaussmf')

    def test_MamdaniFunctions_gauss2mf(self):
        self.assertEqual(MamdaniFunctions['gauss2mf'],
                         MamdaniFunctions.gauss2mf,
                         msg='Test gauss2mf')

    def test_MamdaniFunctions_not_found(self):
        my_exception = "linear"
        with self.assertRaises(Exception) as context:
            _ = MamdaniFunctions['linear']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniFunctions not found")


class MamdaniImpMethodsTest(unittest.TestCase):
    def test_MamdaniImpMethods_max(self):
        self.assertEqual(MamdaniImpMethods['min'],
                         MamdaniImpMethods.min,
                         msg='Test min')

    def test_MamdaniImpMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = MamdaniImpMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniImpMethods not found")


class MamdaniOrMethodsTest(unittest.TestCase):
    def test_MamdaniOrMethods_max(self):
        self.assertEqual(MamdaniOrMethods['max'],
                         MamdaniOrMethods.max,
                         msg='Test max')

    def test_MamdaniOrMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = MamdaniOrMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test MamdaniOrMethods not found")


class OrMethodsTest(unittest.TestCase):
    def test_OrMethods_max(self):
        self.assertEqual(OrMethods['max'],
                         OrMethods.max,
                         msg='Test max')

    def test_OrMethods_probor(self):
        self.assertEqual(OrMethods['probor'],
                         OrMethods.probor,
                         msg='Test probor')

    def test_OrMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = OrMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test OrMethods not found")


class SugenoAggMethodsTest(unittest.TestCase):
    def test_SugenoAggMethods_sum(self):
        self.assertEqual(SugenoAggMethods['sum'],
                         SugenoAggMethods.sum,
                         msg='Test sum')

    def test_SugenoAggMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = SugenoAggMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoAggMethods not found")


class SugenoAndMethodsTest(unittest.TestCase):
    def test_SugenoAndMethods_min(self):
        self.assertEqual(SugenoAndMethods['min'],
                         SugenoAndMethods.min,
                         msg='Test min')

    def test_SugenoAndMethods_prod(self):
        self.assertEqual(SugenoAndMethods['prod'],
                         SugenoAndMethods.prod,
                         msg='Test prod')

    def test_SugenoAndMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = SugenoAndMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoAndMethods not found")


class SugenoDefuzzMethodsTest(unittest.TestCase):
    def test_SugenoDefuzzMethods_wtaver(self):
        self.assertEqual(SugenoDefuzzMethods['wtaver'],
                         SugenoDefuzzMethods.wtaver,
                         msg='Test wtaver')

    def test_SugenoDefuzzMethods_wtsum(self):
        self.assertEqual(SugenoDefuzzMethods['wtsum'],
                         SugenoDefuzzMethods.wtsum,
                         msg='Test wtsum')

    def test_SugenoDefuzzMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = SugenoDefuzzMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoDefuzzMethods not found")


class SugenoImpMethodsTest(unittest.TestCase):
    def test_SugenoImpMethods_prod(self):
        self.assertEqual(SugenoImpMethods['prod'],
                         SugenoImpMethods.prod,
                         msg='Test prod')

    def test_SugenoImpMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = SugenoImpMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoImpMethods not found")


class SugenoInputFunctionsTest(unittest.TestCase):
    def test_SugenoInputFunctions_trimf(self):
        self.assertEqual(SugenoInputFunctions['trimf'],
                         SugenoInputFunctions.trimf,
                         msg='Test trimf')

    def test_SugenoInputFunctions_trapmf(self):
        self.assertEqual(SugenoInputFunctions['trapmf'],
                         SugenoInputFunctions.trapmf,
                         msg='Test trapmf')

    def test_SugenoInputFunctions_gaussmf(self):
        self.assertEqual(SugenoInputFunctions['gaussmf'],
                         SugenoInputFunctions.gaussmf,
                         msg='Test gaussmf')

    def test_SugenoInputFunctions_gauss2mf(self):
        self.assertEqual(SugenoInputFunctions['gauss2mf'],
                         SugenoInputFunctions.gauss2mf,
                         msg='Test gauss2mf')

    def test_SugenoInputFunctions_not_found(self):
        my_exception = "linear"
        with self.assertRaises(Exception) as context:
            _ = SugenoInputFunctions['linear']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoInputFunctions not found")


class SugenoOrMethodsTest(unittest.TestCase):
    def test_SugenoOrMethods_max(self):
        self.assertEqual(SugenoOrMethods['max'],
                         SugenoOrMethods.max,
                         msg='Test max')

    def test_SugenoOrMethods_probor(self):
        self.assertEqual(SugenoOrMethods['probor'],
                         SugenoOrMethods.probor,
                         msg='Test probor')

    def test_SugenoOrMethods_not_found(self):
        my_exception = "mean"
        with self.assertRaises(Exception) as context:
            _ = SugenoOrMethods['mean']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoOrMethods not found")


class SugenoOutputFunctionsTest(unittest.TestCase):
    def test_SugenoOutputFunctions_linear(self):
        self.assertEqual(SugenoOutputFunctions['linear'],
                         SugenoOutputFunctions.linear,
                         msg='Test linear')

    def test_SugenoOutputFunctions_constant(self):
        self.assertEqual(SugenoOutputFunctions['constant'],
                         SugenoOutputFunctions.constant,
                         msg='Test constant')

    def test_SugenoOutputFunctions_not_found(self):
        my_exception = "trimf"
        with self.assertRaises(Exception) as context:
            _ = SugenoOutputFunctions['trimf']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test SugenoOutputFunctions not found")


class FaciesAssociationTest(unittest.TestCase):
    def test_FaciesAssociation_Cape(self):
        self.assertEqual(FaciesAssociation['Cape'],
                         FaciesAssociation.Cape,
                         msg='Test Cape')

    def test_FaciesAssociation_ShallowPlain(self):
        self.assertEqual(FaciesAssociation['ShallowPlain'],
                         FaciesAssociation.ShallowPlain,
                         msg='Test ShallowPlain')

    def test_FaciesAssociation_LowEnergyUnderwaterPlain(self):
        self.assertEqual(FaciesAssociation['LowEnergyUnderwaterPlain'],
                         FaciesAssociation.LowEnergyUnderwaterPlain,
                         msg='Test LowEnergyUnderwaterPlain')

    def test_FaciesAssociation_InterpatchesPlain(self):
        self.assertEqual(FaciesAssociation['InterpatchesPlain'],
                         FaciesAssociation.InterpatchesPlain,
                         msg='Test InterpatchesPlain')

    def test_FaciesAssociation_ClayeyEmbayment(self):
        self.assertEqual(FaciesAssociation['ClayeyEmbayment'],
                         FaciesAssociation.ClayeyEmbayment,
                         msg='Test ClayeyEmbayment')

    def test_FaciesAssociation_StromatoliteEmbayment(self):
        self.assertEqual(FaciesAssociation['StromatoliteEmbayment'],
                         FaciesAssociation.StromatoliteEmbayment,
                         msg='Test StromatoliteEmbayment')

    def test_FaciesAssociation_LaminiteRamp(self):
        self.assertEqual(FaciesAssociation['LaminiteRamp'],
                         FaciesAssociation.LaminiteRamp,
                         msg='Test LaminiteRamp')

    def test_FaciesAssociation_ModerateEnergyIntraclastic(self):
        self.assertEqual(FaciesAssociation['ModerateEnergyIntraclastic'],
                         FaciesAssociation.ModerateEnergyIntraclastic,
                         msg='Test ModerateEnergyIntraclastic')

    def test_FaciesAssociation_HighEnergyIntraclastic(self):
        self.assertEqual(FaciesAssociation['HighEnergyIntraclastic'],
                         FaciesAssociation.HighEnergyIntraclastic,
                         msg='Test HighEnergyIntraclastic')

    def test_FaciesAssociation_SubCoastal(self):
        self.assertEqual(FaciesAssociation['SubCoastal'],
                         FaciesAssociation.SubCoastal,
                         msg='Test SubCoastal')

    def test_FaciesAssociation_Reef(self):
        self.assertEqual(FaciesAssociation['Reef'],
                         FaciesAssociation.Reef,
                         msg='Test Reef')

    def test_FaciesAssociation_ClayeyClasticDeposit(self):
        self.assertEqual(FaciesAssociation['ClayeyClasticDeposit'],
                         FaciesAssociation.ClayeyClasticDeposit,
                         msg='Test ClayeyClasticDeposit')

    def test_FaciesAssociation_Undefined(self):
        self.assertEqual(FaciesAssociation['Undefined'],
                         FaciesAssociation.Undefined,
                         msg='Test Undefined')

    def test_FaciesAssociation_not_found(self):
        my_exception = "AridSubCoastal"
        with self.assertRaises(Exception) as context:
            _ = FaciesAssociation['AridSubCoastal']

        self.assertEqual(my_exception, context.exception.args[0],
                         msg="Test FaciesAssociation not found")