from PySide6 import QtWidgets

from ...ui.ui_info_page import Ui_Info


class InfoWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("info_widget")

        self.ui = Ui_Info()
        self.ui.setupUi(self)
