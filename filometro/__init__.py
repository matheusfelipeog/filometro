"""
filometro
---------

Esse pacote fornece diversas formas de acessar, manipular e filtrar os dados
de todos os postos de saúde que são mostrados no site 'De Olho na Fila'.
"""

__all__ = [
    'Zone',
    'Modality',
    'Situation',
    'Immunizing',
    'District',
    'Filometro'
]
__version__ = '1.2.0'
__author__ = 'Matheus Felipe'

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import Situation
from filometro.enums import Immunizing
from filometro.enums import District

from filometro.filometro import Filometro
