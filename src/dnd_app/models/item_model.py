import math
import typing as t

import attrs
from PySide6 import QtCore

from .. import type_defs as _t
from ..config import Config

ItemDataRole = QtCore.Qt.ItemDataRole


@attrs.define
class Item:
    name: str = attrs.field()
    weight: float = attrs.field(default=0.0, converter=lambda x: round(x, 1))
    value: float = attrs.field(default=0.0, converter=lambda x: round(x, 2))
    description: str = attrs.field(default="")

    def to_dict(self) -> _t.ItemDict:
        return _t.ItemDict(**attrs.asdict(self))

    @classmethod
    def from_dict(cls, data: _t.ItemDict) -> "Item":
        return cls(**data)

    @property
    def slots(self) -> int:
        return math.ceil(self.weight / Config().armor.PoundsPerSlot)


class ItemTableModel(QtCore.QAbstractTableModel):
    def __init__(self, items: list[Item] | None = None, parent: QtCore.QObject | None = None) -> None:
        super().__init__(parent)
        self._items = items or []
        self._header = ("Name", "Value (gp)", "Weight (lbs)", "Slots")

    @property
    def items(self) -> list[Item]:
        return self._items

    def set_items(self, items: list[Item]) -> None:
        self.beginResetModel()
        self._items = items
        self.endResetModel()

    def rowCount(self, parent: _t.ModelIndex | None = None) -> int:
        return len(self._items)

    def columnCount(self, parent: _t.ModelIndex | None = None) -> int:
        return len(self._header)

    def data(self, index: _t.ModelIndex, role: int = ItemDataRole.DisplayRole) -> t.Any:
        if not index.isValid() or not 0 <= index.row() < len(self._items):
            return None

        row, column = index.row(), index.column()
        item = self._items[row]
        if role == ItemDataRole.DisplayRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.value
            elif column == 2:
                return item.weight if item.weight != 0 else "--"
            elif column == 3:
                return item.slots
        elif role == ItemDataRole.EditRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.value
            elif column == 2:
                return item.weight
        elif role == ItemDataRole.UserRole:
            return item
        elif role == ItemDataRole.ToolTipRole:
            return item.description
        return None

    def headerData(
        self,
        section: int,
        orientation: QtCore.Qt.Orientation,
        role: int = ItemDataRole.DisplayRole,
    ) -> t.Any:
        if role == ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self._header[section]
        return None

    def flags(self, index: _t.ModelIndex) -> QtCore.Qt.ItemFlag:
        if not index.isValid():
            return QtCore.Qt.ItemFlag.NoItemFlags
        flags = super().flags(index)
        if 0 <= index.column() < 3:
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
            if not value:
                value = 0.0
            try:
                value = float(value)
            except ValueError:
                return False
            item.value = value
        elif column == 2:
            if not value:
                value = 0.0
            try:
                value = float(value)
            except ValueError:
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
        # column_map = {0: "name", 1: "value", 2: "weight", 3: "slots"}
        if not self._items or not 0 <= column < self.columnCount():
            return

        if column == 0:
            attr = "name"
        elif column == 1:
            attr = "value"
        elif column == 2:
            attr = "weight"
        elif column == 3:
            attr = "slots"
        else:
            return

        self.layoutAboutToBeChanged.emit()
        self._items.sort(
            key=lambda item: getattr(item, attr),
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
        return item

    @QtCore.Slot()
    def add_item(self, item: Item | None = None) -> None:
        if item is None:
            item = Item(name="New Item")
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(item)
        self.endInsertRows()

    def insert_item(self, item: Item, row: int) -> None:
        self.beginInsertRows(QtCore.QModelIndex(), row, row)
        self._items.insert(row, item)
        self.endInsertRows()

    @QtCore.Slot()
    def clear(self) -> None:
        self.beginResetModel()
        self._items.clear()
        self.endResetModel()

    def total_weight(self) -> float:
        return sum(item.weight for item in self._items)

    def total_value(self) -> float:
        return sum(item.value for item in self._items)

    def total_slots(self) -> int:
        return sum(item.slots for item in self._items)
