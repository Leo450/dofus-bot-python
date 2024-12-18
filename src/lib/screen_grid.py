from PyQt5.QtGui import QPen, QColor
from src.lib.screen_cell import ScreenCell

class ScreenGrid:
    window = None
    dimension = (40, 14)
    cell_size = (0, 0)
    size = (0, 0)
    center = (0, 0)
    offset = (0, 0)
    cells = {}

    def __init__(self, window):
        self.window = window

        self.cell_size = (
            window.viewport_size[1] * 0.086,
            window.viewport_size[1] * 0.043
        )
        self.size = (
            self.dimension[1] * self.cell_size[0],
            self.dimension[0] * (self.cell_size[1] / 2)
        )
        self.offset = (
            self.cell_size[1] * 0.5,
            window.viewport_size[1] * -0.055
        )
        self.center = (
            window.viewport_size[0] / 2 + self.offset[0],
            window.viewport_size[1] / 2 + self.offset[1]
        )

        self.cells = {}
        for row in range(self.dimension[0]):
            self.cells[row] = {}
            for col in range(self.dimension[1]):
                row_offset_x = 0 if row % 2 == 0 else self.cell_size[0] / 2
                x = row_offset_x + self.center[0] - self.size[0] / 2 + col * self.cell_size[0]
                y = self.center[1] - self.size[1] / 2 + row * (self.cell_size[1] / 2)

                self.cells[row][col] = ScreenCell(row, col, x, y, self.cell_size[0], self.cell_size[1])

    def get_cell(self, row, col):
        if row < 0 or row >= self.dimension[0] or col < 0 or col >= self.dimension[1]:
            return None
        return self.cells[row][col]

    def get_closest_cell(self, x, y, enabled_only=True):
        closest_cell = None
        min_distance = float('inf')

        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                cell = self.get_cell(row, col)
                if enabled_only and not cell.enabled: continue
                distance = (cell.vertices['center'][0] - x) ** 2 + (cell.vertices['center'][1] - y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_cell = cell

        return closest_cell

    def get_nb_enabled_cells(self):
        nb_cells = 0

        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                cell = self.get_cell(row, col)
                if cell.enabled:
                    nb_cells += 1

        return nb_cells

    def get_last_enabled_cell(self):
        for row in reversed(range(self.dimension[0])):
            for col in reversed(range(self.dimension[1])):
                cell = self.get_cell(row, col)
                if cell.enabled: return cell
        return None

    def get_next_cell(self, prev_row, prev_col):
        for row in range(self.dimension[0]):
            if row < prev_row: continue
            for col in range(self.dimension[1]):
                if row == prev_row and col <= prev_col: continue
                cell = self.get_cell(row, col)
                if cell.enabled: return cell
        return None

    def get_prev_cell(self, prev_row, prev_col):
        for row in reversed(range(self.dimension[0])):
            if row > prev_row: continue
            for col in reversed(range(self.dimension[1])):
                if row == prev_row and col >= prev_col: continue
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
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                self.disable_cell(row, col)

    def get_enabled_cells(self):
        enabled_cells = []
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                cell = self.get_cell(row, col)
                if cell.enabled:
                    enabled_cells.append(cell)
        return enabled_cells

    def apply_resource_filter(self, resource_filter):
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                cell = self.get_cell(row, col)
                if not cell.resource_node:
                    cell.enabled = False
                    continue
                cell.enabled = cell.resource_node in resource_filter

    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawLine(int(self.center[0] - 10), int(self.center[1]), int(self.center[0] + 10), int(self.center[1]))
        painter.drawLine(int(self.center[0]), int(self.center[1] - 10), int(self.center[0]), int(self.center[1] + 10))

        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                cell = self.get_cell(row, col)
                if not cell.enabled: continue
                cell.draw(painter)