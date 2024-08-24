import qfluentwidgets as qfw
from PySide6 import QtCore, QtWidgets

from ..config import Config
from ..enum_defs import EncumbranceStatus


class EncumbranceBar(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.status_label = qfw.StrongBodyLabel("Status: ")
        self.slots_used = qfw.ProgressBar(self)
        self.slots_used.setFixedWidth(300)

        self._setup_actions()
        self._setup_layout()

    def _setup_actions(self) -> None:
        pass

    def _setup_layout(self) -> None:
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.status_label)
        layout.addWidget(self.slots_used)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

    @property
    def max_slots(self) -> int:
        return Config().character.Strength * 3

    def get_encumbrance_status(self) -> EncumbranceStatus:
        curr_str = Config().character.Strength
        slots_used = self.slots_used.value()
        if slots_used <= curr_str:
            return EncumbranceStatus.UNENCUMBERED
        elif curr_str < slots_used <= curr_str * 2:
            return EncumbranceStatus.ENCUMBERED
        else:
            return EncumbranceStatus.HEAVILY_ENCUMBERED

    def refresh_values(self) -> None:
        status = self.get_encumbrance_status()
        self.status_label.setText(f"Status: {status}")
        self.slots_used.setMaximum(self.max_slots)
        self.slots_used.setValue(self.slots_used.maximum() - self.slots_used.value())
