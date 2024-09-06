import typing as t

from dnd5e_srd_api.models.common import APIReference
from dnd5e_srd_api.type_defs import ResourceIndex
from PySide6 import QtCore

from .. import type_defs as _t


class ResourceIndexModel[T: ResourceIndex](QtCore.QAbstractListModel):
    def __init__(self, reference_items: list[APIReference[T]], parent: QtCore.QObject | None = None) -> None:
        super().__init__(parent)
        self._api_references = sorted(reference_items, key=lambda r: r.name)

    @property
    def ref_items(self) -> list[APIReference[T]]:
        return self._api_references

    def item_from_name(self, name: str) -> APIReference[T] | None:
        return next((r for r in self._api_references if r.name.lower() == name.lower()), None)

    def rowCount(self, parent: _t.ModelIndex | None = None) -> int:
        return len(self._api_references)

    def data(self, index: _t.ModelIndex, role: int = QtCore.Qt.ItemDataRole.DisplayRole) -> t.Any:
        if not index.isValid() or not 0 <= index.row() < len(self._api_references):
            return None

        resource = self._api_references[index.row()]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return resource.name
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return resource
        elif role == QtCore.Qt.ItemDataRole.ToolTipRole:
            return resource.url

        return None
