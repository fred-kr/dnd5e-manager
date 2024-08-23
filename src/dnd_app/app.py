import json
import typing as t
from pathlib import Path

import qfluentwidgets as qfw
from PySide6 import QtCore, QtWidgets

from .config import Config
from .icons import Icons
from .widgets.main_window import MainWindow


class EquipmentManager(QtWidgets.QApplication):
    def __init__(self, sys_argv: t.Sequence[str]) -> None:
        super().__init__(sys_argv)

        self.setOrganizationName("QuackTech")
        self.setApplicationName("DnD5e Equipment Manager")

        self.mw = MainWindow()
        self.mw.addCommand(Icons.FolderOpen.icon(), "Import Sheet", self.load_sheet)
        self.mw.addCommand(Icons.Save.icon(), "Save Sheet", self.save_sheet)
        self.mw.addCommand(Icons.Settings.icon(), "Settings", self.mw.open_preferences)

    @QtCore.Slot()
    def save_sheet(self) -> None:
        wealth_data, consumables_data = self.mw.wealth_consumables_interface.get_data()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.mw,
            "Save Inventory Sheet",
            dir=Config().internal.OutputDir,
            filter="JSON Files (*.json)",
        )

        if filename:
            with open(filename, "w") as file:
                try:
                    json.dump(
                        {"wealth": wealth_data, "consumables": consumables_data},
                        file,
                        indent=4,
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
            dir=Config().internal.OutputDir,
            filter="JSON Files (*.json)",
        )

        if filename:
            with open(filename, "r") as file:
                try:
                    data = json.load(file)
                    data_wealth = data.get("wealth", {})
                    data_consumables = data.get("consumables", {})
                    self.mw.wealth_consumables_interface.set_data((data_wealth, data_consumables))
                    qfw.InfoBar.success(
                        "Success!",
                        f"Sheet {Path(filename).name} loaded successfully",
                        duration=3000,
                        parent=self.mw,
                    )
                except Exception as e:
                    qfw.InfoBar.error(
                        "Error!",
                        f"Failed to load sheet: {e}",
                        duration=3000,
                        parent=self.mw,
                    )
