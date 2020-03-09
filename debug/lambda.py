from PyQt5.QtWidgets import *
import  sys

class LambdaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lambda express")
        self.resize(400, 300)
        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")

        #btn1.clicked.connect(lambda :self.btnClicked(20, 30))
        btn2.clicked.connect(self.btnClicked)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def btnClicked(self):
        #QMessageBox.information(self, "Result", str(m+n))
        QMessageBox.information(self, "Result", "Test!!!")

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widt = LambdaWindow()
    widt.show()

    sys.exit(app.exec_())

