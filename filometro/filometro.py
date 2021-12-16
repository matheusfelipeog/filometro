# -*- coding: utf-8 -*-

from typing import List

from enum import Enum

from filometro.deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro import convert


class Zone(Enum):
    SUL = 'SUL'
    OESTE = 'OESTE'
    NORTE = 'NORTE'
    LESTE = 'LESTE'
    CENTRO = 'CENTRO'
    MEGA_DRIVES = 'MEGA-DRIVES'


class Modality(Enum):
    PARQUES = 'PARQUES'
    POSTO_FIXO = 'POSTO FIXO'
    POSTO_VOLANTE = 'POSTO VOLANTE'
    DRIVE_THRU = 'DRIVE-THRU'
    MEGAPOSTO = 'MEGAPOSTO'


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

    def by_zone(self, zone: Zone) -> List[Posto]:
        return [posto for posto in self.postos if posto.crs == zone.value]

    def by_modality(self, modality: Modality) -> List[Posto]:
        return [posto for posto in self.postos if posto.tipo_posto == modality.value]
