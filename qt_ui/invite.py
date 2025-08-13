# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invite.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(595, 428)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(12)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(12)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.name)

        self.email = QLineEdit(Form)
        self.email.setObjectName(u"email")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.email)

        self.info = QTextEdit(Form)
        self.info.setObjectName(u"info")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.info)


        self.gridLayout.addLayout(self.formLayout, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.invite = QPushButton(Form)
        self.invite.setObjectName(u"invite")

        self.gridLayout.addWidget(self.invite, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Admin einladen", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Info:", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("Form", u"Max Muster", None))
        self.email.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("Form", u"max.muster@growv-mail.org", None))
        self.info.setPlaceholderText(QCoreApplication.translate("Form", u"Max ist ein guter Freund von mir, sehr engagiert und m\u00f6chte uns in unserem Wirken unterst\u00fctzen. [...]", None))
        self.invite.setText(QCoreApplication.translate("Form", u"Einladen", None))
    # retranslateUi

