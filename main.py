from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
import sys
from random import randint 


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pix = QPixmap(600, 600)
        self.label.setPixmap(self.pix)
        self.btn.clicked.connect(self.draw_circle)
        self.n = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.btn)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и желтые окружности "))
        self.btn.setText(_translate("MainWindow", "Кнопкаааа"))
        self.label.setText(_translate("MainWindow", "*lobel*"))

    def draw_circle(self):
        x, y = [randint(10, 500) for _ in range(2)]
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.update()


app = QApplication(sys.argv)
w = Test()
w.show()
sys.exit(app.exec_())