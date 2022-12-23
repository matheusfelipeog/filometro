"""
filometro.dataclasses
---------------------

Fornece os modelos de dados utilizados pelo pacote.
"""

__all__ = ['Posto']

from dataclasses import dataclass
from dataclasses import field

from typing import List

import re


@dataclass
class Posto():
    """Modelo de dados do Posto."""

    equipment: str                               # equipamento
    address: str = field(repr=False)             # endereço
    district: str = field(repr=False)            # distrito
    zone: str = field(repr=False)                # crs (Coordinate Reference Systems)
    maps: str = field(init=False, repr=False)
    contacts: List[str] = field(init=False, repr=False, default_factory=list)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    coronavac_pediatrica: str = field(repr=False)
    pfizer: str = field(repr=False)
    pfizer_baby: str = field(repr=False)
    pfizer_bivalente: str = field(repr=False)
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
        self.contacts.extend(self._extract_contacts())
        self.address = self._extract_address()
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
        address = self.address.replace(' ', '+')

        return f'https://www.google.com.br/maps/place/{address}'

    def _extract_contacts(self) -> List[str]:
        address = self.address.replace(' ', '').upper()

        concatenated_contacts = re.split(r'F:|TEL:|FONE:', address)[-1]
        contacts = re.findall(r'\d{4}-?\d{4}', concatenated_contacts)

        for idx, contact in enumerate(contacts):
            if '-' not in contact:
                contacts[idx] = f'{contact[:4]}-{contact[4:]}'

        return contacts
