# -*- coding: utf-8 -*-

from copy import deepcopy

from dataclasses import dataclass
from dataclasses import field

from .deolhonafila import APIDeOlhoNaFila


@dataclass
class Posto():
    equipamento: str = field(repr=False)
    endereco: str = field(repr=False)
    distrito: str
    crs: str = field(repr=False)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    pfizer: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    status_fila: str
    indice_fila: str = field(repr=False)
    data_hora: str
    tipo_posto: str = field(repr=False)
    id_crs: str = field(repr=False)
    id_distrito: str = field(repr=False)
    id_tb_unidades: str = field(repr=False)
    id_tipo_posto: str = field(repr=False)


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
