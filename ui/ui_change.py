# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_update(object):
    def setupUi(self, Dialog_update):
        Dialog_update.setObjectName("Dialog_update")
        Dialog_update.resize(586, 509)
        self.widget = QtWidgets.QWidget(Dialog_update)
        self.widget.setGeometry(QtCore.QRect(170, 20, 189, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = BodyLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_app_name = LineEdit(self.widget)
        self.lineEdit_app_name.setReadOnly(True)
        self.lineEdit_app_name.setObjectName("lineEdit_app_name")
        self.horizontalLayout.addWidget(self.lineEdit_app_name)
        self.widget1 = QtWidgets.QWidget(Dialog_update)
        self.widget1.setGeometry(QtCore.QRect(150, 50, 213, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = BodyLabel(self.widget1)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_hot_update_path = LineEdit(self.widget1)
        self.lineEdit_hot_update_path.setObjectName("lineEdit_hot_update_path")
        self.horizontalLayout_2.addWidget(self.lineEdit_hot_update_path)
        self.widget2 = QtWidgets.QWidget(Dialog_update)
        self.widget2.setGeometry(QtCore.QRect(150, 80, 213, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = BodyLabel(self.widget2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_force_update_path = LineEdit(self.widget2)
        self.lineEdit_force_update_path.setObjectName("lineEdit_force_update_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_force_update_path)
        self.widget3 = QtWidgets.QWidget(Dialog_update)
        self.widget3.setGeometry(QtCore.QRect(150, 110, 213, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = BodyLabel(self.widget3)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_OSS_path = LineEdit(self.widget3)
        self.lineEdit_OSS_path.setObjectName("lineEdit_OSS_path")
        self.horizontalLayout_4.addWidget(self.lineEdit_OSS_path)

        self.retranslateUi(Dialog_update)
        QtCore.QMetaObject.connectSlotsByName(Dialog_update)

    def retranslateUi(self, Dialog_update):
        _translate = QtCore.QCoreApplication.translate
        Dialog_update.setWindowTitle(_translate("Dialog_update", "Dialog"))
        self.label.setText(_translate("Dialog_update", "软件名称"))
        self.label_2.setText(_translate("Dialog_update", "热更本地路径"))
        self.label_3.setText(_translate("Dialog_update", "强更本地路径"))
        self.label_4.setText(_translate("Dialog_update", "对象存储路径"))
from qfluentwidgets import BodyLabel, LineEdit
