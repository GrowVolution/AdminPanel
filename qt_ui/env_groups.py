# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env_groups.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(687, 473)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(18)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(12)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.existing_groups = QListWidget(Form)
        self.existing_groups.setObjectName(u"existing_groups")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.existing_groups)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.my_groups = QListWidget(Form)
        self.my_groups.setObjectName(u"my_groups")

        self.verticalLayout.addWidget(self.my_groups)

        self.new_group = QLineEdit(Form)
        self.new_group.setObjectName(u"new_group")

        self.verticalLayout.addWidget(self.new_group)

        self.add_group = QPushButton(Form)
        self.add_group.setObjectName(u"add_group")

        self.verticalLayout.addWidget(self.add_group)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.verticalLayout)


        self.gridLayout.addLayout(self.formLayout, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.protect = QPushButton(Form)
        self.protect.setObjectName(u"protect")

        self.horizontalLayout_2.addWidget(self.protect)

        self.unprotect = QPushButton(Form)
        self.unprotect.setObjectName(u"unprotect")

        self.horizontalLayout_2.addWidget(self.unprotect)

        self.change_ownership = QPushButton(Form)
        self.change_ownership.setObjectName(u"change_ownership")

        self.horizontalLayout_2.addWidget(self.change_ownership)

        self.delete_2 = QPushButton(Form)
        self.delete_2.setObjectName(u"delete_2")

        self.horizontalLayout_2.addWidget(self.delete_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)

        self.suggest_for_production = QPushButton(Form)
        self.suggest_for_production.setObjectName(u"suggest_for_production")

        self.gridLayout.addWidget(self.suggest_for_production, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Bestehende Grupper:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Meine Gruppen:", None))
        self.new_group.setPlaceholderText(QCoreApplication.translate("Form", u"Meine neue Gruppe", None))
        self.add_group.setText(QCoreApplication.translate("Form", u"Hinzuf\u00fcgen", None))
        self.protect.setText(QCoreApplication.translate("Form", u"Sch\u00fctzen", None))
        self.unprotect.setText(QCoreApplication.translate("Form", u"Freigeben", None))
        self.change_ownership.setText(QCoreApplication.translate("Form", u"Eigentum \u00fcbertragen", None))
        self.delete_2.setText(QCoreApplication.translate("Form", u"L\u00f6schen", None))
        self.suggest_for_production.setText(QCoreApplication.translate("Form", u"Als Produktionsumgebung nominieren", None))
        self.label.setText(QCoreApplication.translate("Form", u"Umgebungsgruppen", None))
    # retranslateUi

