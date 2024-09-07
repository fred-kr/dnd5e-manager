# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wiki_interface.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QSizePolicy, QStackedWidget, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BreadcrumbBar, LineEdit, ListView, Pivot,
    StrongBodyLabel, TreeView)

class Ui_WikiInterface(object):
    def setupUi(self, WikiInterface):
        if not WikiInterface.objectName():
            WikiInterface.setObjectName(u"WikiInterface")
        WikiInterface.resize(1463, 841)
        self.verticalLayout = QVBoxLayout(WikiInterface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pivot_nav_bar = Pivot(WikiInterface)
        self.pivot_nav_bar.setObjectName(u"pivot_nav_bar")

        self.verticalLayout.addWidget(self.pivot_nav_bar)

        self.stacked_info_page = QStackedWidget(WikiInterface)
        self.stacked_info_page.setObjectName(u"stacked_info_page")
        self.page_database_search = QWidget()
        self.page_database_search.setObjectName(u"page_database_search")
        self.gridLayout = QGridLayout(self.page_database_search)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bc_bar_item_list = BreadcrumbBar(self.page_database_search)
        self.bc_bar_item_list.setObjectName(u"bc_bar_item_list")
        self.bc_bar_item_list.setMinimumSize(QSize(0, 31))

        self.gridLayout.addWidget(self.bc_bar_item_list, 0, 0, 1, 3)

        self.label_3 = StrongBodyLabel(self.page_database_search)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.line_edit_filter = LineEdit(self.page_database_search)
        self.line_edit_filter.setObjectName(u"line_edit_filter")
        self.line_edit_filter.setMinimumSize(QSize(0, 31))
        self.line_edit_filter.setFrame(False)
        self.line_edit_filter.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit_filter, 1, 1, 1, 1)

        self.tabWidget = QTabWidget(self.page_database_search)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_description = QWidget()
        self.tab_description.setObjectName(u"tab_description")
        self.verticalLayout_2 = QVBoxLayout(self.tab_description)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.text_browser_search_result = QTextBrowser(self.tab_description)
        self.text_browser_search_result.setObjectName(u"text_browser_search_result")
        font = QFont()
        font.setFamilies([u"Dubai"])
        font.setPointSize(11)
        self.text_browser_search_result.setFont(font)

        self.verticalLayout_2.addWidget(self.text_browser_search_result)

        self.tabWidget.addTab(self.tab_description, "")
        self.tab_details = QWidget()
        self.tab_details.setObjectName(u"tab_details")
        self.verticalLayout_3 = QVBoxLayout(self.tab_details)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.tree_view_json_data = TreeView(self.tab_details)
        self.tree_view_json_data.setObjectName(u"tree_view_json_data")

        self.verticalLayout_3.addWidget(self.tree_view_json_data)

        self.tabWidget.addTab(self.tab_details, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 2, 2, 1)

        self.list_view_api = ListView(self.page_database_search)
        self.list_view_api.setObjectName(u"list_view_api")
        self.list_view_api.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_view_api.setProperty("showDropIndicator", False)
        self.list_view_api.setAlternatingRowColors(True)
        self.list_view_api.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.gridLayout.addWidget(self.list_view_api, 2, 0, 1, 2)

        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 7)
        self.stacked_info_page.addWidget(self.page_database_search)
        self.page_app_info = QWidget()
        self.page_app_info.setObjectName(u"page_app_info")
        self.verticalLayout_4 = QVBoxLayout(self.page_app_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.text_browser_app_info = QTextBrowser(self.page_app_info)
        self.text_browser_app_info.setObjectName(u"text_browser_app_info")

        self.verticalLayout_4.addWidget(self.text_browser_app_info)

        self.stacked_info_page.addWidget(self.page_app_info)

        self.verticalLayout.addWidget(self.stacked_info_page)


        self.retranslateUi(WikiInterface)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(WikiInterface)
    # setupUi

    def retranslateUi(self, WikiInterface):
        WikiInterface.setWindowTitle(QCoreApplication.translate("WikiInterface", u"Wiki & Database Search", None))
        self.label_3.setText(QCoreApplication.translate("WikiInterface", u"Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_description), QCoreApplication.translate("WikiInterface", u"Description", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_description), QCoreApplication.translate("WikiInterface", u"<html><head/><body><p>Shows a description for the selected resource</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_details), QCoreApplication.translate("WikiInterface", u"Details", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_details), QCoreApplication.translate("WikiInterface", u"<html><head/><body><p>Shows a detailed view of the selected resource's attributes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

