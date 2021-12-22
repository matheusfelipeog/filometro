<h1 align="center">
    <img src="./.github/assets/images/logo.png" alt="Logo filômetro" width="70px" />
    <br />Filômetro
</h1>

<p align="center">
    <sup>Metadata</sup>
    <br />
    <a href="https://pypi.org/project/filometro/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/filometro" />
    </a>
    <a href="https://github.com/matheusfelipeog/filometro/releases">
        <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/matheusfelipeog/filometro" />
    </a>
    <a href="https://github.com/matheusfelipeog/filometro/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/matheusfelipeog/filometro" alt="License MIT" />
    </a>
</p>

<p align="center">
    <sup>Status</sup>
    <br />
    <a href="https://pypi.org/project/filometro/">
        <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/filometro" />
    </a>
</p>


## Index

- [O que é?](#o-que-é)
- [Instalação](#instalação)
- [Demo](#demo)
- [Documenação](#documentação)
- [Contribuições](#contribuições)


## O que é?

Filômetro é um pacote que faz o papel de um wrapper (embrulho) do site [De Olho Na Fila](https://deolhonafila.prefeitura.sp.gov.br/), de modo a disponibilizar acesso a diversos dados sobre postos de vacinação em todo o Estado de São Paulo.

Com esse pacote você tem acesso aos seguintes dados dos postos:

- Equipamento
- Endereço
- Distrito
- Zona
- Os imunizantes
- Situação da fila
- Modalidade
- Data e hora da última atualização

As informações são exatamente as mesmas disponíveis no site oficial (De Olho na Fila), porém disponibilizados por meio de uma interface Python simples para facilitar o uso, manipulação e filtragem dos dados. Consulte a [documentação](#documentação) para saber como utiliza-lo.


## Instalação

Instale o pacote usando `pip`:

```shell
$ pip install filometro
```


## Demo

Obtenha uma lista de postos que tem disponível em seu estoque o imunizante da PFizer e mostre a situação da fila, o endereço e a zona em que o posto está localizado:

```python
>>> from filometro import Filometro
>>> from filometro import Immunizing

>>> filometro = Filometro()

>>> postos = filometro.by_immunizing(Immunizing.PFIZER)
>>> postos
[
    Posto(equipment='UBS HUMAITÁ - DR. JOÃO DE AZEVEDO LAGE', last_update='2021-12-22 12:51:18.653'),
    ...  # comprimido
    Posto(equipment='UBS SANTA CRUZ', last_update='2021-12-22 12:46:35.190')
]

>>> for posto in postos:
...     print(f'Fila: {posto.situation}')
...     print(f'Endereço: {posto.address}')
...     print(f'Zona: {posto.zone}', end='\n\n')

Fila: FILA PEQUENA
Endereço: R. HUMAITÁ, 520 - BELA VISTA - CEP: 01321-010 - Tel: 3241- 1632/ 3241-1163
Zona: CENTRO

...  # comprimido

Fila: FILA PEQUENA
Endereço: Rua Santa Cruz, 1.191 - Vila Mariana
Zona: SUL
```

Verifique a documentação para obter informações sobre os métodos disponíveis no pacote.


## Documentação


## Contribuições

Toda contribuição é super bem-vinda!

Abaixo mostro com o que você pode contribuir:

- Encontrou algum bug, quer propor uma nova funcionalidade ou conversar sobre o projeto? [Abra uma Issue](https://github.com/matheusfelipeog/filometro/issues) e descreve seu caso.

- Existe uma issue aberta e você quer resolve-la, quer implementar uma nova funcionalidade ou melhorar a documentação? Faça suas adições e me envie um *Pull Request*

- Gostou do projeto, mas não quer ou ainda não consegue contribuir com ele? Considere deixar uma estrela ⭐ para o **Filometro**

Obrigado pelo interesse em colaborar de alguma forma com o projeto 😄


## Licença
