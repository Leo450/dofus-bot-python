import re
import pytesseract
from PIL import Image
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPen, QColor
from src.lib.screen import get_region_pixmap
from src.lib.struct import Vector, Rect

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class PlayerCoords:
    window = None
    rect = None
    size = None
    start_coords = None

    def __init__(self, window):
        self.window = window
        self.rect = Rect(
            0,
            window.viewport_size.y * 0.02,
            window.viewport_size.y * 0.25,
            window.viewport_size.y * 0.07
        )
        self.size = self.rect.size()

    def init(self):
        self.take_screenshot()
        self.start_coords = self.read_coords()

    def take_screenshot(self):
        screen_top_left = self.window.to_screen(self.rect.top_left())
        get_region_pixmap(screen_top_left, self.size).save('.cache/map_grid_coords.png')

    def read_coords(self) -> Vector:
        ocr_str = pytesseract.image_to_string(Image.open('.cache/map_grid_coords.png'), lang='fra')
        lines = ocr_str.splitlines()
        if len(lines) > 0:
            second_line = lines[1]
            coords = re.findall(r'[-+]\d+', second_line)
            if len(coords) >= 2:
                return Vector(int(coords[0]), int(coords[1]))

    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawRect(QRectF(*self.rect.top_left().tuple(), *self.size.tuple()))