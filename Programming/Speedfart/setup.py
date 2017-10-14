from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Saveme", ext_modules = cythonize("Saveme.pyx")
)