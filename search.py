# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Search_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 384, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.search_field = QLineEdit(self.verticalLayoutWidget)
        self.search_field.setObjectName(u"search_field")
        self.search_field.setMinimumSize(QSize(0, 34))

        self.horizontalLayout.addWidget(self.search_field)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.radio_button_name = QRadioButton(self.verticalLayoutWidget)
        self.radio_button_name.setObjectName(u"radio_button_name")

        self.verticalLayout.addWidget(self.radio_button_name)

        self.radio_button_login = QRadioButton(self.verticalLayoutWidget)
        self.radio_button_login.setObjectName(u"radio_button_login")

        self.verticalLayout.addWidget(self.radio_button_login)

        self.radio_button_url = QRadioButton(self.verticalLayoutWidget)
        self.radio_button_url.setObjectName(u"radio_button_url")

        self.verticalLayout.addWidget(self.radio_button_url)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.seacrh_button = QPushButton(self.verticalLayoutWidget)
        self.seacrh_button.setObjectName(u"seacrh_button")
        self.seacrh_button.setMinimumSize(QSize(280, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.seacrh_button.setIcon(icon1)
        self.seacrh_button.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.seacrh_button)

        self.throw_off_button = QPushButton(self.verticalLayoutWidget)
        self.throw_off_button.setObjectName(u"throw_off_button")
        self.throw_off_button.setMinimumSize(QSize(0, 40))
        self.throw_off_button.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.throw_off_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a:", None))
        self.radio_button_name.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.radio_button_login.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u043b\u043e\u0433\u0438\u043d\u0443", None))
        self.radio_button_url.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u0441\u0441\u044b\u043b\u043a\u0435", None))
        self.seacrh_button.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.throw_off_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
    # retranslateUi

