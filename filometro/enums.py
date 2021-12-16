# -*- coding: utf-8 -*-

from enum import Enum


class Zone(Enum):
    SUL = 'SUL'
    OESTE = 'OESTE'
    NORTE = 'NORTE'
    LESTE = 'LESTE'
    CENTRO = 'CENTRO'
    MEGA_DRIVES = 'MEGA-DRIVES'


class Modality(Enum):
    PARQUES = 'PARQUES'
    POSTO_FIXO = 'POSTO FIXO'
    POSTO_VOLANTE = 'POSTO VOLANTE'
    DRIVE_THRU = 'DRIVE-THRU'
    MEGAPOSTO = 'MEGAPOSTO'