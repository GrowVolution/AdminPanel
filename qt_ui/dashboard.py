# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(741, 572)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(16)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.site_status = QLabel(Form)
        self.site_status.setObjectName(u"site_status")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.site_status.setFont(font2)
        self.site_status.setMargin(0)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.site_status)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.server_status = QLabel(Form)
        self.server_status.setObjectName(u"server_status")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.server_status.setFont(font3)
        self.server_status.setTextFormat(Qt.TextFormat.RichText)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.server_status)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.api_log = QTextBrowser(Form)
        self.api_log.setObjectName(u"api_log")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.api_log)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.admins = QLabel(Form)
        self.admins.setObjectName(u"admins")
        self.admins.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.admins)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.site_log = QTextBrowser(Form)
        self.site_log.setObjectName(u"site_log")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.site_log)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.worker_log = QTextBrowser(Form)
        self.worker_log.setObjectName(u"worker_log")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.worker_log)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.worker_status = QLabel(Form)
        self.worker_status.setObjectName(u"worker_status")
        self.worker_status.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.worker_status)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Status der Hauptseite:", None))
        self.site_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Server Status:", None))
        self.server_status.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>CPU Auslastung: {cpu}<br/>Arbeitsspeicher: {ram}<br/>Festplatte: {disk}</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"API Server Log:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Administratoren:", None))
        self.admins.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Site Server Log:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Worker Log:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Status des Workers:", None))
        self.worker_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

