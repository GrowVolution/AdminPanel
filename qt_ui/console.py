# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(689, 535)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shell = QTextBrowser(Form)
        self.shell.setObjectName(u"shell")

        self.verticalLayout.addWidget(self.shell)

        self.command_line = QLineEdit(Form)
        self.command_line.setObjectName(u"command_line")

        self.verticalLayout.addWidget(self.command_line)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.command_line.setPlaceholderText(QCoreApplication.translate("Form", u"/bin/bash _", None))
    # retranslateUi

