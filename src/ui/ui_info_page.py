# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_page.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_Info(object):
    def setupUi(self, Info):
        if not Info.objectName():
            Info.setObjectName(u"Info")
        Info.resize(1147, 795)
        self.verticalLayout_2 = QVBoxLayout(Info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text_browser_info = QTextBrowser(Info)
        self.text_browser_info.setObjectName(u"text_browser_info")
        self.text_browser_info.setSource(QUrl(u"qrc:/html/sheet_info.html"))

        self.verticalLayout_2.addWidget(self.text_browser_info)


        self.retranslateUi(Info)

        QMetaObject.connectSlotsByName(Info)
    # setupUi

    def retranslateUi(self, Info):
        Info.setWindowTitle(QCoreApplication.translate("Info", u"Form", None))
    # retranslateUi

