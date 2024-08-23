import typing as t

import qfluentwidgets as qfw
from PySide6 import QtCore, QtGui, QtWidgets

from ..config import Config
from ..icons import Icons
from ..interfaces.item_tables import ItemTablesWidget
from ..interfaces.wealth_consumables import WealthConsumablesInterface


class MainWindow(qfw.MSFluentWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        

        self.wealth_consumables_interface = WealthConsumablesInterface()
        self.item_tables_interface = ItemTablesWidget()

        self.info_interface = QtWidgets.QWidget()
        self.info_interface.setObjectName("info_interface")
        self.info_interface.setContentsMargins(0, 0, 0, 0)

        self.config = Config()

        self.config_window: QtWidgets.QDialog | None = None
        self._init_navigation()
        self._init_window()
        self.read_settings()

    def read_settings(self) -> None:
        self.restoreGeometry(self.config.internal.WindowGeometry)

    @QtCore.Slot(QtGui.QCloseEvent)
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.config.internal.WindowGeometry = self.saveGeometry()
        super().closeEvent(event)

    def _init_navigation(self) -> None:
        self.addSubInterface(self.wealth_consumables_interface, Icons.Home.icon(), "Home")
        self.addSubInterface(self.item_tables_interface, Icons.Library.icon(), "Items")
        self.addSubInterface(self.info_interface, Icons.Info.icon(), "Info")

    def _init_window(self) -> None:
        self.setWindowTitle("DnD5e Equipment Manager")
        self.setWindowIcon(Icons.Backpack.icon())
        self.command_bar = qfw.CommandBar(self)
        self.command_bar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        vBoxLayout = QtWidgets.QVBoxLayout()
        vBoxLayout.setContentsMargins(0, 0, 0, 0)
        vBoxLayout.setSpacing(0)
        vBoxLayout.addWidget(self.command_bar)
        vBoxLayout.addWidget(self.stackedWidget.view)

        self.stackedWidget.hBoxLayout.addLayout(vBoxLayout)
        

    def addCommand(
        self, icon: qfw.FluentIconBase | QtGui.QIcon | str, text: str, slot: QtCore.Slot | t.Callable[..., None]
    ) -> None:
        action = qfw.Action(icon, text, self)
        action.triggered.connect(slot)
        self.command_bar.addAction(action)

    def refresh_widgets(self) -> None:
        self.wealth_consumables_interface.refresh_values()
        self.item_tables_interface.refresh_values()

    @QtCore.Slot()
    def reset_config(self) -> None:
        self.config.reset()
        self.refresh_widgets()
        self.open_preferences()

    @QtCore.Slot()
    def open_preferences(self) -> None:
        if self.config_window:
            self.config_window.close()

        config_window = self.config.create_editor_window()

        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle("Preferences")
        dlg.setWindowIcon(Icons.Settings.icon())
        dlg.setStyleSheet(
            "QSpinBox { min-width: 150px; min-height: 31px; } QDoubleSpinBox { min-width: 150px; min-height: 31px; }"
        )

        btn_reset = qfw.PushButton("Restore Defaults")
        btn_reset.clicked.connect(self.reset_config)

        btn_done = qfw.PushButton("Done")
        btn_done.clicked.connect(dlg.close)

        btn_box_layout = QtWidgets.QHBoxLayout()
        btn_box_layout.addStretch()
        btn_box_layout.addWidget(btn_reset)
        btn_box_layout.addWidget(btn_done)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(config_window)
        layout.addLayout(btn_box_layout)

        dlg.setLayout(layout)

        dlg.finished.connect(self.refresh_widgets)
        self.config_window = dlg
        dlg.open()
