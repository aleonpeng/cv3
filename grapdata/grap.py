#-*-coding:utf-8-*-
#import requests
import bs4
import json
import os
from bs4 import BeautifulSoup
from lxml import etree
from prettytable import PrettyTable
import MySQLdb
from requests_html import HTMLSession
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
import sys
import requests
import downloadThread
from UpdateThread import *

from FoundAnlysis import Ui_Form

class MainFrm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainFrm,self).__init__(parent)
        #QtWidgets.QWidget.__init__(self)

        self.setupUi(self)



        #使用QbasicTimer方式；
        # self.timer = QBasicTimer()
        #self.btn_UpdateData.clicked.connect(self.UpdateDataFromInternet)

        '''
        #使用QTimer方式
        self.timer = QTimer()
        self.btn_UpdateData.clicked.connect(self.start_timer)

        self.step = 0
        '''

        '''
        #使用QThread方式；
        self.mythread = ProgressThread()
        self.btn_UpdateData.clicked.connect(self.click_start)
        #self.btn_LoadImage.clicked.connect(self.load_img)
        self.mythread.my_sign.connect(self.updateprogress)
        '''

        '''
        # add file dir;
        self.total_counts = 0
        self.read_num = -1
        self.imgs = []
        self.btn_LoadImage.clicked.connect(self.load_img)
        self.btn_UpImage.clicked.connect(self.up_image)
        self.btn_DownImage.clicked.connect(self.down_image)
        '''

        self.timer_cam = QTimer()
        self.cap = cv2.VideoCapture()
        self.btn_initCam.clicked.connect(self.init_cam_click)
        self.timer_cam.timeout.connect(self.play_vedio)

    def play_vedio(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(showImage).scaled(self.lbl_displayImage.width(), self.lbl_displayImage.height())
        self.lbl_displayImage.setPixmap(pixmap)


    def init_cam_click(self):
        try:
            if self.timer_cam.isActive() == False:
                #print(self.cap)
                flag = self.cap.open(0)
                if flag == False:
                    msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                                        buttons=QtWidgets.QMessageBox.Ok,
                                                        defaultButton=QtWidgets.QMessageBox.Ok)
                else:
                    self.timer_cam.start(30)
                    self.btn_initCam.setText("Shutdown")
            else:
                self.timer_cam.stop()
                self.cap.release()
                self.lbl_displayImage.clear()
                self.btn_initCam.setText('InitCam')
        except Exception as ex:
            print(ex)

    def load_img(self):
        self.dir = QFileDialog.getExistingDirectory(self, "选择文件夹", "E:/halcon/pcbimage")
        self.cmb_Dir.addItem(self.dir)
        self.imgs = os.listdir(self.dir)
        self.total_counts = len(self.imgs)

    def up_image(self):
        self.lbl_displayImage.clear()

        if self.read_num >= self.total_counts -1 :
            self.lbl_displayImage.setStyleSheet("color: red")
            self.lbl_displayImage.setText("Thare are no image, please turn down.")
            return
        else:
            self.read_num += 1
            currenImage = self.dir + "/" + self.imgs[self.read_num]
            self.read_img(currenImage)

    def down_image(self):
        self.lbl_displayImage.clear()

        if self.read_num < 0:
            self.lbl_displayImage.setStyleSheet("background-color: gray")
            self.lbl_displayImage.setText("Thare are no image, please turn up.")
            return
        else:
            self.read_num -= 1
            currenImage = self.dir + "/" + self.imgs[self.read_num]
            self.read_img(currenImage)

    def read_img(self, imageFile):
        try:

            img = cv2.imread(imageFile)
            height, width, bytesPerComponent = img.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(QImg).scaled(self.lbl_displayImage.width(), self.lbl_displayImage.height())

            self.lbl_displayImage.setPixmap(pixmap)
            self.lbl_displayImage.setCursor(Qt.CrossCursor)

        except Exception as ex:
            print(ex)

    def click_start(self):
        self.mythread.is_on = True
        self.mythread.count = 0
        self.btn_UpdateData.setStyleSheet("background-color: green")
        self.btn_UpdateData.setText("Uploading")

        self.mythread.start()


    def click_stop(self):
        self.mythread.is_on = False


    def updateprogress(self, num):
        try:
            if num == 100:

                self.btn_UpdateData.setStyleSheet("background-color: red")
                self.btn_UpdateData.setText("Start")

            self.progressBar.setValue(int(num))

        except Exception as ex:
            print(ex)
            QMessageBox.information(self,'Exception', ex)


    def time_out(self):
        try:
            if self.step >= 100:
               self.timer.stop()
               self.btn_UpdateData.setText('Restart')
               return

            self.step = self.step + 1
            self.progressBar.setValue(self.step)

        except Exception as ex:
            print(ex)

    def start_timer(self):
        self.step = 0
        self.timer.start(100)
        self.timer.timeout.connect(self.time_out)

    def timerEvent(self, event):
        try:
            if self.step >= 100:
               self.timer.stop()
               self.btn_UpdateData.setText('Restart')
               return

            self.step = self.step + 1
            self.progressBar.setValue(self.step)

        except Exception as ex:
            print(ex)

    def UpdateDataFromInternet(self):
        try:
            if self.timer.isActive():
                self.timer.stop()
                self.btn_UpdateData.setText("Start")
            else:
                self.timer.start(100, self)

                self.btn_UpdateData.setText('Stop')
                #self.timerEvent(self)

        except Exception as ex:
            print(ex)

    def TestMySql(self):
        cursor = self.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)

    def QueryData(self, command):
        cursor = self.cursor()
        sql = "SELECT * FROM tray_found2;"
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.commit()

            rows = cursor.fetchall()
            print(rows)
        except BaseException as e:
            # 发生错误时回滚
            print(e)
            self.rollback()

    def InsertDataIntoMySql(self,data):
        # 使用cursor()方法获取操作游标
        cursor = self.cursor()
        #newData = data.replace('%','%%')

        # SQL 插入语句
        tmpCmd = (data[0],data[1],data[2],data[3],\
                  data[4].replace('---','0.0'),\
                  data[5].replace('---','0.0'),\
                  data[6].replace('---','0.0'),\
                  data[7].replace('---','0.0'),\
                  data[8].replace('---','0.0'),\
                  data[9].replace('%','').replace('---','0.0'),\
                  data[10].replace('---','0.0'),\
                  data[11].replace('%','').replace('---','0.0'))
        print(tmpCmd)

        sql = "INSERT INTO tray_found2\
                (idx, alias,foundName, fType, CurrV, CurrSum, ForeV,ForeSum,Incr,Rate,nVal,CEFT) \
                VALUES (%s, %s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s );" % tmpCmd
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.commit()

        except BaseException as e:
            # 发生错误时回滚
            self.rollback()
            print(e)

    def parseWeb1(self):
        import requests
        url = 'http://fund.eastmoney.com/cnjy_jzzzl.html'
        response = requests.get(url)
        response.raise_for_status()  # 返回状态码，200是正常
        response.encoding = response.apparent_encoding  # 识别页面编码
        response.encoding = 'gbk'

        tree = etree.HTML(response.text)
        xPath = "//*[@id=\"tableDiv\"]//text()"
        node_content = tree.xpath(xPath)
        print(len(node_content))

        x = PrettyTable(field_names=['序号', '基金代码','基金简称', '类型','当前净值', '当前累计', '前日净值', '前日累计', '增长值', '增长率', '市价', '折价率'])
        x.align['序号']
        x.padding_width = 1

        #print(x)

        try:
            dd = []
            #提取所有的数据到一个数组列表中；
            for i in range(16, len(node_content)):
                dd.append(node_content[i].strip())

            #print(dd)
            length = len(dd)
            s = 15
            #按15列一行拆分列表；
            for r in range(1,int(length/15)):
                #for col in range(15):
                    #x.add_column(row,ChildrenUrl[row*col])
                row_data = []
                row_data = dd[int((r-1)*15):(r-1)*15+3] + dd[(r-1)*15+6:int(r*15)]
                print(row_data)
                #InsertDataIntoMySql(db, row_data)
        except Exception as e:
            print(e)

    def parseWeb2(self):


        session = HTMLSession()
        url = 'http://fund.eastmoney.com/data/fbsfundranking.html#tct;c0;r;szzf;ddesc;pn10000;'
        '''
        r = requests.get(url)
        print(r.headers['Content-Type'])
        print(r.encoding)
        r.encoding = "utf-8"    
        '''

        r = session.get(url=url)
        r.html.render()
        #r.encoding = "utf-8"
        #r.encoding
        #print(r.text) #its ok.


        tree = etree.HTML(r.html.html, parser=etree.HTMLParser(encoding='gbk'))
        print("aaaa")
        print(tree)
        print("bbbb")
        #xPath = "//*[@id=\"dbtable\"]/tbody//text()"
        xpath2= '//*[@id="dbtable"]/tbody//text()'
        node_content = tree.xpath(xpath2)
        print(node_content)

        x = PrettyTable(field_names=['序号', '基金代码', '基金简称', '类型', '日期', '单位净值', '累计累计', \
                                     '近一周', '近一月', '近三月', '近六月', '近一年', '近二年', '近三年', \
                                     '今年来', '成立来', '成立时间'])
        x.align['序号']
        x.padding_width = 1
        try:
            dd = []
            #提取所有的数据到一个数组列表中；
            for i in range(18, len(node_content)):
                dd.append(node_content[i].strip())

            print(dd)
            length = len(dd)
            s = 17
            #按15列一行拆分列表；
            for r in range(1,int(length/17)):
                #for col in range(15):
                    #x.add_column(row,ChildrenUrl[row*col])
                row_data = []
                #row_data = dd[int((r-1)*17):(r-1)*15+3] + dd[(r-1)*15+6:int(r*15)]
                row_data = dd[int((r-1)*17):int(r*17)]
                #print(row_data)
                #InsertDataIntoMySql(db, row_data)
        except Exception as e:
            print(e)



if __name__ == "__main__":
    #db = MySQLdb.connect("localhost","cigauto", "cigauto@123", "cigauto2", charset='utf8')
    #parseWeb2(db)
    #TestMySql(db)
    #db.close()

    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon("./Resource/cig-logo.jpg"))
    win = MainFrm()
    win.show()
    sys.exit(app.exec_())