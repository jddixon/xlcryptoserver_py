# xlcryptoserver/__init__.py

""" Crypto library for python XLattice packages. """

__version__ = '0.0.6'
__version_date__ = '2017-08-23'

__all__ = ['__version__', '__version_date__',
           'XLCryptoServerError', ]


class XLCryptoServerError(RuntimeError):
    """ General purpose exception for the package. """
    pass
