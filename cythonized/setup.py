from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Ugly made slightly prettier',
  ext_modules = cythonize("ugly_python.pyx"),
)
