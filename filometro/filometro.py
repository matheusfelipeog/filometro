"""
filometro.filometro
-------------------

Fornece a API pública principal do pacote.
"""

__all__ = ['Filometro']

from typing import List

from dataclasses import asdict

from filometro.deolhonafila import APIDeOlhoNaFila

from filometro.dataclasses import Posto

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import Situation
from filometro.enums import Immunizing
from filometro.enums import District


def _posto_factory(data: dict) -> Posto:
    """Cria um objeto Posto com base no dicionário de dados fornecido."""

    return Posto(
        equipment=data['equipamento'],
        address=data['endereco'],
        district=data['distrito'],
        zone=data['crs'],
        astrazeneca=data['astrazeneca'],
        coronavac=data['coronavac'],
        coronavac_pediatrica=data['corona_ped'],
        pfizer=data['pfizer'],
        pfizer_baby=data['pfizer_baby'],
        pfizer_bivalente=data['pfizer_bivalente'],
        pfizer_pediatrica=data['pfizer_ped'],
        janssen=data['janssen'],
        influenza=data['influenza'],
        intercambialidade=data['intercambialidade'],
        situation=data['status_fila'],
        modality=data['tipo_posto'],
        last_update=data['data_hora'],
        _index_situation=data['indice_fila'],
        _id_district=data['id_distrito'],
        _id_zone=data['id_crs'],
        _id_tb_unidades=data['id_tb_unidades'],
        _id_modality=data['id_tipo_posto']
    )


def _postos_factory(data_list: List[dict]) -> List[Posto]:
    """Cria uma lista de objetos Posto com base na lista de dados fornecido."""

    return [_posto_factory(d) for d in data_list]


class Filometro():
    """Filometro é a API príncipal do pacote.

    Fornence os métodos para coletar e filtrar os dados dos postos.
    """

    def __init__(self, _api: APIDeOlhoNaFila = None) -> None:
        self._api = _api or APIDeOlhoNaFila()

        self._postos = self._load_postos()

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(postos={len(self._postos)})'

    def __str__(self) -> str:
        return repr(self)

    def _load_postos(self) -> List[Posto]:
        data_list = self._api.get_data()
        return _postos_factory(data_list)

    def reload(self) -> None:
        """Recarregar os dados com as informações mais recentes."""

        postos = self._load_postos()
        self._postos = postos

    def all_postos(self) -> List[Posto]:
        """Retorna os dados de todos os postos."""

        return self._postos.copy()

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

        return [posto for posto in self._postos if asdict(posto).get(immunizing.value) == '1']

    def to_dict(self) -> List[dict]:
        """Retorna uma lista de dict contendo os dados de todos os postos."""

        return [asdict(posto) for posto in self.all_postos()]
