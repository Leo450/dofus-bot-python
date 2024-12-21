from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor, QPainter
from src.lib.color import similar
from src.lib.screen import get_region_pixmap, pixmap_to_pixels
from src.lib.struct import Vector, Rect


DEBUG_SCREENSHOTS = False

class InventoryGauge:
    window = None
    size = None
    rect = None
    screenshot = None

    def __init__(self, window, top_left: Vector, size: Vector):
        self.window = window
        self.size = size
        self.rect = Rect(
            top_left.x,
            top_left.y,
            top_left.x + size.x,
            top_left.y + size.y
        )

    def get_screenshot_pixmap(self):
        screen_top_left = self.window.to_screen(self.rect.top_left())
        return get_region_pixmap(screen_top_left, self.size)

    def update_screenshot(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('gauge.png')
        self.screenshot = pixmap_to_pixels(pixmap)

    def has_changed(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('gauge_check.png')
        return self.screenshot != pixmap_to_pixels(pixmap)

    def is_full(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('gauge_check.png')
        pixels = pixmap_to_pixels(pixmap)
        for pixel in pixels:
            if similar(pixel, (228, 23, 0)):
                return True
        return False

    def draw(self, painter: QPainter):
        painter.setPen(QPen(QColor(0, 255, 0), 1))
        rect = self.rect.expand(1)
        painter.drawLine(QPointF(*rect.top_left().tuple()), QPointF(*rect.top_right().tuple()))
        painter.drawLine(QPointF(*rect.top_right().tuple()), QPointF(*rect.bottom_right().tuple()))
        painter.drawLine(QPointF(*rect.bottom_right().tuple()), QPointF(*rect.bottom_left().tuple()))
        painter.drawLine(QPointF(*rect.bottom_left().tuple()), QPointF(*rect.top_left().tuple()))