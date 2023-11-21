import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.button.clicked.connect(self.run)
        self.a = False

    def run(self):
        self.a = True
        self.update()

    def paintEvent(self, event):
        if self.a:
            num = randrange(200)
            n = randrange(200)
            painter = QPainter(self)
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.drawEllipse(n, n, num, num)
            self.a = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
