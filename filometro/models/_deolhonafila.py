# -*- coding: utf-8 -*-

import requests

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Posto():
    equipamento: str = field(repr=False)
    endereco: str = field(repr=False)
    distrito: str
    crs: str = field(repr=False)
    astrazeneca: str = field(repr=False)
    coronavac: str = field(repr=False)
    pfizer: str = field(repr=False)
    intercambialidade: str = field(repr=False)
    status_fila: str
    indice_fila: str = field(repr=False)
    data_hora: str
    tipo_posto: str = field(repr=False)
    id_crs: str = field(repr=False)
    id_distrito: str = field(repr=False)
    id_tb_unidades: str = field(repr=False)
    id_tipo_posto: str = field(repr=False)


class APIDeOlhoNaFila():

    def __init__(self) -> None:
        self.endpoint = 'https://deolhonafila.prefeitura.sp.gov.br/processadores/dados.php'
        self.payload = {'dados': 'dados'}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Host': 'deolhonafila.prefeitura.sp.gov.br',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
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

    def get_data(self) -> list:
        response = requests.post(self.endpoint, headers=self.headers, data=self.payload)

        response.raise_for_status()

        return response.json()
