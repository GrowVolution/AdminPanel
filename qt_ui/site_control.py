# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'site_control.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(674, 383)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.sync_sandbox = QPushButton(Form)
        self.sync_sandbox.setObjectName(u"sync_sandbox")

        self.verticalLayout.addWidget(self.sync_sandbox)

        self.critical_actions = QGroupBox(Form)
        self.critical_actions.setObjectName(u"critical_actions")
        self.verticalLayout_2 = QVBoxLayout(self.critical_actions)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clear_logs = QPushButton(self.critical_actions)
        self.clear_logs.setObjectName(u"clear_logs")

        self.verticalLayout_2.addWidget(self.clear_logs)

        self.deploy_updates = QPushButton(self.critical_actions)
        self.deploy_updates.setObjectName(u"deploy_updates")

        self.verticalLayout_2.addWidget(self.deploy_updates)


        self.verticalLayout.addWidget(self.critical_actions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Server Steuerung", None))
        self.sync_sandbox.setText(QCoreApplication.translate("Form", u"Sanbox Sync", None))
        self.critical_actions.setTitle(QCoreApplication.translate("Form", u"Kritische Aktionen", None))
        self.clear_logs.setText(QCoreApplication.translate("Form", u"Logs leeren", None))
        self.deploy_updates.setText(QCoreApplication.translate("Form", u"Aktualisieren", None))
    # retranslateUi

