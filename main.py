import sys
from UI import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r, g, b = random.randrange(0, 250), random.randrange(0, 250), random.randrange(0, 250)
        qp.setBrush(QColor(r, g, b))
        qp.setPen(QColor(r, g, b))
        x, y = random.randrange(0, 300), random.randrange(0, 200)
        a = random.randrange(5, 100)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
