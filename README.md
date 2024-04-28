<h1 align="center">
    <img src="https://raw.githubusercontent.com/matheusfelipeog/filometro/master/.github/assets/images/logo.png" alt="Logo filometro" width="100px" />
    <br />Filometro
</h1>

<p align="center">
    <sup>Metadata</sup>
    <br />
    <a href="https://pypi.org/project/filometro/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/filometro" />
    </a>
    <a href="https://github.com/matheusfelipeog/filometro/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/matheusfelipeog/filometro" alt="License MIT" />
    </a>
    <a href="https://pepy.tech/project/filometro">
        <img alt="Total Downloads" src="https://pepy.tech/badge/filometro" />
    </a>
</p>

<p align="center">
    <sup>Status</sup>
    <br />
    <a href="https://pypi.org/project/filometro/">
        <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/filometro" />
    </a>
    <a href="https://github.com/matheusfelipeog/filometro/actions/workflows/tests.yml">
        <img alt="Tests - Status" src="https://github.com/matheusfelipeog/filometro/actions/workflows/tests.yml/badge.svg" />
    </a>
</p>


## Index

- [O que é?](#o-que-é)
- [Instalação](#instalação)
- [Demo](#demo)
- [Documentação](#documentação)
   - [Como utilizar?](#como-utilizar)
   - [Objeto Posto](#objeto-posto)
   - [Métodos da classe Filometro](#métodos-da-classe-filometro)
   - [Identificadores para filtragem](#identificadores-para-filtragem)
- [Contribuições](#contribuições)
- [Licença](#licença)


## O que é?

Filometro é um wrapper (embrulho) do site [De Olho Na Fila](https://deolhonafila.prefeitura.sp.gov.br/), de modo a disponibilizar acesso a diversos dados sobre os postos de vacinação em todo o Estado de São Paulo.

Com esse pacote você tem acesso aos seguintes dados dos postos:

- Equipamento
- Endereço
- Contatos
- Distrito
- Zona
- Os imunizantes disponíveis
- Situação da fila
- Modalidade
- Data e hora da última atualização

As informações são exatamente as mesmas disponíveis no site oficial (De Olho na Fila), porém disponibilizados por meio de um pacote Python simples para facilitar a coleta, manipulação e filtragem dos dados. Consulte a [documentação](#documentação) para saber como utiliza-lo.


## Instalação

Instale o pacote usando `pip`:

```shell
$ pip install filometro
```


## Demo

Obtenha uma lista de postos que tem disponível em seu estoque o imunizante da PFizer:

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
```

Verifique a documentação para obter informações sobre os atributos e métodos disponíveis.


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

Sempre que precisar, utilize a função `help()` em alguma classe, objeto ou método para obter ajuda:

```python
>>> help(filometro)
```

### Objeto Posto

Todos os métodos tem como retorno uma lista de dados, esses dados são representados no objeto Posto. Veja quais são seus atributos:

```python
>>> posto.equipment             # Equipamento da unidade.
>>> posto.address               # Endereço onde está localizado.
>>> posto.district              # Distrito onde está localizado.
>>> posto.zone                  # Zona onde está localizado.
>>> posto.maps                  # Um link do Google Maps para o endereço.
>>> posto.contacts              # Uma lista de contatos, se houver.
>>> posto.astrazeneca           # '0' ou '1' caso astrazeneca não esteja ou esteja disponível.
>>> posto.coronavac             # '0' ou '1' caso coronavac não esteja ou esteja disponível.
>>> posto.coronavac_pediatrica  # '0' ou '1' caso coronavac pediátrica não esteja ou esteja disponível.
>>> posto.pfizer                # '0' ou '1' caso pfizer não esteja ou esteja disponível.
>>> posto.pfizer_baby           # '0' ou '1' caso pfizer baby não esteja ou esteja disponível.
>>> posto.pfizer_bivalente      # '0' ou '1' caso pfizer bivalente não esteja ou esteja disponível.
>>> posto.pfizer_pediatrica     # '0' ou '1' caso pfizer pediátrica não esteja ou esteja disponível.
>>> posto.janssen               # '0' ou '1' caso janssen não esteja ou esteja disponível.
>>> posto.influenza             # '0' ou '1' caso influenza não esteja ou esteja disponível.
>>> posto.intercambialidade     # '0' ou '1' caso intercambialidade não esteja ou esteja disponível.
>>> posto.dengue                # '0' ou '1' caso dengue não esteja ou esteja disponível.
>>> posto.situation             # A última atualização da situação da fila.
>>> posto.modality              # A modalidade da unidade.
>>> posto.last_update           # Data e hora da última atualização no formato AAAA-MM-DD HH:MM:SS.MS.
```

### Métodos da classe Filometro

```python
>>> filometro.reload()             # Atualizar dados em memória.
>>> filometro.all_postos()         # Obter todos os postos.
>>> filometro.all_postos_open()    # Obter todos os postos abertos.
>>> filometro.all_postos_closed()  # Obter todos os postos fechados.
>>> filometro.by_zone(...)         # Obter todos postos de uma zona.
>>> filometro.by_modality(...)     # Obter todos postos de uma modalidade.
>>> filometro.by_district(...)     # Obter todos postos de um distrito.
>>> filometro.by_situation(...)    # Obter todos postos por situação.
>>> filometro.by_immunizing(...)   # Obter todos postos que possuem um imunizante.
>>> filometro.to_dict()            # Obter todos postos convertidos para `dict`.
```

### Identificadores para filtragem

Todos os identificadores estão disponíveis para uso atráves da interface príncipal do pacote:

```python
>>> from filometro import Zone, Modality, District, Situation, Immunizing
```

`Zone` - Representa as zonas do Estado de São Paulo:

```python
>>> Zone.SUL
>>> Zone.OESTE
>>> Zone.NORTE
>>> Zone.LESTE
>>> Zone.CENTRO
>>> Zone.MEGA_DRIVES
```

`Modality` - Representa as modalidades dos postos:

```python
>>> Modality.PARQUES
>>> Modality.POSTO_FIXO
>>> Modality.POSTO_VOLANTE
>>> Modality.DRIVE_THRU
>>> Modality.MEGAPOSTO
```

`District` - Representa todos os distritos do Estado de São Paulo que disponíbilizam um imunizante em seus postos. Como há muitos distritos, use a função `dir` ou `help` para mais infomações:

```python
>>> help(District)
>>> dir(District)
```

`Situation` - Representa as situações das filas nos postos:

```python
>>> Situation.NAO_FUNCIONANDO
>>> Situation.SEM_FILA
>>> Situation.FILA_PEQUENA
>>> Situation.FILA_MEDIA
>>> Situation.FILA_GRANDE
```

`Immunizing` - Representa os imunizantes disponíveis nos postos no Estado de São Paulo:

```python
>>> Immunizing.ASTRAZENECA
>>> Immunizing.INTERCAMBIALIDADE
>>> Immunizing.PFIZER
>>> Immunizing.PFIZER_BABY
>>> Immunizing.PFIZER_BIVALENTE
>>> Immunizing.PFIZER_PEDIATRICA
>>> Immunizing.CORONAVAC
>>> Immunizing.CORONAVAC_PEDIATRICA
>>> Immunizing.JANSSEN
>>> Immunizing.INFLUENZA
>>> Immunizing.DENGUE
```


## Contribuições

Toda contribuição é super bem-vinda!

Abaixo mostro com o que você pode contribuir:

- Encontrou algum bug, quer propor uma nova funcionalidade ou conversar sobre o projeto? [Abra uma Issue](https://github.com/matheusfelipeog/filometro/issues) e descreva seu caso.

- Existe uma issue aberta e você quer resolve-la, quer implementar uma nova funcionalidade ou melhorar a documentação? Faça suas adições e me envie um *Pull Request*

- Gostou do projeto, mas não quer ou ainda não consegue contribuir com ele? Considere deixar uma estrela ⭐ para o **Filometro**

Obrigado pelo interesse em colaborar de alguma forma com o projeto ❤


## Licença

**Filometro** utiliza a *licença MIT* em todo seu código, confira suas condições em [MIT License](https://github.com/matheusfelipeog/filometro/blob/master/LICENSE).
