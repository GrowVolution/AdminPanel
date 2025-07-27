# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_browser.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(685, 482)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(12)
        self.backend = QLineEdit(self.centralwidget)
        self.backend.setObjectName(u"backend")
        font = QFont()
        font.setPointSize(12)
        self.backend.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.backend)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.subdomain = QLineEdit(self.centralwidget)
        self.subdomain.setObjectName(u"subdomain")
        self.subdomain.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subdomain)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.path = QLineEdit(self.centralwidget)
        self.path.setObjectName(u"path")
        self.path.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.path)


        self.verticalLayout.addLayout(self.formLayout)

        self.browser = QWebEngineView(self.centralwidget)
        self.browser.setObjectName(u"browser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.browser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 685, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backend.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Backend:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Subdomain:", None))
        self.subdomain.setPlaceholderText(QCoreApplication.translate("MainWindow", u"www", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Route Path:", None))
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/", None))
    # retranslateUi

