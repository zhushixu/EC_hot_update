import json

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog, QHBoxLayout, QStyledItemDelegate, QTableWidget
from ui.ui_main import Ui_Form_main
from shared_variable import Global
from PyQt5.QtCore import Qt, QUrl
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition, RoundMenu, Action, MenuAnimationType, Dialog
from qfluentwidgets import FluentIcon as FIF
from shared_variable import CustomMessageBox, NoticeMessageBox, ChangeMessageBox
from ui.ui_update import Ui_Dialog_update
import os


class MainWindow(QWidget, Ui_Form_main):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # self.btn_refresh_Bucket.clicked.connect(self.button_click)
        self.btn_refresh_App.clicked.connect(self.button_click)
        self.lineEdit_search.textChanged.connect(self.search_software)
        self.g = Global()
        # self.table_appList.itemChanged.connect(self.table_change)  # 设置表格更新监听
        self.table_appList.setEditTriggers(QTableWidget.NoEditTriggers)  # 设置为不允许编辑
        self.table_isEdit = True  # 表格是否编辑模式
        self.refresh_app()

    def contextMenuEvent(self, event):
        selected_items = self.table_appList.selectedItems()
        if not selected_items:
            return
        try:
            self.g.info_name = selected_items[0].text()
            self.g.info_hot_path = selected_items[1].text()
            self.g.info_force_path = selected_items[2].text()
            self.g.info_url_path = selected_items[3].text()
            self.g.info_id = selected_items[4].text()
        except Exception as e:
            print(e)

        # 创建右键菜单
        menu = RoundMenu(parent=self)

        hot_update = Action(FIF.UPDATE, '软件热更')
        menu.addAction(hot_update)

        force_update = Action(FIF.UP, '软件强更')
        menu.addAction(force_update)

        notice = Action(FIF.RINGER, '添加公告')
        menu.addAction(notice)

        update_info = Action(FIF.EDIT, '修改信息')
        menu.addAction(update_info)

        delete_app = Action(FIF.DELETE, '删除应用')
        menu.addAction(delete_app)

        # add sub menu
        submenu = RoundMenu("复制内容", self)
        submenu.setIcon(FIF.COPY)

        copy_hot_update_url = Action(FIF.CALORIES, '热更地址')
        submenu.addAction(copy_hot_update_url)

        copy_force_update_url = Action(FIF.SCROLL, '强更地址')
        submenu.addAction(copy_force_update_url)

        copy_notice_url = Action(FIF.RINGER, '公告地址')
        submenu.addAction(copy_notice_url)

        menu.addMenu(submenu)
        # show menu
        menu.exec(event.globalPos(), aniType=MenuAnimationType.DROP_DOWN)

        hot_update.triggered.connect(self.hot_update)
        force_update.triggered.connect(self.app_update)
        notice.triggered.connect(self.update_notice)
        delete_app.triggered.connect(self.delete_software)
        copy_hot_update_url.triggered.connect(self.copy_hot_update_url)
        copy_force_update_url.triggered.connect(self.copy_force_update_url)
        copy_notice_url.triggered.connect(self.copy_notice_url)
        update_info.triggered.connect(self.change_info)

    def change_info(self):

        try:
            data = {
                'name': self.g.info_name,
                'hot_path': self.g.info_hot_path,
                'force_path': self.g.info_force_path,
                'oss_path': self.g.info_url_path
            }
            w = ChangeMessageBox(data, self)
            if w.exec():
                if w.lineedit_force_path.text() == "" and w.lineedit_hot_path.text() == "":
                    self.createInfo_error_bar('热更新和强更新至少保留一项')
                    return
                if w.lineedit_oss_path.text() == "":
                    self.createInfo_error_bar('存储桶路径都不要你更新个der!')
                    return
                self.g.access_data_update(self.g.info_id, 'update_path', w.lineedit_hot_path.text())
                self.g.access_data_update(self.g.info_id, 'update_app_path', w.lineedit_force_path.text())
                self.g.access_data_update(self.g.info_id, 'update_url', w.lineedit_oss_path.text())
                self.createInfo_success_bar('信息修改成功！')
                self.refresh_app()

        except Exception as e:
            print(e)

    def copy_hot_update_url(self):
        url = self.g.get_host() + f'{self.g.info_url_path}'
        self.g.copy_text(f'{url}/update.json')
        self.createInfo_success_bar('复制成功')

    def copy_force_update_url(self):
        url = self.g.get_host() + f'{self.g.info_url_path}'
        self.g.copy_text(f'{url}/update_app.json')
        self.createInfo_success_bar('复制成功')

    def copy_notice_url(self):
        url = self.g.get_host() + f'{self.g.info_url_path}'
        self.g.copy_text(f'{url}/notice.json')
        self.createInfo_success_bar('复制成功')

    def hot_update(self):
        if self.g.info_hot_path == "":
            self.createInfo_error_bar('热更路径错误！')
            return
        # 获取一下更新文档，找到内容
        self.g.could_get_file(self.g.info_url_path + '/update.json', 'update_tmp.json')
        is_dialog = False
        is_force = True
        version = '1.0.0'
        if os.path.isfile('update_tmp.json'):
            with open('update_tmp.json', 'r', encoding='utf-8') as file:
                content = file.read()
            try:
                content_json = json.loads(content)
                is_dialog = bool(content_json['dialog'].lower() == 'true')
                is_force = bool(content_json['force'].lower() == 'true')
                version = self.g.increment_version(content_json['version'])
            except Exception as e:
                print(e)
        data = {
            'mode': '热更新',
            'name': self.g.info_name,
            'version': version,
            'is_dialog': is_dialog,
            'is_force': is_force
        }
        if os.path.isfile('update_tmp.json'):
            # 将下载的文件删除
            os.remove('update_tmp.json')
        w = CustomMessageBox(data, self)
        if w.exec():
            # 先判断文件是否存在
            if not os.path.isfile(self.g.info_hot_path):
                self.createInfo_error_bar('热更文件不存在！')
                return
            # 重写内容，然后上传
            url_file_name = f'{self.g.info_url_path}/release.iec'
            download_url = self.g.get_host() + url_file_name
            version = w.linedit_version.text()

            dict_ = {
                "download_url": download_url,
                "version": version,
                "dialog": str(w.checkBox_dialog.isChecked()),
                "msg": w.textedit_update_info.toPlainText(),
                "force": str(w.checkBox_force.isChecked()),
                "md5": self.g.get_md5(self.g.info_hot_path)
            }
            # 上传更新说明文档
            upload_notes_result = self.g.put_object(self.g.bucket_name, json.dumps(dict_, ensure_ascii=False),
                                                    f'{self.g.info_url_path}/update.json')
            # 上传文件
            upload_file_result = self.g.upload_file(self.g.bucket_name, self.g.info_hot_path, url_file_name)
            # print(upload_file_result,upload_notes_result)
            if upload_notes_result and upload_file_result:
                self.createInfo_success_bar('软件更新完成')
            else:
                self.createInfo_error_bar('软件更新失败')

    def app_update(self):
        # print(self.g.info_mode)
        if self.g.info_force_path == "":
            self.createInfo_error_bar('强更路径错误！')
            return
        # 获取一下更新文档，找到内容
        self.g.could_get_file(self.g.info_url_path + '/update_app.json', 'update_app_tmp.json')
        is_dialog = False
        is_force = True
        version = '1.0.0'
        if os.path.isfile('update_app_tmp.json'):
            with open('update_app_tmp.json', 'r', encoding='utf-8') as file:
                content = file.read()
            try:
                content_json = json.loads(content)
                is_dialog = bool(content_json['dialog'].lower() == 'true')
                is_force = bool(content_json['force'].lower() == 'true')
                version = self.g.increment_version(content_json['version'])
            except Exception as e:
                print(e)
        data = {
            'mode': '强更新',
            'name': self.g.info_name,
            'version': version,
            'is_dialog': is_dialog,
            'is_force': is_force
        }
        if os.path.isfile('update_app_tmp.json'):
            # 将下载的文件删除
            os.remove('update_app_tmp.json')
        w = CustomMessageBox(data, self)
        if w.exec():
            # 先判断文件是否存在
            if not os.path.isfile(self.g.info_hot_path):
                self.createInfo_error_bar('APK文件不存在！')
                return
            # 重写内容，然后上传
            url_file_name = f'{self.g.info_url_path}/release.apk'
            download_url = self.g.get_host() + url_file_name
            version = w.linedit_version.text()

            dict_ = {
                "download_url": download_url,
                "version": version,
                "dialog": str(w.checkBox_dialog.isChecked()),
                "msg": w.textedit_update_info.toPlainText(),
                "force": str(w.checkBox_force.isChecked()),
                "md5": self.g.get_md5(self.g.info_hot_path)
            }
            # 上传更新说明文档
            upload_notes_result = self.g.put_object(self.g.bucket_name, json.dumps(dict_, ensure_ascii=False),
                                                    f'{self.g.info_url_path}/update_app.json')
            # 上传文件
            upload_file_result = self.g.upload_file(self.g.bucket_name, self.g.info_force_path, url_file_name)
            if upload_notes_result and upload_file_result:
                self.createInfo_success_bar('软件更新完成')
            else:
                self.createInfo_error_bar('软件更新失败')

    def update_notice(self):
        w = NoticeMessageBox(self)
        if w.exec():
            print(w.textedit_notice_info.toPlainText())
            dict_ = {
                'ret': '1',
                'notice': w.textedit_notice_info.toPlainText()
            }
            result = self.g.put_object(self.g.bucket_name, json.dumps(dict_, ensure_ascii=False),
                                       self.g.info_url_path + '/notice.json')
            if result:
                self.createInfo_success_bar('公告更新成功')
            else:
                self.createInfo_error_bar('公告更新失败')

    def delete_software(self):
        # 弹窗询问是否确认删除
        w = Dialog('确认删除？', f'确定要删除【{self.g.info_name}】软件吗？此操作是不可逆的！')
        w.yesButton.setText("确定删除")
        w.cancelButton.setText("不删了")
        if not w.exec():
            return
            # 先删除数据库的内容
        self.g.access_data_delete(self.g.info_id)
        # 删除对象存储的文件
        self.g.could_delete_file(self.g.bucket_name, self.g.info_url_path)
        self.createInfo_success_bar('删除完成')
        self.refresh_app()
        # pass

    def table_change(self, item):
        """用来检测更新table的操作"""
        if self.table_isEdit:
            print(
                f'Item edited: {item.row()}, {item.column()} - New value: {item.text()},id:{self.table_appList.item(item.row(), self.table_get_column_index("ID")).text()}')
            update_id = self.table_appList.item(item.row(), self.table_get_column_index("ID")).text()
            row = item.row()  # 行
            column = item.column()  # 列
            name = ''
            value = item.text()
            # print(value)
            if column == self.table_get_column_index("ID"):
                return
            elif column == self.table_get_column_index("名称"):
                if value == "":
                    print("名称不允许为空")
                    self.createInfo_error_bar('软件名称不允许为空')
                    self.refresh_app()
                    return
                name = 'name'
            elif column == self.table_get_column_index("热更路径"):
                name = 'update_path'
            elif column == self.table_get_column_index("强更路径"):
                name = 'update_app_path'
            elif column == self.table_get_column_index("远程地址"):
                name = 'update_url'
            result = self.g.access_data_update(update_id, name, value)
            if result:
                self.createInfo_success_bar('信息修改成功')
            else:
                self.createInfo_error_bar('信息修改失败')

    def button_click(self):
        btn_name = self.sender().objectName()
        if btn_name == "btn_refresh_App":
            self.refresh_app()

        # elif btn_name == "btn_creat":
        #     creat_form = QDialog(self)
        #     creat_form.exec_()
    def search_software(self):
        self.refresh_app()

    def refresh_app(self):
        """
        这个完全以数据库为主体，忽略对象存储的内容
        :param mode: 0:刷新所有，1：搜索指定
        :return:
        """
        self.table_appList.clearContents()
        self.table_appList.setRowCount(0)  # 将行数设置为0，从而删除所有行
        name = self.lineEdit_search.text()
        if name == "":
            data = self.g.access_data_get_all_app()
        else:
            data = self.g.access_date_search(name)
        self.table_isEdit = False
        # print(data)
        for j in data:
            data_ = {
                'ID': str(j[0]),
                '名称': j[1],
                '热更路径': j[2],
                '强更路径': j[3],
                '远程地址': j[4]
            }
            self.table_addRow(data_)
        self.table_appList.setColumnWidth(self.table_get_column_index('名称'), 150)
        self.table_appList.setColumnWidth(self.table_get_column_index('热更路径'), 200)
        self.table_appList.setColumnWidth(self.table_get_column_index('强更路径'), 200)
        self.table_appList.setColumnWidth(self.table_get_column_index('远程地址'), 180)
        self.table_appList.setColumnWidth(self.table_get_column_index('ID'), 0)
        self.table_isEdit = True

    def table_addRow(self, data):
        column_count = self.table_appList.columnCount()
        column_names = [self.table_appList.horizontalHeaderItem(i).text() for i in range(column_count)]
        # 获取当前行数
        current_row = self.table_appList.rowCount()
        # 插入一行
        self.table_appList.insertRow(current_row)
        for key in data:
            # print(key, data[key])
            item = QTableWidgetItem(data[key])
            column_index = column_names.index(key) if key in key else -1
            self.table_appList.setItem(current_row, column_index, item)

    def table_get_column_index(self, name):
        """
        输入标题名称，返回当前标题的列索引
        :param name: 标题名称
        :return: 当前标题的列索引
        """
        column_count = self.table_appList.columnCount()
        column_names = [self.table_appList.horizontalHeaderItem(i).text() for i in range(column_count)]
        column_index = column_names.index(name) if name in name else -1
        return column_index

    def createInfo_error_bar(self, content):
        w = InfoBar(InfoBarIcon.ERROR, title='错误', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()

    def createInfo_success_bar(self, content):
        w = InfoBar(InfoBarIcon.SUCCESS, title='成功', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()



class updatewindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_update()
        self.ui.setupUi(self)
