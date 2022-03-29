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

import json

from dataclasses import asdict

from pandas import DataFrame

from filometro.deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import Situation
from filometro.enums import Immunizing
from filometro.enums import District


def _posto_dict_to_posto_object(posto_dict: dict) -> Posto:
    """Converte um dict com informações de um posto em um objeto Posto."""

    return Posto(
        equipment=posto_dict['equipamento'],
        address=posto_dict['endereco'],
        district=posto_dict['distrito'],
        zone=posto_dict['crs'],
        astrazeneca=posto_dict['astrazeneca'],
        coronavac=posto_dict['coronavac'],
        coronavac_pediatrica=posto_dict['corona_ped'],
        pfizer=posto_dict['pfizer'],
        pfizer_pediatrica=posto_dict['pfizer_ped'],
        janssen=posto_dict['janssen'],
        influenza=posto_dict['influenza'],
        intercambialidade=posto_dict['intercambialidade'],
        situation=posto_dict['status_fila'],
        modality=posto_dict['tipo_posto'],
        last_update=posto_dict['data_hora'],
        _index_situation=posto_dict['indice_fila'],
        _id_district=posto_dict['id_distrito'],
        _id_zone=posto_dict['id_crs'],
        _id_tb_unidades=posto_dict['id_tb_unidades'],
        _id_modality=posto_dict['id_tipo_posto']
    )


def _postos_dicts_to_postos_objects(postos_dicts: List[dict]) -> List[Posto]:
    """Converte uma lista de dict com informações de vários postos em 
    uma lista de objetos Posto."""

    postos_objects = []
    for posto_dict in postos_dicts:
        posto_object = _posto_dict_to_posto_object(posto_dict)
        postos_objects.append(posto_object)

    return postos_objects


class Filometro():
    """Filometro é a API príncipal do pacote. 

    Fornence os métodos para coletar e filtrar os dados dos postos.
    """

    def __init__(self) -> None:
        self._api = APIDeOlhoNaFila()

        self._postos = self._load_postos()

    def _load_postos(self) -> List[Posto]:
        postos_dicts = self._api.get_data()
        postos_objects = _postos_dicts_to_postos_objects(postos_dicts)
        return postos_objects

    def reload(self) -> None:
        """Recarregar os dados com as informações mais recentes."""

        postos = self._load_postos()
        self._postos = postos

    def all_postos(self) -> List[Posto]:
        """Retorna os dados de todos os postos."""

        return self._postos

    def all_postos_open(self) -> List[Posto]:
        """Retorna uma lista com todos os postos abertos no momento da busca."""

        return [
            posto for posto in self._postos
            if posto.situation != Situation.NAO_FUNCIONANDO.value
        ]

    def all_postos_closed(self) -> List[Posto]:
        """Retorna uma lista com todos os postos fechados no momento da busca."""

        return self.by_situation(Situation.NAO_FUNCIONANDO)

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

    def to_dict(self) -> List[dict]:
        """Retorna uma lista de dict contendo os dados de todos os postos."""

        return [asdict(posto) for posto in self.all_postos()]

    def to_json(self, *args, **kwargs) -> str:
        """Retorna uma string json contendo os dados de todos os postos.

        Argumentos para configurar o retorno em json são aceitos:

        >>> filometro.to_json(indent=4)

        Consulte a documentação do pacote json para saber quais argumentos
        são suportados.
        """

        data = self.to_dict()

        return json.dumps(data, *args, **kwargs)

    def to_dataframe(self) -> DataFrame:
        """Retorna um DataFrame contendo os dados de todos os postos."""

        return DataFrame(self.all_postos())
