# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledKiGCQd.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject)
from PyQt5.QtGui import (QColor)
from PyQt5.QtWidgets import *
from pyqt_color_picker import ColorPickerWidget

from settings import Settings


class Ui_SettingsWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.color = QColor()
        self.setupUi()


    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"SettingsWindow")
        self.resize(312, 113)
        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName(u"formLayout")
        self.default_level_label = QLabel(self)
        self.default_level_label.setObjectName(u"default_level_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.default_level_label)

        self.level_text_edit = QLineEdit(self)
        self.level_text_edit.setObjectName(u"level_text_edit")
        self.level_text_edit.setText(str(Settings.level_number))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.level_text_edit)

        self.color_label = QLabel(self)
        self.color_label.setObjectName(u"color_label")


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.color_label)

        self.__colorPicker = ColorPickerWidget(Settings.color, 'vertical')
        self.__colorPicker.colorChanged.connect(self.color_changed)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.__colorPicker)

        self.save_button = QPushButton(self)
        self.save_button.setObjectName(u"save_button")
        self.save_button.clicked.connect(self.save_changes)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.save_button)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.default_level_label.setText(QCoreApplication.translate("SettingsWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.color_label.setText(QCoreApplication.translate("SettingsWindow", u"\u0426\u0432\u0435\u0442", None))
        self.save_button.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))

    def color_changed(self, color):
        self.color = color

    def save_changes(self):
        Settings.level_number = int(self.level_text_edit.text())
        Settings.color = self.color


