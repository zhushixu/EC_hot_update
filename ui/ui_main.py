# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(745, 601)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_main)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = BodyLabel(Form_main)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_search = LineEdit(Form_main)
        self.lineEdit_search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.btn_refresh_App = PushButton(Form_main)
        self.btn_refresh_App.setObjectName("btn_refresh_App")
        self.horizontalLayout.addWidget(self.btn_refresh_App)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_appList = TableWidget(Form_main)
        self.table_appList.setObjectName("table_appList")
        self.table_appList.setColumnCount(5)
        self.table_appList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_appList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_appList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_appList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_appList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_appList.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.table_appList)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "Form"))
        self.label_4.setText(_translate("Form_main", "搜索软件"))
        self.btn_refresh_App.setText(_translate("Form_main", "刷新软件"))
        item = self.table_appList.horizontalHeaderItem(0)
        item.setText(_translate("Form_main", "名称"))
        item = self.table_appList.horizontalHeaderItem(1)
        item.setText(_translate("Form_main", "热更路径"))
        item = self.table_appList.horizontalHeaderItem(2)
        item.setText(_translate("Form_main", "强更路径"))
        item = self.table_appList.horizontalHeaderItem(3)
        item.setText(_translate("Form_main", "远程地址"))
        item = self.table_appList.horizontalHeaderItem(4)
        item.setText(_translate("Form_main", "ID"))
from qfluentwidgets import BodyLabel, LineEdit, PushButton, TableWidget