# -*- coding: utf-8 -*-

from typing import List

from filometro.models._deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro import convert


class Filometro():
    def __init__(self) -> None:
        self._api = APIDeOlhoNaFila()

        self.postos = self._load_postos()
    
    def _load_postos(self) -> List[Posto]:
        postos_dicts = self._api.get_data()
        postos_objects = convert.postos_dicts_to_postos_objects(postos_dicts)
        return postos_objects

    def reload(self) -> None:
        postos = self._load_postos()
        self.postos = postos
