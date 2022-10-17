"""Testes do módulo filometro.filometro."""

import unittest

from filometro.dataclasses import Posto
from filometro.filometro import _posto_factory
from filometro.filometro import _postos_factory


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

    def test_postos_factory(self):
        number_of_postos = 5
        data_list = [self.data.copy() for _ in range(number_of_postos)]

        postos = _postos_factory(data_list)

        self.assertIsInstance(postos, list)

        postos_length = len(postos)
        self.assertEqual(postos_length, number_of_postos)

        for posto in postos:
            with self.subTest():
                self.assertIsInstance(posto, Posto)

        data_list[1].pop('equipamento')
        with self.assertRaises(KeyError):
            _postos_factory(data_list)
