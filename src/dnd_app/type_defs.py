import typing as t

if t.TYPE_CHECKING:
    from PySide6 import QtCore


class WealthConfigDict(t.TypedDict):
    CoinsGemsPerSlot: int
    GoldPerGem: int
    GoldPerPlatinum: int
    GoldPerElectrum: float
    GoldPerSilver: float
    GoldPerCopper: float


class ConsumablesConfigDict(t.TypedDict):
    TorchesPerSlot: int
    OilFlasksPerSlot: int
    RationsPerSlot: int
    DaggersPerSlot: int
    ArrowsPerSlot: int
    BoltsPerSlot: int
    DartsPerSlot: int
    BulletsPerSlot: int
    NeedlesPerSlot: int


class ArmorConfigDict(t.TypedDict):
    PoundsPerSlot: int


class InternalConfigDict(t.TypedDict):
    InputDir: str
    OutputDir: str
    RecentFiles: list[str]
    WindowGeometry: "QtCore.QByteArray"
    WindowState: "QtCore.QByteArray"


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