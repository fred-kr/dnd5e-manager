import math
import typing as t

import attrs
import numpy as np
from PySide6 import QtCore

from .. import type_defs as _t
from ..config import Config

ItemDataRole = QtCore.Qt.ItemDataRole


@attrs.define
class Item:
    name: str = attrs.field()
    weight: float = attrs.field(default=0.0, converter=lambda x: round(x, 1))
    value: float = attrs.field(default=0.0, converter=lambda x: round(x, 2))
    description: str = attrs.field(default="", converter=str)

    def to_dict(self) -> _t.ItemDict:
        return _t.ItemDict(**attrs.asdict(self))


class ItemTableModel(QtCore.QAbstractTableModel):
    def __init__(
        self, items: list[Item] | None = None, parent: QtCore.QObject | None = None
    ) -> None:
        super().__init__(parent)
        self._items = items or []
        self._header = ("Name", "Value (gp)", "Weight (lbs)")

    @property
    def items(self) -> list[Item]:
        return self._items

    def rowCount(self, parent: _t.ModelIndex | None = None) -> int:
        return len(self._items)

    def columnCount(self, parent: _t.ModelIndex | None = None) -> int:
        return 3

    def data(self, index: _t.ModelIndex, role: int = ItemDataRole.DisplayRole) -> t.Any:
        if not index.isValid():
            return None

        row, column = index.row(), index.column()
        item = self._items[row]
        display = {
            0: item.name,
            1: np.format_float_positional(
                item.value, precision=2, trim="0", fractional=True
            ),
            2: np.format_float_positional(
                item.weight, precision=1, trim="0", fractional=True
            )
            if item.weight != 0
            else "--",
        }
        edit = {0: item.name, 1: item.value, 2: item.weight}
        if role == ItemDataRole.DisplayRole:
            return display.get(column)
        elif role == ItemDataRole.EditRole:
            return edit.get(column)
        elif role == ItemDataRole.ToolTipRole:
            return item.description
        return None

    def headerData(
        self,
        section: int,
        orientation: QtCore.Qt.Orientation,
        role: int = ItemDataRole.DisplayRole,
    ) -> t.Any:
        if role != ItemDataRole.DisplayRole:
            return None
        if orientation == QtCore.Qt.Orientation.Horizontal:
            return self._header[section]
        else:
            return f"{section + 1}"

    def flags(self, index: _t.ModelIndex) -> QtCore.Qt.ItemFlag:
        if not index.isValid():
            return QtCore.Qt.ItemFlag.NoItemFlags
        flags = super().flags(index)
        if 0 <= index.column() < self.columnCount():
            flags |= QtCore.Qt.ItemFlag.ItemIsEditable
        return flags

    def setData(
        self, index: _t.ModelIndex, value: t.Any, role: int = ItemDataRole.EditRole
    ) -> bool:
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
        column_map = {0: "name", 1: "value", 2: "weight"}
        if (
            not self._items
            or column not in column_map
            or not 0 <= column < self.columnCount()
        ):
            return

        attr = column_map[column]
        self.layoutAboutToBeChanged.emit()
        self._items.sort(
            key=lambda item: getattr(item, attr),
            reverse=order == QtCore.Qt.SortOrder.DescendingOrder,
        )
        self.layoutChanged.emit()

    @QtCore.Slot(QtCore.QModelIndex)
    def remove_item(self, index: QtCore.QModelIndex) -> None:
        if not index.isValid() or index.row() >= len(self._items):
            return
        self.beginRemoveRows(index.parent(), index.row(), index.row())
        del self._items[index.row()]
        self.endRemoveRows()

    @QtCore.Slot()
    def add_item(self) -> None:
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(Item(name="New Item"))
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
        return math.ceil(self.total_weight() / Config().armor.PoundsPerSlot)
