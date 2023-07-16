"""Testes do módulo filometro.deolhonafila."""

import unittest

from filometro.deolhonafila import APIDeOlhoNaFila


class TestAPIDeOlhoNaFila(unittest.TestCase):
    """Testes da classe APIDeOlhoNaFila."""

    def setUp(self):
        self.api = APIDeOlhoNaFila()

    def test_if_has_the_endpoint_attribute_with_the_valid_value(self):
        valid_endpoint = (
            'https://deolhonafila.prefeitura.sp.gov.br'
            '/processadores/dados.php'
        )

        self.assertTrue(hasattr(self.api, 'endpoint'))
        self.assertEqual(self.api.endpoint, valid_endpoint)

    def test_if_has_the_payload_attribute_with_the_valid_value(self):
        valid_payload = {'dados': 'dados'}

        self.assertTrue(hasattr(self.api, 'payload'))
        self.assertEqual(self.api.payload, valid_payload)

    def test_if_has_the_headers_attribute_with_the_valid_value(self):
        valid_headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            ),
            'Host': 'deolhonafila.prefeitura.sp.gov.br',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'sec-ch-ua': (
                '"Google Chrome";v="95", "Chromium";'
                'v="95", ";Not A Brand";v="99"'
            ),
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://deolhonafila.prefeitura.sp.gov.br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://deolhonafila.prefeitura.sp.gov.br/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'pt,en-US;q=0.9,en;q=0.8,de;q=0.7',
            'dnt': '1',
            'sec-gpc': '1'
        }

        self.assertTrue(hasattr(self.api, 'headers'))
        self.assertEqual(self.api.headers, valid_headers)
