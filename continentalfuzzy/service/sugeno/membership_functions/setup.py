from setuptools import setup
from Cython.Build import cythonize

setup(name="membership_functions", ext_modules=cythonize('membership_functions.pyx'),)