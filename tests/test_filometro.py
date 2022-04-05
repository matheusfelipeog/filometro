"""Testes do módulo filometro.filometro."""

import unittest

from filometro.dataclasses import Posto
from filometro.filometro import _posto_dict_to_posto_object
from filometro.filometro import _postos_dicts_to_postos_objects


class TestPostoConversions(unittest.TestCase):
    """Testes para todas as conversões de dados relacionados aos Postos."""

    def setUp(self):
        self.posto_dict = {
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

    def test_conversion_posto_dict_to_posto_object(self):
        posto_object = _posto_dict_to_posto_object(self.posto_dict)

        self.assertIsInstance(posto_object, Posto)

        self.posto_dict.pop('equipamento')

        with self.assertRaises(KeyError):
            _posto_dict_to_posto_object(self.posto_dict)

    def test_conversions_postos_dicts_to_postos_objects(self):
        number_of_postos = 5
        postos_dicts = [self.posto_dict.copy() for _ in range(number_of_postos)]

        postos_objects = _postos_dicts_to_postos_objects(postos_dicts)

        self.assertIsInstance(postos_objects, list)

        postos_objects_length = len(postos_objects)
        self.assertEqual(postos_objects_length, number_of_postos)

        for posto_object in postos_objects:
            with self.subTest():
                self.assertIsInstance(posto_object, Posto)

        postos_dicts[1].pop('equipamento')
        with self.assertRaises(KeyError):
            _postos_dicts_to_postos_objects(postos_dicts)
