from PyQt5.QtGui import QPen, QColor
from src.lib.screen_cell import ScreenCell
from src.lib.struct import Vector


class ScreenGrid:
    window = None
    dimension = Vector(40, 14)
    cell_size = None
    size = None
    center = None
    offset = None
    cells = {}

    def __init__(self, window):
        self.window = window

        self.cell_size = Vector(
            window.viewport_size.y * 0.086,
            window.viewport_size.y * 0.043
        )
        self.size = Vector(
            self.dimension.y * self.cell_size.x,
            self.dimension.x * (self.cell_size.y / 2)
        )
        self.offset = Vector(
            self.cell_size.y * 0.5,
            window.viewport_size.y * -0.055
        )
        self.center = Vector(
            window.viewport_size.x / 2 + self.offset.x,
            window.viewport_size.y / 2 + self.offset.y
        )

        self.cells = {}
        for row in range(self.dimension.x):
            self.cells[row] = {}
            for col in range(self.dimension.y):
                row_offset_x = 0 if row % 2 == 0 else self.cell_size.x / 2
                x = row_offset_x + self.center.x - self.size.x / 2 + col * self.cell_size.x
                y = self.center.y - self.size.y / 2 + row * (self.cell_size.y / 2)

                self.cells[row][col] = ScreenCell(Vector(col, row), Vector(x, y), self.cell_size)

    def get_cell(self, row, col):
        return self.cells[row][col]

    def get_closest_cell(self, x, y, enabled_only=True):
        closest_cell = None
        min_distance = float('inf')

        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                cell = self.get_cell(row, col)
                if enabled_only and not cell.enabled: continue
                distance = (cell.rect.center().x - x) ** 2 + (cell.rect.center().y - y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_cell = cell

        return closest_cell

    def get_nb_enabled_cells(self):
        nb_cells = 0

        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                cell = self.get_cell(row, col)
                if cell.enabled:
                    nb_cells += 1

        return nb_cells

    def get_last_enabled_cell(self):
        for row in reversed(range(self.dimension.x)):
            for col in reversed(range(self.dimension.y)):
                cell = self.get_cell(row, col)
                if cell.enabled: return cell
        return None

    def get_next_cell(self, prev_row, prev_col):
        for row in range(self.dimension.x):
            if row < prev_row: continue
            for col in range(self.dimension.y):
                if row == prev_row and col <= prev_col: continue
                cell = self.get_cell(row, col)
                if cell.enabled: return cell
        return None

    def get_prev_cell(self, prev_coords):
        for row in reversed(range(self.dimension.x)):
            if row > prev_coords.y: continue
            for col in reversed(range(self.dimension.y)):
                if row == prev_coords.y and col >= prev_coords.x: continue
                cell = self.get_cell(row, col)
                if cell.enabled: return cell
        return None

    def disable_cell(self, row, col):
        cell = self.get_cell(row, col)
        if cell: cell.enabled = False

    def enable_cell(self, row, col):
        cell = self.get_cell(row, col)
        if cell: cell.enabled = True

    def disable_all(self):
        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                self.disable_cell(row, col)

    def get_enabled_cells(self):
        enabled_cells = []
        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                cell = self.get_cell(row, col)
                if cell.enabled:
                    enabled_cells.append(cell)
        return enabled_cells

    def apply_resource_filter(self, resource_filter=None):
        if resource_filter is None: return
        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                cell = self.get_cell(row, col)
                if not cell.resource_node:
                    cell.enabled = False
                    continue
                cell.enabled = cell.resource_node in resource_filter

    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawLine(int(self.center.x - 10), int(self.center.y), int(self.center.x + 10), int(self.center.y))
        painter.drawLine(int(self.center.x), int(self.center.y - 10), int(self.center.x), int(self.center.y + 10))

        for row in range(self.dimension.x):
            for col in range(self.dimension.y):
                cell = self.get_cell(row, col)
                if not cell.enabled: continue
                cell.draw(painter)