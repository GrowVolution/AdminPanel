# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(488, 291)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(18)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.username_label = QLabel(Form)
        self.username_label.setObjectName(u"username_label")
        font = QFont()
        font.setPointSize(12)
        self.username_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.username_label)

        self.username = QLineEdit(Form)
        self.username.setObjectName(u"username")
        self.username.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.username)

        self.psw_label = QLabel(Form)
        self.psw_label.setObjectName(u"psw_label")
        self.psw_label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.psw_label)

        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.password)

        self.create_new = QCheckBox(Form)
        self.create_new.setObjectName(u"create_new")
        self.create_new.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.create_new)

        self.creation_token = QLineEdit(Form)
        self.creation_token.setObjectName(u"creation_token")
        self.creation_token.setEnabled(True)
        self.creation_token.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.creation_token)


        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)

        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setFont(font)

        self.gridLayout_2.addWidget(self.login_btn, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"Benutzername: ", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"admin", None))
        self.psw_label.setText(QCoreApplication.translate("Form", u"Passwort: ", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"**********", None))
        self.create_new.setText(QCoreApplication.translate("Form", u"Neu anlegen", None))
        self.creation_token.setPlaceholderText(QCoreApplication.translate("Form", u"Dein Einmaltoken", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"Anmelden", None))
    # retranslateUi

