import random
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)

        self.pushButton.clicked.connect(self.do_or_not)
        self.do_paint = False

    def do_or_not(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.do_paint = False

    def draw_flag(self, qp):
        brush = QBrush(QColor("yellow"))
        qp.setBrush(brush)

        qp.drawEllipse(random.randint(1, 400), random.randint(1, 400), 200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
