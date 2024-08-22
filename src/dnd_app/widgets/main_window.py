import qfluentwidgets as qfw
from PySide6 import QtCore, QtGui, QtWidgets

from ...ui.ui_main_window import Ui_EquipmentManager
from ..config import Config
from .tracker_widget import TrackerWidget
from .wealth_widget import WealthWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

        self.ui = Ui_EquipmentManager()
        self.ui.setupUi(self)

        self.config = Config()

        self.wealth_widget = WealthWidget()
        self.tracker_widget = TrackerWidget()

        self.config_window: QtWidgets.QDialog | None = None
        
        self._setup_pages()
        self._connect_qsignals()
        self.read_settings()

    def _connect_qsignals(self) -> None:
        self.ui.action_open_preferences.triggered.connect(self.open_preferences)

    def read_settings(self) -> None:
        self.restoreGeometry(self.config.internal.WindowGeometry)
        self.restoreState(self.config.internal.WindowState)

    @QtCore.Slot(QtGui.QCloseEvent)
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.config.internal.WindowGeometry = self.saveGeometry()
        self.config.internal.WindowState = self.saveState()
        super().closeEvent(event)

    def _setup_pages(self) -> None:
        layout_wealth_consumables = QtWidgets.QGridLayout()
        layout_wealth_consumables.addWidget(
            self.wealth_widget, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop
        )
        layout_wealth_consumables.addWidget(
            self.tracker_widget, 0, 1, 2, 1, QtCore.Qt.AlignmentFlag.AlignTop
        )

        self.ui.tab_wealth_consumables.setLayout(layout_wealth_consumables)

    @QtCore.Slot()
    def refresh_widgets(self) -> None:
        self.tracker_widget.refresh_values()
        self.wealth_widget.refresh_values()

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
        dlg.setStyleSheet("QSpinBox { min-width: 150px; min-height: 31px; } QDoubleSpinBox { min-width: 150px; min-height: 31px; }")
        
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
