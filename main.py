import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(Qt.yellow))
        qp.setPen(QColor(Qt.yellow))
        x, y = random.randrange(0, 300), random.randrange(0, 200)
        a = random.randrange(5, 100)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
