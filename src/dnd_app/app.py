import json
import typing as t
from pathlib import Path

import qfluentwidgets as qfw
import requests
from packaging import version
from PySide6 import QtCore, QtWidgets

from .config import Config
from .icons import Icons
from .widgets.main_window import MainWindow

APP_NAME = "DnD5e Equipment Manager"
VERSION = "v0.2.0-alpha"
GITHUB_REPO = "fred-kr/dnd-app"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"


class Updater(QtCore.QObject):
    sig_update_available = QtCore.Signal(str, str)
    sig_update_progress = QtCore.Signal(int)
    sig_update_done = QtCore.Signal()

    def check_for_update(self) -> None:
        try:
            response = requests.get(GITHUB_API_URL)
            response.raise_for_status()
            release_info = json.loads(response.text)
            latest_version = release_info["tag_name"].lstrip("v")

            if version.parse(latest_version) > version.parse(VERSION):
                download_url = release_info["assets"][0]["browser_download_url"]

                self.sig_update_available.emit(latest_version, download_url)
            else:
                print("No update available")

        except Exception as e:
            print(f"Error checking for update: {e}")

    def download_and_install_update(self, download_url: str) -> None:
        try:
            response = requests.get(download_url, stream=True)
            response.raise_for_status()
            total_size = int(response.headers.get("content-length", 0))
            block_size = 1024  # 1 KB
            downloaded = 0

            update_file = f"{APP_NAME}_update.exe"
            with open(update_file, "wb") as file:
                for data in response.iter_content(block_size):
                    size = file.write(data)
                    downloaded += size
                    progress = int((downloaded / total_size) * 100)

                    self.sig_update_progress.emit(progress)
            # Here you would typically close your app and run the updater
            # For demonstration, we'll just print a message
            print(f"Update downloaded to {update_file}. Please run it to complete the update.")
            self.sig_update_done.emit()
        except Exception as e:
            print(f"Error downloading update: {e}")


class EquipmentManager(QtWidgets.QApplication):
    def __init__(self, sys_argv: t.Sequence[str]) -> None:
        super().__init__(sys_argv)

        self.setOrganizationName("QuackTech")
        self.setApplicationName("DnD5e Equipment Manager")

        self.mw = MainWindow()
        self._setup_command_bar()
        self.mw.setWindowTitle(f"{APP_NAME} {VERSION}")
        self.updater = Updater()
        self.updater.sig_update_available.connect(self.prompt_update)
        self.updater.sig_update_progress.connect(self.update_progress_dialog)
        self.updater.sig_update_done.connect(self.update_complete)
        self.check_for_update()

    def _setup_command_bar(self) -> None:
        self.mw.addCommand(Icons.FolderOpen.icon(), "Import Sheet", self.load_sheet)
        self.mw.addCommand(Icons.Save.icon(), "Save Sheet", self.save_sheet)
        self.mw.addCommand(Icons.Settings.icon(), "Settings", self.mw.open_preferences)

    def check_for_update(self) -> None:
        update_thread = QtCore.QThread()
        self.updater.moveToThread(update_thread)
        update_thread.started.connect(self.updater.check_for_update)
        update_thread.start()

    @QtCore.Slot(str, str)
    def prompt_update(self, new_version: str, download_url: str) -> None:
        reply = QtWidgets.QMessageBox.question(
            self.mw,
            "Update Available",
            f"A new version ({new_version}) of {APP_NAME} is available. Do you want to download it now?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            self.start_update(download_url)

    def start_update(self, download_url: str) -> None:
        self.progress_dialog = QtWidgets.QProgressDialog("Downloading update...", "Cancel", 0, 100, self.mw)
        self.progress_dialog.setWindowTitle("Updating")
        self.progress_dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.progress_dialog.show()

        update_thread = QtCore.QThread()
        self.updater.moveToThread(update_thread)
        update_thread.started.connect(lambda: self.updater.download_and_install_update(download_url))
        update_thread.start()

    @QtCore.Slot(int)
    def update_progress_dialog(self, progress: int) -> None:
        self.progress_dialog.setValue(progress)

    @QtCore.Slot()
    def update_complete(self) -> None:
        self.progress_dialog.close()
        QtWidgets.QMessageBox.information(
            self.mw,
            "Update Complete",
            f"{APP_NAME} has been updated. Please restart the application to complete the update.",
        )

    @QtCore.Slot()
    def save_sheet(self) -> None:
        wealth_data, consumables_data = self.mw.wealth_consumables_interface.get_data()
        inventory_data, storage_data = self.mw.item_tables_interface.get_data()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.mw,
            "Save Inventory Sheet",
            dir=Config().internal.OutputDir,
            filter="JSON Files (*.json)",
        )

        if filename:
            Config().internal.OutputDir = Path(filename).parent.as_posix()
            with open(filename, "w") as file:
                try:
                    json.dump(
                        {
                            "wealth": wealth_data,
                            "consumables": consumables_data,
                            "inventory": inventory_data,
                            "storage": storage_data,
                        },
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
            Config().internal.OutputDir = Path(filename).parent.as_posix()
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
                    )
                except Exception as e:
                    qfw.InfoBar.error(
                        "Error!",
                        f"Failed to load sheet: {e}",
                        duration=3000,
                        parent=self.mw,
                    )
