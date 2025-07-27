# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sandbox.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(596, 426)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(18)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.sandbox_control = QPushButton(Form)
        self.sandbox_control.setObjectName(u"sandbox_control")
        font = QFont()
        font.setPointSize(12)
        self.sandbox_control.setFont(font)

        self.gridLayout.addWidget(self.sandbox_control, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setVerticalSpacing(12)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.container_status = QLabel(Form)
        self.container_status.setObjectName(u"container_status")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.container_status.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.container_status)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.containers_active = QLabel(Form)
        self.containers_active.setObjectName(u"containers_active")
        self.containers_active.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.containers_active)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.notes = QTextBrowser(Form)
        self.notes.setObjectName(u"notes")
        self.notes.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.notes)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.dev_note = QLineEdit(Form)
        self.dev_note.setObjectName(u"dev_note")
        self.dev_note.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dev_note)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.public_key = QPlainTextEdit(Form)
        self.public_key.setObjectName(u"public_key")
        self.public_key.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.public_key)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.env_group = QComboBox(Form)
        self.env_group.setObjectName(u"env_group")
        self.env_group.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.env_group)


        self.gridLayout.addLayout(self.formLayout, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.sandbox_control.setText(QCoreApplication.translate("Form", u"Container {command}", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Container l\u00e4uft:", None))
        self.container_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Aktive Container:", None))
        self.containers_active.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Entwicklernotizen:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Deine Notiz:", None))
        self.dev_note.setPlaceholderText(QCoreApplication.translate("Form", u"Arbeite gerade an ...", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Public Key (ssh):", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Debug Umgebung:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Meine Sandbox", None))
    # retranslateUi

