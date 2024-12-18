from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor

class ScreenCell:
    enabled = True
    coords = (0, 0)
    vertices = {
        'center': (0, 0),
        'left': (0, 0),
        'top': (0, 0),
        'right': (0, 0),
        'bottom': (0, 0)
    }
    size = (0, 0)
    mouse_target = 'center'
    resource_node = None
    resource_mouse_offset = (0, 0)
    highlighted = False

    def __init__(self, row, col, x, y, w, h):
        self.coords = (row, col)
        self.vertices = {
            'center': (x, y),
            'left': (int(x - w / 2), y),
            'top': (x, int(y - h / 2)),
            'right': (int(x + w / 2), y),
            'bottom': (x, int(y + h / 2))
        }
        self.size = (w, h)

    def set_resource_node(self, resource_node):
        self.resource_node = resource_node
        return self

    def set_resource_mouse_offset(self, offset):
        self.resource_mouse_offset = offset
        return self

    def draw(self, painter):
        if self.highlighted:
            painter.setPen(QPen(QColor(255, 255, 255), 5))
        elif self.resource_node:
            painter.setPen(QPen(QColor(*self.resource_node['overlay_color']), 2))
        else:
            painter.setPen(QPen(QColor(0, 0, 0), 2))

        painter.drawLine(QPointF(*self.vertices['left']), QPointF(*self.vertices['top']))
        painter.drawLine(QPointF(*self.vertices['top']), QPointF(*self.vertices['right']))
        painter.drawLine(QPointF(*self.vertices['right']), QPointF(*self.vertices['bottom']))
        painter.drawLine(QPointF(*self.vertices['bottom']), QPointF(*self.vertices['left']))