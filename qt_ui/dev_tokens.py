# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dev_tokens.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 407)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(30)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setVerticalSpacing(12)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.token_select = QComboBox(Form)
        self.token_select.setObjectName(u"token_select")
        self.token_select.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.token_select)

        self.new_token_label = QLabel(Form)
        self.new_token_label.setObjectName(u"new_token_label")
        self.new_token_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.new_token_label)

        self.new_token_settings = QWidget(Form)
        self.new_token_settings.setObjectName(u"new_token_settings")
        self.verticalLayout = QVBoxLayout(self.new_token_settings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(12)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.new_token_name = QLineEdit(self.new_token_settings)
        self.new_token_name.setObjectName(u"new_token_name")
        self.new_token_name.setFont(font1)

        self.vertical_layout.addWidget(self.new_token_name)

        self.valid_select = QComboBox(self.new_token_settings)
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.addItem("")
        self.valid_select.setObjectName(u"valid_select")
        self.valid_select.setFont(font1)

        self.vertical_layout.addWidget(self.valid_select)


        self.verticalLayout.addLayout(self.vertical_layout)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.new_token_settings)


        self.gridLayout.addLayout(self.formLayout, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_token = QPushButton(Form)
        self.create_token.setObjectName(u"create_token")
        self.create_token.setFont(font1)

        self.horizontalLayout.addWidget(self.create_token)

        self.del_token = QPushButton(Form)
        self.del_token.setObjectName(u"del_token")
        self.del_token.setFont(font1)

        self.horizontalLayout.addWidget(self.del_token)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)


        self.retranslateUi(Form)

        self.valid_select.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Entwickler Tokens", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Aktive Tokens:", None))
        self.new_token_label.setText(QCoreApplication.translate("Form", u"Neues Token:", None))
        self.new_token_name.setPlaceholderText(QCoreApplication.translate("Form", u"Token name...", None))
        self.valid_select.setItemText(0, QCoreApplication.translate("Form", u"5 Tage g\u00fcltig", None))
        self.valid_select.setItemText(1, QCoreApplication.translate("Form", u"15 Tage g\u00fcltig", None))
        self.valid_select.setItemText(2, QCoreApplication.translate("Form", u"30 Tage g\u00fcltig (standard)", None))
        self.valid_select.setItemText(3, QCoreApplication.translate("Form", u"60 Tage g\u00fcltig", None))
        self.valid_select.setItemText(4, QCoreApplication.translate("Form", u"90 Tage g\u00fcltig", None))
        self.valid_select.setItemText(5, QCoreApplication.translate("Form", u"180 Tage g\u00fcltig", None))
        self.valid_select.setItemText(6, QCoreApplication.translate("Form", u"365 Tage g\u00fcltig", None))

        self.create_token.setText(QCoreApplication.translate("Form", u"Erstellen", None))
        self.del_token.setText(QCoreApplication.translate("Form", u"L\u00f6schen", None))
    # retranslateUi

