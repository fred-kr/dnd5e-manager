import typing as t

import qfluentwidgets as qfw
from PySide6 import QtCore, QtGui, QtWidgets
from pyside_config import config

from ..app_config import Config
from ..icons import Icons
# from ..interfaces.info_wiki import InfoWidget
from ..interfaces.item_tables import ItemTablesWidget
from ..interfaces.wealth_consumables import WealthConsumablesInterface
from .encumbrance_bar import EncumbranceBar


class MainWindow(qfw.MSFluentWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.wealth_consumables_interface = WealthConsumablesInterface()
        self.item_tables_interface = ItemTablesWidget()
        # self.info_interface = InfoWidget()

        # self.config_window: QtWidgets.QDialog | None = None
        self._init_navigation()
        self._init_window()
        self.read_settings()

    def read_settings(self) -> None:
        self.restoreGeometry(Config.internal.window_geometry)

    @QtCore.Slot(QtGui.QCloseEvent)
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        Config.internal.window_geometry = self.saveGeometry()
        super().closeEvent(event)

    def _init_navigation(self) -> None:
        self.addSubInterface(self.wealth_consumables_interface, Icons.Home.icon(), "Home")
        self.addSubInterface(self.item_tables_interface, Icons.Library.icon(), "Items")
        # self.addSubInterface(self.info_interface, Icons.Info.icon(), "Info")

    def _init_window(self) -> None:
        self.setWindowTitle("DnD5e Equipment Manager")
        self.setWindowIcon(Icons.Backpack.icon())
        self.command_bar = qfw.CommandBar(self)
        self.command_bar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        layout_cb_encumbrance = QtWidgets.QHBoxLayout()
        self.encumbrance_bar = EncumbranceBar(self)
        layout_cb_encumbrance.addWidget(self.command_bar)
        layout_cb_encumbrance.addWidget(self.encumbrance_bar)

        vBoxLayout = QtWidgets.QVBoxLayout()
        vBoxLayout.setContentsMargins(0, 0, 0, 0)
        vBoxLayout.setSpacing(0)
        vBoxLayout.addLayout(layout_cb_encumbrance)
        vBoxLayout.addWidget(self.stackedWidget.view)

        self.stackedWidget.hBoxLayout.addLayout(vBoxLayout)

    def addCommand(
        self,
        icon: qfw.FluentIconBase | QtGui.QIcon | str,
        text: str,
        slot: QtCore.Slot | t.Callable[..., None],
        hidden: bool = False,
    ) -> None:
        action = qfw.Action(icon, text, self)
        action.triggered.connect(slot)
        if hidden:
            self.command_bar.addHiddenAction(action)
        else:
            self.command_bar.addAction(action)

    def refresh_widgets(self) -> None:
        self.wealth_consumables_interface.refresh_values()
        self.item_tables_interface.refresh_values()

    @QtCore.Slot()
    def reset_config(self) -> None:
        config.clean()
        self.refresh_widgets()
        self.open_preferences()

    @QtCore.Slot()
    def open_preferences(self) -> None:
        config_window = config.create_editor(self, include=["General", "AmountPerSlot", "Database"])
        config_window.setWindowTitle("Preferences")
        config_window.setWindowIcon(Icons.Settings.icon())
        config_window.setStyleSheet(
            "QSpinBox { min-width: 150px; min-height: 31px; }"
            "QDoubleSpinBox { min-width: 150px; min-height: 31px; }"
            "EnumComboBox { min-width: 150px; min-height: 31px; padding-left: 10px; }"
            "EnumComboBox QAbstractItemView::item { min-height: 31px; }"
            "QLineEdit { min-width: 150px; min-height: 31px; padding-left: 10px; }"
        )
        config_window.finished.connect(self.refresh_widgets)
        config_window.open()

        # dlg = QtWidgets.QDialog(self)

        # btn_reset = qfw.PushButton("Restore Defaults")
        # btn_reset.clicked.connect(self.reset_config)

        # btn_done = qfw.PushButton("Done")
        # btn_done.clicked.connect(dlg.close)

        # btn_box_layout = QtWidgets.QHBoxLayout()
        # btn_box_layout.addStretch()
        # btn_box_layout.addWidget(btn_reset)
        # btn_box_layout.addWidget(btn_done)

        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(config_window)
        # layout.addLayout(btn_box_layout)

        # dlg.setLayout(layout)

        # dlg.finished.connect(self.refresh_widgets)
        # self.config_window = dlg
        # dlg.open()
