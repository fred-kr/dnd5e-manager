# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from qfluentwidgets import RoundMenu
from . import resources_rc

class Ui_EquipmentManager(object):
    def setupUi(self, EquipmentManager):
        if not EquipmentManager.objectName():
            EquipmentManager.setObjectName(u"EquipmentManager")
        EquipmentManager.resize(800, 600)
        self.action_open = QAction(EquipmentManager)
        self.action_open.setObjectName(u"action_open")
        icon = QIcon()
        icon.addFile(u":/icons/fluent-icons/DocumentArrowRight.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_open.setIcon(icon)
        self.action_open.setMenuRole(QAction.MenuRole.NoRole)
        self.action_save = QAction(EquipmentManager)
        self.action_save.setObjectName(u"action_save")
        icon1 = QIcon()
        icon1.addFile(u":/icons/fluent-icons/Save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_save.setIcon(icon1)
        self.action_save.setMenuRole(QAction.MenuRole.NoRole)
        self.action_save_as = QAction(EquipmentManager)
        self.action_save_as.setObjectName(u"action_save_as")
        icon2 = QIcon()
        icon2.addFile(u":/icons/fluent-icons/SaveEdit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_save_as.setIcon(icon2)
        self.action_save_as.setMenuRole(QAction.MenuRole.NoRole)
        self.action_open_preferences = QAction(EquipmentManager)
        self.action_open_preferences.setObjectName(u"action_open_preferences")
        icon3 = QIcon()
        icon3.addFile(u":/icons/fluent-icons/Settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_open_preferences.setIcon(icon3)
        self.action_open_preferences.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.centralwidget = QWidget(EquipmentManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_wealth_consumables = QWidget()
        self.tab_wealth_consumables.setObjectName(u"tab_wealth_consumables")
        self.tab_widget.addTab(self.tab_wealth_consumables, "")
        self.tab_items = QWidget()
        self.tab_items.setObjectName(u"tab_items")
        self.tab_widget.addTab(self.tab_items, "")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.tab_widget.addTab(self.tab_info, "")

        self.verticalLayout.addWidget(self.tab_widget)

        EquipmentManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EquipmentManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu_file = RoundMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_settings = RoundMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        EquipmentManager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EquipmentManager)
        self.statusbar.setObjectName(u"statusbar")
        EquipmentManager.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_settings.addAction(self.action_open_preferences)

        self.retranslateUi(EquipmentManager)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EquipmentManager)
    # setupUi

    def retranslateUi(self, EquipmentManager):
        EquipmentManager.setWindowTitle(QCoreApplication.translate("EquipmentManager", u"EquipmentManager", None))
        self.action_open.setText(QCoreApplication.translate("EquipmentManager", u"Open File...", None))
        self.action_save.setText(QCoreApplication.translate("EquipmentManager", u"Save", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("EquipmentManager", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("EquipmentManager", u"Save As...", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("EquipmentManager", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_open_preferences.setText(QCoreApplication.translate("EquipmentManager", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.action_open_preferences.setShortcut(QCoreApplication.translate("EquipmentManager", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_wealth_consumables), QCoreApplication.translate("EquipmentManager", u"Wealth && Consumables", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_items), QCoreApplication.translate("EquipmentManager", u"Items", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_info), QCoreApplication.translate("EquipmentManager", u"Info", None))
        self.menu_file.setTitle(QCoreApplication.translate("EquipmentManager", u"File", None))
        self.menu_settings.setTitle(QCoreApplication.translate("EquipmentManager", u"Settings", None))
    # retranslateUi

