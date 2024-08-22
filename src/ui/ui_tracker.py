# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tracker.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QWidget)

from dnd_app import (SlotDoubleSpinBox, SlotSpinBox)
from qfluentwidgets import (BodyLabel, StrongBodyLabel, SubtitleLabel, TransparentToolButton)
from . import resources_rc

class Ui_Tracker(object):
    def setupUi(self, Tracker):
        if not Tracker.objectName():
            Tracker.setObjectName(u"Tracker")
        Tracker.resize(732, 348)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tracker.sizePolicy().hasHeightForWidth())
        Tracker.setSizePolicy(sizePolicy)
        Tracker.setStyleSheet(u"QDoubleSpinBox { min-height: 31px; min-width: 150px; }\n"
"QSpinBox { min-height: 31px; min-width: 150px; }")
        self.gridLayout_5 = QGridLayout(Tracker)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(Tracker)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = StrongBodyLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = StrongBodyLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)

        self.frame_consumables = QFrame(self.frame)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.n_torches.sizePolicy().hasHeightForWidth())
        self.n_torches.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.n_oil_flasks.sizePolicy().hasHeightForWidth())
        self.n_oil_flasks.setSizePolicy(sizePolicy2)
        self.n_oil_flasks.setMinimumSize(QSize(152, 33))
        self.n_oil_flasks.setFrame(False)
        self.n_oil_flasks.setMaximum(999)

        self.gridLayout.addWidget(self.n_oil_flasks, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_consumables, 1, 0, 1, 1)

        self.frame_ammunition = QFrame(self.frame)
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

        self.label_4 = StrongBodyLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.frame_nourishment = QFrame(self.frame)
        self.frame_nourishment.setObjectName(u"frame_nourishment")
        self.frame_nourishment.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout_2 = QGridLayout(self.frame_nourishment)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.waterJugLabel = BodyLabel(self.frame_nourishment)
        self.waterJugLabel.setObjectName(u"waterJugLabel")
        self.waterJugLabel.setMinimumSize(QSize(150, 0))
        self.waterJugLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.waterJugLabel, 3, 0, 1, 1)

        self.n_waterskins = SlotSpinBox(self.frame_nourishment)
        self.n_waterskins.setObjectName(u"n_waterskins")
        self.n_waterskins.setMinimumSize(QSize(152, 33))
        self.n_waterskins.setFrame(False)
        self.n_waterskins.setMaximum(999)

        self.gridLayout_2.addWidget(self.n_waterskins, 2, 1, 1, 1)

        self.rationsLabel = BodyLabel(self.frame_nourishment)
        self.rationsLabel.setObjectName(u"rationsLabel")
        self.rationsLabel.setMinimumSize(QSize(150, 0))
        self.rationsLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.rationsLabel, 1, 0, 1, 1)

        self.n_rations = SlotDoubleSpinBox(self.frame_nourishment)
        self.n_rations.setObjectName(u"n_rations")
        self.n_rations.setMinimumSize(QSize(152, 33))
        self.n_rations.setFrame(False)
        self.n_rations.setDecimals(1)
        self.n_rations.setMaximum(999.000000000000000)
        self.n_rations.setSingleStep(0.500000000000000)

        self.gridLayout_2.addWidget(self.n_rations, 1, 1, 1, 1)

        self.n_jugs = SlotSpinBox(self.frame_nourishment)
        self.n_jugs.setObjectName(u"n_jugs")
        self.n_jugs.setMinimumSize(QSize(152, 33))
        self.n_jugs.setFrame(False)
        self.n_jugs.setMaximum(999)

        self.gridLayout_2.addWidget(self.n_jugs, 3, 1, 1, 1)

        self.waterWaterskinLabel = BodyLabel(self.frame_nourishment)
        self.waterWaterskinLabel.setObjectName(u"waterWaterskinLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.waterWaterskinLabel.sizePolicy().hasHeightForWidth())
        self.waterWaterskinLabel.setSizePolicy(sizePolicy3)
        self.waterWaterskinLabel.setMinimumSize(QSize(150, 0))
        self.waterWaterskinLabel.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.waterWaterskinLabel, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_nourishment, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 2)

        self.btn_reset_all = TransparentToolButton(Tracker)
        self.btn_reset_all.setObjectName(u"btn_reset_all")
        self.btn_reset_all.setMinimumSize(QSize(31, 31))
        icon = QIcon()
        icon.addFile(u":/icons/fluent-icons/Broom.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset_all.setIcon(icon)
        self.btn_reset_all.setAutoRaise(True)

        self.gridLayout_5.addWidget(self.btn_reset_all, 0, 1, 1, 1)

        self.label = SubtitleLabel(Tracker)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Tracker)

        QMetaObject.connectSlotsByName(Tracker)
    # setupUi

    def retranslateUi(self, Tracker):
        Tracker.setWindowTitle(QCoreApplication.translate("Tracker", u"Consumables Tracker", None))
        self.label_3.setText(QCoreApplication.translate("Tracker", u"Lighting", None))
        self.label_5.setText(QCoreApplication.translate("Tracker", u"Ammunition", None))
        self.torchesLabel.setText(QCoreApplication.translate("Tracker", u"Torches", None))
        self.n_torches.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.oilFlasksLabel.setText(QCoreApplication.translate("Tracker", u"Oil flasks", None))
        self.n_oil_flasks.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.arrowsLabel_4.setText(QCoreApplication.translate("Tracker", u"Bullets", None))
        self.n_needles.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.n_darts.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.n_daggers.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.arrowsLabel_5.setText(QCoreApplication.translate("Tracker", u"Needles", None))
        self.n_bolts.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.n_bullets.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.n_arrows.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.daggersLabel.setText(QCoreApplication.translate("Tracker", u"Daggers", None))
        self.arrowsLabel_2.setText(QCoreApplication.translate("Tracker", u"Bolts", None))
        self.arrowsLabel.setText(QCoreApplication.translate("Tracker", u"Arrows", None))
        self.arrowsLabel_3.setText(QCoreApplication.translate("Tracker", u"Darts", None))
        self.label_4.setText(QCoreApplication.translate("Tracker", u"Nourishment", None))
        self.waterJugLabel.setText(QCoreApplication.translate("Tracker", u"<html><head/><body><p>Jugs (1-gallon)</p></body></html>", None))
        self.n_waterskins.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.rationsLabel.setText(QCoreApplication.translate("Tracker", u"Rations", None))
        self.n_rations.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.n_jugs.setSuffix(QCoreApplication.translate("Tracker", u" (0 slots)", None))
        self.waterWaterskinLabel.setText(QCoreApplication.translate("Tracker", u"<html><head/><body><p>Waterskins (\u00bd-gallon)</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_all.setToolTip(QCoreApplication.translate("Tracker", u"Set all tracker inputs to 0", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_all.setText("")
        self.label.setText(QCoreApplication.translate("Tracker", u"Consumables", None))
    # retranslateUi

