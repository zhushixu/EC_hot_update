# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_update)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = BodyLabel(Dialog_update)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_app_name = LineEdit(Dialog_update)
        self.lineEdit_app_name.setReadOnly(True)
        self.lineEdit_app_name.setObjectName("lineEdit_app_name")
        self.gridLayout.addWidget(self.lineEdit_app_name, 0, 1, 1, 1)
        self.label_2 = BodyLabel(Dialog_update)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_app_name_2 = LineEdit(Dialog_update)
        self.lineEdit_app_name_2.setReadOnly(True)
        self.lineEdit_app_name_2.setObjectName("lineEdit_app_name_2")
        self.gridLayout.addWidget(self.lineEdit_app_name_2, 1, 1, 1, 1)
        self.label_3 = BodyLabel(Dialog_update)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_app_name_3 = LineEdit(Dialog_update)
        self.lineEdit_app_name_3.setReadOnly(True)
        self.lineEdit_app_name_3.setObjectName("lineEdit_app_name_3")
        self.gridLayout.addWidget(self.lineEdit_app_name_3, 2, 1, 1, 1)
        self.label_4 = BodyLabel(Dialog_update)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_app_name_4 = LineEdit(Dialog_update)
        self.lineEdit_app_name_4.setObjectName("lineEdit_app_name_4")
        self.gridLayout.addWidget(self.lineEdit_app_name_4, 3, 1, 1, 1)
        self.label_5 = BodyLabel(Dialog_update)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_update_toast = ComboBox(Dialog_update)
        self.comboBox_update_toast.setObjectName("comboBox_update_toast")
        self.comboBox_update_toast.addItem("")
        self.comboBox_update_toast.addItem("")
        self.gridLayout.addWidget(self.comboBox_update_toast, 4, 1, 1, 1)
        self.label_6 = BodyLabel(Dialog_update)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboBox_update_force = ComboBox(Dialog_update)
        self.comboBox_update_force.setObjectName("comboBox_update_force")
        self.comboBox_update_force.addItem("")
        self.comboBox_update_force.addItem("")
        self.gridLayout.addWidget(self.comboBox_update_force, 5, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = BodyLabel(Dialog_update)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.textEdit_update_content = TextEdit(Dialog_update)
        self.textEdit_update_content.setObjectName("textEdit_update_content")
        self.horizontalLayout.addWidget(self.textEdit_update_content)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_creat_app = PushButton(Dialog_update)
        self.btn_creat_app.setObjectName("btn_creat_app")
        self.horizontalLayout_2.addWidget(self.btn_creat_app)
        self.btn_creat_app_2 = PrimaryPushButton(Dialog_update)
        self.btn_creat_app_2.setObjectName("btn_creat_app_2")
        self.horizontalLayout_2.addWidget(self.btn_creat_app_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = CheckBox(Dialog_update)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = CheckBox(Dialog_update)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog_update)
        QtCore.QMetaObject.connectSlotsByName(Dialog_update)

    def retranslateUi(self, Dialog_update):
        _translate = QtCore.QCoreApplication.translate
        Dialog_update.setWindowTitle(_translate("Dialog_update", "Dialog"))
        self.label.setText(_translate("Dialog_update", "软件名称"))
        self.label_2.setText(_translate("Dialog_update", "本地路径"))
        self.label_3.setText(_translate("Dialog_update", "现行版本"))
        self.label_4.setText(_translate("Dialog_update", "更新版本"))
        self.label_5.setText(_translate("Dialog_update", "显示弹窗"))
        self.comboBox_update_toast.setItemText(0, _translate("Dialog_update", "false"))
        self.comboBox_update_toast.setItemText(1, _translate("Dialog_update", "true"))
        self.label_6.setText(_translate("Dialog_update", "强制更新"))
        self.comboBox_update_force.setItemText(0, _translate("Dialog_update", "true"))
        self.comboBox_update_force.setItemText(1, _translate("Dialog_update", "false"))
        self.label_7.setText(_translate("Dialog_update", "更新说明"))
        self.btn_creat_app.setText(_translate("Dialog_update", "取消更新"))
        self.btn_creat_app_2.setText(_translate("Dialog_update", "更新软件"))
        self.checkBox.setText(_translate("Dialog_update", "是否弹窗"))
        self.checkBox_2.setText(_translate("Dialog_update", "是否强更"))
from qfluentwidgets import BodyLabel, CheckBox, ComboBox, LineEdit, PrimaryPushButton, PushButton, TextEdit
