# -*- coding: utf-8 -*-

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Posto():
    equipamento: str
    endereco: str = field(repr=False)
    distrito: str = field(repr=False)
    crs: str = field(repr=False)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    pfizer: str = field(repr=False)
    janssen: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    status_fila: str = field(repr=False)
    indice_fila: str = field(repr=False)
    data_hora: str
    tipo_posto: str = field(repr=False)
    id_crs: str = field(repr=False)
    id_distrito: str = field(repr=False)
    id_tb_unidades: str = field(repr=False)
    id_tipo_posto: str = field(repr=False)
