# -*- coding: utf-8 -*-

from typing import List

from filometro.dataclasses import Posto


def posto_dict_to_posto_object(posto_dict: dict) -> Posto:
    return Posto(
        equipamento=posto_dict['equipamento'],
        endereco=posto_dict['endereco'],
        distrito=posto_dict['distrito'],
        crs=posto_dict['crs'],
        astrazeneca=posto_dict['astrazeneca'],
        coronavac=posto_dict['coronavac'],
        pfizer=posto_dict['pfizer'],
        intercambialidade=posto_dict['intercambialidade'],
        status_fila=posto_dict['status_fila'],
        indice_fila=posto_dict['indice_fila'],
        data_hora=posto_dict['data_hora'],
        tipo_posto=posto_dict['tipo_posto'],
        id_crs=posto_dict['id_crs'],
        id_distrito=posto_dict['id_distrito'],
        id_tb_unidades=posto_dict['id_tb_unidades'],
        id_tipo_posto=posto_dict['id_tipo_posto']
    )


def postos_dicts_to_postos_objects(postos_dicts: List[dict]) -> List[Posto]:
    postos_objects = []
    for posto_dict in postos_dicts:
        posto_object = posto_dict_to_posto_object(posto_dict)
        postos_objects.append(posto_object)
    
    return postos_objects
