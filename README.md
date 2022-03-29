<h1 align="center">
    <img src="https://raw.githubusercontent.com/matheusfelipeog/filometro/master/.github/assets/images/logo.png" alt="Logo filômetro" width="100px" />
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
    <a href="https://pypi.org/project/filometro/">
        <img alt="Downloads in month" src="https://img.shields.io/pypi/dm/filometro" />
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
- [Documentação](#documentação)
   - [Como utilizar?](#como-utilizar)
   - [Métodos da classe Filometro](#métodos-da-classe-filometro)
   - [Identificadores para filtragem (Enums)](#identificadores-para-filtragem-enumsidentificadores-para-filtragem-enums)
- [Contribuições](#contribuições)
- [Licença](#licença)


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

Essa é a documentação completa do pacote Filometro. Nessa seção contém o necessário para utilizar o pacote completamente.

### Como utilizar?

Para utilizar o pacote é necessário importar a classe `Filometro` e instanciar um objeto dessa mesma classe:

```python
>>> from filometro import Filometro
>>> filometro = Filometro()
```

Quando o objeto é instanciado ocorre a coleta dos dados no site De Olho na Fila e, quando finalizado, são armazenados na memória em um atributo de uso interno do objeto. Para obter todos os dados é aconselhado utilizar o método `all_postos`:

```python
>>> postos = filometro.all_postos()
```

Uma lista de objetos do tipo `Posto` será retornada. O objeto `Posto` contém atributos que armazenam as informações de um posto. Por exemplo, é possível verificar o endereço de um posto acessando o atributo `address`:

```python
>>> posto = postos[10]  # Obtendo o posto na posição 10 da lista de postos
>>> posto.address
```

Também é possível obter uma lista de postos conforme um requisito de filtragem, para isso existem métodos que usam identificadores (Enumeração ou Enum para os íntimos) específicos para realizar a filtragem. Você deve importar o identificador que deseja utilizar e passar como argumento para o método de filtragem. Por exemplo, caso você queira obter uma lista de postos que estão localizados na zona Sul de São Paulo:

```python
>>> from filometro import Zone
>>> filometro.by_zone(Zone.SUL)
```

Para atualizar os dados dos postos armazenados em memória é indicado utilizar o método `reload`:

```python
>>> filometro.reload()
```

Esse método recarrega todos os dados com as informações mais recentes disponíveis no site oficial.

### Métodos da classe Filometro

- `Filometro.reload(...)` - Recarregar os dados com as informações mais recentes.
- `Filometro.all_postos(...)` - Retorna os dados de todos os postos.
- `Filometro.all_postos_open(...)` - Retorna os dados de todos os postos abertos no momento da busca.
- `Filometro.all_postos_closed(...)` - Retorna os dados de todos os postos fechados no momento da busca.
- `Filometro.by_zone(...)` - Retorna os dados dos postos por zona selecionada.
- `Filometro.by_modality(...)` - Retorna os dados dos postos por modalidade selecionada.
- `Filometro.by_district(...)` - Retorna os dados dos postos por distrito selecionado.
- `Filometro.by_situation(...)` - Retorna os dados dos postos por situação selecionada.
- `Filometro.by_immunizing(...)` - Retorna os dados dos postos por imunizante selecionado.
- `Filometro.to_dict(...)` - Retorna uma lista de objetos do tipo `dict` contendo todos os dados de postos.
- `Filometro.to_json(...)` - Retorna uma string `json` contendo todos os dados de postos. Também há suporte para a manipulação do retorno utilizando os mesmos argumentos do [método json integrado ao Python](https://docs.python.org/3/library/json.html).
- `Filometro.to_dataframe(...)` - Retorna um [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) contendo os dados de todos os postos.

### Identificadores para filtragem (Enums)

Todos os Enums estão disponíveis para uso atráves da interface príncipal do pacote:

```python
>>> from filometro import Zone, Modality, District, Situation, Immunizing
```

> Para obter mais informações sobre cada um dos Enums, use as funções `dir()` ou `help()` passando um dos Enums como argumento.

- `Zone` - Representa as zonas do Estado de São Paulo.
    - `Zone.SUL`
    - `Zone.OESTE`
    - `Zone.NORTE`
    - `Zone.LESTE`
    - `Zone.CENTRO`
    - `Zone.MEGA_DRIVES`

- `Modality` - Representa as modalidades dos postos de saúde.
    - `Modality.PARQUES`
    - `Modality.POSTO_FIXO`
    - `Modality.POSTO_VOLANTE`
    - `Modality.DRIVE_THRU`
    - `Modality.MEGAPOSTO`

- `District` - Representa todos os distritos do Estado de São Paulo que disponíbilizam um imunizante em seus postos de saúde. Use a função `dir(District)` ou `help(District)` para mais infomações.

- `Situation` - Representa as possíveis situações das filas nos postos de saúde.
    - `Situation.NAO_FUNCIONANDO`
    - `Situation.SEM_FILA`
    - `Situation.FILA_PEQUENA`
    - `Situation.FILA_MEDIA`
    - `Situation.FILA_GRANDE`

- `Immunizing` - Representa os imunizantes disponíveis nos postos de saúde do Estado de São Paulo.
    - `Immunizing.ASTRAZENECA`
    - `Immunizing.INTERCAMBIALIDADE`
    - `Immunizing.PFIZER`
    - `Immunizing.PFIZER_PEDIATRICA`
    - `Immunizing.CORONAVAC`
    - `Immunizing.CORONAVAC_PEDIATRICA`
    - `Immunizing.JANSSEN`
    - `Immunizing.INFLUENZA`


## Contribuições

Toda contribuição é super bem-vinda!

Abaixo mostro com o que você pode contribuir:

- Encontrou algum bug, quer propor uma nova funcionalidade ou conversar sobre o projeto? [Abra uma Issue](https://github.com/matheusfelipeog/filometro/issues) e descreva seu caso.

- Existe uma issue aberta e você quer resolve-la, quer implementar uma nova funcionalidade ou melhorar a documentação? Faça suas adições e me envie um *Pull Request*

- Gostou do projeto, mas não quer ou ainda não consegue contribuir com ele? Considere deixar uma estrela ⭐ para o **Filômetro**

Obrigado pelo interesse em colaborar de alguma forma com o projeto 😄


## Licença

**Filômetro** utiliza a *licença MIT* em todo seu código, confira suas condições em [MIT License](https://github.com/matheusfelipeog/filometro/blob/master/LICENSE).
