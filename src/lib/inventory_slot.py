from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor, QPainter
from src.lib.screen import get_region_pixmap, pixmap_to_pixels
from src.lib.struct import Vector, Rect


DEBUG_SCREENSHOTS = False

class InventorySlot:
    window = None
    coords = None
    size = None
    rect = None
    screenshot = None

    def __init__(self, window, coords: Vector, center: Vector, size: Vector):
        self.window = window
        self.coords = coords
        self.size = size
        self.rect = Rect(
            center.x - size.x / 2,
            center.y - size.y / 2,
            center.x + size.x / 2,
            center.y + size.y / 2
        )

    def get_screenshot_pixmap(self):
        screen_top_left = self.window.to_screen(self.rect.top_left())
        return get_region_pixmap(screen_top_left, self.size)

    def update_screenshot(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('slot_{}_{}.png'.format(*self.coords.tuple()))
        self.screenshot = pixmap_to_pixels(pixmap)

    def has_changed(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('slot_{}_{}_check.png'.format(*self.coords.tuple()))
        return self.screenshot != pixmap_to_pixels(pixmap)

    def draw(self, painter: QPainter):
        painter.setPen(QPen(QColor(0, 255, 0), 1))
        rect = self.rect.expand(1)
        painter.drawLine(QPointF(*rect.top_left().tuple()), QPointF(*rect.top_right().tuple()))
        painter.drawLine(QPointF(*rect.top_right().tuple()), QPointF(*rect.bottom_right().tuple()))
        painter.drawLine(QPointF(*rect.bottom_right().tuple()), QPointF(*rect.bottom_left().tuple()))
        painter.drawLine(QPointF(*rect.bottom_left().tuple()), QPointF(*rect.top_left().tuple()))