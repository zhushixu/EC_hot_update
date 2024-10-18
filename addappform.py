import json
import os
import hashlib
from PyQt5.QtWidgets import QWidget
from ui.ui_add_app import Ui_Form_add_app
from shared_variable import Global
from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition


class AddappWindow(QWidget, Ui_Form_add_app):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.btn_creat_app.clicked.connect(self.button_click)
        # self.btn_refresh_Bucket.clicked.connect(self.button_click)
        self.g = Global()
    def button_click(self):
        btn_name = self.sender().objectName()
        if btn_name == "btn_creat_app":
            # if self.comboBox_BucketList.currentIndex() == -1:
            #     self.createInfo_error_bar('请选择存储桶名称')
            #     return
            if self.g.bucket_name == "":
                self.createInfo_error_bar('请先配置OSS')
                return
            if self.lineEdit_app_name.text() == "":
                self.createInfo_error_bar('请填写软件名称')
                return
            if self.lineEdit_hot_update_path.text() == "" and self.lineEdit_force_update_path.text() == "":
                self.createInfo_error_bar('请至少填写一个更新路径')
                return
            if self.lineEdit_OSS_path.text() == "":
                self.createInfo_error_bar('请填写存储桶路径')
                return
            if self.lineEdit_Version.text() == "":
                self.createInfo_error_bar('请填写软件版本号！')
                return

            # 检测完成，开始创建OSS文件
            # bucket = self.comboBox_BucketList.text()
            oss_path = self.lineEdit_OSS_path.text()
            # 先判断热更文件是否存在
            hot_update_path = self.lineEdit_hot_update_path.text()
            download_url = self.g.get_host() + f'{oss_path}'
            if hot_update_path != "":
                # 制作并上传update.json文件
                md5 = self.g.get_md5(hot_update_path)

                dict_ = {
                    'download_url': download_url+'/release.iec',
                    'version': self.lineEdit_Version.text(),
                    'dialog': self.comboBox_update_toast.text(),
                    'msg': self.textEdit_update_content.toPlainText(),
                    'force': self.comboBox_update_force.text(),
                    'md5': md5
                }

                try:
                    response = self.g.put_object(self.g.bucket_name,json.dumps(dict_,ensure_ascii=False),f'{oss_path}/update.json')

                    print(f"上传热更说明完成：{response}")

                    # 上传更新日志
                    self.g.put_object(self.g.bucket_name, '',f'{oss_path}/updateLog.txt')
                    if md5 != '':
                        print("开始上传热更文件")
                        self.g.upload_file(self.g.bucket_name, hot_update_path, f'{oss_path}/release.iec')
                except Exception as e:
                    print(f"热更新说明和文件上传失败：{e}")

            force_update_path = self.lineEdit_force_update_path.text()
            if force_update_path:
                md5 = self.g.get_md5(force_update_path)
                # 上传强更说明
                dict_ = {
                    'download_url': download_url+'/release.apk',
                    'version': self.lineEdit_Version.text(),
                    'dialog': self.comboBox_update_toast.text(),
                    'msg': self.textEdit_update_content.toPlainText(),
                    'force': self.comboBox_update_force.text(),
                    'md5': md5
                }
                try:
                    response = self.g.put_object(self.g.bucket_name, json.dumps(dict_, ensure_ascii=False),
                                                 f'{oss_path}/update_app.json')
                    print(f"上传强更说明完成：{response}")
                    # 上传强更文件
                    if md5 != "":
                        print("开始上传强更文件")
                        self.g.upload_file(self.g.bucket_name, hot_update_path, f'{oss_path}/release.apk')
                except Exception as e:
                    print(f"强更文件和说明上传失败{e}")

            self.g.access_data_add(self.lineEdit_app_name.text(), update_path=hot_update_path,
                                   update_app_path=force_update_path, update_url=oss_path)
            self.createInfo_success_bar('软件创建成功！')
            self.lineEdit_app_name.clear()
            self.lineEdit_hot_update_path.clear()
            self.lineEdit_force_update_path.clear()
            self.lineEdit_OSS_path.clear()
            self.textEdit_update_content.clear()
            self.g.copy_text(f'{download_url}/update.json')
            self.createInfo_success_bar('热更地址已写入粘贴板，可直接粘贴使用')


    def createInfo_success_bar(self, content):
        w = InfoBar(InfoBarIcon.SUCCESS, title='成功', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()

    def createInfo_error_bar(self, content):
        w = InfoBar(InfoBarIcon.ERROR, title='错误', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()
