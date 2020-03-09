#-*-coding:utf-8-*-
import sys
import matplotlib as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
from matplotlib.figure import Figure

import PlotWin
import MyFigure


def plotcos(self):
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    self.F.axes.plot(t, s)
    self.F.fig.suptitle("cos")


def plotother(self):
    F1 = MyFigure(width=5, height=4, dpi=100)
    F1.fig.suptitle("Figuer_4")
    F1.axes1 = F1.fig.add_subplot(221)
    x = np.arange(0, 50)
    y = np.random.rand(50)
    F1.axes1.hist(y, bins=50)
    F1.axes1.plot(x, y)
    F1.axes1.bar(x, y)
    F1.axes1.set_title("hist")
    F1.axes2 = F1.fig.add_subplot(222)

    ## 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
    F1.axes2.plot(x, y)
    F1.axes2.set_title("line")
    # 散点图
    F1.axes3 = F1.fig.add_subplot(223)
    F1.axes3.scatter(np.random.rand(20), np.random.rand(20))
    F1.axes3.set_title("scatter")
    # 折线图
    F1.axes4 = F1.fig.add_subplot(224)
    x = np.arange(0, 5, 0.1)
    F1.axes4.plot(x, np.sin(x), x, np.cos(x))
    F1.axes4.set_title("sincos")
    #self.gridlayout.addWidget(F1, 0, 2)
    self.gridLayout.addWidget(self.F,0,1)

if __name__ == "__main__":
    app = QApplication([])
    main_win = QMainWindow()
    ui = PlotWin.Ui_MainWindow()
    ui.setupUi(main_win)
    #data = np.zeros()
    print("test...")

    # 第五步：定义MyFigure类的一个实例
    ui.F = MyFigure(width=3, height=2, dpi=100)
    # self.F.plotsin()
    ui.plotcos()
    # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
    #ui.gridLayout = QGridLayout(ui.groupBox)  # 继承容器groupBox
    #ui.gridLayout.addWidget(ui.F, 0, 1)

    # 补充：另创建一个实例绘图并显示
    #ui.plotother()

    main_win.show()
    sys.exit(app.exec_())