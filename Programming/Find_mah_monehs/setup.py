from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Node", ext_modules = cythonize("Node.pyx")
)