# -*- coding: utf-8 -*-

from typing import List

from filometro.deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro import convert

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import District


class Filometro():
    def __init__(self) -> None:
        self._api = APIDeOlhoNaFila()

        self._postos = self._load_postos()
    
    def _load_postos(self) -> List[Posto]:
        postos_dicts = self._api.get_data()
        postos_objects = convert.postos_dicts_to_postos_objects(postos_dicts)
        return postos_objects

    def reload(self) -> None:
        postos = self._load_postos()
        self._postos = postos

    def all_postos(self) -> List[Posto]:
        return self._postos

    def by_zone(self, zone: Zone) -> List[Posto]:
        return [posto for posto in self._postos if posto.crs == zone.value]

    def by_modality(self, modality: Modality) -> List[Posto]:
        return [posto for posto in self._postos if posto.tipo_posto == modality.value]

    def by_district(self, district: District) -> List[Posto]:
        return [posto for posto in self._postos if posto.distrito == district.value]
