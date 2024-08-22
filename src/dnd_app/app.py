import json
import typing as t

from PySide6 import QtCore, QtWidgets

from .config import Config
from .widgets.main_window import MainWindow


class EquipmentManager(QtWidgets.QApplication):
    def __init__(self, sys_argv: t.Sequence[str]) -> None:
        super().__init__(sys_argv)

        self.setOrganizationName("QuackTech")
        self.setApplicationName("DnD5e Equipment Manager")

        self.mw = MainWindow()
        self.mw.ui.action_save.triggered.connect(self.save_sheet)
        self.mw.ui.action_open.triggered.connect(self.load_sheet)

    @QtCore.Slot()
    def save_sheet(self) -> None:
        wealth_data = self.mw.wealth_widget.get_data()
        tracker_data = self.mw.tracker_widget.get_data()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.mw,
            "Save Inventory Sheet",
            dir=Config().internal.OutputDir,
            filter="JSON Files (*.json)",
        )

        if filename:
            with open(filename, "w") as file:
                json.dump(
                    {"wealth": wealth_data, "tracker": tracker_data},
                    file,
                    indent=4,
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
                data = json.load(file)

                self.mw.wealth_widget.set_data(data["wealth"])
                self.mw.tracker_widget.set_data(data["tracker"])
