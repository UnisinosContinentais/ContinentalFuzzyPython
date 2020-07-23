"""
Developed by Projeto Continentais and Petrobras
author: Rudi César Comiotto Modena
email: rmodena@unisinos.br
date: July, 2020
"""
import numpy as np
from typing import Union, List, Dict
import skfuzzy as fuzz
from continentalfuzzy.domain.MembershipFunction import MembershipFunction
from continentalfuzzy.domain.membership_function.TrapMF import TrapMF
from continentalfuzzy.domain.membership_function.TriMF import TriMF
from continentalfuzzy.domain.membership_function.GaussMF import GaussMF
from continentalfuzzy.domain.membership_function.Gauss2MF import Gauss2MF
from continentalfuzzy.domain.definition.MamdaniFunctions import MamdaniFunctions


class FuzzyUtil:
    @classmethod
    def create_universe(cls,
                        u_range: List[float],
                        mfs: Dict[int, MembershipFunction]) -> np.ndarray:
        universe_set = set()
        universe_set.add(u_range[0])
        universe_set.add(u_range[1])
        for f_mf in mfs.values():
            if f_mf.function == MamdaniFunctions.trimf:
                for value in cls.get_trimf_values(f_mf):
                    if (value >= u_range[0]) and (value <= u_range[1]):
                        universe_set.add(value)

            elif f_mf.function == MamdaniFunctions.trapmf:
                for value in cls.get_trapmf_values(f_mf):
                    if (value >= u_range[0]) and (value <= u_range[1]):
                        universe_set.add(value)

            elif f_mf.function == MamdaniFunctions.gaussmf:
                for value in cls.get_gaussmf_values(f_mf):
                    if (value >= u_range[0]) and (value <= u_range[1]):
                        universe_set.add(value)

            elif f_mf.function == MamdaniFunctions.gauss2mf:
                for value in cls.get_gauss2mf_values(f_mf):
                    if (value >= u_range[0]) and (value <= u_range[1]):
                        universe_set.add(value)

        return np.sort(np.array(list(universe_set)))

    @staticmethod
    def get_trimf_values(f_mf: TriMF) -> List[float]:
        return f_mf.abc

    @staticmethod
    def get_trapmf_values(f_mf: TrapMF) -> List[float]:
        return f_mf.abcd

    @staticmethod
    def get_gaussmf_values(f_mf: GaussMF) -> np.ndarray:
        mf_mean = f_mf.mean
        mf_sigma = f_mf.sigma
        mf_min = mf_mean - (mf_sigma * 4)
        mf_max = mf_mean + (mf_sigma * 4)
        return np.linspace(mf_min,
                           mf_max,
                           num=100,
                           endpoint=True)

    @staticmethod
    def get_gauss2mf_values(f_mf: Gauss2MF) -> np.ndarray:
        mf_mean1 = f_mf.mean1
        mf_sigma1 = f_mf.sigma1
        mf_mean2 = f_mf.mean2
        mf_sigma2 = f_mf.sigma2
        mf_fist = np.linspace(mf_mean1 - (mf_sigma1 * 4),
                              mf_mean1,
                              num=50,
                              endpoint=True)
        mf_second = np.linspace(mf_mean2,
                                mf_mean2 + (mf_sigma2 * 4),
                                num=50,
                                endpoint=True)
        return np.concatenate((mf_fist, mf_second))

    @staticmethod
    def membership_function(mf: Union[TriMF, TrapMF, GaussMF, Gauss2MF],
                            univ: np.ndarray) -> np.ndarray:
        """
        Gera os pontos das curvas de pertinência implementadas.

        Parâmetros
        ----------
        mf : Union[FISTriMF, FISTrapMF, FISGaussMF, FISGauss2MF]
            Instância de classe filha da FISMembershipFunc.

        univ :np.ndarray
            Numpy array com o universo da variável fuzzy.

        Retorna
        -------
        np.ndarray
            Retorna uma numpy array com os pontos da curva de pertinência.
        """

        if not isinstance(mf, MembershipFunction):
            raise Exception("O parâmetro não é uma instância da classe "
                            "FISMembershipFunc!")

        if not isinstance(univ, np.ndarray):
            raise Exception("O parâmetro não é um numpy array!")

        # Se a curva de pertinência for triangular.
        if mf.function == MamdaniFunctions.trimf:
            f_function = fuzz.trimf(x=univ, abc=mf.abc)

        # Se a curva de pertinência for trapezoidal.
        elif mf.function == MamdaniFunctions.trapmf:
            f_function = fuzz.trapmf(x=univ, abcd=mf.abcd)

        # Se a curva de pertinência for gaussiana.
        elif mf.function == MamdaniFunctions.gaussmf:
            f_function = fuzz.gaussmf(x=univ, sigma=mf.sigma, mean=mf.mean)

        # Se a curva de pertinência for de duas gaussianas combinadas
        elif mf.function == MamdaniFunctions.gauss2mf:
            f_function = fuzz.gauss2mf(x=univ,
                                       sigma1=mf.sigma1,
                                       mean1=mf.mean1,
                                       sigma2=mf.sigma2,
                                       mean2=mf.mean2)
        else:
            raise Exception("Função de pertinência não implementada!")

        return f_function
