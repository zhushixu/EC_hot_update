import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QDesktopServices, QPixmap
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QUrl

from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationItemPosition, NavigationAvatarWidget, \
    MessageBoxBase, SubtitleLabel, TextEdit, MessageBox, BodyLabel
from mainform import MainWindow
from settingform import SettingWindow
from addappform import AddappWindow
from resource_rc import *

class AboutMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('关于软件', self)

        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        content = ('本软件由Kad开发，软件完全免费！请勿付费购买！\n'
                   '各种安卓、IOS、电脑脚本、网页填表等脚本开发可联系作者定制\n')
        self.label_1 = BodyLabel(content, self)
        self.horizontalLayout_1.addWidget(self.label_1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # 添加图片
        pixmap = QPixmap(':image/wx.png')
        self.wx_pic = BodyLabel()
        self.wx_pic.setPixmap(pixmap)
        self.wx_pic.setFixedSize(250, 270)
        self.wx_pic.setScaledContents(True)

        # 添加图片
        pixmap = QPixmap(':image/QQ.png')
        self.qq_pic = BodyLabel()
        self.qq_pic.setPixmap(pixmap)
        self.qq_pic.setFixedSize(250, 270)
        self.qq_pic.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.wx_pic)
        self.horizontalLayout_2.addWidget(self.qq_pic)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addLayout(self.horizontalLayout_2)
        self.viewLayout.addLayout(self.horizontalLayout_1)
        self.widget.setMinimumWidth(500)
        self.yesButton.setText('检查更新')
        self.cancelButton.setText('确定')


class MainForm(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EC热更工具")
        self.resize(830, 700)
        self.center()
        # 添加子界面
        self.main_form = MainWindow(self)
        self.setting_form = SettingWindow(self)
        self.addapp_form = AddappWindow(self)

        self.addSubInterface(self.main_form, FluentIcon.HOME, "软件更新")
        self.addSubInterface(self.addapp_form, FluentIcon.ADD, "创建软件")
        self.addSubInterface(self.setting_form, FluentIcon.SETTING, "软件设置")
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('kad', ':image/ico.png'),
            position=NavigationItemPosition.BOTTOM,
            onClick=self.showMessageBox
        )
        self.version = '1.0.0'

    def showMessageBox(self):
        try:
            w = AboutMessageBox(self)
            if w.exec():
                # QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))
                response = requests.get(
                    url='https://update-1305175740.cos.ap-nanjing.myqcloud.com/EC_hot_update/update_app.json')
                if response.status_code == 200:
                    try:
                        data = response.json()
                        # print(data['version'], self.version)
                        if data['version'] != self.version:
                            update_msg = data['msg']
                            m = MessageBox('发现新版本', f'作者懒，没有写自动更新，自己去网盘下载吧\n{update_msg}', self)
                            m.yesButton.setText('确定')
                            m.cancelButton.setText('取消')
                            if m.exec():
                                QDesktopServices.openUrl(QUrl(data['download_url']))
                        else:
                            m = MessageBox('已是最新', '当前为最新版本，无需更新', self)
                            m.yesButton.setText('确定')
                            # m.cancelButton.setEnabled(False)
                            m.cancelButton.setHidden(True)
                            m.exec()

                    except Exception as e:
                        print(f"更新失败,{e}")


        except Exception as e:
            print(e)

    def center(self):
        # 获取屏幕的中心坐标
        screen_geo = QDesktopWidget().screenGeometry()
        window_geo = self.geometry()

        x = (screen_geo.width() - window_geo.width()) // 2
        y = (screen_geo.height() - window_geo.height()) // 2

        # 将窗口左上角移动到中心坐标
        self.move(x, y)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    # setTheme(Theme.DARK)
    w = MainForm()
    w.show()
    app.exec_()
