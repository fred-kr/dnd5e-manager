import enum
import math

from .config import Config


class Armor(enum.IntEnum):
    Padded = 8
    Leather = 10
    Hide = 12
    StuddedLeather = 13
    ChainShirt = 20
    Breastplate = 20
    HalfPlate = 40
    RingMail = 40
    ScaleMail = 45
    ChainMail = 55
    Splint = 60
    Plate = 65

    def slots(self) -> int:
        return math.ceil(self.value / Config().armor.PoundsPerSlot)


class EncumbranceStatus(enum.StrEnum):
    UNENCUMBERED = "Unencumbered"
    ENCUMBERED = "Encumbered"
    HEAVILY_ENCUMBERED = "Heavily encumbered"