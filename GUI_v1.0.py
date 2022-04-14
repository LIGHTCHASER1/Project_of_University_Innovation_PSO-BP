# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:51:48 2021

@author: LIGHT CHASER
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()#界面绘制交给InitUI
        
    def initUI(self):
        #设置窗口位置大小
        self.setGeometry(800,400,800,600)
        #设置窗口标题
        self.setWindowTitle('GUI_v1.0')
        #设置窗口图标
        self.setWindowIcon(QIcon('picture'))
        
        self.show()

if __name__ == '__main__' :
    #创建应用程序和对象
    app = QApplication(sys.argv)
    GUI = GUI()
    sys.exit(app.exec_())