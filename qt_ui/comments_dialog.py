# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comments_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 372)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.comments = QFormLayout()
        self.comments.setObjectName(u"comments")
        self.comments.setHorizontalSpacing(12)

        self.verticalLayout.addLayout(self.comments)

        self.comment = QLineEdit(Dialog)
        self.comment.setObjectName(u"comment")

        self.verticalLayout.addWidget(self.comment)

        self.add_comment = QPushButton(Dialog)
        self.add_comment.setObjectName(u"add_comment")

        self.verticalLayout.addWidget(self.add_comment)

        self.confirm = QPushButton(Dialog)
        self.confirm.setObjectName(u"confirm")

        self.verticalLayout.addWidget(self.confirm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comment.setPlaceholderText(QCoreApplication.translate("Dialog", u"Bez\u00fcglich dieser Aktion denke ich...", None))
        self.add_comment.setText(QCoreApplication.translate("Dialog", u"Kommentar hinzuf\u00fcgen", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"Verstanden", None))
    # retranslateUi

