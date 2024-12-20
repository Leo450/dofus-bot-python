from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor, QPainter
from src.lib.struct import Vector, Rect


class ScreenCell:
    enabled = True
    coords = None
    size = None
    rect = None
    vertices = {
        'center': None,
        'left': None,
        'top': None,
        'right': None,
        'bottom': None
    }
    resource_node = None
    resource_mouse_offset = Vector(0, 0)
    highlighted = False

    def __init__(self, coords: Vector, center: Vector, size: Vector):
        self.coords = coords
        self.size = size
        self.rect = Rect(
            center.x - size.x / 2,
            center.y - size.y / 2,
            center.x + size.x / 2,
            center.y + size.y / 2
        )
        self.vertices = {
            'center': center,
            'left': Vector(self.rect.min.x, center.y),
            'top': Vector(center.x, self.rect.min.y),
            'right': Vector(self.rect.max.x, center.y),
            'bottom': Vector(center.x, self.rect.max.y)
        }

    def set_resource_node(self, resource_node):
        self.resource_node = resource_node
        return self

    def set_resource_mouse_offset(self, x, y):
        self.resource_mouse_offset = Vector(x, y)
        return self

    def draw(self, painter: QPainter):
        if self.highlighted:
            painter.setPen(QPen(QColor(255, 255, 255), 5))
        elif self.resource_node:
            painter.setPen(QPen(QColor(*self.resource_node['overlay_color']), 2))
        else:
            painter.setPen(QPen(QColor(0, 0, 0), 2))

        painter.drawLine(QPointF(*self.vertices['left'].tuple()), QPointF(*self.vertices['top'].tuple()))
        painter.drawLine(QPointF(*self.vertices['top'].tuple()), QPointF(*self.vertices['right'].tuple()))
        painter.drawLine(QPointF(*self.vertices['right'].tuple()), QPointF(*self.vertices['bottom'].tuple()))
        painter.drawLine(QPointF(*self.vertices['bottom'].tuple()), QPointF(*self.vertices['left'].tuple()))