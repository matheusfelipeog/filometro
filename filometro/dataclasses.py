# -*- coding: utf-8 -*-

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
    pfizer: str = field(repr=False)
    janssen: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    situation: str = field(repr=False)           # status_fila
    index_situation: str = field(repr=False)     # indice_fila
    last_update: str                             # data_hora
    modality: str = field(repr=False)            # tipo_posto
    id_zone: str = field(repr=False)             # id_crs
    id_district: str = field(repr=False)         # id_distrito
    id_tb_unidades: str = field(repr=False)
    id_modality: str = field(repr=False)         # id_tipo_posto
