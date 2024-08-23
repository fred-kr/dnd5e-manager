# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_tables.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

from qfluentwidgets import (CommandBar, SubtitleLabel, TableView)

class Ui_ItemTables(object):
    def setupUi(self, ItemTables):
        if not ItemTables.objectName():
            ItemTables.setObjectName(u"ItemTables")
        ItemTables.resize(574, 254)
        self.verticalLayout_5 = QVBoxLayout(ItemTables)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter = QSplitter(ItemTables)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.container_widget_inventory = QWidget(self.splitter)
        self.container_widget_inventory.setObjectName(u"container_widget_inventory")
        self.verticalLayout_4 = QVBoxLayout(self.container_widget_inventory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = SubtitleLabel(self.container_widget_inventory)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.frame_inventory = QFrame(self.container_widget_inventory)
        self.frame_inventory.setObjectName(u"frame_inventory")
        self.frame_inventory.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_inventory.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_inventory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.command_bar_inventory = CommandBar(self.frame_inventory)
        self.command_bar_inventory.setObjectName(u"command_bar_inventory")
        self.command_bar_inventory.setFrameShape(QFrame.Shape.StyledPanel)
        self.command_bar_inventory.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.command_bar_inventory)

        self.table_view_inventory = TableView(self.frame_inventory)
        self.table_view_inventory.setObjectName(u"table_view_inventory")

        self.verticalLayout.addWidget(self.table_view_inventory)


        self.verticalLayout_4.addWidget(self.frame_inventory)

        self.splitter.addWidget(self.container_widget_inventory)
        self.container_widget_storage = QWidget(self.splitter)
        self.container_widget_storage.setObjectName(u"container_widget_storage")
        self.verticalLayout_3 = QVBoxLayout(self.container_widget_storage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = SubtitleLabel(self.container_widget_storage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_storage = QFrame(self.container_widget_storage)
        self.frame_storage.setObjectName(u"frame_storage")
        self.frame_storage.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_storage.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_storage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.command_bar_storage = CommandBar(self.frame_storage)
        self.command_bar_storage.setObjectName(u"command_bar_storage")
        self.command_bar_storage.setFrameShape(QFrame.Shape.StyledPanel)
        self.command_bar_storage.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.command_bar_storage)

        self.table_view_storage = TableView(self.frame_storage)
        self.table_view_storage.setObjectName(u"table_view_storage")

        self.verticalLayout_2.addWidget(self.table_view_storage)


        self.verticalLayout_3.addWidget(self.frame_storage)

        self.splitter.addWidget(self.container_widget_storage)

        self.verticalLayout_5.addWidget(self.splitter)


        self.retranslateUi(ItemTables)

        QMetaObject.connectSlotsByName(ItemTables)
    # setupUi

    def retranslateUi(self, ItemTables):
        ItemTables.setWindowTitle(QCoreApplication.translate("ItemTables", u"ItemTables", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ItemTables", u"<html><head/><body><p>Items that you are currently carrying in your inventory</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ItemTables", u"Inventory", None))
#if QT_CONFIG(tooltip)
        self.frame_inventory.setToolTip(QCoreApplication.translate("ItemTables", u"<html><head/><body><p>Items that you are currently carrying in your inventory</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("ItemTables", u"<html><head/><body><p>Items that you are not currently carrying</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ItemTables", u"Storage", None))
#if QT_CONFIG(tooltip)
        self.frame_storage.setToolTip(QCoreApplication.translate("ItemTables", u"<html><head/><body><p>Items that you are not currently carrying</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

