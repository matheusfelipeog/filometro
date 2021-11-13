# -*- coding: utf-8 -*-

from copy import deepcopy

from dataclasses import dataclass
from dataclasses import field

from .deolhonafila import APIDeOlhoNaFila


@dataclass
class Posto():
    equipamento: str = field(default=None)
    endereco: str = field(default=None)
    distrito: str = field(default=None)
    crs: str = field(default=None)
    astrazeneca: str = field(default=None)
    coronavac: str = field(default=None)
    pfizer: str = field(default=None)
    intercambialidade: str = field(default=None)
    status_fila: str = field(default=None)
    indice_fila: str = field(default=None)
    data_hora: str = field(default=None)
    tipo_posto: str = field(default=None)
    id_crs: str = field(default=None)
    id_distrito: str = field(default=None)
    id_tb_unidades: str = field(default=None)
    id_tipo_posto: str = field(default=None)


class Data():

    def __init__(self) -> None:
        self._data = []
        self.length = 0

    @property
    def data(self) -> list:

        if not self._data:
            self.update()
        
        return deepcopy(self._data)

    def update(self) -> None:

        data = APIDeOlhoNaFila.get_data()
        data_length = len(data)

        self._data = data
        self.length = data_length

    def to_json(self):
        ...

    def to_csv(self):
        ...
