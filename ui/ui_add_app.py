# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_add_app(object):
    def setupUi(self, Form_add_app):
        Form_add_app.setObjectName("Form_add_app")
        Form_add_app.resize(775, 576)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_add_app)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 4, 1, 1)
        self.label_3 = BodyLabel(Form_add_app)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_update_toast = ComboBox(Form_add_app)
        self.comboBox_update_toast.setObjectName("comboBox_update_toast")
        self.comboBox_update_toast.addItem("")
        self.comboBox_update_toast.addItem("")
        self.gridLayout.addWidget(self.comboBox_update_toast, 5, 2, 1, 3)
        self.label_9 = BodyLabel(Form_add_app)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.lineEdit_OSS_path = LineEdit(Form_add_app)
        self.lineEdit_OSS_path.setObjectName("lineEdit_OSS_path")
        self.gridLayout.addWidget(self.lineEdit_OSS_path, 3, 2, 1, 3)
        self.btn_creat_app = PushButton(Form_add_app)
        self.btn_creat_app.setObjectName("btn_creat_app")
        self.gridLayout.addWidget(self.btn_creat_app, 8, 3, 1, 1)
        self.label = BodyLabel(Form_add_app)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = BodyLabel(Form_add_app)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_Version = LineEdit(Form_add_app)
        self.lineEdit_Version.setObjectName("lineEdit_Version")
        self.gridLayout.addWidget(self.lineEdit_Version, 4, 2, 1, 3)
        self.label_6 = BodyLabel(Form_add_app)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_2 = BodyLabel(Form_add_app)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_update_force = ComboBox(Form_add_app)
        self.comboBox_update_force.setObjectName("comboBox_update_force")
        self.comboBox_update_force.addItem("")
        self.comboBox_update_force.addItem("")
        self.gridLayout.addWidget(self.comboBox_update_force, 6, 2, 1, 3)
        self.lineEdit_hot_update_path = LineEdit(Form_add_app)
        self.lineEdit_hot_update_path.setObjectName("lineEdit_hot_update_path")
        self.gridLayout.addWidget(self.lineEdit_hot_update_path, 1, 2, 1, 3)
        self.textEdit_update_content = TextEdit(Form_add_app)
        self.textEdit_update_content.setObjectName("textEdit_update_content")
        self.gridLayout.addWidget(self.textEdit_update_content, 7, 2, 1, 3)
        self.label_7 = BodyLabel(Form_add_app)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_5 = BodyLabel(Form_add_app)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_force_update_path = LineEdit(Form_add_app)
        self.lineEdit_force_update_path.setObjectName("lineEdit_force_update_path")
        self.gridLayout.addWidget(self.lineEdit_force_update_path, 2, 2, 1, 3)
        self.lineEdit_app_name = LineEdit(Form_add_app)
        self.lineEdit_app_name.setObjectName("lineEdit_app_name")
        self.gridLayout.addWidget(self.lineEdit_app_name, 0, 2, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form_add_app)
        QtCore.QMetaObject.connectSlotsByName(Form_add_app)

    def retranslateUi(self, Form_add_app):
        _translate = QtCore.QCoreApplication.translate
        Form_add_app.setWindowTitle(_translate("Form_add_app", "Form"))
        self.label_3.setText(_translate("Form_add_app", "强更本地路径"))
        self.comboBox_update_toast.setItemText(0, _translate("Form_add_app", "false"))
        self.comboBox_update_toast.setItemText(1, _translate("Form_add_app", "true"))
        self.label_9.setText(_translate("Form_add_app", "强制更新"))
        self.btn_creat_app.setText(_translate("Form_add_app", "新建软件"))
        self.label.setText(_translate("Form_add_app", "软件名称"))
        self.label_4.setText(_translate("Form_add_app", "对象存储路径"))
        self.lineEdit_Version.setText(_translate("Form_add_app", "1.0.0"))
        self.label_6.setText(_translate("Form_add_app", "更新弹窗"))
        self.label_2.setText(_translate("Form_add_app", "热更本地路径"))
        self.comboBox_update_force.setItemText(0, _translate("Form_add_app", "true"))
        self.comboBox_update_force.setItemText(1, _translate("Form_add_app", "false"))
        self.label_7.setText(_translate("Form_add_app", "更新说明"))
        self.label_5.setText(_translate("Form_add_app", "现行版本"))
from qfluentwidgets import BodyLabel, ComboBox, LineEdit, PushButton, TextEdit
