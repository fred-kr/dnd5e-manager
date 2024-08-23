import typing as t

import attrs
import qfluentwidgets as qfw
from PySide6 import QtCore, QtWidgets

from . import type_defs as _t


def app_dir_posix() -> str:
    app_instance = QtWidgets.QApplication.instance()
    import sys

    return (
        QtCore.QDir(app_instance.applicationDirPath()).canonicalPath()
        if hasattr(sys, "frozen") and app_instance is not None
        else QtCore.QDir.current().canonicalPath()
    )


def sync[T](inst: attrs.AttrsInstance, attr: t.Any, value: T) -> T:
    path = attr.metadata.get("path", None)
    settings = QtCore.QSettings()
    if path and path in settings.allKeys():
        settings.setValue(path, value)
        settings.sync()
    return value


@attrs.define(on_setattr=sync)
class _Wealth:
    CoinsGemsPerSlot: int = attrs.field(
        default=250,
        metadata={
            "path": "Wealth/CoinsGemsPerSlot",
            "ui_name": "Coins/Gems per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of coins/gems that take up one slot.",
        },
    )
    GoldPerGem: int = attrs.field(
        default=50,
        metadata={
            "path": "Wealth/GoldPerGem",
            "ui_name": "Gold per Gem",
            "widget": QtWidgets.QSpinBox,
            "description": "Value of a single gem in gold (gp).",
        },
    )
    GoldPerPlatinum: int = attrs.field(
        default=10,
        metadata={
            "path": "Wealth/GoldPerPlatinum",
            "ui_name": "Gold per Platinum",
            "widget": QtWidgets.QSpinBox,
            "description": "Value of a single platinum in gold (gp).",
        },
    )
    GoldPerElectrum: float = attrs.field(
        default=0.5,
        converter=lambda x: round(x, 1),
        metadata={
            "path": "Wealth/GoldPerElectrum",
            "ui_name": "Gold per Electrum",
            "widget": QtWidgets.QDoubleSpinBox,
            "description": "Value of a single electrum in gold (gp).",
        },
    )
    GoldPerSilver: float = attrs.field(
        default=0.1,
        converter=lambda x: round(x, 1),
        metadata={
            "path": "Wealth/GoldPerSilver",
            "ui_name": "Gold per Silver",
            "widget": QtWidgets.QDoubleSpinBox,
            "description": "Value of a single silver in gold (gp).",
        },
    )
    GoldPerCopper: float = attrs.field(
        default=0.01,
        converter=lambda x: round(x, 2),
        metadata={
            "path": "Wealth/GoldPerCopper",
            "ui_name": "Gold per Copper",
            "widget": QtWidgets.QDoubleSpinBox,
            "description": "Value of a single copper in gold (gp).",
        },
    )

    def to_dict(self) -> _t.WealthConfigDict:
        return _t.WealthConfigDict(**attrs.asdict(self))

    @classmethod
    def from_qsettings(cls) -> "_Wealth":
        settings = QtCore.QSettings()
        settings.beginGroup("Wealth")
        coinsgems_value = settings.value("CoinsGemsPerSlot", 250, type=int)
        gem_value = settings.value("GoldPerGem", 50, type=int)
        platinum_value = settings.value("GoldPerPlatinum", 10, type=int)
        electrum_value = settings.value("GoldPerElectrum", 0.5, type=float)
        silver_value = settings.value("GoldPerSilver", 0.1, type=float)
        copper_value = settings.value("GoldPerCopper", 0.01, type=float)
        settings.endGroup()

        return cls(
            CoinsGemsPerSlot=coinsgems_value,  # type: ignore
            GoldPerGem=gem_value,  # type: ignore
            GoldPerPlatinum=platinum_value,  # type: ignore
            GoldPerElectrum=electrum_value,  # type: ignore
            GoldPerSilver=silver_value,  # type: ignore
            GoldPerCopper=copper_value,  # type: ignore
        )

    def save(self) -> None:
        settings = QtCore.QSettings()
        settings.beginGroup("Wealth")
        settings.setValue("CoinsGemsPerSlot", self.CoinsGemsPerSlot)
        settings.setValue("GoldPerGem", self.GoldPerGem)
        settings.setValue("GoldPerPlatinum", self.GoldPerPlatinum)
        settings.setValue("GoldPerElectrum", self.GoldPerElectrum)
        settings.setValue("GoldPerSilver", self.GoldPerSilver)
        settings.setValue("GoldPerCopper", self.GoldPerCopper)
        settings.endGroup()

        settings.sync()

    def reset(self) -> None:
        self.CoinsGemsPerSlot = 250
        self.GoldPerGem = 50
        self.GoldPerPlatinum = 10
        self.GoldPerElectrum = 0.5
        self.GoldPerSilver = 0.1
        self.GoldPerCopper = 0.01
        self.save()

    def create_editor_widget(self) -> QtWidgets.QFrame:
        widget = QtWidgets.QFrame()
        widget.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Raised)
        layout = QtWidgets.QFormLayout()
        widget.setLayout(layout)

        for field in attrs.fields(self.__class__):
            name = field.metadata.get("ui_name")
            input_widget = field.metadata.get("widget")()
            input_widget.setFrame(False)
            input_widget.setRange(0, 100_000)
            input_widget.setValue(getattr(self, field.name))
            input_widget.setToolTip(field.metadata.get("description", ""))
            input_widget.valueChanged.connect(lambda value, field=field: setattr(self, field.name, value))
            layout.addRow(name, input_widget)

        return widget


@attrs.define(on_setattr=sync)
class _Consumables:
    TorchesPerSlot: int = attrs.field(
        default=5,
        metadata={
            "path": "Consumables/TorchesPerSlot",
            "ui_name": "Torches per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of torches that take up one slot.",
        },
    )
    OilFlasksPerSlot: int = attrs.field(
        default=5,
        metadata={
            "path": "Consumables/OilFlasksPerSlot",
            "ui_name": "Oil Flasks per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of oil flasks that take up one slot.",
        },
    )
    RationsPerSlot: int = attrs.field(
        default=5,
        metadata={
            "path": "Consumables/RationsPerSlot",
            "ui_name": "Rations per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of rations that take up one slot.",
        },
    )
    WaterskinsPerSlot: int = attrs.field(
        default=1,
        metadata={
            "path": "Consumables/WaterskinsPerSlot",
            "ui_name": "Waterskins per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of waterskins (\u00bd-gallon) that take up one slot.",
        },
    )
    JugsPerSlot: float = attrs.field(
        default=0.5,
        converter=lambda x: round(x, 1),
        metadata={
            "path": "Consumables/JugsPerSlot",
            "ui_name": "Jugs per Slot",
            "widget": QtWidgets.QDoubleSpinBox,
            "description": "Amount of jugs (1-gallon) that take up one slot.",
        },
    )
    DaggersPerSlot: int = attrs.field(
        default=5,
        metadata={
            "path": "Consumables/DaggersPerSlot",
            "ui_name": "Daggers per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of daggers that take up one slot.",
        },
    )
    ArrowsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "path": "Consumables/ArrowsPerSlot",
            "ui_name": "Arrows per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of arrows that take up one slot.",
        },
    )
    BoltsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "path": "Consumables/BoltsPerSlot",
            "ui_name": "Bolts per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of bolts that take up one slot.",
        },
    )
    DartsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "path": "Consumables/DartsPerSlot",
            "ui_name": "Darts per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of darts that take up one slot.",
        },
    )
    BulletsPerSlot: int = attrs.field(
        default=20,
        metadata={
            "path": "Consumables/BulletsPerSlot",
            "ui_name": "Bullets per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of bullets that take up one slot.",
        },
    )
    NeedlesPerSlot: int = attrs.field(
        default=50,
        metadata={
            "path": "Consumables/NeedlesPerSlot",
            "ui_name": "Needles per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "Amount of needles that take up one slot.",
        },
    )

    def to_dict(self) -> _t.ConsumablesConfigDict:
        return _t.ConsumablesConfigDict(**attrs.asdict(self))

    @classmethod
    def from_qsettings(cls) -> "_Consumables":
        settings = QtCore.QSettings()
        settings.beginGroup("Consumables")
        torch_value = settings.value("TorchesPerSlot", 5, type=int)
        oilflask_value = settings.value("OilFlasksPerSlot", 5, type=int)
        rations_value = settings.value("RationsPerSlot", 5, type=int)
        waterskins_value = settings.value("WaterskinsPerSlot", 1, type=int)
        jugs_value = settings.value("JugsPerSlot", 0.5, type=float)
        daggers_value = settings.value("DaggersPerSlot", 5, type=int)
        arrows_value = settings.value("ArrowsPerSlot", 20, type=int)
        bolts_value = settings.value("BoltsPerSlot", 20, type=int)
        darts_value = settings.value("DartsPerSlot", 20, type=int)
        bullets_value = settings.value("BulletsPerSlot", 20, type=int)
        needles_value = settings.value("NeedlesPerSlot", 50, type=int)
        settings.endGroup()

        return cls(
            TorchesPerSlot=torch_value,  # type: ignore
            OilFlasksPerSlot=oilflask_value,  # type: ignore
            RationsPerSlot=rations_value,  # type: ignore
            WaterskinsPerSlot=waterskins_value,  # type: ignore
            JugsPerSlot=jugs_value,  # type: ignore
            DaggersPerSlot=daggers_value,  # type: ignore
            ArrowsPerSlot=arrows_value,  # type: ignore
            BoltsPerSlot=bolts_value,  # type: ignore
            DartsPerSlot=darts_value,  # type: ignore
            BulletsPerSlot=bullets_value,  # type: ignore
            NeedlesPerSlot=needles_value,  # type: ignore
        )

    def save(self) -> None:
        settings = QtCore.QSettings()
        settings.beginGroup("Consumables")
        settings.setValue("TorchesPerSlot", self.TorchesPerSlot)
        settings.setValue("OilFlasksPerSlot", self.OilFlasksPerSlot)
        settings.setValue("RationsPerSlot", self.RationsPerSlot)
        settings.setValue("WaterskinsPerSlot", self.WaterskinsPerSlot)
        settings.setValue("JugsPerSlot", self.JugsPerSlot)
        settings.setValue("DaggersPerSlot", self.DaggersPerSlot)
        settings.setValue("ArrowsPerSlot", self.ArrowsPerSlot)
        settings.setValue("BoltsPerSlot", self.BoltsPerSlot)
        settings.setValue("DartsPerSlot", self.DartsPerSlot)
        settings.setValue("BulletsPerSlot", self.BulletsPerSlot)
        settings.setValue("NeedlesPerSlot", self.NeedlesPerSlot)
        settings.endGroup()

        settings.sync()

    def reset(self) -> None:
        self.TorchesPerSlot = 5
        self.OilFlasksPerSlot = 5
        self.RationsPerSlot = 5
        self.WaterskinsPerSlot = 1
        self.JugsPerSlot = 0.5
        self.DaggersPerSlot = 5
        self.ArrowsPerSlot = 20
        self.BoltsPerSlot = 20
        self.DartsPerSlot = 20
        self.BulletsPerSlot = 20
        self.NeedlesPerSlot = 50
        self.save()

    def create_editor_widget(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QFrame()
        widget.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Raised)
        layout = QtWidgets.QFormLayout()
        widget.setLayout(layout)

        for field in attrs.fields(self.__class__):
            name = field.metadata.get("ui_name")
            input_widget = field.metadata.get("widget")()
            input_widget.setFrame(False)
            input_widget.setRange(0, 100_000)
            input_widget.setValue(getattr(self, field.name))
            input_widget.setToolTip(field.metadata.get("description", ""))
            input_widget.valueChanged.connect(lambda value, field=field: setattr(self, field.name, value))
            layout.addRow(name, input_widget)

        return widget


@attrs.define(on_setattr=sync)
class _Armor:
    PoundsPerSlot: int = attrs.field(
        default=5,
        metadata={
            "path": "Armor/PoundsPerSlot",
            "ui_name": "Pounds (lbs) per Slot",
            "widget": QtWidgets.QSpinBox,
            "description": "For heavy items such as armor and chests, fill one slot per this amount of pounds. Rounds up.",
        },
    )

    def to_dict(self) -> _t.ArmorConfigDict:
        return _t.ArmorConfigDict(**attrs.asdict(self))

    @classmethod
    def from_qsettings(cls) -> "_Armor":
        settings = QtCore.QSettings()
        settings.beginGroup("Armor")
        pounds_value = settings.value("PoundsPerSlot", 5, type=int)
        settings.endGroup()

        return cls(
            PoundsPerSlot=pounds_value,  # type: ignore
        )

    def save(self) -> None:
        settings = QtCore.QSettings()
        settings.beginGroup("Armor")
        settings.setValue("PoundsPerSlot", self.PoundsPerSlot)
        settings.endGroup()

        settings.sync()

    def reset(self) -> None:
        self.PoundsPerSlot = 5
        self.save()

    def create_editor_widget(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QFrame()
        widget.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Raised)
        layout = QtWidgets.QFormLayout()
        widget.setLayout(layout)

        for field in attrs.fields(self.__class__):
            name = field.metadata.get("ui_name")
            input_widget = field.metadata.get("widget")()
            input_widget.setFrame(False)
            input_widget.setRange(0, 100_000)
            input_widget.setValue(getattr(self, field.name))
            input_widget.setToolTip(field.metadata.get("description", ""))
            input_widget.valueChanged.connect(lambda value, field=field: setattr(self, field.name, value))
            layout.addRow(name, input_widget)

        return widget


@attrs.define(on_setattr=sync)
class _InternalConfig:
    InputDir: str = attrs.field(factory=app_dir_posix, metadata={"path": "Internal/InputDir"})
    OutputDir: str = attrs.field(factory=app_dir_posix, metadata={"path": "Internal/OutputDir"})
    RecentFiles: list[str] = attrs.field(factory=list, metadata={"path": "Internal/RecentFiles"})
    WindowGeometry: QtCore.QByteArray = attrs.field(
        factory=QtCore.QByteArray, metadata={"path": "Internal/WindowGeometry"}
    )
    WindowState: QtCore.QByteArray = attrs.field(factory=QtCore.QByteArray, metadata={"path": "Internal/WindowState"})

    def to_dict(self) -> _t.InternalConfigDict:
        return _t.InternalConfigDict(**attrs.asdict(self))

    @classmethod
    def from_qsettings(cls) -> "_InternalConfig":
        settings = QtCore.QSettings()
        settings.beginGroup("Internal")
        input_dir = settings.value("InputDir", app_dir_posix(), type=str)
        output_dir = settings.value("OutputDir", app_dir_posix(), type=str)
        recent_files = settings.value("RecentFiles", [], type=list)
        window_geometry = settings.value("WindowGeometry", QtCore.QByteArray(), type=QtCore.QByteArray)
        window_state = settings.value("WindowState", QtCore.QByteArray(), type=QtCore.QByteArray)
        settings.endGroup()

        return cls(
            InputDir=input_dir,  # type: ignore
            OutputDir=output_dir,  # type: ignore
            RecentFiles=recent_files,  # type: ignore
            WindowGeometry=window_geometry,  # type: ignore
            WindowState=window_state,  # type: ignore
        )

    def save(self) -> None:
        settings = QtCore.QSettings()
        settings.beginGroup("Internal")
        settings.setValue("InputDir", self.InputDir)
        settings.setValue("OutputDir", self.OutputDir)
        settings.setValue("RecentFiles", self.RecentFiles)
        settings.setValue("WindowGeometry", self.WindowGeometry)
        settings.setValue("WindowState", self.WindowState)
        settings.endGroup()

        settings.sync()

    def reset(self) -> None:
        self.InputDir = app_dir_posix()
        self.OutputDir = app_dir_posix()
        self.RecentFiles.clear()
        self.WindowGeometry = QtCore.QByteArray()
        self.WindowState = QtCore.QByteArray()
        self.save()


class Config:
    _instance: "Config | None" = None

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._wealth_config = _Wealth.from_qsettings()
        self._consumables_config = _Consumables.from_qsettings()
        self._armor_config = _Armor.from_qsettings()
        self._internal_config = _InternalConfig.from_qsettings()
        self.save()  # If running for the first time, initializes the settings with default values

    @property
    def wealth(self) -> _Wealth:
        return self._wealth_config

    @property
    def consumables(self) -> _Consumables:
        return self._consumables_config

    @property
    def armor(self) -> _Armor:
        return self._armor_config

    @property
    def internal(self) -> _InternalConfig:
        return self._internal_config

    def update_value(self, group: str | None, key: str, value: t.Any) -> None:
        if group is None:
            return
        group = group.lower()
        if group not in {"wealth", "consumables", "armor", "internal"}:
            return

        if group == "wealth":
            if hasattr(self._wealth_config, key):
                setattr(self._wealth_config, key, value)
        elif group == "consumables":
            if hasattr(self._consumables_config, key):
                setattr(self._consumables_config, key, value)
        elif group == "armor":
            if hasattr(self._armor_config, key):
                setattr(self._armor_config, key, value)
        elif group == "internal":
            if hasattr(self._internal_config, key):
                setattr(self._internal_config, key, value)

        self.save()

    def save(self) -> None:
        self._wealth_config.save()
        self._consumables_config.save()
        self._armor_config.save()
        self._internal_config.save()

    def reset(self) -> None:
        self._wealth_config.reset()
        self._consumables_config.reset()
        self._armor_config.reset()
        self._internal_config.reset()

    def create_editor_window(self) -> QtWidgets.QWidget:
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        widget.setLayout(layout)

        wealth_widget = self._wealth_config.create_editor_widget()
        consumables_widget = self._consumables_config.create_editor_widget()
        armor_widget = self._armor_config.create_editor_widget()

        wealth_label = qfw.SubtitleLabel("Wealth")
        consumables_label = qfw.SubtitleLabel("Consumables")
        armor_label = qfw.SubtitleLabel("Armor")

        layout.addWidget(consumables_label, 0, 0, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        layout.addWidget(consumables_widget, 1, 0, 3, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        layout.addWidget(wealth_label, 0, 1, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        layout.addWidget(wealth_widget, 1, 1, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        layout.addWidget(armor_label, 2, 1, 1, 1)
        layout.addWidget(armor_widget, 3, 1, 1, 1)

        return widget
