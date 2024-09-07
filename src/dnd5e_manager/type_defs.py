import decimal
import typing as t

from PySide6 import QtCore

from .enum_defs import CharacterRace, CreatureSize, ItemWeightFormat

type ModelIndex = QtCore.QModelIndex | QtCore.QPersistentModelIndex
type Number = int | float | decimal.Decimal | str

# if t.TYPE_CHECKING:
    # from .models.equipment import Cost

class ConfigBaseDict(t.TypedDict):
    pass


class CharacterConfigDict(ConfigBaseDict):
    Name: str
    Race: CharacterRace
    Class: str
    Level: int
    Size: CreatureSize
    Strength: int
    Dexterity: int
    Constitution: int
    Intelligence: int
    Wisdom: int
    Charisma: int


class EquipmentConfigDict(ConfigBaseDict):
    CoinsGemsPerSlot: int
    GoldPerGem: int
    HeavyItemsPoundsPerSlot: int
    WeightFormat: ItemWeightFormat


class ConsumablesConfigDict(ConfigBaseDict):
    TorchesPerSlot: int
    OilFlasksPerSlot: int
    RationsPerSlot: int
    WaterskinsPerSlot: int
    JugsPerSlot: float
    DaggersPerSlot: int
    ArrowsPerSlot: int
    BoltsPerSlot: int
    DartsPerSlot: int
    BulletsPerSlot: int
    NeedlesPerSlot: int


class InternalConfigDict(ConfigBaseDict):
    SavesDir: str
    WindowGeometry: "QtCore.QByteArray"


class WealthDataDict(t.TypedDict):
    gems: int
    platinum: int
    gold: int
    electrum: int
    silver: int
    copper: int


class ConsumablesDataDict(t.TypedDict):
    torches: int
    oil_flasks: int
    rations: float
    waterskins: int
    jugs: int
    daggers: int
    arrows: int
    bolts: int
    darts: int
    bullets: int
    needles: int

class CostDict(t.TypedDict):
    display_currency: str
    quantity: str

class ItemDict(t.TypedDict):
    name: str
    category: str
    pounds: decimal.Decimal
    slots: int
    cost: CostDict
    description: str


class SheetDataDict(t.TypedDict):
    wealth: WealthDataDict
    consumables: ConsumablesDataDict
    inventory: list[ItemDict]
    storage: list[ItemDict]

