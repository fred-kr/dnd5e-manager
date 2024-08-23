# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wealth_consumables_tracker.ui'
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
    QGridLayout, QHBoxLayout, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

from dnd_app import (SlotDoubleSpinBox, SlotSpinBox)
from qfluentwidgets import (BodyLabel, StrongBodyLabel, SubtitleLabel, TransparentToolButton)
from . import resources_rc

class Ui_WealthConsumablesTracker(object):
    def setupUi(self, WealthConsumablesTracker):
        if not WealthConsumablesTracker.objectName():
            WealthConsumablesTracker.setObjectName(u"WealthConsumablesTracker")
        WealthConsumablesTracker.resize(1098, 354)
        self.horizontalLayout_3 = QHBoxLayout(WealthConsumablesTracker)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container_wealth = QWidget(WealthConsumablesTracker)
        self.container_wealth.setObjectName(u"container_wealth")
        self.verticalLayout = QVBoxLayout(self.container_wealth)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_wealth_header = QWidget(self.container_wealth)
        self.container_wealth_header.setObjectName(u"container_wealth_header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_wealth_header.sizePolicy().hasHeightForWidth())
        self.container_wealth_header.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.container_wealth_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = SubtitleLabel(self.container_wealth_header)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.btn_clear_wealth = TransparentToolButton(self.container_wealth_header)
        self.btn_clear_wealth.setObjectName(u"btn_clear_wealth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear_wealth.sizePolicy().hasHeightForWidth())
        self.btn_clear_wealth.setSizePolicy(sizePolicy1)
        self.btn_clear_wealth.setMinimumSize(QSize(31, 31))
        icon = QIcon()
        icon.addFile(u":/icons/fluent-icons/Broom.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_wealth.setIcon(icon)
        self.btn_clear_wealth.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.btn_clear_wealth)


        self.verticalLayout.addWidget(self.container_wealth_header)

        self.frame = QFrame(self.container_wealth)
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
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
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

        self.n_total = SlotSpinBox(self.frame)
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


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.container_wealth, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.container_consumables = QWidget(WealthConsumablesTracker)
        self.container_consumables.setObjectName(u"container_consumables")
        self.verticalLayout_2 = QVBoxLayout(self.container_consumables)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.container_consumable_header = QWidget(self.container_consumables)
        self.container_consumable_header.setObjectName(u"container_consumable_header")
        sizePolicy.setHeightForWidth(self.container_consumable_header.sizePolicy().hasHeightForWidth())
        self.container_consumable_header.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.container_consumable_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = SubtitleLabel(self.container_consumable_header)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.btn_clear_consumables = TransparentToolButton(self.container_consumable_header)
        self.btn_clear_consumables.setObjectName(u"btn_clear_consumables")
        self.btn_clear_consumables.setMinimumSize(QSize(31, 31))
        self.btn_clear_consumables.setMaximumSize(QSize(31, 31))
        self.btn_clear_consumables.setIcon(icon)
        self.btn_clear_consumables.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.btn_clear_consumables)


        self.verticalLayout_2.addWidget(self.container_consumable_header)

        self.frame_2 = QFrame(self.container_consumables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = StrongBodyLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = StrongBodyLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)

        self.frame_consumables = QFrame(self.frame_2)
        self.frame_consumables.setObjectName(u"frame_consumables")
        self.frame_consumables.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout = QGridLayout(self.frame_consumables)
        self.gridLayout.setObjectName(u"gridLayout")
        self.torchesLabel = BodyLabel(self.frame_consumables)
        self.torchesLabel.setObjectName(u"torchesLabel")
        self.torchesLabel.setMinimumSize(QSize(150, 0))
        self.torchesLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.torchesLabel, 0, 0, 1, 1)

        self.n_torches = SlotSpinBox(self.frame_consumables)
        self.n_torches.setObjectName(u"n_torches")
        sizePolicy.setHeightForWidth(self.n_torches.sizePolicy().hasHeightForWidth())
        self.n_torches.setSizePolicy(sizePolicy)
        self.n_torches.setMinimumSize(QSize(152, 33))
        self.n_torches.setFrame(False)
        self.n_torches.setMaximum(999)

        self.gridLayout.addWidget(self.n_torches, 0, 1, 1, 1)

        self.oilFlasksLabel = BodyLabel(self.frame_consumables)
        self.oilFlasksLabel.setObjectName(u"oilFlasksLabel")
        self.oilFlasksLabel.setMinimumSize(QSize(150, 0))
        self.oilFlasksLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.oilFlasksLabel, 1, 0, 1, 1)

        self.n_oil_flasks = SlotSpinBox(self.frame_consumables)
        self.n_oil_flasks.setObjectName(u"n_oil_flasks")
        sizePolicy.setHeightForWidth(self.n_oil_flasks.sizePolicy().hasHeightForWidth())
        self.n_oil_flasks.setSizePolicy(sizePolicy)
        self.n_oil_flasks.setMinimumSize(QSize(152, 33))
        self.n_oil_flasks.setFrame(False)
        self.n_oil_flasks.setMaximum(999)

        self.gridLayout.addWidget(self.n_oil_flasks, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_consumables, 1, 0, 1, 1)

        self.frame_ammunition = QFrame(self.frame_2)
        self.frame_ammunition.setObjectName(u"frame_ammunition")
        self.frame_ammunition.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout_3 = QGridLayout(self.frame_ammunition)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.arrowsLabel_4 = BodyLabel(self.frame_ammunition)
        self.arrowsLabel_4.setObjectName(u"arrowsLabel_4")
        self.arrowsLabel_4.setMinimumSize(QSize(150, 0))
        self.arrowsLabel_4.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.arrowsLabel_4, 4, 0, 1, 1)

        self.n_needles = SlotSpinBox(self.frame_ammunition)
        self.n_needles.setObjectName(u"n_needles")
        self.n_needles.setMinimumSize(QSize(152, 33))
        self.n_needles.setFrame(False)
        self.n_needles.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_needles, 5, 1, 1, 1)

        self.n_darts = SlotSpinBox(self.frame_ammunition)
        self.n_darts.setObjectName(u"n_darts")
        self.n_darts.setMinimumSize(QSize(152, 33))
        self.n_darts.setFrame(False)
        self.n_darts.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_darts, 3, 1, 1, 1)

        self.n_daggers = SlotSpinBox(self.frame_ammunition)
        self.n_daggers.setObjectName(u"n_daggers")
        self.n_daggers.setMinimumSize(QSize(152, 33))
        self.n_daggers.setFrame(False)
        self.n_daggers.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_daggers, 0, 1, 1, 1)

        self.arrowsLabel_5 = BodyLabel(self.frame_ammunition)
        self.arrowsLabel_5.setObjectName(u"arrowsLabel_5")
        self.arrowsLabel_5.setMinimumSize(QSize(150, 0))
        self.arrowsLabel_5.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.arrowsLabel_5, 5, 0, 1, 1)

        self.n_bolts = SlotSpinBox(self.frame_ammunition)
        self.n_bolts.setObjectName(u"n_bolts")
        self.n_bolts.setMinimumSize(QSize(152, 33))
        self.n_bolts.setFrame(False)
        self.n_bolts.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_bolts, 2, 1, 1, 1)

        self.n_bullets = SlotSpinBox(self.frame_ammunition)
        self.n_bullets.setObjectName(u"n_bullets")
        self.n_bullets.setMinimumSize(QSize(152, 33))
        self.n_bullets.setFrame(False)
        self.n_bullets.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_bullets, 4, 1, 1, 1)

        self.n_arrows = SlotSpinBox(self.frame_ammunition)
        self.n_arrows.setObjectName(u"n_arrows")
        self.n_arrows.setMinimumSize(QSize(152, 33))
        self.n_arrows.setFrame(False)
        self.n_arrows.setMaximum(999999)

        self.gridLayout_3.addWidget(self.n_arrows, 1, 1, 1, 1)

        self.daggersLabel = BodyLabel(self.frame_ammunition)
        self.daggersLabel.setObjectName(u"daggersLabel")
        self.daggersLabel.setMinimumSize(QSize(150, 0))
        self.daggersLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.daggersLabel, 0, 0, 1, 1)

        self.arrowsLabel_2 = BodyLabel(self.frame_ammunition)
        self.arrowsLabel_2.setObjectName(u"arrowsLabel_2")
        self.arrowsLabel_2.setMinimumSize(QSize(150, 0))
        self.arrowsLabel_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.arrowsLabel_2, 2, 0, 1, 1)

        self.arrowsLabel = BodyLabel(self.frame_ammunition)
        self.arrowsLabel.setObjectName(u"arrowsLabel")
        self.arrowsLabel.setMinimumSize(QSize(150, 0))
        self.arrowsLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.arrowsLabel, 1, 0, 1, 1)

        self.arrowsLabel_3 = BodyLabel(self.frame_ammunition)
        self.arrowsLabel_3.setObjectName(u"arrowsLabel_3")
        self.arrowsLabel_3.setMinimumSize(QSize(150, 0))
        self.arrowsLabel_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.arrowsLabel_3, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_ammunition, 1, 1, 3, 1)

        self.label_14 = StrongBodyLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.frame_nourishment = QFrame(self.frame_2)
        self.frame_nourishment.setObjectName(u"frame_nourishment")
        self.frame_nourishment.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout_5 = QGridLayout(self.frame_nourishment)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.waterJugLabel = BodyLabel(self.frame_nourishment)
        self.waterJugLabel.setObjectName(u"waterJugLabel")
        self.waterJugLabel.setMinimumSize(QSize(150, 0))
        self.waterJugLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.waterJugLabel, 3, 0, 1, 1)

        self.n_waterskins = SlotSpinBox(self.frame_nourishment)
        self.n_waterskins.setObjectName(u"n_waterskins")
        self.n_waterskins.setMinimumSize(QSize(152, 33))
        self.n_waterskins.setFrame(False)
        self.n_waterskins.setMaximum(999)

        self.gridLayout_5.addWidget(self.n_waterskins, 2, 1, 1, 1)

        self.rationsLabel = BodyLabel(self.frame_nourishment)
        self.rationsLabel.setObjectName(u"rationsLabel")
        self.rationsLabel.setMinimumSize(QSize(150, 0))
        self.rationsLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.rationsLabel, 1, 0, 1, 1)

        self.n_rations = SlotDoubleSpinBox(self.frame_nourishment)
        self.n_rations.setObjectName(u"n_rations")
        self.n_rations.setMinimumSize(QSize(152, 33))
        self.n_rations.setFrame(False)
        self.n_rations.setDecimals(1)
        self.n_rations.setMaximum(999.000000000000000)
        self.n_rations.setSingleStep(0.500000000000000)

        self.gridLayout_5.addWidget(self.n_rations, 1, 1, 1, 1)

        self.n_jugs = SlotSpinBox(self.frame_nourishment)
        self.n_jugs.setObjectName(u"n_jugs")
        self.n_jugs.setMinimumSize(QSize(152, 33))
        self.n_jugs.setFrame(False)
        self.n_jugs.setMaximum(999)

        self.gridLayout_5.addWidget(self.n_jugs, 3, 1, 1, 1)

        self.waterWaterskinLabel = BodyLabel(self.frame_nourishment)
        self.waterWaterskinLabel.setObjectName(u"waterWaterskinLabel")
        sizePolicy2.setHeightForWidth(self.waterWaterskinLabel.sizePolicy().hasHeightForWidth())
        self.waterWaterskinLabel.setSizePolicy(sizePolicy2)
        self.waterWaterskinLabel.setMinimumSize(QSize(150, 0))
        self.waterWaterskinLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.waterWaterskinLabel, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_nourishment, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.container_consumables, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(WealthConsumablesTracker)

        QMetaObject.connectSlotsByName(WealthConsumablesTracker)
    # setupUi

    def retranslateUi(self, WealthConsumablesTracker):
        WealthConsumablesTracker.setWindowTitle(QCoreApplication.translate("WealthConsumablesTracker", u"Wealth and Consumables Tracker", None))
        self.label_11.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Wealth", None))
#if QT_CONFIG(tooltip)
        self.btn_clear_wealth.setToolTip(QCoreApplication.translate("WealthConsumablesTracker", u"Set all amounts to 0", None))
#endif // QT_CONFIG(tooltip)
        self.btn_clear_wealth.setText("")
        self.label_4.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Value", None))
        self.label_7.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Gold", None))
        self.label_3.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Amount", None))
        self.gp_gold.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.label_8.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Electrum", None))
        self.n_total.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.label.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Total:", None))
        self.gp_total.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.gp_gems.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.label_10.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Copper", None))
        self.gp_platinum.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.label_9.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Silver", None))
        self.gp_copper.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.label_6.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Platinum", None))
        self.gp_silver.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.gp_electrum.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" gp", None))
        self.label_5.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Gems", None))
        self.label_2.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Currency", None))
        self.label_15.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Consumables", None))
#if QT_CONFIG(tooltip)
        self.btn_clear_consumables.setToolTip(QCoreApplication.translate("WealthConsumablesTracker", u"Set all tracker inputs to 0", None))
#endif // QT_CONFIG(tooltip)
        self.btn_clear_consumables.setText("")
        self.label_12.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Lighting", None))
        self.label_13.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Ammunition", None))
        self.torchesLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Torches", None))
        self.n_torches.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.oilFlasksLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Oil flasks", None))
        self.n_oil_flasks.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.arrowsLabel_4.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Bullets", None))
        self.n_needles.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.n_darts.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.n_daggers.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.arrowsLabel_5.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Needles", None))
        self.n_bolts.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.n_bullets.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.n_arrows.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.daggersLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Daggers", None))
        self.arrowsLabel_2.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Bolts", None))
        self.arrowsLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Arrows", None))
        self.arrowsLabel_3.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Darts", None))
        self.label_14.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Nourishment", None))
        self.waterJugLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"<html><head/><body><p>Jugs (1-gallon)</p></body></html>", None))
        self.n_waterskins.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.rationsLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"Rations", None))
        self.n_rations.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.n_jugs.setSuffix(QCoreApplication.translate("WealthConsumablesTracker", u" (0 slots)", None))
        self.waterWaterskinLabel.setText(QCoreApplication.translate("WealthConsumablesTracker", u"<html><head/><body><p>Waterskins (\u00bd-gallon)</p></body></html>", None))
    # retranslateUi

