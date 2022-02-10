# -*- coding: utf-8 -*-
"""
filometro.filometro
-------------------

Fornece a API pública principal do pacote.
"""

__all__ = ['Filometro']

from filometro import __version__
from filometro import __author__

from typing import List

from pandas import DataFrame

from filometro.deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro import convert

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import Situation
from filometro.enums import Immunizing
from filometro.enums import District


class Filometro():
    """Filometro é a API príncipal do pacote. 
    
    Fornence os métodos para coletar e filtrar os dados dos postos.
    """

    def __init__(self) -> None:
        self._api = APIDeOlhoNaFila()

        self._postos = self._load_postos()
    
    def _load_postos(self) -> List[Posto]:
        postos_dicts = self._api.get_data()
        postos_objects = convert.postos_dicts_to_postos_objects(postos_dicts)
        return postos_objects

    def reload(self) -> None:
        """Recarregar os dados com as informações mais recentes."""

        postos = self._load_postos()
        self._postos = postos

    def all_postos(self) -> List[Posto]:
        """Retorna os dados de todos os postos."""

        return self._postos

    def by_zone(self, zone: Zone) -> List[Posto]:
        """Retorna os dados dos postos por zona selecionada."""

        return [posto for posto in self._postos if posto.zone == zone.value]

    def by_modality(self, modality: Modality) -> List[Posto]:
        """Retorna os dados dos postos por modalidade selecionada."""

        return [posto for posto in self._postos if posto.modality == modality.value]

    def by_district(self, district: District) -> List[Posto]:
        """Retorna os dados dos postos por distrito selecionado."""

        return [posto for posto in self._postos if posto.district == district.value]

    def by_situation(self, situation: Situation) -> List[Posto]:
        """Retorna os dados dos postos por situação selecionada."""

        return [posto for posto in self._postos if posto.situation == situation.value]

    def by_immunizing(self, immunizing: Immunizing) -> List[Posto]:
        """Retorna os dados dos postos por imunizante selecionado."""
        
        return [posto for posto in self._postos if posto.__dict__[immunizing.value] == '1']
    
    def to_dataframe(self) -> DataFrame:
        """Retorna um DataFrame contendo os dados de todos os postos."""

        return convert.to_dataframe(self.all_postos())
