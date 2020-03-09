import sys
import matplotlib as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
from matplotlib.figure import Figure

class DrawGraph(QMainWindow):
    def __init__(self):
        super(self).__init__()

        app = QApplication
