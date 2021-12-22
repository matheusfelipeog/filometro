# -*- coding: utf-8 -*-
"""
filometro.convert
-----------------

Fornece as funções de conversão de dados utilizada no pacote.
"""

__all__ = [
    'posto_dict_to_posto_object',
    'postos_dicts_to_postos_objects'
]

from typing import List

from filometro.dataclasses import Posto


def posto_dict_to_posto_object(posto_dict: dict) -> Posto:
    return Posto(
        equipment=posto_dict['equipamento'],
        address=posto_dict['endereco'],
        district=posto_dict['distrito'],
        zone=posto_dict['crs'],
        astrazeneca=posto_dict['astrazeneca'],
        coronavac=posto_dict['coronavac'],
        pfizer=posto_dict['pfizer'],
        janssen=posto_dict['janssen'],
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


def postos_dicts_to_postos_objects(postos_dicts: List[dict]) -> List[Posto]:
    postos_objects = []
    for posto_dict in postos_dicts:
        posto_object = posto_dict_to_posto_object(posto_dict)
        postos_objects.append(posto_object)
    
    return postos_objects
