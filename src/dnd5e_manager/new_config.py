import functools
import decimal
from pyside_config import config
from pyside_config.properties import LineEditProperties, SpinBoxProperties, DoubleSpinBoxProperties,ComboBoxProperties
from pyside_config.helpers import make_spin_box_info, make_check_box_info, make_combo_box_info, make_line_edit_info, make_double_spin_box_info
from pyside_widgets.enum_combo_box import EnumComboBox
from PySide6 import QtCore, QtGui, QtWidgets
import attrs


from .enum_defs import CharacterRace, search_enum

from . import type_defs as _t

D = decimal.Decimal

@config.config_define
class AmountPerSlot:
    coins_gems: int = attrs.field(
        default=250,
        metadata={
            "editor": make_spin_box_info(label="Coins/Gems"),
            "description": "The amount of coins and gems that fill one slot.",
        }
    )
    lb_heavy_items: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Heavy Items (lbs)"),
            "description": "For heavy items such as armor and chests, fill one slot per this amount of pounds. Rounds up.",
        }
    )
    torches: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Torches"),
            "description": "The amount of torches that fill one slot.",
        }
    )
    oil_flasks: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Oil Flasks"),
            "description": "The amount of oil flasks that fill one slot.",
        }
    )
    rations: int = attrs.field(
        default=5,
        metadata={
            "editor": make_spin_box_info(label="Rations"),
            "description": "The amount of rations that fill one slot.",
        }
    )
    waterskins: int = attrs.field(
        default=1,
        metadata={
            "editor": make_spin_box_info(label="Waterskins"),
            "description": "The amount of waterskins that fill one slot.",
        }
    )
    jugs: D = attrs.field(
        default=D("0.5"),
        metadata={
            "editor": make_double_spin_box_info(
                label="Jugs",
                singleStep=0.5,
            ),
        