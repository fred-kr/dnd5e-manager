import typing as t

from PySide6 import QtCore, QtWidgets

from ...ui.ui_wealth_consumables_tracker import Ui_WealthConsumablesTracker
from .. import type_defs as _t
from ..config import Config

if t.TYPE_CHECKING:
    from ..widgets.slot_spin_box import SlotDoubleSpinBox, SlotSpinBox


class WealthConsumablesInterface(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("wealth_consumables_interface")
        self.setContentsMargins(0, 0, 0, 0)

        self.ui = Ui_WealthConsumablesTracker()
        self.ui.setupUi(self)
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading)
        self._connect_qsignals()
        self.set_amount_per_slot()

    @property
    def lighting(self) -> list["SlotSpinBox"]:
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

    @property
    def wealth_amount(self) -> list[QtWidgets.QSpinBox]:
        return [
            self.ui.n_gems,
            self.ui.n_platinum,
            self.ui.n_gold,
            self.ui.n_electrum,
            self.ui.n_silver,
            self.ui.n_copper,
        ]

    @property
    def wealth_gp(self) -> list[QtWidgets.QDoubleSpinBox]:
        return [
            self.ui.gp_gems,
            self.ui.gp_platinum,
            self.ui.gp_gold,
            self.ui.gp_electrum,
            self.ui.gp_silver,
            self.ui.gp_copper,
        ]

    @property
    def slot_spin_boxes(self) -> list["SlotSpinBox | SlotDoubleSpinBox"]:
        return self.lighting + self.nourishment + self.ammunition + [self.ui.n_total]

    def _connect_qsignals(self) -> None:
        self.ui.btn_clear_wealth.clicked.connect(self.clear_wealth)
        self.ui.btn_clear_consumables.clicked.connect(self.clear_consumables)
        for widget in self.wealth_amount:
            widget.valueChanged.connect(lambda: self.refresh_wealth())

    def set_amount_per_slot(self) -> None:
        conf = Config()
        self.ui.n_torches.amount_per_slot = conf.consumables.TorchesPerSlot
        self.ui.n_oil_flasks.amount_per_slot = conf.consumables.OilFlasksPerSlot
        self.ui.n_rations.amount_per_slot = conf.consumables.RationsPerSlot
        self.ui.n_waterskins.amount_per_slot = conf.consumables.WaterskinsPerSlot
        self.ui.n_jugs.amount_per_slot = conf.consumables.JugsPerSlot
        self.ui.n_daggers.amount_per_slot = conf.consumables.DaggersPerSlot
        self.ui.n_arrows.amount_per_slot = conf.consumables.ArrowsPerSlot
        self.ui.n_bolts.amount_per_slot = conf.consumables.BoltsPerSlot
        self.ui.n_darts.amount_per_slot = conf.consumables.DartsPerSlot
        self.ui.n_bullets.amount_per_slot = conf.consumables.BulletsPerSlot
        self.ui.n_needles.amount_per_slot = conf.consumables.NeedlesPerSlot

        self.ui.n_total.amount_per_slot = conf.wealth.CoinsGemsPerSlot

    @QtCore.Slot()
    def clear_wealth(self) -> None:
        for widget in self.wealth_amount:
            widget.setValue(0)

    @QtCore.Slot()
    def clear_consumables(self) -> None:
        for widget in self.lighting + self.nourishment + self.ammunition:
            widget.setValue(0)

    @QtCore.Slot()
    def refresh_wealth(self) -> None:
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

        self.ui.n_total.setValue(n_total)
        self.update_wealth_gp(gp_gems, gp_platinum, gp_gold, gp_electrum, gp_silver, gp_copper)

    def update_wealth_gp(
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

        self.ui.gp_total.setValue(gp_gems + gp_platinum + gp_gold + gp_electrum + gp_silver + gp_copper)

    def refresh_consumables(self) -> None:
        self.set_amount_per_slot()
        for widget in self.slot_spin_boxes:
            widget.update_suffix()

    def get_data(self) -> tuple[_t.WealthDataDict, _t.ConsumablesDataDict]:
        self.refresh_wealth()
        self.refresh_consumables()
        return (
            {
                "gems": self.ui.n_gems.value(),
                "platinum": self.ui.n_platinum.value(),
                "gold": self.ui.n_gold.value(),
                "electrum": self.ui.n_electrum.value(),
                "silver": self.ui.n_silver.value(),
                "copper": self.ui.n_copper.value(),
            },
            {
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
            },
        )

    def set_data(self, data: tuple[_t.WealthDataDict, _t.ConsumablesDataDict]) -> None:
        wealth, consumables = data
        self.ui.n_gems.setValue(wealth["gems"])
        self.ui.n_platinum.setValue(wealth["platinum"])
        self.ui.n_gold.setValue(wealth["gold"])
        self.ui.n_electrum.setValue(wealth["electrum"])
        self.ui.n_silver.setValue(wealth["silver"])
        self.ui.n_copper.setValue(wealth["copper"])

        self.ui.n_torches.setValue(consumables["torches"])
        self.ui.n_oil_flasks.setValue(consumables["oil_flasks"])
        self.ui.n_rations.setValue(consumables["rations"])
        self.ui.n_waterskins.setValue(consumables["waterskins"])
        self.ui.n_jugs.setValue(consumables["jugs"])
        self.ui.n_daggers.setValue(consumables["daggers"])
        self.ui.n_arrows.setValue(consumables["arrows"])
        self.ui.n_bolts.setValue(consumables["bolts"])
        self.ui.n_darts.setValue(consumables["darts"])
        self.ui.n_bullets.setValue(consumables["bullets"])
        self.ui.n_needles.setValue(consumables["needles"])

        self.refresh_wealth()
        self.refresh_consumables()

    def refresh_values(self) -> None:
        self.refresh_wealth()
        self.refresh_consumables()
