import shutil

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition
from ui.ui_agent import Ui_Form_agent
import subprocess
import psutil
import sys
import os


class AgentWindow(QWidget, Ui_Form_agent):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 如果是调试模式则不进行临时文件的copy
        self.debug = False
        if not self.debug:
            self.extract_file()
        self.adb = ""
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        self.btn_start_activation.clicked.connect(self.init_Start_activation)
        self.btn_restart_adb.clicked.connect(self.restart_adb)
        self.btn_open_adb_wifi.clicked.connect(self.open_adb_wifi)
        self.btn_shizuku_start.clicked.connect(self.shizuku_start)
        self.btn_shizuku_download.clicked.connect(self.shizuku_download)

    def btn_refresh_clicked(self):
        # 当点击刷新设备后的操作
        self.is_adb_running()
        if self.adb == "":
            self.createInfo_error_bar("启动adb失败，请重新刷新")
            return
        output = self.adb_command("devices")
        output_list = output.splitlines()
        devices_list = []
        for o in output_list:
            print(f"o的值{o}")
            if "List" not in o and "adb server" not in o and "daemon" not in o and o != "":
                device_state = ""
                device_name = ""
                try:
                    if "device" in o:
                        device_name = o.split()[0].strip()
                        device_state = "device"
                    else:
                        device_name = o.split()[0].strip()
                        device_state = "offline"
                except Exception:
                    continue

                # 获取CPU类型
                self.adb_command(f"-s {device_name} root")
                CPU_types = self.adb_command(f"-s {device_name} shell getprop ro.product.cpu.abi")

                # 获取激活状态active_state
                active_state_str = self.adb_command(f"-s {device_name} shell netstat -ant")
                active_state = "已激活" if "19901" in active_state_str else "未激活"
                devices_list.append([device_name, device_state, active_state, CPU_types.strip(), ""])

        self.insert_data_to_table(devices_list)

    def shizuku_download(self):
        QDesktopServices.openUrl(QUrl("https://shizuku.rikka.app/zh-hans/download/"))

    def is_adb_running(self):
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'adb.exe':
                    if psutil.pid_exists(proc.info["pid"]):
                        process = psutil.Process(proc.info["pid"])
                        self.adb = process.exe()
                        return True
            self.start_adb()
        except Exception as e:
            print(e)

    def start_adb(self):
        try:
            # 获取当前目录
            current_directory = os.path.dirname(__file__)
            # 构建 adb.exe 文件的路径
            adb_path = os.path.join(current_directory, r'agent\adb\adb.exe')
            print(adb_path)
            self.adb = adb_path
            process = subprocess.Popen(f"{adb_path} devices", shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            output, error = process.communicate()
            # print("输出内容：", output.decode('utf-8'))
            # print("错误内容：", error.decode('utf-8'))
        except Exception:
            self.adb = ""

    def adb_command(self, command):
        # 执行命令
        process = subprocess.Popen(f"{self.adb} {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode('utf-8')
        # 打印输出结果
        # print(output.decode('utf-8'))
        # print(error.decode('utf-8'))

    def extract_file(self):
        # 获取 adb.exe 在打包后的可执行文件中的路径
        file_path = os.path.join(sys._MEIPASS, 'agent')
        shutil.copytree(file_path, r'.\agent', dirs_exist_ok=True)

    def insert_data_to_table(self, data):
        # 设置表格的行数和列数
        self.table_devices_list.setRowCount(len(data))
        self.table_devices_list.setColumnCount(len(data[0]))

        # 插入数据
        for i, row_data in enumerate(data):
            # 自动生成序号（行数 + 1）
            item = QTableWidgetItem(str(i + 1))
            item.setFlags(Qt.ItemIsEnabled)  # 禁止编辑
            self.table_devices_list.setVerticalHeaderItem(i, item)

            for j, cell_data in enumerate(row_data):
                self.table_devices_list.setItem(i, j, QTableWidgetItem(str(cell_data)))

    def createInfo_success_bar(self, content):
        w = InfoBar(InfoBarIcon.SUCCESS, title='成功', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()

    def createInfo_error_bar(self, content):
        w = InfoBar(InfoBarIcon.ERROR, title='错误', content=content, orient=Qt.Vertical, isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT, duration=2000, parent=self)
        w.show()

    def init_Start_activation(self):
        if self.table_devices_list.rowCount() < 1:
            self.createInfo_error_bar("手机都没连接，激活个锤子！")
            return
        for i in range(self.table_devices_list.rowCount()):
            device_name = self.table_devices_list.item(i, 0).text()
            device_state = self.table_devices_list.item(i, 1).text()
            device_activation_state = self.table_devices_list.item(i, 2).text()
            CPU_types = self.table_devices_list.item(i, 3).text()
            if device_activation_state == "未激活" and device_state == "device":
                # print(f"准备激活：{device_name}")
                result = self.Start_activation(device_name, CPU_types)
                if result:
                    result_content = "激活成功"
                    result_activation_content = "已激活"
                else:
                    result_content = "激活失败"
                    result_activation_content = "未激活"

                item = QTableWidgetItem(result_activation_content)  # 创建一个新的 QTableWidgetItem 对象
                self.table_devices_list.setItem(i, 2, item)

                item = QTableWidgetItem(result_content)  # 创建一个新的 QTableWidgetItem 对象
                self.table_devices_list.setItem(i, 4, item)
            else:
                item = QTableWidgetItem("跳过激活")  # 创建一个新的 QTableWidgetItem 对象
                self.table_devices_list.setItem(i, 4, item)
        self.createInfo_success_bar("操作完成")

    def Start_activation(self, devices_name, cpu_types):
        # 先判断文件名称
        filename = "agentd"
        if "arm64" in cpu_types:
            filename = "newagent-arm-64"
        elif "86" in cpu_types:
            filename = "newagent-x86"
        elif "arm" not in cpu_types and "arm64" not in cpu_types:
            filename = "newagent-arm"
        else:
            filename = "agentd"
        self.adb_command(f"-s {devices_name} shell chmod -R 777 /data/local/tmp")
        file_path = fr".\agent\agent\{filename}"
        self.adb_command(fr"-s {devices_name} push {file_path}  /data/local/tmp/agent/{filename}")
        self.adb_command(f"-s {devices_name} shell chmod -R 777  /data/local/tmp/agent")
        output = self.adb_command(
            f"-s {devices_name} shell /data/local/tmp/agent/{filename}  -mode=runagent -dport=19901,19902,19903 --password={self.lineEdit_pwd.text()}")
        print(output)
        if "pong" in output:
            print("激活成功")
            return True
        else:
            print("激活失败")
            return False

    def restart_adb(self):
        try:
            # 遍历系统中的所有进程
            for proc in psutil.process_iter(['pid', 'name']):
                # 如果进程名为 adb.exe，则终止该进程
                if proc.info['name'] == 'adb.exe':
                    print(f"终止进程：{proc.info['pid']} - {proc.info['name']}")
                    proc.terminate()
        except Exception as e:
            print(f"发生异常：{e}")

    def open_adb_wifi(self):
        if self.table_devices_list.rowCount() < 1:
            self.createInfo_error_bar("手机都没连接，开启个锤子！")
            return
        for i in range(self.table_devices_list.rowCount()):
            device_name = self.table_devices_list.item(i, 0).text()
            result = self.adb_command(f"-s {device_name} tcpip 5555")
            if "restarting in TCP mode port: 5555" in result:
                content = "wifi激活成功"
            else:
                content = "wifi激活失败"
            item = QTableWidgetItem(content)  # 创建一个新的 QTableWidgetItem 对象
            self.table_devices_list.setItem(i, 4, item)
        self.createInfo_success_bar("操作完成")

    def shizuku_start(self):
        if self.table_devices_list.rowCount() < 1:
            self.createInfo_error_bar("手机都没连接，开启个锤子！")
            return
        for i in range(self.table_devices_list.rowCount()):
            device_name = self.table_devices_list.item(i, 0).text()
            result = self.adb_command(f"-s {device_name}  shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh")
            if "shizuku_starter exit with 0" in result:
                content = "shizuku激活成功"
            else:
                content = "shizuku激活失败"
            item = QTableWidgetItem(content)  # 创建一个新的 QTableWidgetItem 对象
            self.table_devices_list.setItem(i, 4, item)
        self.createInfo_success_bar("操作完成")
