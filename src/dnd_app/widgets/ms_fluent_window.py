from ctypes.wintypes import MSG

import qfluentwidgets as qfw
import win32con
from PySide6 import QtCore, QtGui, QtWidgets
from qframelesswindow import AcrylicWindow
from qframelesswindow.titlebar.title_bar_buttons import TitleBarButtonState


class FramelessWindow(AcrylicWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.windowEffect.setMicaEffect(self.winId())

    def nativeEvent(self, eventType: QtCore.QByteArray, message: int) -> tuple[bool, int]:
        """Handle the Windows message"""
        msg = MSG.from_address(message.__int__())
        if not msg.hWnd:
            return super().nativeEvent(eventType, message)

        if msg.message == win32con.WM_NCHITTEST and self._isResizeEnabled:
            if self._isHoverMaxBtn():
                self.titleBar.maxBtn.setState(TitleBarButtonState.HOVER)
                return True, win32con.HTMAXBUTTON

        elif msg.message in [0x2A2, win32con.WM_MOUSELEAVE]:
            self.titleBar.maxBtn.setState(TitleBarButtonState.NORMAL)
        elif msg.message in [win32con.WM_NCLBUTTONDOWN, win32con.WM_NCLBUTTONDBLCLK] and self._isHoverMaxBtn():
            e = QtGui.QMouseEvent(
                QtCore.QEvent.Type.MouseButtonPress,
                QtCore.QPoint(),
                QtCore.Qt.MouseButton.LeftButton,
                QtCore.Qt.MouseButton.LeftButton,
                QtCore.Qt.KeyboardModifier.NoModifier,
            )
            QtWidgets.QApplication.sendEvent(self.titleBar.maxBtn, e)
            return True, 0
        elif msg.message in [win32con.WM_NCLBUTTONUP, win32con.WM_NCRBUTTONUP] and self._isHoverMaxBtn():
            e = QtGui.QMouseEvent(
                QtCore.QEvent.Type.MouseButtonRelease,
                QtCore.QPoint(),
                QtCore.Qt.MouseButton.LeftButton,
                QtCore.Qt.MouseButton.LeftButton,
                QtCore.Qt.KeyboardModifier.NoModifier,
            )
            QtWidgets.QApplication.sendEvent(self.titleBar.maxBtn, e)

        return super().nativeEvent(eventType, message)

    def _isHoverMaxBtn(self) -> bool:
        pos = QtGui.QCursor.pos() - self.geometry().topLeft() - self.titleBar.pos()
        return self.titleBar.childAt(pos) is self.titleBar.maxBtn


class StackedWidget(QtWidgets.QFrame):
    currentChanged = QtCore.Signal(int)

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.hBoxLayout = QtWidgets.QHBoxLayout(self)
        self.commandBar = qfw.CommandBar(self)
        self.commandBar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.view = QtWidgets.QStackedWidget(self)
        self.vBoxLayout = QtWidgets.QVBoxLayout()
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.commandBar)
        self.vBoxLayout.addWidget(self.view)

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.view.currentChanged.connect(self.currentChanged)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground)

    def addWidget(self, widget: QtWidgets.QWidget) -> None:
        self.view.addWidget(widget)

    def widget(self, index: int) -> QtWidgets.QWidget:
        return self.view.widget(index)

    def setCurrentWidget(self, widget: QtWidgets.QWidget) -> None:
        if isinstance(widget, QtWidgets.QAbstractScrollArea):
            widget.verticalScrollBar().setValue(0)

        self.view.setCurrentWidget(widget)

    def setCurrentIndex(self, index: int) -> None:
        self.setCurrentWidget(self.view.widget(index))

    def currentIndex(self) -> int:
        return self.view.currentIndex()

    def currentWidget(self) -> QtWidgets.QWidget:
        return self.view.currentWidget()

    def indexOf(self, widget: QtWidgets.QWidget) -> int:
        return self.view.indexOf(widget)

    def count(self) -> int:
        return self.view.count()


class MSFluentWindow(FramelessWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setTitleBar(qfw.MSFluentTitleBar(self))

        self.hBoxLayout = QtWidgets.QHBoxLayout(self)
        self.stackedWidget = StackedWidget(self)

        qfw.FluentStyleSheet.FLUENT_WINDOW.apply(self.stackedWidget)

        self.navigationInterface = qfw.NavigationBar(self)
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 48, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackedWidget, 1)

        self.titleBar.raise_()
        self.titleBar.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground)

    def addSubInterface(
        self,
        interface: QtWidgets.QWidget,
        icon: qfw.FluentIconBase | QtGui.QIcon | str,
        text: str,
        selectedIcon: qfw.FluentIconBase | QtGui.QIcon | str | None = None,
        position: qfw.NavigationItemPosition = qfw.NavigationItemPosition.TOP,
        isTransparent: bool = False,
    ) -> qfw.NavigationBarPushButton | None:
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be an empty string.")

        self.stackedWidget.addWidget(interface)

        routeKey = interface.objectName()
        item = self.navigationInterface.addItem(
            routeKey=routeKey,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            selectedIcon=selectedIcon,
            position=position,
        )

        if self.stackedWidget.count() == 1:
            self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigationInterface.setCurrentItem(routeKey)

        return item

    def switchTo(self, interface: QtWidgets.QWidget) -> None:
        self.stackedWidget.setCurrentWidget(interface)

    def _onCurrentInterfaceChanged(self, index: int) -> None:
        widget = self.stackedWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())
