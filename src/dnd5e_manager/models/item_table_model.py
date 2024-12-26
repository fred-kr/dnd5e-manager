import decimal
import typing as t

from PySide6 import QtCore

from .. import type_defs as _t
from ..app_config import Config
from ..enum_defs import CurrencyType
from .equipment import Cost, Item

ItemDataRole = QtCore.Qt.ItemDataRole
D = decimal.Decimal


class ItemTableModel(QtCore.QAbstractTableModel):
    def __init__(self, items: list[Item] | None = None, parent: QtCore.QObject | None = None) -> None:
        super().__init__(parent)
        self._items = items or []
        self._display_currency = CurrencyType.GOLD

    @property
    def items(self) -> list[Item]:
        return self._items

    @property
    def table_header(self) -> tuple[str, str, str, str]:
        return ("Name", "Category", f"Cost ({self._display_currency})", f"Weight ({Config.general.weight_display_format})")

    def set_display_currency(self, currency: CurrencyType) -> None:
        self._display_currency = currency
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def set_items(self, items: list[Item]) -> None:
        self.beginResetModel()
        self._items = items
        self.endResetModel()

        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def rowCount(self, parent: _t.ModelIndex | None = None) -> int:
        return len(self._items)

    def columnCount(self, parent: _t.ModelIndex | None = None) -> int:
        return 4

    def data(self, index: _t.ModelIndex, role: int = ItemDataRole.DisplayRole) -> t.Any:
        if not index.isValid() or not 0 <= index.row() < len(self._items):
            return None

        row, column = index.row(), index.column()
        item = self._items[row]
        if role == ItemDataRole.DisplayRole:
            if column == 0:  # name
                return item.name
            elif column == 1:  # category
                return item.category
            elif column == 2:  # cost
                return str(item.cost.to_currency(self._display_currency))
            elif column == 3:  # weight
                return str(item.weight)
        elif role == ItemDataRole.EditRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.category
            elif column == 2:
                return item.cost.to_currency(self._display_currency)
            elif column == 3:
                return item.weight
        elif role == ItemDataRole.UserRole:
            return item
        elif role == ItemDataRole.ToolTipRole:
            return str(item.cost.converted_values) if column == 2 else item.description
        return None

    def headerData(
        self,
        section: int,
        orientation: QtCore.Qt.Orientation,
        role: int = ItemDataRole.DisplayRole,
    ) -> t.Any:
        if role == ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.table_header[section]
        return None

    def flags(self, index: _t.ModelIndex) -> QtCore.Qt.ItemFlag:
        if not index.isValid():
            return QtCore.Qt.ItemFlag.NoItemFlags
        flags = super().flags(index)
        if 0 <= index.column() < self.columnCount():
            flags |= QtCore.Qt.ItemFlag.ItemIsEditable
        return flags

    def setData(self, index: _t.ModelIndex, value: t.Any, role: int = ItemDataRole.EditRole) -> bool:
        if not index.isValid() or role != ItemDataRole.EditRole:
            return False

        row, column = index.row(), index.column()
        item = self._items[row]
        if column == 0:
            item.name = value
        elif column == 1:
            item.category = value
        elif column == 2:
            if not value:
                value = D(0.00)
            try:
                value = D(value)
            except decimal.InvalidOperation:
                return False
            item.cost = Cost.from_currency(self._display_currency, value)
        elif column == 3:
            if not value:
                value = D(0.0)
            try:
                value = D(value)
            except decimal.InvalidOperation:
                return False
            item.weight = value
        else:
            return False

        self.dataChanged.emit(index, index)
        return True

    def sort(
        self,
        column: int,
        order: QtCore.Qt.SortOrder = QtCore.Qt.SortOrder.AscendingOrder,
    ) -> None:
        if not self._items or not 0 <= column < self.columnCount():
            return

        if column == 0:
            attr_name = "name"
        elif column == 1:
            attr_name = "category"
        elif column == 2:
            attr_name = "cost"
        elif column == 3:
            attr_name = "weight"
        else:
            return

        self.layoutAboutToBeChanged.emit()
        self._items.sort(
            key=lambda item: getattr(item, attr_name),
            reverse=order == QtCore.Qt.SortOrder.DescendingOrder,
        )
        self.layoutChanged.emit()

    @QtCore.Slot(QtCore.QModelIndex)
    def remove_item(self, index: QtCore.QModelIndex) -> Item | None:
        if not index.isValid() or index.row() >= len(self._items):
            return
        self.beginRemoveRows(index.parent(), index.row(), index.row())
        item = self._items.pop(index.row())
        self.endRemoveRows()
        self.dataChanged.emit(index, index)
        return item

    @QtCore.Slot()
    def add_item(self, item: Item | None = None) -> None:
        if item is None:
            item = Item(name="New Item")
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(item)
        self.endInsertRows()
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    def insert_item(self, item: Item, row: int) -> None:
        self.beginInsertRows(QtCore.QModelIndex(), row, row)
        self._items.insert(row, item)
        self.endInsertRows()
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())

    @QtCore.Slot()
    def clear(self) -> None:
        self.beginResetModel()
        self._items.clear()
        self.endResetModel()
        self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
