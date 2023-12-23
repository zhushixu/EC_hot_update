import json

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from ui.ui_setting import Ui_Form_setting
import os


# from shared_variable import var

class SettingWindow(QWidget, Ui_Form_setting):
    def __init__(self, parent=None, var=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.btn_save_setting.clicked.connect(self.button_click)
        self.btn_register.clicked.connect(self.button_click)
        self.btn_apply_key.clicked.connect(self.button_click)
        self.cloud_name = ""
        self.access_key_id = ""
        self.access_key_secret = ""
        self.region = ''
        self.bucket_name = ''
        self.custom_domain = ''
        # 启动读取配置
        if os.path.exists('config.ini'):
            with open('config.ini', 'r', encoding='utf-8') as file:
                config_str = file.read()
                try:
                    config = json.loads(config_str)
                    self.cloud_name = config['cloud_name']
                    self.region = config['region']
                    self.bucket_name = config['bucket_name']
                    self.access_key_id = config['access_key_id']
                    self.access_key_secret = config['access_key_secret']
                    self.custom_domain = config['custom_domain']
                    if self.cloud_name == "腾讯云OSS":
                        self.comboBox_colud_name.setCurrentIndex(0)
                    elif self.cloud_name == "阿里云OSS":
                        self.comboBox_colud_name.setCurrentIndex(1)
                    elif self.cloud_name == "七牛云OSS":
                        self.comboBox_colud_name.setCurrentIndex(1)
                    self.lineEdit_region.setText(self.region)
                    self.lineEdit_bucket_name.setText(self.bucket_name)
                    self.lineEdit_key_id.setText(self.access_key_id)
                    self.lineEdit_key_secret.setText(self.access_key_secret)
                    self.lineEdit_custom_domain.setText(self.custom_domain)
                except Exception as e:
                    print("读取初始配置项失败")

    def button_click(self):
        btn_name = self.sender().objectName()
        if btn_name == 'btn_register':
            cloud_name = self.comboBox_colud_name.text()
            if cloud_name == "腾讯云OSS":
                self.open_url('https://cloud.tencent.com/product/cos')
            elif cloud_name == "阿里云OSS":
                self.open_url('https://www.aliyun.com/product/oss')
            elif cloud_name == "七牛云OSS":
                pass
        elif btn_name == "btn_apply_key":
            cloud_name = self.comboBox_colud_name.text()
            if cloud_name == "腾讯云OSS":
                self.open_url('https://console.cloud.tencent.com/cam/capi')
            elif cloud_name == "阿里云OSS":
                self.open_url('https://ram.console.aliyun.com/manage/ak')
            elif cloud_name == "七牛云OSS":
                pass
        elif btn_name == "btn_save_setting":
            cloud_name = self.comboBox_colud_name.text()
            self.cloud_name = cloud_name
            self.region = self.lineEdit_region.text()
            self.bucket_name = self.lineEdit_bucket_name.text()
            self.access_key_id = self.lineEdit_key_id.text()
            self.access_key_secret = self.lineEdit_key_secret.text()
            self.custom_domain = self.lineEdit_custom_domain.text()
            config = {
                'cloud_name': self.cloud_name,
                'region': self.region,
                'bucket_name': self.bucket_name,
                'access_key_id': self.access_key_id,
                'access_key_secret': self.access_key_secret,
                'custom_domain': self.custom_domain
            }
            with open('config.ini', 'w', encoding='utf-8') as file:
                file.write(json.dumps(config))

    def open_url(self, url):
        _url = QUrl(url)
        QDesktopServices.openUrl(_url)
