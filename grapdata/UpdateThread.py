#-*-coding:utf-8-*-
from PyQt5.QtCore import *
import time

class ProgressThread(QThread):

    my_sign = pyqtSignal(int)

    def __init__(self):
        super(ProgressThread,self).__init__()
        self.count = 0
        self.is_on = True

    def run(self):
        while self.is_on:
            if self.count <= 100:

                self.my_sign.emit(self.count)
                time.sleep(0.5)
                self.count += 5
            else:
                self.is_on = False