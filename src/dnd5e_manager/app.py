import json
import typing as t
from pathlib import Path

import qfluentwidgets as qfw
from PySide6 import QtCore, QtWidgets

from . import type_defs as _t
# from .config import Config
from .app_config import Config
from .icons import Icons
from .widgets.main_window import MainWindow


class EquipmentManager(QtWidgets.QApplication):
    def __init__(self, sys_argv: t.Sequence[str]) -> None:
        super().__init__(sys_argv)

        self.mw = MainWindow()
        self._setup_command_bar()
        self.mw.setWindowTitle("DnD5e Equipment Manager")
        self.capacity_exceeded_msg_shown = False
        self._connect_qsignals()

    def _connect_qsignals(self) -> None:
        for ssb in self.mw.wealth_consumables_interface.slot_spin_boxes:
            ssb.sig_slots_value_changed.connect(self.update_slots_used)
        self.mw.item_tables_interface.sig_inventory_slots_changed.connect(self.update_slots_used)
        self.mw.encumbrance_bar.sig_capacity_exceeded.connect(self.show_capacity_exceeded_msg)

    def _setup_command_bar(self) -> None:
        self.mw.addCommand(Icons.ArrowImport.icon(), "Open Sheet", self.load_sheet)
        self.mw.addCommand(Icons.Save.icon(), "Save Sheet", self.save_sheet)
        self.mw.addCommand(Icons.Settings.icon(), "Preferences", self.mw.open_preferences)
        self.mw.addCommand(Icons.ArrowReset.icon(), "Reset Preferences", self.mw.reset_config, hidden=True)

    @QtCore.Slot(str)
    def show_error(self, error: str) -> None:
        QtWidgets.QMessageBox.critical(self.mw, "Error", error)

    @QtCore.Slot()
    def show_capacity_exceeded_msg(self) -> None:
        if not self.capacity_exceeded_msg_shown:
            w = qfw.InfoBar.warning(
                title="Carrying Capacity Exceeded",
                content="Looks like you've been hitting the loot a bit too hard. Unless you plan on dragging that mountain of gear behind you, it might be time to reconsider your life choices (or at least your inventory).",
                orient=QtCore.Qt.Orientation.Vertical,
                isClosable=True,
                position=qfw.InfoBarPosition.TOP,
                duration=-1,
                parent=self.mw,
            )
            chkbx = qfw.CheckBox("Don't show again for this session")
            chkbx.checkStateChanged.connect(
                lambda check_state: setattr(
                    self, "capacity_exceeded_msg_shown", check_state == QtCore.Qt.CheckState.Checked
                ) # type: ignore
            )
            w.addWidget(chkbx)
            w.show()

    @QtCore.Slot()
    def save_sheet(self) -> None:
        wealth_data, consumables_data = self.mw.wealth_consumables_interface.get_data()
        inventory_data, storage_data = self.mw.item_tables_interface.get_data()

        sheet_data: _t.SheetDataDict = {
            "wealth": wealth_data,
            "consumables": consumables_data,
            "inventory": inventory_data,
            "storage": storage_data,
        }

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.mw,
            "Save Inventory Sheet",
            dir=Config.general.saves_dir,
            filter="JSON Files (*.json)",
        )

        if filename:
            Config.general.saves_dir = Path(filename).parent.as_posix()
            with open(filename, "w") as file:
                try:
                    json.dump(
                        sheet_data,
                        file,
                        indent=4,
                        sort_keys=True,
                    )
                    qfw.InfoBar.success(
                        "Success!",
                        f"Sheet saved to {filename}",
                        duration=3000,
                        parent=self.mw,
                    )
                except Exception as e:
                    qfw.InfoBar.error(
                        "Error!",
                        f"Failed to save sheet: {e}",
                        duration=3000,
                        parent=self.mw,
                    )

    @QtCore.Slot()
    def load_sheet(self) -> None:
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.mw,
            "Open Inventory Sheet",
            dir=Config.general.saves_dir,
            filter="JSON Files (*.json)",
        )

        if filename:
            Config.general.saves_dir = Path(filename).parent.as_posix()
            with open(filename, "r") as file:
                try:
                    data = json.load(file)
                    data_wealth = data.get("wealth", {})
                    data_consumables = data.get("consumables", {})
                    data_inventory = data.get("inventory", [])
                    data_storage = data.get("storage", [])

                    self.mw.wealth_consumables_interface.set_data((data_wealth, data_consumables))
                    self.mw.item_tables_interface.set_data((data_inventory, data_storage))

                    qfw.InfoBar.success(
                        "Success!",
                        f"Sheet {Path(filename).name} loaded successfully",
                        duration=3000,
                        parent=self.mw,
                        position=qfw.InfoBarPosition.TOP,
                    )

                except Exception as e:
                    qfw.InfoBar.error(
                        "Error!",
                        f"Failed to load sheet: {e}",
                        duration=3000,
                        parent=self.mw,
                        position=qfw.InfoBarPosition.TOP,
                    )

    @QtCore.Slot()
    def update_slots_used(self) -> None:
        wealth_consumables = self.mw.wealth_consumables_interface.get_slots_used()
        items = self.mw.item_tables_interface.get_slots_used()

        self.mw.encumbrance_bar.update_encumbrance(wealth_consumables + items)
