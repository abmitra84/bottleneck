"""
Use to convert move.pyx to a C file.

This setup.py is NOT used to install the DSNA package. The DSNA setup.py
file is dsna/setup.py

The C files are distributed with dsna, so this file is only useful if you
modify move_sum.pyx or move_std.pyx or ...

To convert from cython to C:

$ cd dsna/dsna/src
$ python move/setup.py build_ext --inplace

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension("move", ["move/move.pyx"],
               include_dirs=[numpy.get_include()])]

setup(
  name = 'move',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)

