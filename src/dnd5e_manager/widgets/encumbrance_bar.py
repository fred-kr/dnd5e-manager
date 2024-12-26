import qfluentwidgets as qfw
from PySide6 import QtCore, QtGui, QtWidgets

from ..app_config import Config
from ..enum_defs import CreatureSize, EncumbranceStatus, SVGColors


class EncumbranceBar(QtWidgets.QFrame):
    sig_capacity_exceeded = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.status_label = qfw.SubtitleLabel(self)
        self.status_label.pixelFontSize = 16  # type: ignore
        self.status_label.installEventFilter(qfw.ToolTipFilter(self.status_label))
        self.status_label.setMinimumWidth(self.status_label.fontMetrics().horizontalAdvance("Heavily Encumbered"))
        self.slots_used = QtWidgets.QProgressBar(self)
        self.slots_used.installEventFilter(qfw.ToolTipFilter(self.slots_used))
        self.slots_used.setStyleSheet(self._get_progress_bar_style_sheet(SVGColors.LIME_GREEN.qcolor()))
        self.slots_used.setTextVisible(True)
        self.slots_used.setFormat("Slots used: %v / %m")

        self._setup_actions()
        self._setup_layout()
        self.update_encumbrance(0)

    def _setup_actions(self) -> None:
        pass

    def _setup_layout(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.status_label)
        layout.addWidget(self.slots_used)
        self.setLayout(layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

    @property
    def max_slots(self) -> int:
        return Config.general.character_strength * 3

    def get_encumbrance_status(self, slots_used: int) -> EncumbranceStatus:
        curr_str = Config.general.character_strength
        creature_size = Config.general.character_size

        # TODO: Implement the logic for size modifiers
        if creature_size >= CreatureSize.LARGE:
            curr_str *= 2
        elif creature_size == CreatureSize.TINY:
            curr_str //= 2

        if slots_used <= curr_str:
            return EncumbranceStatus.UNENCUMBERED
        elif slots_used <= curr_str * 2:
            return EncumbranceStatus.ENCUMBERED
        elif slots_used <= curr_str * 3:
            return EncumbranceStatus.HEAVILY_ENCUMBERED
        else:
            return EncumbranceStatus.OVER_CAPACITY

    def update_encumbrance(self, slots_used: int) -> None:
        status = self.get_encumbrance_status(slots_used)
        self.status_label.setText(f"{status}")
        self.status_label.setTextColor(status.color())

        self.slots_used.setMaximum(self.max_slots)
        self.slots_used.setValue(slots_used)
        self.slots_used.setFormat("Slots used: %v / %m")
        self.slots_used.setStyleSheet(self._get_progress_bar_style_sheet(status.color()))
        if slots_used > self.max_slots:
            self.sig_capacity_exceeded.emit()
            self.status_label.setText("Over capacity!")
            self.slots_used.setFormat(f"Slots used: {slots_used} / %m")

        for w in [self.status_label, self.slots_used]:
            w.setToolTip(status.penalties())

    def _get_progress_bar_style_sheet(self, color: QtGui.QColor) -> str:
        return (
            "QProgressBar { border: 1px solid grey; border-radius: 5px; text-align: center; font: bold; min-width: 300px; }"
            f"QProgressBar::chunk {{ background-color: {color.name(QtGui.QColor.NameFormat.HexArgb)}; }}"
        )
