# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logs.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(583, 391)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.log_title = QLabel(Form)
        self.log_title.setObjectName(u"log_title")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.log_title.setFont(font1)
        self.log_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.log_title)

        self.available_logs = QComboBox(Form)
        self.available_logs.setObjectName(u"available_logs")

        self.verticalLayout.addWidget(self.available_logs)

        self.log = QTextBrowser(Form)
        self.log.setObjectName(u"log")

        self.verticalLayout.addWidget(self.log)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.log_title.setText("")
    # retranslateUi

