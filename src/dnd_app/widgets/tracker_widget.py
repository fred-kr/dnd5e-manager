import typing as t

from PySide6 import QtCore, QtWidgets

from ...ui.ui_tracker import Ui_Tracker
from .. import type_defs as _t
from ..config import Config

if t.TYPE_CHECKING:
    from .slot_spin_box import SlotDoubleSpinBox, SlotSpinBox


class TrackerWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_Tracker()
        self.ui.setupUi(self)

        self._connect_qsignals()
        self.set_amount_per_slot()

    @property
    def consumables(self) -> list["SlotSpinBox"]:
        return [self.ui.n_torches, self.ui.n_oil_flasks]

    @property
    def nourishment(self) -> list["SlotDoubleSpinBox | SlotSpinBox"]:
        return [self.ui.n_rations, self.ui.n_waterskins, self.ui.n_jugs]

    @property
    def ammunition(self) -> list["SlotSpinBox"]:
        return [
            self.ui.n_daggers,
            self.ui.n_arrows,
            self.ui.n_bolts,
            self.ui.n_darts,
            self.ui.n_bullets,
            self.ui.n_needles,
        ]

    def _connect_qsignals(self) -> None:
        self.ui.btn_reset_all.clicked.connect(self.clear_all)

    def set_amount_per_slot(self) -> None:
        conf = Config().consumables
        self.ui.n_torches.amount_per_slot = conf.TorchesPerSlot
        self.ui.n_oil_flasks.amount_per_slot = conf.OilFlasksPerSlot
        self.ui.n_rations.amount_per_slot = conf.RationsPerSlot
        self.ui.n_waterskins.amount_per_slot = conf.WaterskinsPerSlot
        self.ui.n_jugs.amount_per_slot = conf.JugsPerSlot
        self.ui.n_daggers.amount_per_slot = conf.DaggersPerSlot
        self.ui.n_arrows.amount_per_slot = conf.ArrowsPerSlot
        self.ui.n_bolts.amount_per_slot = conf.BoltsPerSlot
        self.ui.n_darts.amount_per_slot = conf.DartsPerSlot
        self.ui.n_bullets.amount_per_slot = conf.BulletsPerSlot
        self.ui.n_needles.amount_per_slot = conf.NeedlesPerSlot

    @QtCore.Slot()
    def clear_all(self) -> None:
        for widget in self.consumables + self.nourishment + self.ammunition:
            widget.setValue(0)

    def refresh_values(self) -> None:
        self.set_amount_per_slot()
        for widget in self.consumables + self.nourishment + self.ammunition:
            widget.update_suffix()

    def get_data(self) -> _t.ConsumablesDataDict:
        self.refresh_values()
        return {
            "torches": self.ui.n_torches.value(),
            "oil_flasks": self.ui.n_oil_flasks.value(),
            "rations": self.ui.n_rations.value(),
            "waterskins": self.ui.n_waterskins.value(),
            "jugs": self.ui.n_jugs.value(),
            "daggers": self.ui.n_daggers.value(),
            "arrows": self.ui.n_arrows.value(),
            "bolts": self.ui.n_bolts.value(),
            "darts": self.ui.n_darts.value(),
            "bullets": self.ui.n_bullets.value(),
            "needles": self.ui.n_needles.value(),
        }

    def set_data(self, data: _t.ConsumablesDataDict) -> None:
        self.ui.n_torches.setValue(data["torches"])
        self.ui.n_oil_flasks.setValue(data["oil_flasks"])
        self.ui.n_rations.setValue(data["rations"])
        self.ui.n_waterskins.setValue(data["waterskins"])
        self.ui.n_jugs.setValue(data["jugs"])
        self.ui.n_daggers.setValue(data["daggers"])
        self.ui.n_arrows.setValue(data["arrows"])
        self.ui.n_bolts.setValue(data["bolts"])
        self.ui.n_darts.setValue(data["darts"])
        self.ui.n_bullets.setValue(data["bullets"])
        self.ui.n_needles.setValue(data["needles"])
        self.refresh_values()
