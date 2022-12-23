"""
filometro.enums
---------------

Fornece todas as enumerações constantes para facilitar a buscas dos dados.
"""

__all__ = [
    'Zone',
    'Modality',
    'Situation',
    'Immunizing',
    'District'
]

from enum import Enum


class Zone(Enum):
    """Fornece todas as zonas onde há um ou mais postos disponíveis."""

    SUL = 'SUL'
    OESTE = 'OESTE'
    NORTE = 'NORTE'
    LESTE = 'LESTE'
    CENTRO = 'CENTRO'
    MEGA_DRIVES = 'MEGA-DRIVES'


class Modality(Enum):
    """Fornece todas as modalidades dos postos."""

    PARQUES = 'PARQUES'
    POSTO_FIXO = 'POSTO FIXO'
    POSTO_VOLANTE = 'POSTO VOLANTE'
    DRIVE_THRU = 'DRIVE-THRU'
    MEGAPOSTO = 'MEGAPOSTO'


class Situation(Enum):
    """Fornece todas as situações que um posto pode estar."""

    NAO_FUNCIONANDO = 'NÃO FUNCIONANDO'
    SEM_FILA = 'SEM FILA'
    FILA_PEQUENA = 'FILA PEQUENA'
    FILA_MEDIA = 'FILA MÉDIA'
    FILA_GRANDE = 'FILA GRANDE'


class Immunizing(Enum):
    """Fornece todos os imunizantes disponíveis nos postos."""

    ASTRAZENECA = 'astrazeneca'
    INTERCAMBIALIDADE = 'intercambialidade'
    PFIZER = 'pfizer'
    PFIZER_BABY = 'pfizer_baby'
    PFIZER_BIVALENTE = 'pfizer_bivalente'
    PFIZER_PEDIATRICA = 'pfizer_pediatrica'
    CORONAVAC = 'coronavac'
    CORONAVAC_PEDIATRICA = 'coronavac_pediatrica'
    JANSSEN = 'janssen'
    INFLUENZA = 'influenza'


class District(Enum):
    """Fornece todos os distritos onde há um ou mais postos."""

    AGUA_RASA = 'Água Rasa'
    ALTO_DE_PINHEIROS = 'Alto de Pinheiros'
    ANHANGUERA = 'Anhanguera'
    ARICANDUVA = 'Aricanduva'
    ARTUR_ALVIM = 'Artur Alvim'
    BELA_VISTA = 'Bela Vista'
    BELEM = 'Belém'
    BOM_RETIRO = 'Bom Retiro'
    BRASILANDIA = 'Brasilândia'
    BRAS = 'Brás'
    BUTANTA = 'Butantã'
    CACHOEIRINHA = 'Cachoeirinha'
    CAMBUCI = 'Cambuci'
    CAMPO_BELO = 'Campo Belo'
    CAMPO_GRANDE = 'Campo Grande'
    CAMPO_LIMPO = 'Campo Limpo'
    CANGAIBA = 'Cangaíba'
    CAPAO_REDONDO = 'Capão Redondo'
    CARRAO = 'Carrão'
    CASA_VERDE = 'Casa Verde'
    CIDADE_ADEMAR = 'Cidade Ademar'
    CIDADE_DUTRA = 'Cidade Dutra'
    CIDADE_LIDER = 'Cidade Líder'
    CIDADE_TIRADENTES = 'Cidade Tiradentes'
    CURSINO = 'Cursino'
    ERMELINO_MATARAZZO = 'Ermelino Matarazzo'
    FREGUESIA_DO_O = 'Freguesia do Ó'
    GRAJAU = 'Grajaú'
    GUAIANASES = 'Guaianases'
    IGUATEMI = 'Iguatemi'
    IPIRANGA = 'Ipiranga'
    ITAIM_BIBI = 'Itaim Bibi'
    ITAIM_PAULISTA = 'Itaim Paulista'
    ITAQUERA = 'Itaquera'
    JABAQUARA = 'Jabaquara'
    JAGUARA = 'Jaguara'
    JAGUARE = 'Jaguaré'
    JARAGUA = 'Jaraguá'
    JARDIM_HELENA = 'Jardim Helena'
    JARDIM_SAO_LUIS = 'Jardim São Luis'
    JARDIM_ANGELA = 'Jardim Ângela'
    JACANA = 'Jaçanã'
    JOSE_BONIFACIO = 'José Bonifácio'
    LAJEADO = 'Lajeado'
    LAPA = 'Lapa'
    LIMAO = 'Limão'
    MANDAQUI = 'Mandaqui'
    MARSILAC = 'Marsilac'
    MOEMA = 'Moema'
    MOOCA = 'Mooca'
    MORUMBI = 'Morumbi'
    PARELHEIROS = 'Parelheiros'
    PARI = 'Pari'
    PARQUE_DO_CARMO = 'Parque do Carmo'
    PEDREIRA = 'Pedreira'
    PENHA = 'Penha'
    PERDIZES = 'Perdizes'
    PERUS = 'Perus'
    PINHEIROS = 'Pinheiros'
    PIRITUBA = 'Pirituba'
    PONTE_RASA = 'Ponte Rasa'
    RAPOSO_TAVARES = 'Raposo Tavares'
    RIO_PEQUENO = 'Rio Pequeno'
    SACOMA = 'Sacomã'
    SANTA_CECILIA = 'Santa Cecília'
    SANTANA = 'Santana'
    SANTO_AMARO = 'Santo Amaro'
    SAPOPEMBA = 'Sapopemba'
    SAUDE = 'Saúde'
    SOCORRO = 'Socorro'
    SAO_DOMINGOS = 'São Domingos'
    SAO_LUCAS = 'São Lucas'
    SAO_MATEUS = 'São Mateus'
    SAO_MIGUEL = 'São Miguel'
    SAO_RAFAEL = 'São Rafael'
    SE = 'Sé'
    TATUAPE = 'Tatuapé'
    TREMEMBE = 'Tremembé'
    TUCURUVI = 'Tucuruvi'
    VILA_ANDRADE = 'Vila Andrade'
    VILA_CURUCA = 'Vila Curuçá'
    VILA_FORMOSA = 'Vila Formosa'
    VILA_GUILHERME = 'Vila Guilherme'
    VILA_JACUI = 'Vila Jacuí'
    VILA_LEOPOLDINA = 'Vila Leopoldina'
    VILA_MARIA = 'Vila Maria'
    VILA_MARIANA = 'Vila Mariana'
    VILA_MATILDE = 'Vila Matilde'
    VILA_MEDEIROS = 'Vila Medeiros'
    VILA_PRUDENTE = 'Vila Prudente'
    VILA_SONIA = 'Vila Sônia'
