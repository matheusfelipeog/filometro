"""
filometro.dataclasses
---------------------

Fornece os modelos de dados utilizados pelo pacote.
"""

__all__ = ['Posto']

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Posto():
    """Modelo de dados do Posto."""

    equipment: str                               # equipamento
    address: str = field(repr=False)             # endereço
    district: str = field(repr=False)            # distrito
    zone: str = field(repr=False)                # crs (Coordinate Reference Systems)
    maps: str = field(init=False, repr=False)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    coronavac_pediatrica: str = field(repr=False)
    pfizer: str = field(repr=False)
    pfizer_pediatrica: str = field(repr=False)
    janssen: str = field(repr=False)
    influenza: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    situation: str = field(repr=False)           # status_fila
    modality: str = field(repr=False)            # tipo_posto
    last_update: str                             # data_hora
    _index_situation: str = field(repr=False)    # indice_fila
    _id_district: str = field(repr=False)        # id_distrito
    _id_zone: str = field(repr=False)            # id_crs
    _id_tb_unidades: str = field(repr=False)
    _id_modality: str = field(repr=False)        # id_tipo_posto

    def __post_init__(self) -> None:
        self.maps = self._build_maps_link()

    @staticmethod
    def _remove_substring_until_the_end(string: str, substring: str) -> str:
        new_string = string
        if substring in string:
            idx_substring = string.find(substring)
            new_string = string[:idx_substring]
        return new_string

    def _extract_address(self) -> str:
        address = self.address.upper()
        address = address.replace('ENDEREÇO:', '')

        address = self._remove_substring_until_the_end(address, 'F:')
        address = self._remove_substring_until_the_end(address, 'FONE:')
        address = self._remove_substring_until_the_end(address, 'TEL:')

        address = address.strip().strip('-').strip(',')

        return address.strip()

    def _build_maps_link(self) -> str:
        address = self._extract_address()
        address = address.replace(' ', '+')

        return f'https://www.google.com.br/maps/place/{address}'
