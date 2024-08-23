import qfluentwidgets as qfw
from PySide6 import QtWidgets

from ...ui.ui_item_tables import Ui_ItemTables


class ItemTablesWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("item_tables_widget")

        self.ui = Ui_ItemTables()
        self.ui.setupUi(self)

    @property
    def tables(self) -> list[qfw.TableView]:
        return [self.ui.table_view_inventory, self.ui.table_view_storage]

    @property
    def command_bars(self) -> list[qfw.CommandBar]:
        return [self.ui.command_bar_inventory, self.ui.command_bar_storage]
