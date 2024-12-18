import re
import pytesseract
from PIL import Image
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPen, QColor
from src.lib.screen import get_region_pixmap

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class MapGridCoords:
    start_coords = None

    def __init__(self, window):
        self.window = window
        self.rect = (0, window.viewport_size[1] * 0.02, window.viewport_size[1] * 0.25, window.viewport_size[1] * 0.07)
        self.size = (self.rect[2] - self.rect[0], self.rect[3] - self.rect[1])

    def init(self):
        self.take_screenshot()
        self.start_coords = self.read_coord()

    def take_screenshot(self):
        screen_top_left = self.window.to_screen(self.rect[0], self.rect[1])
        get_region_pixmap(int(screen_top_left[0]), int(screen_top_left[1]), int(self.size[0]), int(self.size[1])).save('.cache/map_grid_coords.png')

    def read_coord(self):
        ocr_str = pytesseract.image_to_string(Image.open('.cache/map_grid_coords.png'), lang='fra')
        lines = ocr_str.splitlines()
        if len(lines) > 0:
            second_line = lines[1]
            coords = re.findall(r'[-+]\d+', second_line)
            if len(coords) >= 2:
                return int(coords[0]), int(coords[1])

    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawRect(QRectF(self.rect[0], self.rect[1], self.size[0], self.size[1]))