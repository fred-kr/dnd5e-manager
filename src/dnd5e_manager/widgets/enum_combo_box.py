import enum
import typing as t

from PySide6 import QtCore,QtWidgets

from ..models.enum_combo_box_model import EnumModel


class EnumComboBox(QtWidgets.QComboBox):
    sig_current_enum_changed = QtCore.Signal(enum.Enum)
    
    def __init__(self, enum_class: t.Type[enum.Enum] | None = None, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self._enum_class = enum_class
        self.setModel(EnumModel(enum_class))
        self.currentTextChanged.connect(self.emit_current_enum_changed)

    def set_enum_class(self, enum_class: t.Type[enum.Enum] | None) -> None:
        self._enum_class = enum_class
        self.setModel(EnumModel(enum_class))
        
    def current_enum(self) -> enum.Enum:
        if self._enum_class is None:
            raise ValueError("No enum class set")
        return self._enum_class(self.currentData())

    def set_current_enum(self, value: enum.Enum) -> None:
        self.setCurrentText(str(value))

    def emit_current_enum_changed(self, value: str) -> None:
        self.sig_current_enum_changed.emit(self.current_enum())