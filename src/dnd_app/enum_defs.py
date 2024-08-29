import decimal
import enum
import typing as t

import attrs
from PySide6 import QtGui

D = decimal.Decimal


def search_enum[T: enum.Enum](value: t.Any, enum_class: t.Type[T]) -> T:
    try:
        return enum_class[value]
    except KeyError:
        return enum_class(value)


class EncumbranceStatus(enum.StrEnum):
    UNENCUMBERED = "unencumbered"
    ENCUMBERED = "encumbered"
    HEAVILY_ENCUMBERED = "heavily_encumbered"
    OVER_CAPACITY = "over_capacity"

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()

    def color(self) -> QtGui.QColor:
        if self == EncumbranceStatus.UNENCUMBERED:
            return SVGColors.LIME_GREEN.qcolor()
        elif self == EncumbranceStatus.ENCUMBERED:
            return SVGColors.ORANGE.qcolor()
        else:
            return SVGColors.INDIAN_RED.qcolor()

    def penalties(self) -> str:
        if self == EncumbranceStatus.UNENCUMBERED:
            return "No penalties"
        elif self == EncumbranceStatus.ENCUMBERED:
            return "Your speed drops by 10 feet"
        else:
            return "Your speed drops by 20 feet\n\nYou have disadvantage on ability checks, attack rolls, and saving throws\nthat use Strength, Dexterity, or Constitution"


class SVGColors(enum.StrEnum):
    ALICE_BLUE = "#f0f8ff"
    ANTIQUE_WHITE = "#faebd7"
    AQUA = "#00ffff"
    AQUAMARINE = "#7fffd4"
    AZURE = "#f0ffff"
    BEIGE = "#f5f5dc"
    BISQUE = "#ffe4c4"
    BLACK = "#000000"
    BLANCHED_ALMOND = "#ffebcd"
    BLUE = "#0000ff"
    BLUE_VIOLET = "#8a2be2"
    BROWN = "#a52a2a"
    BURLY_WOOD = "#deb887"
    CADET_BLUE = "#5f9ea0"
    CHARTREUSE = "#7fff00"
    CHOCOLATE = "#d2691e"
    CORAL = "#ff7f50"
    CORNFLOWER_BLUE = "#6495ed"
    CORNSILK = "#fff8dc"
    CRIMSON = "#dc143c"
    CYAN = "#00ffff"
    DARK_BLUE = "#00008b"
    DARK_CYAN = "#008b8b"
    DARK_GOLDEN_ROD = "#b8860b"
    DARK_GRAY = "#a9a9a9"
    DARK_GREEN = "#006400"
    DARK_GREY = "#a9a9a9"
    DARK_KHAKI = "#bdb76b"
    DARK_MAGENTA = "#8b008b"
    DARK_OLIVE_GREEN = "#556b2f"
    DARK_ORANGE = "#ff8c00"
    DARK_ORCHID = "#9932cc"
    DARK_RED = "#8b0000"
    DARK_SALMON = "#e9967a"
    DARK_SEA_GREEN = "#8fbc8f"
    DARK_SLATE_BLUE = "#483d8b"
    DARK_SLATE_GRAY = "#2f4f4f"
    DARK_SLATE_GREY = "#2f4f4f"
    DARK_TURQUOISE = "#00ced1"
    DARK_VIOLET = "#9400d3"
    DEEP_PINK = "#ff1493"
    DEEP_SKY_BLUE = "#00bfff"
    DIM_GRAY = "#696969"
    DIM_GREY = "#696969"
    DODGER_BLUE = "#1e90ff"
    FIRE_BRICK = "#b22222"
    FLORAL_WHITE = "#fffaf0"
    FOREST_GREEN = "#228b22"
    FUCHSIA = "#ff00ff"
    GAINSBORO = "#dcdcdc"
    GHOST_WHITE = "#f8f8ff"
    GOLD = "#ffd700"
    GOLDEN_ROD = "#daa520"
    GRAY = "#808080"
    GREEN = "#008000"
    GREEN_YELLOW = "#adff2f"
    GREY = "#808080"
    HONEY_DEW = "#f0fff0"
    HOT_PINK = "#ff69b4"
    INDIAN_RED = "#cd5c5c"
    INDIGO = "#4b0082"
    IVORY = "#fffff0"
    KHAKI = "#f0e68c"
    LAVENDER = "#e6e6fa"
    LAVENDER_BLUSH = "#fff0f5"
    LAWN_GREEN = "#7cfc00"
    LEMON_CHIFFON = "#fffacd"
    LIGHT_BLUE = "#add8e6"
    LIGHT_CORAL = "#f08080"
    LIGHT_CYAN = "#e0ffff"
    LIGHT_GOLDEN_ROD_YELLOW = "#fafad2"
    LIGHT_GRAY = "#d3d3d3"
    LIGHT_GREEN = "#90ee90"
    LIGHT_GREY = "#d3d3d3"
    LIGHT_PINK = "#ffb6c1"
    LIGHT_SALMON = "#ffa07a"
    LIGHT_SEA_GREEN = "#20b2aa"
    LIGHT_SKY_BLUE = "#87cefa"
    LIGHT_SLATE_GRAY = "#778899"
    LIGHT_SLATE_GREY = "#778899"
    LIGHT_STEEL_BLUE = "#b0c4de"
    LIGHT_YELLOW = "#ffffe0"
    LIME = "#00ff00"
    LIME_GREEN = "#32cd32"
    LINEN = "#faf0e6"
    MAGENTA = "#ff00ff"
    MAROON = "#800000"
    MEDIUM_AQUA_MARINE = "#66cdaa"
    MEDIUM_BLUE = "#0000cd"
    MEDIUM_ORCHID = "#ba55d3"
    MEDIUM_PURPLE = "#9370db"
    MEDIUM_SEA_GREEN = "#3cb371"
    MEDIUM_SLATE_BLUE = "#7b68ee"
    MEDIUM_SPRING_GREEN = "#00fa9a"
    MEDIUM_TURQUOISE = "#48d1cc"
    MEDIUM_VIOLET_RED = "#c71585"
    MIDNIGHT_BLUE = "#191970"
    MINT_CREAM = "#f5fffa"
    MISTY_ROSE = "#ffe4e1"
    MOCCASIN = "#ffe4b5"
    NAVAJO_WHITE = "#ffdead"
    NAVY = "#000080"
    OLD_LACE = "#fdf5e6"
    OLIVE = "#808000"
    OLIVE_DRAB = "#6b8e23"
    ORANGE = "#ffa500"
    ORANGE_RED = "#ff4500"
    ORCHID = "#da70d6"
    PALE_GOLDEN_ROD = "#eee8aa"
    PALE_GREEN = "#98fb98"
    PALE_TURQUOISE = "#afeeee"
    PALE_VIOLET_RED = "#db7093"
    PAPAYA_WHIP = "#ffefd5"
    PEACH_PUFF = "#ffdab9"
    PERU = "#cd853f"
    PINK = "#ffc0cb"
    PLUM = "#dda0dd"
    POWDER_BLUE = "#b0e0e6"
    PURPLE = "#800080"
    RED = "#ff0000"
    ROSY_BROWN = "#bc8f8f"
    ROYAL_BLUE = "#4169e1"
    SADDLE_BROWN = "#8b4513"
    SALMON = "#fa8072"
    SANDY_BROWN = "#f4a460"
    SEA_GREEN = "#2e8b57"
    SEA_SHELL = "#fff5ee"
    SIENNA = "#a0522d"
    SILVER = "#c0c0c0"
    SKY_BLUE = "#87ceeb"
    SLATE_BLUE = "#6a5acd"
    SLATE_GRAY = "#708090"
    SLATE_GREY = "#708090"
    SNOW = "#fffafa"
    SPRING_GREEN = "#00ff7f"
    STEEL_BLUE = "#4682b4"
    TAN = "#d2b48c"
    TEAL = "#008080"
    THISTLE = "#d8bfd8"
    TOMATO = "#ff6347"
    TURQUOISE = "#40e0d0"
    VIOLET = "#ee82ee"
    WHEAT = "#f5deb3"
    WHITE = "#ffffff"
    WHITE_SMOKE = "#f5f5f5"
    YELLOW = "#ffff00"
    YELLOW_GREEN = "#9acd32"

    def qcolor(self) -> QtGui.QColor:
        return QtGui.QColor(self.value)

    def qicon(self) -> QtGui.QIcon:
        pixmap = QtGui.QPixmap(16, 16)
        pixmap.fill(QtGui.QColor(self.value))
        return QtGui.QIcon(pixmap)


class CreatureSize(enum.IntEnum):
    TINY = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    GARGANTUAN = 5

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


class ItemWeightFormat(enum.Enum):
    POUNDS = "pounds"
    SLOTS = "slots"

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


@attrs.frozen
class _CoinData:
    name: str
    symbol: str
    copper_exchange_rate: decimal.Decimal
    silver_exchange_rate: decimal.Decimal
    electrum_exchange_rate: decimal.Decimal
    gold_exchange_rate: decimal.Decimal
    platinum_exchange_rate: decimal.Decimal


class Coin(enum.Enum):
    COPPER = _CoinData(
        "Copper",
        "cp",
        D(1),
        D(1) / D(10),
        D(1) / D(50),
        D(1) / D(100),
        D(1) / D(1000),
    )
    SILVER = _CoinData(
        "Silver",
        "sp",
        D(10),
        D(1),
        D(1) / D(5),
        D(1) / D(10),
        D(1) / D(100),
    )
    ELECTRUM = _CoinData(
        "Electrum",
        "ep",
        D(50),
        D(5),
        D(1),
        D(1) / D(2),
        D(1) / D(20),
    )
    GOLD = _CoinData(
        "Gold",
        "gp",
        D(100),
        D(10),
        D(2),
        D(1),
        D(1) / D(10),
    )
    PLATINUM = _CoinData(
        "Platinum",
        "pp",
        D(1000),
        D(100),
        D(20),
        D(10),
        D(1),
    )

    def __str__(self) -> str:
        return self.value.name

    @property
    def symbol(self) -> str:
        return self.value.symbol

    @property
    def copper_exchange_rate(self) -> decimal.Decimal:
        return self.value.copper_exchange_rate

    @property
    def silver_exchange_rate(self) -> decimal.Decimal:
        return self.value.silver_exchange_rate

    @property
    def electrum_exchange_rate(self) -> decimal.Decimal:
        return self.value.electrum_exchange_rate

    @property
    def gold_exchange_rate(self) -> decimal.Decimal:
        return self.value.gold_exchange_rate

    @property
    def platinum_exchange_rate(self) -> decimal.Decimal:
        return self.value.platinum_exchange_rate


class EquipmentCategory(enum.StrEnum):
    CURRENCY = "currency"
    ARMOR = "armor"
    WEAPON = "weapon"
    ADVENTURING_GEAR = "adventuring_gear"
    TOOL = "tool"
    MOUNT = "mount"
    VEHICLE = "vehicle"
    TRADEGOOD = "trade_good"
    LIFESTYLE_EXPENSE = "lifestyle_expense"
    FOOD_DRINK_LODGING = "food_drink_lodging"
    SERVICE = "service"

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()


class CharacterRace(enum.StrEnum):
    DRAGONBORN = "dragonborn"
    DWARF = "dwarf"
    ELF = "elf"
    GNOME = "gnome"
    HALF_ELF = "half-elf"
    HALF_ORC = "half-orc"
    HALFING = "halfling"
    HUMAN = "human"
    TIEFLING = "tiefling"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return self.name.replace("_", "-").title()


