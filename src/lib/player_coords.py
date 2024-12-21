import re
import pytesseract
from PIL import Image
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPen, QColor

from src.lib.console import BCOLORS
from src.lib.screen import get_region_pixmap
from src.lib.struct import Vector, Rect


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class PlayerCoords:
    window = None
    rect = None
    size = None
    start_coords = None
    prev_ocr_str = None
    prev_lines = None
    prev_split = None
    prev_coords = None

    def __init__(self, window):
        self.window = window
        self.rect = Rect(
            0,
            window.viewport_size.y * 0.026,
            window.viewport_size.y * 0.3,
            window.viewport_size.y * 0.078
        )
        self.size = self.rect.size()

    def init(self):
        self.start_coords = self.read_coords()

    def take_screenshot(self):
        screen_top_left = self.window.to_screen(self.rect.top_left())
        get_region_pixmap(screen_top_left, self.size).save('.cache/map_grid_coords.png')

    def read_coords(self) -> Vector:
        self.prev_coords = None
        self.take_screenshot()
        self.prev_ocr_str = pytesseract.image_to_string(Image.open('.cache/map_grid_coords.png'), lang='fra', config='--psm 6')
        self.prev_lines = self.prev_ocr_str.splitlines()
        if len(self.prev_lines) < 2:
            print(' >> OCR failed: not enough lines ', BCOLORS.BG_RED + BCOLORS.BLACK + BCOLORS.BOLD)
            print('String:')
            print(self.prev_ocr_str)
            print('Lines:')
            print(self.prev_lines)
            raise Exception('OCR failed: not enough lines')
        second_line = self.prev_lines[1]
        self.prev_split = re.findall(r'[-+]?\d+', second_line.replace('A', '4'))
        if len(self.prev_split) < 2:
            print(' >> OCR failed: not enough numbers ', BCOLORS.BG_RED + BCOLORS.BLACK + BCOLORS.BOLD)
            print('String:')
            print(self.prev_ocr_str)
            print('Lines:')
            print(self.prev_lines)
            print('Split:')
            print(self.prev_split)
            raise Exception('OCR failed: not enough numbers')
        x = int(self.prev_split[0])
        y = int(self.prev_split[1])
        self.prev_coords = Vector(x, y)
        return self.prev_coords

    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawRect(QRectF(*self.rect.top_left().tuple(), *self.size.tuple()))