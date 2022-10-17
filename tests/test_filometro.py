"""Testes do módulo filometro.filometro."""

import unittest

from typing import List

from filometro.dataclasses import Posto

from filometro.filometro import _posto_factory
from filometro.filometro import _postos_factory
from filometro.filometro import Filometro


class FakeAPIDeOlhoNaFila:
    def __init__(self) -> None:
        self._data = [
            {
                'equipamento': 'test',
                'endereco': 'test',
                'distrito': 'Campo Limpo',
                'crs': 'SUL',
                'astrazeneca': '0',
                'coronavac': '0',
                'corona_ped': '0',
                'pfizer': '0',
                'pfizer_ped': '0',
                'janssen': '0',
                'influenza': '0',
                'intercambialidade': '0',
                'status_fila': 'NÃO FUNCIONANDO',
                'tipo_posto': 'POSTO FIXO',
                'data_hora': 'test',
                'indice_fila': 'test',
                'id_distrito': 'test',
                'id_crs': 'test',
                'id_tb_unidades': 'test',
                'id_tipo_posto': 'test'
            },
            {
                'equipamento': 'test',
                'endereco': 'test',
                'distrito': 'Brás',
                'crs': 'LESTE',
                'astrazeneca': '1',
                'coronavac': '1',
                'corona_ped': '1',
                'pfizer': '1',
                'pfizer_ped': '1',
                'janssen': '1',
                'influenza': '1',
                'intercambialidade': '1',
                'status_fila': 'FILA GRANDE',
                'tipo_posto': 'POSTO FIXO',
                'data_hora': 'test',
                'indice_fila': 'test',
                'id_distrito': 'test',
                'id_crs': 'test',
                'id_tb_unidades': 'test',
                'id_tipo_posto': 'test'
            }
        ]

    def get_data(self) -> List[dict]:
        return self._data.copy()


class TestPostoFactory(unittest.TestCase):
    """Testes para criação de objetos Posto."""

    def setUp(self):
        self.data = {
            'equipamento': 'test',
            'endereco': 'test',
            'distrito': 'test',
            'crs': 'test',
            'astrazeneca': 'test',
            'coronavac': 'test',
            'corona_ped': 'test',
            'pfizer': 'test',
            'pfizer_ped': 'test',
            'janssen': 'test',
            'influenza': 'test',
            'intercambialidade': 'test',
            'status_fila': 'test',
            'tipo_posto': 'test',
            'data_hora': 'test',
            'indice_fila': 'test',
            'id_distrito': 'test',
            'id_crs': 'test',
            'id_tb_unidades': 'test',
            'id_tipo_posto': 'test'
        }

    def test_create_posto_object(self):
        posto = _posto_factory(self.data)

        self.assertIsInstance(posto, Posto)

    def test_raise_exception_with_missing_mandatory_key(self):
        self.data.pop('equipamento')

        with self.assertRaises(KeyError):
            _posto_factory(self.data)

    def test_create_a_list_of_postos_objects(self):
        number_of_postos = 5
        data_list = [self.data.copy() for _ in range(number_of_postos)]

        postos = _postos_factory(data_list)

        self.assertIsInstance(postos, list)

        postos_length = len(postos)
        self.assertEqual(postos_length, number_of_postos)

        for posto in postos:
            with self.subTest():
                self.assertIsInstance(posto, Posto)


class TestFilometro(unittest.TestCase):
    """Testes relacionados a classe Filometro."""

    def setUp(self):
        self.filometro = Filometro(_api=FakeAPIDeOlhoNaFila)
