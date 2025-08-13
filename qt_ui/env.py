# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 450)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(30)
        self.new_var_value = QLineEdit(Form)
        self.new_var_value.setObjectName(u"new_var_value")
        font = QFont()
        font.setPointSize(12)
        self.new_var_value.setFont(font)

        self.gridLayout.addWidget(self.new_var_value, 5, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setVerticalSpacing(18)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.env_select = QComboBox(Form)
        self.env_select.setObjectName(u"env_select")
        self.env_select.setFont(font)

        self.verticalLayout_2.addWidget(self.env_select)

        self.new_var_name = QLineEdit(Form)
        self.new_var_name.setObjectName(u"new_var_name")
        self.new_var_name.setFont(font)

        self.verticalLayout_2.addWidget(self.new_var_name)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.env_groups = QListWidget(Form)
        self.env_groups.setObjectName(u"env_groups")
        self.env_groups.setFont(font)

        self.verticalLayout.addWidget(self.env_groups)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.verticalLayout)


        self.gridLayout.addLayout(self.formLayout, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.set_value = QPushButton(Form)
        self.set_value.setObjectName(u"set_value")
        self.set_value.setFont(font)

        self.horizontalLayout.addWidget(self.set_value)

        self.del_value = QPushButton(Form)
        self.del_value.setObjectName(u"del_value")
        self.del_value.setFont(font)

        self.horizontalLayout.addWidget(self.del_value)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.new_var_value.setPlaceholderText(QCoreApplication.translate("Form", u"Neuer Variablenwert...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Aktive Variablen:", None))
        self.new_var_name.setPlaceholderText(QCoreApplication.translate("Form", u"VAR_EXAMPLE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Umgebungsgruppen:", None))
        self.set_value.setText(QCoreApplication.translate("Form", u"Aktualisieren", None))
        self.del_value.setText(QCoreApplication.translate("Form", u"L\u00f6schen", None))
        self.label.setText(QCoreApplication.translate("Form", u"Umgebungsvariablen", None))
    # retranslateUi

