# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectcode.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(221, 219)
        self.listWidget = QListWidget(dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 221, 201))
        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-1, 199, 113, 21))
        self.pushButton_2 = QPushButton(dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(109, 199, 113, 21))

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\ucf54\ub4dc \uc120\ud0dd", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"\uc120\ud0dd", None))
        self.pushButton_2.setText(QCoreApplication.translate("dialog", u"\ucde8\uc18c", None))
    # retranslateUi

