# -*- coding: utf-8 -*-

from copy import deepcopy

from dataclasses import dataclass
from dataclasses import field

from .deolhonafila import APIDeOlhoNaFila


@dataclass
class Posto():
    equipamento: str = field(repr=False, default=None)
    endereco: str = field(repr=False, default=None)
    distrito: str = field(default=None)
    crs: str = field(repr=False, default=None)
    astrazeneca: str = field(repr=False, default=None)
    coronavac: str = field(repr=False, default=None)
    pfizer: str = field(repr=False, default=None)
    intercambialidade: str = field(repr=False, default=None)
    status_fila: str = field(default=None)
    indice_fila: str = field(repr=False, default=None)
    data_hora: str = field(default=None)
    tipo_posto: str = field(repr=False, default=None)
    id_crs: str = field(repr=False, default=None)
    id_distrito: str = field(repr=False, default=None)
    id_tb_unidades: str = field(repr=False, default=None)
    id_tipo_posto: str = field(repr=False, default=None)


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

        postos = []
        for d in data:
            postos.append(Posto(**d))

        self._data = postos
        self.length = data_length

    def to_json(self):
        ...

    def to_csv(self):
        ...
