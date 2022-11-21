import math
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 510, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.bb)
        self.point = 100,100
        self.kn = -1

    def paintEvent(self, event):

        if self.kn == 0:
            x, y = self.point
            # Рисовать будем на самом себе
            painter = QPainter(self)
            s = random.randint(10, 100)
            # Для рисования точки хватит setPen, но для других фигур (типо rect) понадобится setBrush
            painter.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), s))
            # Рисование точки
            painter.drawPoint(x, y)

        elif self.kn == 1:
            painter = QPainter(self)
            x, y = self.point
            s = random.randint(10, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setPen(QPen(color, 8, Qt.SolidLine))
            painter.setBrush(QBrush(color, Qt.SolidPattern))

            painter.drawEllipse(x, y, s, s)

        elif self.kn == 2:
            self.drawing.begin(self)
            s = random.randint(10, 150)
            r = a = s
            x, y = self.point
            self.drawing.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            coordss = [(x, y + r), (x + a, y - r), (x - a, y - r)]
            path = QPainterPath()
            path.moveTo(*coordss[0])
            path.lineTo(*coordss[1])
            path.lineTo(*coordss[2])
            self.drawing.drawPath(path)
            self.drawing.end()

    def bb(self):
        self.kn = 1
        self.update()

if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()
    sys.exit(app.exec())