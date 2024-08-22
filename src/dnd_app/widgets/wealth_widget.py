import math

from PySide6 import QtCore, QtWidgets

from ...ui.ui_wealth import Ui_WealthControls
from .. import type_defs as _t
from ..config import Config


class WealthWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_WealthControls()
        self.ui.setupUi(self)

        self._connect_qsignals()

    @property
    def widgets_amount(self) -> list[QtWidgets.QSpinBox]:
        return [
            self.ui.n_gems,
            self.ui.n_platinum,
            self.ui.n_gold,
            self.ui.n_electrum,
            self.ui.n_silver,
            self.ui.n_copper,
        ]

    @property
    def widgets_gp(self) -> list[QtWidgets.QDoubleSpinBox]:
        return [
            self.ui.gp_gems,
            self.ui.gp_platinum,
            self.ui.gp_gold,
            self.ui.gp_electrum,
            self.ui.gp_silver,
            self.ui.gp_copper,
        ]

    def _connect_qsignals(self) -> None:
        self.ui.btn_reset_all.clicked.connect(self.clear_all)
        for widget in self.widgets_amount:
            widget.valueChanged.connect(lambda: self.refresh_values())

    @QtCore.Slot()
    def clear_all(self) -> None:
        for widget in self.widgets_amount:
            widget.setValue(0)

    @QtCore.Slot()
    def refresh_values(self) -> None:
        n_gems = self.ui.n_gems.value()
        n_platinum = self.ui.n_platinum.value()
        n_gold = self.ui.n_gold.value()
        n_electrum = self.ui.n_electrum.value()
        n_silver = self.ui.n_silver.value()
        n_copper = self.ui.n_copper.value()

        n_total = n_gems + n_platinum + n_gold + n_electrum + n_silver + n_copper

        w_conf = Config().wealth
        gp_gems = n_gems * w_conf.GoldPerGem
        gp_platinum = n_platinum * w_conf.GoldPerPlatinum
        gp_gold = n_gold
        gp_electrum = n_electrum * w_conf.GoldPerElectrum
        gp_silver = n_silver * w_conf.GoldPerSilver
        gp_copper = n_copper * w_conf.GoldPerCopper

        self.set_total_amount(n_total)
        self.set_gp_values(
            gp_gems, gp_platinum, gp_gold, gp_electrum, gp_silver, gp_copper
        )

    def set_total_amount(self, value: int) -> None:
        slots_used = math.ceil(value / Config().wealth.CoinsGemsPerSlot)
        self.ui.n_total.setValue(value)
        self.ui.n_total.setSuffix(
            f" ({slots_used} slot{'' if slots_used == 1 else 's'})"
        )

    def set_gp_values(
        self,
        gp_gems: float,
        gp_platinum: float,
        gp_gold: float,
        gp_electrum: float,
        gp_silver: float,
        gp_copper: float,
    ) -> None:
        self.ui.gp_gems.setValue(gp_gems)
        self.ui.gp_platinum.setValue(gp_platinum)
        self.ui.gp_gold.setValue(gp_gold)
        self.ui.gp_electrum.setValue(gp_electrum)
        self.ui.gp_silver.setValue(gp_silver)
        self.ui.gp_copper.setValue(gp_copper)

        self.ui.gp_total.setValue(
            gp_gems + gp_platinum + gp_gold + gp_electrum + gp_silver + gp_copper
        )

    def get_data(self) -> _t.WealthDataDict:
        self.refresh_values()
        return {
            "gems": self.ui.n_gems.value(),
            "platinum": self.ui.n_platinum.value(),
            "gold": self.ui.n_gold.value(),
            "electrum": self.ui.n_electrum.value(),
            "silver": self.ui.n_silver.value(),
            "copper": self.ui.n_copper.value(),
        }

    def set_data(self, data: _t.WealthDataDict) -> None:
        self.ui.n_gems.setValue(data["gems"])
        self.ui.n_platinum.setValue(data["platinum"])
        self.ui.n_gold.setValue(data["gold"])
        self.ui.n_electrum.setValue(data["electrum"])
        self.ui.n_silver.setValue(data["silver"])
        self.ui.n_copper.setValue(data["copper"])
        self.refresh_values()
