import qfluentwidgets as qfw
from PySide6 import QtCore, QtWidgets

from ...ui.ui_item_tables import Ui_ItemTables
from .. import type_defs as _t
from ..icons import Icons
from ..models.item_model import Item, ItemTableModel

ItemDataRole = QtCore.Qt.ItemDataRole


class ItemTableDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)

    def createEditor(
        self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: _t.ModelIndex
    ) -> QtWidgets.QWidget:
        initial_value = index.model().data(index, ItemDataRole.EditRole)

        if isinstance(initial_value, float):
            editor = QtWidgets.QDoubleSpinBox(parent)
            editor.setRange(0, 100_000)
            editor.setFrame(False)
        elif isinstance(initial_value, int):
            editor = QtWidgets.QSpinBox(parent)
            editor.setRange(0, 100_000)
            editor.setFrame(False)
        elif isinstance(initial_value, str):
            editor = QtWidgets.QLineEdit(parent)
            editor.setFrame(False)
            editor.setClearButtonEnabled(True)
        else:
            editor = super().createEditor(parent, option, index)

        return editor

    def setEditorData(self, editor: QtWidgets.QWidget, index: _t.ModelIndex) -> None:
        value = index.model().data(index, ItemDataRole.EditRole)
        if isinstance(editor, QtWidgets.QLineEdit):
            editor.setText(value)
        elif isinstance(editor, (QtWidgets.QDoubleSpinBox, QtWidgets.QSpinBox)):
            editor.setValue(value)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel, index: _t.ModelIndex) -> None:
        if isinstance(editor, QtWidgets.QLineEdit):
            model.setData(index, editor.text(), ItemDataRole.EditRole)
        elif isinstance(editor, (QtWidgets.QDoubleSpinBox, QtWidgets.QSpinBox)):
            model.setData(index, editor.value(), ItemDataRole.EditRole)
        else:
            super().setModelData(editor, model, index)

    def updateEditorGeometry(
        self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: _t.ModelIndex
    ) -> None:
        editor.setGeometry(option.rect)


class ItemTablesWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("item_tables_widget")

        self.ui = Ui_ItemTables()
        self.ui.setupUi(self)
        self.ui.table_view_inventory.setItemDelegate(ItemTableDelegate(self.ui.table_view_inventory))
        self.ui.table_view_storage.setItemDelegate(ItemTableDelegate(self.ui.table_view_storage))

        self.inventory_model = ItemTableModel()
        self.storage_model = ItemTableModel()

        self._setup_tables()
        self._setup_actions()
        self._setup_command_bars()

    @property
    def tables(self) -> list[QtWidgets.QTableView]:
        return [self.ui.table_view_inventory, self.ui.table_view_storage]

    @property
    def command_bars(self) -> list[qfw.CommandBar]:
        return [self.ui.command_bar_inventory, self.ui.command_bar_storage]

    def _setup_tables(self) -> None:
        for table in self.tables:
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            table.horizontalHeader().setDefaultAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter
            )

        self.ui.table_view_inventory.setModel(self.inventory_model)
        self.ui.table_view_storage.setModel(self.storage_model)

    def _setup_actions(self) -> None:
        self.action_add_inventory_item = qfw.Action(Icons.New.icon(), "New Item", self)
        self.action_add_inventory_item.triggered.connect(lambda: self.inventory_model.add_item())

        self.action_remove_inventory_item = qfw.Action(Icons.Delete.icon(), "Remove Item", self)
        self.action_remove_inventory_item.triggered.connect(
            lambda: self.inventory_model.remove_item(self.ui.table_view_inventory.currentIndex())
        )

        self.action_clear_inventory = qfw.Action(Icons.Broom.icon(), "Clear All", self)
        self.action_clear_inventory.triggered.connect(self.inventory_model.clear)

        self.action_move_to_storage = qfw.Action(Icons.ArrowRight.icon(), "Move to Storage", self)
        self.action_move_to_storage.triggered.connect(self.move_to_storage)

        self.action_edit_inventory_item = qfw.Action(Icons.CircleEdit.icon(), "Edit Details", self)
        self.action_edit_inventory_item.triggered.connect(self.edit_inventory_item)

        self.action_add_storage_item = qfw.Action(Icons.New.icon(), "New Item", self)
        self.action_add_storage_item.triggered.connect(lambda: self.storage_model.add_item())

        self.action_remove_storage_item = qfw.Action(Icons.Delete.icon(), "Remove Item", self)
        self.action_remove_storage_item.triggered.connect(
            lambda: self.storage_model.remove_item(self.ui.table_view_storage.currentIndex())
        )

        self.action_clear_storage = qfw.Action(Icons.Broom.icon(), "Clear All", self)
        self.action_clear_storage.triggered.connect(self.storage_model.clear)

        self.action_move_to_inventory = qfw.Action(Icons.ArrowLeft.icon(), "Move to Inventory", self)
        self.action_move_to_inventory.triggered.connect(self.move_to_inventory)

        self.action_edit_storage_item = qfw.Action(Icons.CircleEdit.icon(), "Edit Details", self)
        self.action_edit_storage_item.triggered.connect(self.edit_storage_item)

    def _setup_command_bars(self) -> None:
        for cb in self.command_bars:
            cb.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.ui.command_bar_inventory.addActions(
            [
                self.action_add_inventory_item,
                self.action_remove_inventory_item,
                self.action_clear_inventory,
                self.action_move_to_storage,
            ]
        )
        self.ui.command_bar_storage.addActions(
            [
                self.action_add_storage_item,
                self.action_remove_storage_item,
                self.action_clear_storage,
                self.action_move_to_inventory,
            ]
        )

    def refresh_values(self) -> None:
        self.inventory_model.layoutChanged.emit()
        self.storage_model.layoutChanged.emit()

    def get_data(self) -> tuple[list[_t.ItemDict], list[_t.ItemDict]]:
        inventory_data = [item.to_dict() for item in self.inventory_model.items]
        storage_data = [item.to_dict() for item in self.storage_model.items]
        return inventory_data, storage_data

    def set_data(self, data: tuple[list[_t.ItemDict], list[_t.ItemDict]]) -> None:
        inventory_data, storage_data = data
        inventory_items = [Item.from_dict(inv_item) for inv_item in inventory_data]
        storage_items = [Item.from_dict(stor_item) for stor_item in storage_data]
        self.inventory_model.set_items(inventory_items)
        self.storage_model.set_items(storage_items)

    @QtCore.Slot()
    def move_to_storage(self) -> None:
        selected_index = self.ui.table_view_inventory.currentIndex()
        if item := self.inventory_model.remove_item(selected_index):
            self.storage_model.add_item(item)

    @QtCore.Slot()
    def move_to_inventory(self) -> None:
        selected_index = self.ui.table_view_storage.currentIndex()
        if item := self.storage_model.remove_item(selected_index):
            self.inventory_model.add_item(item)

    @QtCore.Slot()
    def edit_inventory_item(self) -> None:
        selected_index = self.ui.table_view_inventory.currentIndex()
        item = self.inventory_model.data(selected_index, ItemDataRole.UserRole)
        new_description, ok = QtWidgets.QInputDialog.getText(
            self, "Edit Item", "Enter a new description:", text=item.description
        )
        if ok:
            item.description = new_description
            self.inventory_model.layoutChanged.emit()

    @QtCore.Slot()
    def edit_storage_item(self) -> None:
        selected_index = self.ui.table_view_storage.currentIndex()
        item = self.storage_model.data(selected_index, ItemDataRole.UserRole)
        new_description, ok = QtWidgets.QInputDialog.getText(
            self, "Edit Item", "Enter a new description:", text=item.description
        )
        if ok:
            item.description = new_description
            self.storage_model.layoutChanged.emit()
