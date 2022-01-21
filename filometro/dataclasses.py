# -*- coding: utf-8 -*-
"""
filometro.dataclasses
---------------------

Fornece os modelos de dados utilizados pelo pacote.
"""

__all__ = ['Posto']

from filometro import __version__
from filometro import __author__

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Posto():
    equipment: str                               # equipamento
    address: str = field(repr=False)             # endereço
    district: str = field(repr=False)            # distrito
    zone: str = field(repr=False)                # crs (Coordinate Reference Systems)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    coronavac_pediatrica: str = field(repr=False)
    pfizer: str = field(repr=False)
    pfizer_pediatrica: str = field(repr=False)
    janssen: str = field(repr=False)
    influenza: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    situation: str = field(repr=False)           # status_fila
    modality: str = field(repr=False)            # tipo_posto
    last_update: str                             # data_hora
    _index_situation: str = field(repr=False)    # indice_fila
    _id_district: str = field(repr=False)        # id_distrito
    _id_zone: str = field(repr=False)            # id_crs
    _id_tb_unidades: str = field(repr=False)
    _id_modality: str = field(repr=False)        # id_tipo_posto
