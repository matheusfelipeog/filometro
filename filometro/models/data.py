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

        data = APIDeOlhoNaFila.get_data()
        data_length = len(data)

        self._data = data
        self.length = data_length
