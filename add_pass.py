# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pass.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class AddPass(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(520, 420)
        Dialog.setMinimumSize(QSize(520, 420))
        Dialog.setMaximumSize(QSize(520, 420))
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 501, 401))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name_field = QLineEdit(self.formLayoutWidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_field)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.login_field = QLineEdit(self.formLayoutWidget)
        self.login_field.setObjectName(u"login_field")
        self.login_field.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.login_field)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.pass_field = QLineEdit(self.formLayoutWidget)
        self.pass_field.setObjectName(u"pass_field")
        self.pass_field.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pass_field)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.url_field = QLineEdit(self.formLayoutWidget)
        self.url_field.setObjectName(u"url_field")
        self.url_field.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.url_field)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 34))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.notes_field = QPlainTextEdit(self.formLayoutWidget)
        self.notes_field.setObjectName(u"notes_field")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.notes_field)

        self.submit_button = QPushButton(self.formLayoutWidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.submit_button.setIcon(icon1)
        self.submit_button.setAutoDefault(False)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.submit_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Url:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u0438\u0441\u0438:", None))
        self.submit_button.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

