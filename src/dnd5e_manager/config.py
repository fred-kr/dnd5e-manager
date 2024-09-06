import enum
import functools
import inspect
import typing as t

import attrs
import qfluentwidgets as qfw
from attr._make import Factory
from PySide6 import QtCore, QtWidgets

from . import type_defs as _t
from .enum_defs import CharacterRace, CreatureSize, ItemWeightFormat, search_enum
from .widgets.enum_combo_box import EnumComboBox


def get_app_dir() -> str:
    """Get the application's working directory as a posix filepath."""
    app_instance = QtWidgets.QApplication.instance()
    import sys

    return (
        QtCore.QDir(app_instance.applicationDirPath()).canonicalPath()
        if hasattr(sys, "frozen") and app_instance is not None
        else QtCore.QDir.current().canonicalPath()
    )


# def get_saves_dir() -> str:
#     return QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)


def get_setting_path(inst_or_cls: attrs.AttrsInstance | t.Type[attrs.AttrsInstance], attr: t.Any) -> str:
    class_name = inst_or_cls.__name__ if inspect.isclass(inst_or_cls) else inst_or_cls.__class__.__name__
    return f"{class_name}/{attr.name}"


def sync[T](inst: attrs.AttrsInstance, attr: t.Any, value: T) -> T:
    path = get_setting_path(inst, attr)
    settings = QtCore.QSettings()
    if path:
        settings.setValue(path, value)
        settings.sync()
    return value


def _stat_validator(inst: attrs.AttrsInstance, attr: t.Any, value: int) -> None:
    if not 1 <= value <= 20:
        raise ValueError("Stat values must be between 1 and 20.")


class EditorInfo(t.NamedTuple):
    name: str
    widget: t.Type[QtWidgets.QLineEdit | QtWidgets.QSpinBox | QtWidgets.QDoubleSpinBox | EnumComboBox]
    min_max: tuple[int, int] | None = None


def _make_editor(attrs_inst: attrs.AttrsInstance) -> QtWidgets.QFrame:
    container = QtWidgets.QFrame()
    container.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Raised)
    layout = QtWidgets.QFormLayout()
    container.setLayout(layout)

    for field in attrs.fields(attrs_inst.__class__):
        editor_info: EditorInfo | None = field.metadata.get("editor", None)
        if not editor_info:
            continue

        widget = editor_info.widget()
        widget.setFrame(False)

        if isinstance(widget, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
            if editor_info.min_max is not None:
                widget.setRange(*editor_info.min_max)
            widget.setValue(getattr(attrs_inst, field.name))
            widget.valueChanged.connect(lambda value, field=field: setattr(attrs_inst, field.name, value))
            if isinstance(widget, QtWidgets.QDoubleSpinBox):
                widget.setDecimals(1)
                widget.setSingleStep(0.5)
        elif isinstance(widget, QtWidgets.QLineEdit):
            widget.setText(getattr(attrs_inst, field.name))
            widget.textEdited.connect(lambda text, field=field: setattr(attrs_inst, field.name, text))
        else:
            widget.set_enum_class(field.type)
            widget.set_current_enum(getattr(attrs_inst, field.name))
            widget.sig_current_enum_changed.connect(lambda value, field=field: setattr(attrs_inst, field.name, value))

        widget.installEventFilter(qfw.ToolTipFilter(widget))
        widget.setToolTip(field.metadata.get("description", ""))

        layout.addRow(editor_info.name, widget)

    return container


@attrs.define
class ConfigBase:
    def to_dict(self) -> _t.ConfigBaseDict:
        return _t.ConfigBaseDict(**attrs.asdict(self))

    @classmethod
    def from_qsettings(cls) -> t.Self:
        settings = QtCore.QSettings()
        init_values = {}
        for field in attrs.fields(cls):
            path = get_setting_path(cls, field)
            value = settings.value(path, field.default)
            if isinstance(value, Factory):
                value = value.factory()
            init_values[field.name] = value

        return cls(**init_values)

    def to_qsettings(self) -> None:
        settings = QtCore.QSettings()
        for field in attrs.fields(self.__class__):
            path = get_setting_path(self, field)
            value = getattr(self, field.name)
            if isinstance(value, enum.Enum):
                value = value.name
            settings.setValue(path, value)

        settings.sync()

    def restore_defaults(self) -> None:
        for field in attrs.fields(self.__class__):
            setattr(self, field.name, field.default)

        self.to_qsettings()

    def create_editor(self) -> QtWidgets.QFrame:
        return _make_editor(self)


@attrs.define(on_setattr=sync)
class Character(ConfigBase):
    Name: str = attrs.field(
        default="",
        metadata={
            "editor": EditorInfo(name="Name of Character", widget=QtWidgets.QLineEdit),
            "description": "Your character's name.",
        },
    )
    Race: CharacterRace = attrs.field(
        default=CharacterRace.HUMAN,
        converter=functools.partial(search_enum, enum_class=CharacterRace),
        metadata={
            "editor": EditorInfo(name="Race", widget=EnumComboBox),
            "description": "Your character's race.",
        },
    )
    Class: str = attrs.field(
        default="",
        metadata={
            "editor": EditorInfo(name="Class", widget=QtWidgets.QLineEdit),
            "description": "Your character's class.",
        },
    )
    Level: int = attrs.field(
        default=1,
        metadata={
            "editor": EditorInfo(name="Level", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's level.",
        },
    )
    Size: CreatureSize = attrs.field(
        default=CreatureSize.MEDIUM,
        converter=functools.partial(search_enum, enum_class=CreatureSize),
        metadata={
            "editor": EditorInfo(name="Size", widget=EnumComboBox),
            "description": "Your character's size.",
        },
    )
    Strength: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Strength", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's strength.",
        },
    )
    Dexterity: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Dexterity", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's dexterity.",
        },
    )
    Constitution: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Constitution", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's constitution.",
        },
    )
    Intelligence: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Intelligence", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's intelligence.",
        },
    )
    Wisdom: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Wisdom", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's wisdom.",
        },
    )
    Charisma: int = attrs.field(
        default=10,
        validator=_stat_validator,
        metadata={
            "editor": EditorInfo(name="Charisma", widget=QtWidgets.QSpinBox, min_max=(1, 20)),
            "description": "Your character's charisma.",
        },
    )


@attrs.define(on_setattr=sync)
class Equipment(ConfigBase):
    CoinsGemsPerSlot: int = attrs.field(
        default=250,
        metadata={
            "editor": EditorInfo(name="Coins/Gems per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of coins/gems that take up one slot.",
        },
    )
    GoldPerGem: int = attrs.field(
        default=50,
        metadata={
            "editor": EditorInfo(name="Gold per Gem", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Worth of a single gem in gold.",
        },
    )
    HeavyItemsPoundsPerSlot: int = attrs.field(
        default=5,
        metadata={
            "editor": EditorInfo(name="Pounds per Slot (Heavy Items)", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "For heavy items such as armor and chests, fill one slot per this amount of pounds. Rounds up.",
        },
    )
    WeightFormat: ItemWeightFormat = attrs.field(
        default=ItemWeightFormat.SLOTS,
        converter=functools.partial(search_enum, enum_class=ItemWeightFormat),
        metadata={
            "editor": EditorInfo(name="Weight Format", widget=EnumComboBox),
            "description": "Switch between displaying an item's weight as 'Slots used' or 'Pounds (lbs)'.",
        },
    )


@attrs.define(on_setattr=sync)
class Consumables(ConfigBase):
    TorchesPerSlot: int = attrs.field(
        default=5,
        metadata={
            "editor": EditorInfo(name="Torches per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of torches that take up one slot.",
        },
    )
    OilFlasksPerSlot: int = attrs.field(
        default=5,
        metadata={
            "editor": EditorInfo(name="Oil Flasks per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of oil flasks that take up one slot.",
        },
    )
    RationsPerSlot: int = attrs.field(
        default=5,
        metadata={
            "editor": EditorInfo(name="Rations per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of rations that take up one slot.",
        },
    )
    WaterskinsPerSlot: int = attrs.field(
        default=1,
        metadata={
            "editor": EditorInfo(name="Waterskins per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of waterskins (\u00bd-gallon) that take up one slot.",
        },
    )
    JugsPerSlot: float = attrs.field(
        default=0.5,
        converter=lambda x: round(float(x), 1),
        metadata={
            "editor": EditorInfo(name="Jugs per Slot", widget=QtWidgets.QDoubleSpinBox, min_max=(1, 100_000)),
            "description": "Amount of jugs (1-gallon) that take up one slot.",
        },
    )
    DaggersPerSlot: int = attrs.field(
        default=5,
        metadata={
            "editor": EditorInfo(name="Daggers per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of daggers that take up one slot.",
        },
    )
    ArrowsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "editor": EditorInfo(name="Arrows per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of arrows that take up one slot.",
        },
    )
    BoltsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "editor": EditorInfo(name="Bolts per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of bolts that take up one slot.",
        },
    )
    DartsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "editor": EditorInfo(name="Darts per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of darts that take up one slot.",
        },
    )
    BulletsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "editor": EditorInfo(name="Bullets per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of bullets that take up one slot.",
        },
    )
    NeedlesPerSlot: int = attrs.field(
        default=50,
        metadata={
            "editor": EditorInfo(name="Needles per Slot", widget=QtWidgets.QSpinBox, min_max=(1, 100_000)),
            "description": "Amount of needles that take up one slot.",
        },
    )


@attrs.define(on_setattr=sync)
class Database(ConfigBase):
    BaseURL: str = attrs.field(
        default="https://www.dnd5eapi.co/api/",
        metadata={
            "editor": EditorInfo(name="Base URL", widget=QtWidgets.QLineEdit),
            "description": "The base URL of the API.",
        },
    )


@attrs.define(on_setattr=sync)
class Internal(ConfigBase):
    SavesDir: str = attrs.field(
        default=QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
    )
    WindowGeometry: QtCore.QByteArray = attrs.field(factory=QtCore.QByteArray)

    @t.override
    def create_editor(self) -> QtWidgets.QFrame:
        raise NotImplementedError


class Config:
    __slots__ = (
        "_character_config",
        "_equipment_config",
        "_consumables_config",
        "_database_config",
        "_internal_config",
        "_group_names",
    )
    _instance: "Config | None" = None

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._character_config = Character.from_qsettings()
        self._equipment_config = Equipment.from_qsettings()
        self._consumables_config = Consumables.from_qsettings()
        self._database_config = Database.from_qsettings()
        self._internal_config = Internal.from_qsettings()
        self._group_names = frozenset(["character", "equipment", "consumables", "database", "internal"])
        self.save()  # If running for the first time, initializes the settings with default values

    @property
    def character(self) -> Character:
        return self._character_config

    @property
    def equipment(self) -> Equipment:
        return self._equipment_config

    @property
    def consumables(self) -> Consumables:
        return self._consumables_config

    @property
    def database(self) -> Database:
        return self._database_config

    @property
    def internal(self) -> Internal:
        return self._internal_config

    def update_value(self, group: str | None, key: str, value: t.Any) -> None:
        if group is None:
            return
        group = group.lower()
        if group not in self._group_names:
            return

        if group == "character":
            if hasattr(self._character_config, key):
                setattr(self._character_config, key, value)
        elif group == "equipment":
            if hasattr(self._equipment_config, key):
                setattr(self._equipment_config, key, value)
        elif group == "consumables":
            if hasattr(self._consumables_config, key):
                setattr(self._consumables_config, key, value)
        elif group == "internal":
            if hasattr(self._internal_config, key):
                setattr(self._internal_config, key, value)
        elif group == "database":
            if hasattr(self._database_config, key):
                setattr(self._database_config, key, value)

        self.save()

    def save(self) -> None:
        for s in self._group_names:
            config = getattr(self, s)
            config.to_qsettings()

    def reset(self) -> None:
        for s in self.__slots__:
            config = getattr(self, s)
            config.restore_defaults()

    def create_editor_window(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        widget.setLayout(layout)

        character_widget = self._character_config.create_editor()
        equipment_widget = self._equipment_config.create_editor()
        consumables_widget = self._consumables_config.create_editor()
        database_widget = self._database_config.create_editor()

        character_label = qfw.SubtitleLabel("Character")
        equipment_label = qfw.SubtitleLabel("Equipment")
        consumables_label = qfw.SubtitleLabel("Consumables")
        database_label = qfw.SubtitleLabel("Database")

        layout.addWidget(character_label, 0, 0)
        layout.addWidget(character_widget, 1, 0)

        layout.addWidget(equipment_label, 2, 0)
        layout.addWidget(equipment_widget, 3, 0)

        layout.addWidget(consumables_label, 0, 1)
        layout.addWidget(consumables_widget, 1, 1)

        layout.addWidget(database_label, 2, 1)
        layout.addWidget(database_widget, 3, 1)

        return widget

    def clean_and_reset(self) -> None:
        QtCore.QSettings().clear()
        self.reset()
