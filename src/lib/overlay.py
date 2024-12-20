from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from src.lib.console import BCOLORS


class Overlay(QWidget):

    drawables = {}

    def __init__(self, window):
        super().__init__()

        self.setWindowTitle("Dofus Overlay")
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(window.viewport_rect.min.x, window.viewport_rect.min.y, window.viewport_size.x, window.viewport_size.y)

        self.show()

    def set_drawable(self, key, drawable):
        self.drawables[key] = drawable
        self.update()

    def remove_drawable(self, key):
        if key in self.drawables:
            del self.drawables[key]
            self.update()

    def paintEvent(self, event):
        #print(BCOLORS.grey('(Overlay paintEvent)'))
        painter = QPainter()

        painter.begin(self)

        for key, drawable in self.drawables.items():
            drawable.draw(painter)

        painter.end()