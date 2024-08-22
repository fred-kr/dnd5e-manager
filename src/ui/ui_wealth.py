# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wealth.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QSizePolicy, QSpinBox, QWidget)

from qfluentwidgets import (BodyLabel, StrongBodyLabel, SubtitleLabel, TransparentToolButton)
from . import resources_rc

class Ui_WealthControls(object):
    def setupUi(self, WealthControls):
        if not WealthControls.objectName():
            WealthControls.setObjectName(u"WealthControls")
        WealthControls.resize(430, 368)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WealthControls.sizePolicy().hasHeightForWidth())
        WealthControls.setSizePolicy(sizePolicy)
        WealthControls.setStyleSheet(u"")
        self.gridLayout = QGridLayout(WealthControls)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = SubtitleLabel(WealthControls)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)

        self.frame = QFrame(WealthControls)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.n_gold = QSpinBox(self.frame)
        self.n_gold.setObjectName(u"n_gold")
        self.n_gold.setMinimumSize(QSize(150, 31))
        self.n_gold.setMaximumSize(QSize(150, 16777215))
        self.n_gold.setFrame(False)
        self.n_gold.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_gold.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_gold, 4, 1, 1, 1)

        self.n_silver = QSpinBox(self.frame)
        self.n_silver.setObjectName(u"n_silver")
        self.n_silver.setMinimumSize(QSize(150, 31))
        self.n_silver.setMaximumSize(QSize(150, 16777215))
        self.n_silver.setFrame(False)
        self.n_silver.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_silver.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_silver, 6, 1, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)

        self.label_4 = StrongBodyLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_7 = BodyLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = StrongBodyLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.gp_gold = QDoubleSpinBox(self.frame)
        self.gp_gold.setObjectName(u"gp_gold")
        self.gp_gold.setMinimumSize(QSize(150, 31))
        self.gp_gold.setMaximumSize(QSize(150, 16777215))
        self.gp_gold.setFrame(False)
        self.gp_gold.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_gold.setReadOnly(True)
        self.gp_gold.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_gold.setDecimals(0)
        self.gp_gold.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_gold, 4, 2, 1, 1)

        self.label_8 = BodyLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)

        self.n_total = QSpinBox(self.frame)
        self.n_total.setObjectName(u"n_total")
        self.n_total.setMinimumSize(QSize(150, 31))
        self.n_total.setFrame(False)
        self.n_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_total.setReadOnly(True)
        self.n_total.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.n_total.setMaximum(999999)

        self.gridLayout_2.addWidget(self.n_total, 9, 1, 1, 1)

        self.label = StrongBodyLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(80, 0))

        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)

        self.gp_total = QDoubleSpinBox(self.frame)
        self.gp_total.setObjectName(u"gp_total")
        self.gp_total.setMinimumSize(QSize(150, 31))
        self.gp_total.setFrame(False)
        self.gp_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_total.setReadOnly(True)
        self.gp_total.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_total.setMaximum(99999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_total, 9, 2, 1, 1)

        self.gp_gems = QDoubleSpinBox(self.frame)
        self.gp_gems.setObjectName(u"gp_gems")
        self.gp_gems.setMinimumSize(QSize(150, 31))
        self.gp_gems.setMaximumSize(QSize(150, 16777215))
        self.gp_gems.setFrame(False)
        self.gp_gems.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_gems.setReadOnly(True)
        self.gp_gems.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_gems.setDecimals(0)
        self.gp_gems.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_gems, 2, 2, 1, 1)

        self.label_10 = BodyLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(80, 0))
        self.label_10.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)

        self.gp_platinum = QDoubleSpinBox(self.frame)
        self.gp_platinum.setObjectName(u"gp_platinum")
        self.gp_platinum.setMinimumSize(QSize(150, 31))
        self.gp_platinum.setMaximumSize(QSize(150, 16777215))
        self.gp_platinum.setFrame(False)
        self.gp_platinum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_platinum.setReadOnly(True)
        self.gp_platinum.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_platinum.setDecimals(0)
        self.gp_platinum.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_platinum, 3, 2, 1, 1)

        self.n_copper = QSpinBox(self.frame)
        self.n_copper.setObjectName(u"n_copper")
        self.n_copper.setMinimumSize(QSize(150, 31))
        self.n_copper.setMaximumSize(QSize(150, 16777215))
        self.n_copper.setFrame(False)
        self.n_copper.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_copper.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_copper, 7, 1, 1, 1)

        self.n_electrum = QSpinBox(self.frame)
        self.n_electrum.setObjectName(u"n_electrum")
        self.n_electrum.setMinimumSize(QSize(150, 31))
        self.n_electrum.setMaximumSize(QSize(150, 16777215))
        self.n_electrum.setFrame(False)
        self.n_electrum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_electrum.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_electrum, 5, 1, 1, 1)

        self.label_9 = BodyLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 3)

        self.gp_copper = QDoubleSpinBox(self.frame)
        self.gp_copper.setObjectName(u"gp_copper")
        self.gp_copper.setMinimumSize(QSize(150, 31))
        self.gp_copper.setMaximumSize(QSize(150, 16777215))
        self.gp_copper.setFrame(False)
        self.gp_copper.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_copper.setReadOnly(True)
        self.gp_copper.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_copper.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_copper, 7, 2, 1, 1)

        self.label_6 = BodyLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.n_gems = QSpinBox(self.frame)
        self.n_gems.setObjectName(u"n_gems")
        self.n_gems.setMinimumSize(QSize(150, 31))
        self.n_gems.setMaximumSize(QSize(150, 16777215))
        self.n_gems.setFrame(False)
        self.n_gems.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_gems.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_gems, 2, 1, 1, 1)

        self.gp_silver = QDoubleSpinBox(self.frame)
        self.gp_silver.setObjectName(u"gp_silver")
        self.gp_silver.setMinimumSize(QSize(150, 31))
        self.gp_silver.setMaximumSize(QSize(150, 16777215))
        self.gp_silver.setFrame(False)
        self.gp_silver.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_silver.setReadOnly(True)
        self.gp_silver.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_silver.setDecimals(1)
        self.gp_silver.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_silver, 6, 2, 1, 1)

        self.gp_electrum = QDoubleSpinBox(self.frame)
        self.gp_electrum.setObjectName(u"gp_electrum")
        self.gp_electrum.setMinimumSize(QSize(150, 31))
        self.gp_electrum.setMaximumSize(QSize(150, 16777215))
        self.gp_electrum.setFrame(False)
        self.gp_electrum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gp_electrum.setReadOnly(True)
        self.gp_electrum.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.gp_electrum.setDecimals(1)
        self.gp_electrum.setMaximum(999999.000000000000000)

        self.gridLayout_2.addWidget(self.gp_electrum, 5, 2, 1, 1)

        self.n_platinum = QSpinBox(self.frame)
        self.n_platinum.setObjectName(u"n_platinum")
        self.n_platinum.setMinimumSize(QSize(150, 31))
        self.n_platinum.setMaximumSize(QSize(150, 16777215))
        self.n_platinum.setFrame(False)
        self.n_platinum.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.n_platinum.setMaximum(9999)

        self.gridLayout_2.addWidget(self.n_platinum, 3, 1, 1, 1)

        self.label_5 = BodyLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_2 = StrongBodyLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(80, 0))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 3)

        self.btn_reset_all = TransparentToolButton(WealthControls)
        self.btn_reset_all.setObjectName(u"btn_reset_all")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_reset_all.sizePolicy().hasHeightForWidth())
        self.btn_reset_all.setSizePolicy(sizePolicy4)
        self.btn_reset_all.setMinimumSize(QSize(31, 31))
        icon = QIcon()
        icon.addFile(u":/icons/fluent-icons/Broom.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset_all.setIcon(icon)
        self.btn_reset_all.setAutoRaise(True)

        self.gridLayout.addWidget(self.btn_reset_all, 0, 2, 1, 1)


        self.retranslateUi(WealthControls)

        QMetaObject.connectSlotsByName(WealthControls)
    # setupUi

    def retranslateUi(self, WealthControls):
        WealthControls.setWindowTitle(QCoreApplication.translate("WealthControls", u"Wealth", None))
        self.label_11.setText(QCoreApplication.translate("WealthControls", u"Wealth", None))
        self.label_4.setText(QCoreApplication.translate("WealthControls", u"Value", None))
        self.label_7.setText(QCoreApplication.translate("WealthControls", u"Gold", None))
        self.label_3.setText(QCoreApplication.translate("WealthControls", u"Amount", None))
        self.gp_gold.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.label_8.setText(QCoreApplication.translate("WealthControls", u"Electrum", None))
        self.n_total.setSuffix(QCoreApplication.translate("WealthControls", u" (0 slots)", None))
        self.label.setText(QCoreApplication.translate("WealthControls", u"Total:", None))
        self.gp_total.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.gp_gems.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.label_10.setText(QCoreApplication.translate("WealthControls", u"Copper", None))
        self.gp_platinum.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.label_9.setText(QCoreApplication.translate("WealthControls", u"Silver", None))
        self.gp_copper.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.label_6.setText(QCoreApplication.translate("WealthControls", u"Platinum", None))
        self.gp_silver.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.gp_electrum.setSuffix(QCoreApplication.translate("WealthControls", u" gp", None))
        self.label_5.setText(QCoreApplication.translate("WealthControls", u"Gems", None))
        self.label_2.setText(QCoreApplication.translate("WealthControls", u"Currency", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_all.setToolTip(QCoreApplication.translate("WealthControls", u"Set all amounts to 0", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_all.setText("")
    # retranslateUi

