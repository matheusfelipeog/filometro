# -*- coding: utf-8 -*-

from copy import deepcopy

from .deolhonafila import APIDeOlhoNaFila


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
        api = APIDeOlhoNaFila()
        data = api.get_data()
        data_length = len(data)

        postos = []
        for d in data:
            postos.append(d)

        self._data = postos
        self.length = data_length

    def to_json(self):
        ...

    def to_csv(self):
        ...
