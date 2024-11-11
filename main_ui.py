# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 604)
        MainWindow.setMinimumSize(QSize(800, 604))
        MainWindow.setMaximumSize(QSize(800, 604))
        icon = QIcon()
        icon.addFile(u"icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.pass_table = QTableWidget(self.centralwidget)
        self.pass_table.setObjectName(u"pass_table")
        self.pass_table.setGeometry(QRect(10, 10, 781, 501))
        self.pass_table.setTabletTracking(False)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 520, 781, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.open_db_button = QPushButton(self.horizontalLayoutWidget_3)
        self.open_db_button.setObjectName(u"open_db_button")
        self.open_db_button.setMinimumSize(QSize(150, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_db_button.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.open_db_button)

        self.line_3 = QFrame(self.horizontalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.add_button = QPushButton(self.horizontalLayoutWidget_3)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(150, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_button.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.add_button)

        self.line_4 = QFrame(self.horizontalLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.search_button = QPushButton(self.horizontalLayoutWidget_3)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.search_button)

        self.line = QFrame(self.horizontalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.edit_button = QPushButton(self.horizontalLayoutWidget_3)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_button.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.edit_button)

        self.delete_button = QPushButton(self.horizontalLayoutWidget_3)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_button.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.delete_button)

        self.line_2 = QFrame(self.horizontalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_button = QPushButton(self.horizontalLayoutWidget_3)
        self.prev_button.setObjectName(u"prev_button")
        self.prev_button.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prev_button.setIcon(icon6)

        self.horizontalLayout.addWidget(self.prev_button)

        self.page_counter_label = QLabel(self.horizontalLayoutWidget_3)
        self.page_counter_label.setObjectName(u"page_counter_label")
        font = QFont()
        font.setBold(True)
        self.page_counter_label.setFont(font)

        self.horizontalLayout.addWidget(self.page_counter_label)

        self.next_button = QPushButton(self.horizontalLayoutWidget_3)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(0, 40))
        self.next_button.setLayoutDirection(Qt.RightToLeft)
        self.next_button.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.next_button.setIcon(icon7)

        self.horizontalLayout.addWidget(self.next_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WPass", None))
        self.open_db_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.prev_button.setText("")
        self.page_counter_label.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.next_button.setText("")
    # retranslateUi

