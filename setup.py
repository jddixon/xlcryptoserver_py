#!/usr/bin/python3
# ~/dev/py/xlcryptoserver_py/setup.py

""" Set up distutils for xlcryptoserver_py. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('xlcryptoserver/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='xlcryptoserver_py',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      #
      # wherever we have a .py file that will be imported, we
      # list it here, without the .py extension but SQuoted
      py_modules=[],
      #
      packages=['xlcryptoserver', ],
      #
      # following could be in scripts/ subdir; SQuote
      scripts=[],
      description='cryptoserver layer for xlattice_py',
      url='https://jddixon/github.io/xlcryptoserver_py',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)