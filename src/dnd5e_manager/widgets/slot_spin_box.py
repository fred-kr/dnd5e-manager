import decimal
import math

from PySide6 import QtCore, QtWidgets

D = decimal.Decimal


class SlotSpinBox(QtWidgets.QSpinBox):
    sig_slots_value_changed = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self._amount_per_slot = 1
        self.valueChanged.connect(lambda: self.update_suffix())

    @property
    def amount_per_slot(self) -> int | float | decimal.Decimal:
        return self._amount_per_slot

    @amount_per_slot.setter
    def amount_per_slot(self, amount: int | float | decimal.Decimal) -> None:
        self._amount_per_slot = amount
        self.update_suffix()

    @property
    def slots(self) -> int:
        return math.ceil(self.value() / self._amount_per_slot)

    @QtCore.Slot()
    def update_suffix(self) -> None:
        slots = self.slots
        self.setSuffix(f" ({slots} slot{'s' if slots != 1 else ''})")
        self.sig_slots_value_changed.emit()


class SlotDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    sig_slots_value_changed = QtCore.Signal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self._amount_per_slot = 1
        self.valueChanged.connect(lambda: self.update_suffix())

    @property
    def amount_per_slot(self) -> int | float | decimal.Decimal:
        return self._amount_per_slot

    @amount_per_slot.setter
    def amount_per_slot(self, amount: int | float | decimal.Decimal) -> None:
        self._amount_per_slot = amount
        self.update_suffix()

    @property
    def slots(self) -> int:
        return math.ceil(D(self.value()) / D(self._amount_per_slot))

    @QtCore.Slot()
    def update_suffix(self) -> None:
        slots = self.slots
        self.setSuffix(f" ({self.slots} slot{'s' if slots != 1 else ''})")
        self.sig_slots_value_changed.emit()
