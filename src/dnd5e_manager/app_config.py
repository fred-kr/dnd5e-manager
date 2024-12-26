import decimal
import functools
import typing as t

import attrs
from PySide6 import QtCore
from pyside_config import config, config_define
from pyside_config.helpers import (
    make_combo_box_info,
    make_decimal_spin_box_info,
    make_line_edit_info,
    make_spin_box_info,
)
from pyside_widgets.enum_combo_box import EnumComboBox

from .enum_defs import CreatureSize, ItemWeightFormat, search_enum

D = decimal.Decimal


@config_define
class AmountPerSlot:
    coins_gems: int = attrs.field(
        default=250,
        metadata={
            "editor": make_spin_box_info(label="Coins/Gems"),
            "description": "The amount of coins and gems that fill one slot.",
        },
    )
    lb_heavy_items: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Heavy Items (lbs)"),
            "description": "For heavy items such as armor and chests, fill one slot per this amount of pounds. Rounds up.",
        },
    )
    torches: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Torches"),
            "description": "The amount of torches that fill one slot.",
        },
    )
    oil_flasks: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Oil Flasks"),
            "description": "The amount of oil flasks that fill one slot.",
        },
    )
    rations: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Rations"),
            "description": "The amount of rations that fill one slot.",
        },
    )
    waterskins: int = attrs.field(
        default=1,
        metadata={
            "editor": make_spin_box_info(label="Waterskins"),
            "description": "The amount of waterskins that fill one slot.",
        },
    )
    jugs: D = attrs.field(
        default=D("0.5"),
        metadata={
            "editor": make_decimal_spin_box_info(
                label="Jugs",
                singleStep=D("0.5"),
                decimals=1,
                minimum=D("0"),
                maximum=D("1000"),
            ),
            "description": "The amount of jugs that fill one slot.",
        },
    )
    daggers: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Daggers"),
            "description": "The amount of daggers that fill one slot.",
        },
    )
    arrows: int = attrs.field(
        default=20,
        metadata={
            "editor": make_spin_box_info(label="Arrows"),
            "description": "The amount of arrows that fill one slot.",
        },
    )
    bolts: int = attrs.field(
        default=20,
        metadata={
            "editor": make_spin_box_info(label="Bolts"),
            "description": "The amount of bolts that fill one slot.",
        },
    )
    darts: int = attrs.field(
        default=20,
        metadata={
            "editor": make_spin_box_info(label="Darts"),
            "description": "The amount of darts that fill one slot.",
        },
    )
    bullets: int = attrs.field(
        default=20,
        metadata={
            "editor": make_spin_box_info(label="Bullets"),
            "description": "The amount of bullets that fill one slot.",
        },
    )
    needles: int = attrs.field(
        default=50,
        metadata={
            "editor": make_spin_box_info(label="Needles"),
            "description": "The amount of needles that fill one slot.",
        },
    )


amount_per_slot: AmountPerSlot = config.get("AmountPerSlot")
del AmountPerSlot


@config_define
class General:
    saves_dir: str = attrs.field(
        default=QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation),
        metadata={
            "editor": None,
            "description": "The directory where the character's saves are stored.",
        },
    )
    weight_display_format: ItemWeightFormat = attrs.field(
        default=ItemWeightFormat.SLOTS,
        converter=functools.partial(search_enum, enum_class=ItemWeightFormat),
        metadata={
            "editor": make_combo_box_info(
                label="Weight Format",
                widget_factory=functools.partial(EnumComboBox, enum_class=ItemWeightFormat),
                sig_value_changed="sig_current_enum_changed",
                set_value_method="set_current_enum",
            ),
            "description": "Switch between displaying an item's weight as 'Slots used' or 'Pounds (lbs)'.",
        },
    )
    gold_per_gem: int = attrs.field(
        default=50,
        metadata={
            "editor": make_spin_box_info(label="Gold per Gem"),
            "description": "Worth of a single gem in gold.",
        },
    )
    character_strength: int = attrs.field(
        default=10,
        metadata={
            "editor": make_spin_box_info(label="Strength", minimum=1, maximum=20),
            "description": "Your character's strength.",
        },
    )
    character_size: CreatureSize = attrs.field(
        default=CreatureSize.MEDIUM,
        converter=functools.partial(search_enum, enum_class=CreatureSize),
        metadata={
            "editor": make_combo_box_info(
                label="Size",
                widget_factory=functools.partial(EnumComboBox, enum_class=CreatureSize),
                sig_value_changed="sig_current_enum_changed",
                set_value_method="set_current_enum",
            ),
            "description": "Your character's size.",
        },
    )
    character_level: int = attrs.field(
        default=1,
        metadata={
            "editor": make_spin_box_info(label="Level", minimum=1, maximum=20),
            "description": "Your character's level.",
        },
    )


general: General = config.get("General")
del General


@config_define
class Database:
    base_url: str = attrs.field(
        default="https://www.dnd5eapi.co/api/",
        metadata={
            "editor": make_line_edit_info(label="Base URL"),
            "description": "URL of the D&D 5e API.",
        },
    )


database: Database = config.get("Database")
del Database


@config_define
class Internal:
    window_geometry: QtCore.QByteArray = attrs.field(
        default=QtCore.QByteArray(),
        metadata={
            "editor": None,
        },
    )
    window_state: QtCore.QByteArray = attrs.field(
        default=QtCore.QByteArray(),
        metadata={
            "editor": None,
        },
    )


internal: Internal = config.get("Internal")
del Internal


class Config(t.NamedTuple):
    amount_per_slot = amount_per_slot
    database = database
    general = general
    internal = internal
