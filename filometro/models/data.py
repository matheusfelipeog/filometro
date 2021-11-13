# -*- coding: utf-8 -*-

from copy import deepcopy

from dataclasses import dataclass

from .deolhonafila import APIDeOlhoNaFila


@dataclass
class Posto():
    equipamento: str
    endereco: str
    distrito: str
    crs: str
    astrazeneca: str
    coronavac: str
    pfizer: str
    intercambialidade: str
    status_fila: str
    indice_fila: str
    data_hora: str
    tipo_posto: str
    id_crs: str
    id_distrito: str
    id_tb_unidades: str
    id_tipo_posto: str


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
