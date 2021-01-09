import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from Ui import Ui_Form

def generate_color():
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


class CircleDrawer(QWidget, Ui_Form):
    CIRCLES_NUMBER = 5
    BORDER = 5

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ellipses = []
        self.need_to_draw = False
        self.drawButton.clicked.connect(self.draw)

    def draw(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        width, height = self.width(), self.height()
        if self.need_to_draw:
            self.draw_last_circles(qp)
            color = generate_color()
            qp.setBrush(QColor(*color))
            radius = randrange(5, 60)
            x, y = randrange(radius + self.BORDER, width - radius * 2 - self.BORDER), \
                randrange(radius + self.BORDER, height - radius * 2 - self.BORDER)
            qp.drawEllipse(x, y, radius * 2, radius * 2)
            self.ellipses.append((x, y, radius, color))
            self.need_to_draw = False
        else:
            self.draw_last_circles(qp)

    def draw_last_circles(self, qp):
        for x, y, radius, color in self.ellipses:
            qp.setBrush(QColor(*color))
            qp.drawEllipse(x, y, radius * 2, radius * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())