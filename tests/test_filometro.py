"""Testes do módulo filometro.filometro."""

import unittest

from typing import List

from filometro.dataclasses import Posto

from filometro.enums import Zone
from filometro.enums import Modality
from filometro.enums import District
from filometro.enums import Situation
from filometro.enums import Immunizing

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
                'pfizer_baby': '0',
                'pfizer_ped': '0',
                'pfizer_bivalente': '0',
                'janssen': '0',
                'influenza': '0',
                'intercambialidade': '0',
                'dengue': '0',
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
                'pfizer_baby': '1',
                'pfizer_ped': '1',
                'pfizer_bivalente': '1',
                'janssen': '1',
                'influenza': '1',
                'intercambialidade': '1',
                'dengue': '1',
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
            'pfizer_baby': 'test',
            'pfizer_ped': 'test',
            'pfizer_bivalente': 'test',
            'janssen': 'test',
            'influenza': 'test',
            'intercambialidade': 'test',
            'dengue': 'test',
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
        self.filometro = Filometro(_api=FakeAPIDeOlhoNaFila())  # type: ignore
        self.total_of_postos = len(self.filometro._postos)

    def test_get_all_postos(self):
        postos = self.filometro.all_postos()

        self.assertIsInstance(postos, list)

        num_of_postos = len(postos)
        self.assertEqual(num_of_postos, self.total_of_postos)

    def test_return_from_all_postos_cannot_reference_internal_data_list(self):
        postos = self.filometro.all_postos()

        self.assertIsNot(postos, self.filometro._postos)

    def test_get_all_postos_open(self):
        postos = self.filometro.all_postos_open()

        num_of_postos = len(postos)
        expected_number_of_postos_open = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_open)

    def test_get_all_postos_closed(self):
        postos = self.filometro.all_postos_closed()

        num_of_postos = len(postos)
        expected_number_of_postos_closed = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_closed)

    def test_get_all_postos_from_a_specific_zone(self):
        postos = self.filometro.by_zone(Zone.SUL)

        num_of_postos = len(postos)
        expected_number_of_postos_from_sul_zone = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_from_sul_zone)

    def test_get_all_postos_from_a_specific_modality(self):
        postos = self.filometro.by_modality(Modality.POSTO_FIXO)

        num_of_postos = len(postos)
        expected_number_of_postos_fixos = 2

        self.assertEqual(num_of_postos, expected_number_of_postos_fixos)

    def test_get_all_postos_from_a_specific_district(self):
        postos = self.filometro.by_district(District.CAMPO_LIMPO)

        num_of_postos = len(postos)
        expected_number_of_postos_from_campo_limpo_district = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_from_campo_limpo_district)

    def test_get_all_postos_from_a_specific_situation(self):
        postos = self.filometro.by_situation(Situation.FILA_GRANDE)

        num_of_postos = len(postos)
        expected_number_of_postos_from_situation = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_from_situation)

    def test_get_all_postos_from_a_specific_immunizing(self):
        postos = self.filometro.by_immunizing(Immunizing.CORONAVAC)

        num_of_postos = len(postos)
        expected_number_of_postos_from_coronavac_immunizing = 1

        self.assertEqual(num_of_postos, expected_number_of_postos_from_coronavac_immunizing)

    def test_convert_postos_to_dict(self):
        data = self.filometro.to_dict()

        self.assertIsInstance(data, list)

        num_of_data = len(data)
        self.assertEqual(num_of_data, self.total_of_postos)

        for d in data:
            with self.subTest():
                self.assertIsInstance(d, dict)
