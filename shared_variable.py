import hashlib
import json
import os
import re
import sqlite3
import time

from PyQt5 import QtWidgets
from qcloud_cos import CosConfig, CosS3Client
from qcloud_cos.cos_threadpool import SimpleThreadPool
from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, TextEdit, CheckBox, BodyLabel

import pyperclip

import oss2


class Global:
    def __init__(self):
        self.client = None
        self.access_key_id = ''
        self.access_key_secret = ''
        self.region = ''
        self.cloud_name = ''
        self.bucket_name = ''
        self.conn, self.conn_cursor = self.access_data_creat()
        self.oss2 = None
        self.info_name = ''
        self.info_hot_path = ''
        self.info_force_path = ''
        self.info_url_path = ''
        self.info_id = ''
        self.info_path = ''  # 这里决定是更新iec还是app
        self.info_mode = ''
        self.custom_domain = ''
        self.read_config()

    def read_config(self):
        # 读取一下配置项
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
                    # print("读取配置完成",self.access_key_id,self.access_key_secret)

                except Exception as e:
                    print(f"读取初始配置项失败,{e}")
        # print(self.bucket_name,'sdfs',self.cloud_name)

    def get_client(self):
        self.read_config()
        if self.client is None:
            if self.access_key_secret == '' or self.access_key_id == '' or self.region == '':
                return None
            if self.cloud_name == "腾讯云OSS":
                # print("连接", self.access_key_id, self.access_key_secret)
                config = CosConfig(Region=self.region, Secret_id=self.access_key_id, Secret_key=self.access_key_secret)
                client = CosS3Client(config)
                self.client = client
                return client
            elif self.cloud_name == '阿里云OSS':
                print("阿里云")
                auth = oss2.Auth(self.access_key_id, self.access_key_secret)
                client = oss2.Bucket(auth, f'http://{self.region}.aliyuncs.com', self.bucket_name)
                self.client = client
                self.oss2 = oss2
                return client
        else:
            return self.client

    def upload_file(self, bucket_name, local_file_path, path_name):
        if self.client is None:
            self.client = self.get_client()
        print(self.cloud_name)
        if self.cloud_name == '腾讯云OSS':
            try:
                response = self.client.upload_file(
                    Bucket=bucket_name,
                    LocalFilePath=local_file_path,
                    Key=path_name,
                    PartSize=1,
                    MAXThread=10,
                    EnableMD5=True,
                )
                etag = response['ETag']
                # print(etag)
                if len(etag[1:-1]) >= 32:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"上传文件错误：{e}")
                return False
        elif self.cloud_name == '阿里云OSS':
            try:
                print("开始上传文件")
                with open(local_file_path,'rb') as file:
                    result = self.client.put_object(key=path_name,data=file)
                if len(result.etag) >= 32:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"上传文件错误::{e}")
                return False

    def put_object(self, bucket, content, file_name):
        if self.client is None:
            self.client = self.get_client()
        if self.cloud_name == '腾讯云OSS':
            try:
                response = self.client.put_object(
                    Bucket=bucket,
                    Body=content.encode('utf-8'),
                    Key=file_name
                )
                etag = response['ETag']
                if len(etag[1:-1]) >= 32:
                    return True
                else:
                    return False
            except Exception as e:
                print("put_objet错误：", e)
        elif self.cloud_name == '阿里云OSS':
            try:
                result = self.client.put_object(key=file_name, data=content)
                print(result.status,result.etag)
                return True
            except Exception as e:
                print(e)
                return False

    def could_get_file(self, url_path, local_path):
        if self.client is None:
            self.client = self.get_client()
        if self.cloud_name == '腾讯云OSS':
            try:
                self.client.download_file(
                    Bucket=self.bucket_name,
                    Key=url_path,
                    DestFilePath=local_path
                )
                return True
            except Exception as e:
                print('get_file的错误信息：', e)
                return False
        elif self.cloud_name == '阿里云OSS':
            # print("阿里云")
            try:
                self.client.get_object_to_file('test/update.json', local_path)
                return True
            except Exception as e:
                print('get_file的错误信息：', e)
                return False

    def could_delete_file(self, bucket, url_path):
        if self.client is None:
            self.client = self.get_client()
        if self.cloud_name == '腾讯云OSS':
            folder = url_path + '/'
            pool = SimpleThreadPool()
            marker = ""
            while True:
                file_infos = []

                # 列举一页100个对象
                response = self.client.list_objects(Bucket=bucket, Prefix=folder, Marker=marker, MaxKeys=100)

                if "Contents" in response:
                    contents = response.get("Contents")
                    file_infos.extend(contents)
                    pool.add_task(self.delete_files, file_infos)

                # 列举完成，退出
                if response['IsTruncated'] == 'false':
                    break

                # 列举下一页
                marker = response["NextMarker"]

            pool.wait_completion()
            return True
        elif self.cloud_name == '阿里云OSS':
            try:
                # print("阿里云")
                # print('这是地址', url_path)
                objects = oss2.ObjectIteratorV2(self.client, prefix=url_path + "/")
                # print(objects)
                for obj in objects:
                    print(obj.key)
                    self.client.delete_object(obj.key)
                return True
            except Exception as e:
                print(f'删除文件错误:{e}')
                return False

    def delete_files(self, file_infos):
        # 构造批量删除请求，腾讯云的
        delete_list = []
        for file in file_infos:
            delete_list.append({"Key": file['Key']})
        response = self.client.delete_objects(Bucket=self.bucket_name, Delete={"Object": delete_list})
        # print(response)

    def access_data_creat(self):
        # 创建数据库
        conn = sqlite3.connect('data.db')
        # 创建一个游标对象
        cursor = conn.cursor()
        # 创建一个表
        cursor.execute(
            '''create table if not exists update_app(id INTEGER PRIMARY KEY , name Text,update_path TEXT,update_app_path TEXT,update_url TEXT)''')
        conn.commit()
        # self.conn = conn
        # self.conn_cursor = cursor
        return conn, cursor

    def access_data_add(self, name, update_path="", update_app_path='', update_url=''):
        """
        :param name: 软件名称
        :param update_path: 热更路径
        :param update_app_path: 强更路径
        :param update_url: 更新远程目录
        :return:
        """
        # if self.conn is None:
        #     self.creat_access_data()
        data = (name, update_path, update_app_path, update_url)
        self.conn_cursor.execute(
            'INSERT INTO update_app(name,update_path,update_app_path,update_url) VALUES (?,?,?,?)',
            data)
        self.conn.commit()
        return True

    def access_data_get_all_app(self):
        """获取数据库中所有的APP名称和信息"""
        self.conn_cursor.execute('SELECT * FROM update_app')
        rows = self.conn_cursor.fetchall()
        dict_ = {
            'code': 1,
            'msg': '获取数据完成',
            'result': rows
        }
        return rows

    def access_data_update(self, update_id, update_name, update_value):
        """
        修改数据库中的内容
        :param update_id: 数据库中的ID，唯一
        :param update_name: 修改的名称
        :param update_value: 修改后的内容
        :return:
        """
        # print("进来了")
        update_query = f"UPDATE update_app SET {update_name} = ? WHERE id = ?"
        # print('这是语句：',update_query)
        try:
            self.conn_cursor.execute(update_query, (update_value, update_id))
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def access_data_delete(self, delete_id):
        try:
            self.conn_cursor.execute('DELETE FROM update_app WHERE id = ?', (delete_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def access_date_search(self,name):
        try:
            sql = 'SELECT * FROM update_app WHERE name LIKE ?'
            name_pattern = '%{}%'.format(name)
            self.conn_cursor.execute(sql, (name_pattern,))
            row = self.conn_cursor.fetchall()
            self.conn.commit()
            # print(row)
            return row
        except Exception as e:
            print(e)
            return []

    def get_md5(self, file_path):
        if os.path.isfile(file_path):
            md5 = hashlib.md5()
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    md5.update(chunk)
            return md5.hexdigest()
        else:
            return ''

    def copy_text(self, content):
        pyperclip.copy(content)

    def increment_version(self, version):
        """
        将版本号加1
        :param version: 原版本号
        :return: 新版本号
        """
        # 使用正则表达式提取版本号中的数字部分
        match = re.match(r'(\d+(\.\d+)*)', version)
        if match:
            # 提取版本号中的数字部分
            current_version = match.group(1)

            # 将版本号转换为列表
            version_list = list(map(int, current_version.split('.')))

            # 将最后一位加1
            version_list[-1] += 1

            # 将列表中的数字转换为字符串，并拼接为新的版本号
            new_version = '.'.join(map(str, version_list))

            return new_version
        else:
            # 如果无法匹配版本号，则返回原始版本号
            return version

    def get_host(self):
        """
        根据选择的服务商，生成不同的host
        :return:
        """
        url = ''

        if self.custom_domain and self.custom_domain.endswith('/'):
            self.custom_domain = self.custom_domain[:-1]
        # print(self.custom_domain)
        if self.cloud_name == "腾讯云OSS":
            if self.custom_domain == '':
                url = f'https://{self.bucket_name}.cos.{self.region}.myqcloud.com/'
            else:
                url = f'{self.custom_domain}/'
        elif self.cloud_name == "阿里云OSS":
            if self.custom_domain == '':
                url = f'https://{self.bucket_name}.{self.region}.aliyuncs.com/'
            else:
                url = f'{self.custom_domain}/'

        return url


class CustomMessageBox(MessageBoxBase):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        # print(data)
        self.titleLabel = SubtitleLabel(f'{data["mode"]}【{data["name"]}】', self)
        self.textedit_update_info = TextEdit(self)
        self.textedit_update_info.setPlaceholderText('更新说明')
        self.linedit_version = LineEdit(self)
        self.linedit_version.setPlaceholderText('版本号')
        version = data['version']
        self.linedit_version.setText(version)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_dialog = CheckBox(self)
        self.checkBox_dialog.setObjectName("checkBox_dialog")
        self.checkBox_dialog.setText("是否弹窗")
        self.checkBox_dialog.setChecked(data['is_dialog'])
        self.horizontalLayout_3.addWidget(self.checkBox_dialog)
        self.checkBox_force = CheckBox(self)
        self.checkBox_force.setObjectName("checkBox_force")
        self.checkBox_force.setText("是否强更")
        self.checkBox_force.setChecked(data['is_force'])
        self.horizontalLayout_3.addWidget(self.checkBox_force)
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.textedit_update_info)
        self.viewLayout.addWidget(self.linedit_version)
        self.viewLayout.addLayout(self.horizontalLayout_3)
        # change the text of button
        self.yesButton.setText('更新')
        self.cancelButton.setText('取消')
        self.widget.setMinimumWidth(350)
        if version != "":
            # print(version)
            self.yesButton.setEnabled(True)
        # self.textedit_update_info.textChanged.connect(self.update_info)
        self.linedit_version.textChanged.connect(self.update_info)

        # self.hideYesButton()

    def update_info(self):
        try:
            # text_content = self.textedit_update_info.toPlainText()
            text_content = self.linedit_version.text()
            if text_content != "":
                self.yesButton.setEnabled(True)
            else:
                self.yesButton.setEnabled(False)
        except Exception as e:
            print(e)


class NoticeMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        # print(data)
        self.titleLabel = SubtitleLabel('更新公告', self)
        self.textedit_notice_info = TextEdit(self)
        self.textedit_notice_info.setPlaceholderText('公告内容')

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.textedit_notice_info)

        # change the text of button
        self.yesButton.setText('更新')
        self.cancelButton.setText('取消')
        self.widget.setMinimumWidth(350)


class ChangeMessageBox(MessageBoxBase):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        print(data)
        self.titleLabel = SubtitleLabel(f'修改信息', self)

        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.label_1 = BodyLabel('当前软件名称', self)
        self.horizontalLayout_1.addWidget(self.label_1)
        self.lineedit_name = LineEdit(self)
        self.lineedit_name.setReadOnly(True)
        self.lineedit_name.setText(data['name'])
        self.horizontalLayout_1.addWidget(self.lineedit_name)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_2 = BodyLabel('热更本地路径', self)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineedit_hot_path = LineEdit(self)
        self.lineedit_hot_path.setText(data['hot_path'])
        self.horizontalLayout_2.addWidget(self.lineedit_hot_path)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.label_3 = BodyLabel('强更本地路径', self)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineedit_force_path = LineEdit(self)
        self.lineedit_force_path.setText(data['force_path'])
        self.horizontalLayout_3.addWidget(self.lineedit_force_path)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_4 = BodyLabel('对象存储路径', self)
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineedit_oss_path = LineEdit(self)
        self.lineedit_oss_path.setText(data['oss_path'])
        self.horizontalLayout_4.addWidget(self.lineedit_oss_path)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addLayout(self.horizontalLayout_1)
        self.viewLayout.addLayout(self.horizontalLayout_2)
        self.viewLayout.addLayout(self.horizontalLayout_3)
        self.viewLayout.addLayout(self.horizontalLayout_4)
        # change the text of button
        self.yesButton.setText('更新')
        self.cancelButton.setText('取消')
        self.widget.setMinimumWidth(500)
