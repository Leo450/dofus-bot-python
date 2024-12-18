import time
import asyncio
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor
from src.lib.console import BCOLORS
from src.lib.color import similar
from src.lib.screen import get_region_pixmap, get_pixel_color, pixmap_to_pixels

DEBUG_SCREENSHOTS = False

class Cell:
    window = None
    coords = (0, 0)
    size = (0, 0)
    vertices = {
        'top_left': (0, 0),
        'top_right': (0, 0),
        'bottom_right': (0, 0),
        'bottom_left': (0, 0)
    }
    screenshot = None

    def __init__(self, window, row, col, x, y, w, h):
        self.window = window
        self.coords = (row, col)
        self.size = (w, h)
        self.vertices = {
            'top_left': (x - w / 2, y - h / 2),
            'top_right': (x + w / 2, y - h / 2),
            'bottom_right': (x + w / 2, y + h / 2),
            'bottom_left': (x - w / 2, y + h / 2)
        }

    def get_screenshot_pixmap(self):
        screen_top_left = self.window.to_screen(*self.vertices['top_left'])
        return get_region_pixmap(int(screen_top_left[0]), int(screen_top_left[1]), int(self.size[0]), int(self.size[1]))

    def update_screenshot(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('cell_{}_{}.png'.format(*self.coords))
        self.screenshot = pixmap_to_pixels(pixmap)

    def has_changed(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('cell_{}_{}_check.png'.format(*self.coords))
        return self.screenshot != pixmap_to_pixels(pixmap)

    def draw(self, painter):
        min_x = min(self.vertices['top_left'][0], self.vertices['top_right'][0], self.vertices['bottom_right'][0], self.vertices['bottom_left'][0]) - 1
        max_x = max(self.vertices['top_left'][0], self.vertices['top_right'][0], self.vertices['bottom_right'][0], self.vertices['bottom_left'][0])
        min_y = min(self.vertices['top_left'][1], self.vertices['top_right'][1], self.vertices['bottom_right'][1], self.vertices['bottom_left'][1]) - 1
        max_y = max(self.vertices['top_left'][1], self.vertices['top_right'][1], self.vertices['bottom_right'][1], self.vertices['bottom_left'][1])

        painter.setPen(QPen(QColor(0, 255, 0), 1))
        # painter.drawLine(QPointF(*self.vertices['top_left']), QPointF(*self.vertices['top_right']))
        # painter.drawLine(QPointF(*self.vertices['top_right']), QPointF(*self.vertices['bottom_right']))
        # painter.drawLine(QPointF(*self.vertices['bottom_right']), QPointF(*self.vertices['bottom_left']))
        # painter.drawLine(QPointF(*self.vertices['bottom_left']), QPointF(*self.vertices['top_left']))
        painter.drawLine(QPointF(min_x, min_y), QPointF(max_x, min_y))
        painter.drawLine(QPointF(max_x, min_y), QPointF(max_x, max_y))
        painter.drawLine(QPointF(max_x, max_y), QPointF(min_x, max_y))
        painter.drawLine(QPointF(min_x, max_y), QPointF(min_x, min_y))

class Inventory:
    window = None

    top_y = 0
    bottom_y = 0
    height = 0
    scan_start_y = 0
    scan_step = 10

    dimension = (1, 5)

    grid_top_left = (0, 0)
    cell_size = (0, 0)
    cell_spacing = 0

    # full_top_left = (0, 0)
    # full_size = (0, 0)
    # full_screenshot = None

    wait_update_start_time = None

    def __init__(self, window):
        self.window = window

    def init(self):
        self.scan_position()

        self.grid_top_left = (
            self.height * 0.702,
            self.height * 0.196
        )
        self.cell_size = (
            self.height * 0.078,
            self.height * 0.078,
        )
        self.cell_spacing = self.cell_size[0] * 0.115

        # self.full_top_left = (
        #     self.height * 0.678,
        #     self.height * 0.975
        # )
        # self.full_size = (
        #     self.height * 0.02,
        #     self.height * 0.02
        # )

        self.cells = {}
        for row in range(self.dimension[0]):
            self.cells[row] = {}
            for col in range(self.dimension[1]):
                x = self.grid_top_left[0] + self.cell_size[0] * col + self.cell_size[0] / 2 + self.cell_spacing * col
                y = self.top_y + self.grid_top_left[1] + self.cell_size[1] * row + self.cell_size[1] / 2 + self.cell_spacing * row

                self.cells[row][col] = Cell(self.window, row, col, x, y, self.cell_size[0], self.cell_size[1])

        self.update_screenshot()

    def has_changed(self):
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                if self.cells[row][col].has_changed():
                    return True
        return False

    def scan_position(self):
        print(BCOLORS.grey('Scanning inventory height for viewport height: {}...'.format(self.window.viewport_size[1])))

        self.scan_start_y = int(self.window.viewport_size[1] * 0.1)

        # Search for not black pixel by step
        not_black_y = 0
        for y in range(self.scan_start_y, self.window.viewport_size[1], self.scan_step):
            color = get_pixel_color(self.window.viewport_rect[0] + 10, self.window.viewport_rect[1] + y)
            if not similar(color, (0, 0, 0)):
                not_black_y = y
                break
        if not_black_y == 0: raise Exception('Inventory not found')

        # Search for inventory top
        inventory_top_y = 0
        for y in range(not_black_y - self.scan_step, self.window.viewport_size[1], 1):
            color = get_pixel_color(self.window.viewport_rect[0] + 10, self.window.viewport_rect[1] + y)
            if not similar(color, (0, 0, 0)):
                inventory_top_y = y
                break
        if inventory_top_y == 0: raise Exception('Inventory not found')

        # Search for black by step
        black_y = 0
        for y in range(inventory_top_y, self.window.viewport_size[1], self.scan_step):
            color = get_pixel_color(self.window.viewport_rect[0] + 10, self.window.viewport_rect[1] + y)
            if similar(color, (0, 0, 0)):
                black_y = y
                break
        if black_y == 0: raise Exception('Inventory not found')

        # Search for inventory bottom
        inventory_bottom_y = 0
        for y in range(black_y - self.scan_step, self.window.viewport_size[1], 1):
            color = get_pixel_color(self.window.viewport_rect[0] + 10, self.window.viewport_rect[1] + y)
            if similar(color, (0, 0, 0)):
                inventory_bottom_y = y
                break
        if inventory_bottom_y == 0: raise Exception('Inventory not found')

        self.top_y = inventory_top_y
        self.bottom_y = inventory_bottom_y
        self.height = inventory_bottom_y - inventory_top_y

    def update_screenshot(self):
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                self.cells[row][col].update_screenshot()

    async def wait_update(self, max_time=10):
        if self.wait_update_start_time is None:
            self.wait_update_start_time = time.time()

        if time.time() - self.wait_update_start_time > max_time:
            self.wait_update_start_time = None
            return False

        if self.has_changed():
            self.update_screenshot()
            self.wait_update_start_time = None
            return True

        await asyncio.sleep(1)
        return await self.wait_update(max_time)

    def draw(self, painter):
        # Draw scan start
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawLine(-10, self.scan_start_y - 10, 10, self.scan_start_y + 10)
        painter.drawLine(-10, self.scan_start_y + 10, 10, self.scan_start_y - 10)

        # Draw inventory top
        painter.setPen(QPen(QColor(0, 255, 0), 2))
        painter.drawLine(-10, self.top_y - 10, 10, self.top_y + 10)
        painter.drawLine(-10, self.top_y + 10, 10, self.top_y - 10)

        # Draw inventory bottom
        painter.setPen(QPen(QColor(0, 0, 255), 2))
        painter.drawLine(-10, self.bottom_y - 10, 10, self.bottom_y + 10)
        painter.drawLine(-10, self.bottom_y + 10, 10, self.bottom_y - 10)

        # Draw cells
        for row in range(self.dimension[0]):
            for col in range(self.dimension[1]):
                self.cells[row][col].draw(painter)

        # Draw full
        # painter.setPen(QPen(QColor(0, 255, 0), 1))
        # painter.drawLine(QPointF(*self.full_top_left), QPointF(self.full_top_left[0] + self.full_size[0], self.full_top_left[1]))
        # painter.drawLine(QPointF(self.full_top_left[0] + self.full_size[0], self.full_top_left[1]), QPointF(self.full_top_left[0] + self.full_size[0], self.full_top_left[1] + self.full_size[1]))
        # painter.drawLine(QPointF(self.full_top_left[0], self.full_top_left[1] + self.full_size[1]), QPointF(self.full_top_left[0] + self.full_size[0], self.full_top_left[1] + self.full_size[1]))
        # painter.drawLine(QPointF(*self.full_top_left), QPointF(self.full_top_left[0], self.full_top_left[1] + self.full_size[1]))