"""
filometro.exceptions
--------------------

Disponibiliza as exceções que podem ocorrer no pacote.
"""


class FilometroException(Exception):
    ...


class DataCollectionError(FilometroException):
    ...
