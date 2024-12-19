import time
import asyncio
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor, QPainter
from src.lib.console import BCOLORS
from src.lib.color import similar
from src.lib.screen import get_region_pixmap, get_pixel_color, pixmap_to_pixels
from src.lib.struct import Vector, Rect

DEBUG_SCREENSHOTS = True

class InventoryCell:
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
        if DEBUG_SCREENSHOTS: pixmap.save('cell_{}_{}.png'.format(*self.coords.tuple()))
        self.screenshot = pixmap_to_pixels(pixmap)

    def has_changed(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('cell_{}_{}_check.png'.format(*self.coords.tuple()))
        return self.screenshot != pixmap_to_pixels(pixmap)

    def draw(self, painter: QPainter):
        painter.setPen(QPen(QColor(0, 255, 0), 1))
        rect = self.rect.expand(1)
        painter.drawLine(QPointF(*rect.top_left().tuple()), QPointF(*rect.top_right().tuple()))
        painter.drawLine(QPointF(*rect.top_right().tuple()), QPointF(*rect.bottom_right().tuple()))
        painter.drawLine(QPointF(*rect.bottom_right().tuple()), QPointF(*rect.bottom_left().tuple()))
        painter.drawLine(QPointF(*rect.bottom_left().tuple()), QPointF(*rect.top_left().tuple()))

class Inventory:
    window = None

    top_y = 0
    bottom_y = 0
    height = 0
    scan_start_y = 0
    scan_step = 10

    dimension = Vector(5, 1)

    grid_top_left = None
    cell_size = None
    cell_spacing = 0

    wait_update_start_time = None

    def __init__(self, window):
        self.window = window

    def init(self):
        self.scan_position()

        self.grid_top_left = Vector(
            self.height * 0.702,
            self.height * 0.196
        )
        self.cell_size = Vector(
            self.height * 0.078,
            self.height * 0.078,
        )
        self.cell_spacing = self.cell_size.x * 0.115

        self.cells = {}
        for row in range(self.dimension.y):
            self.cells[row] = {}
            for col in range(self.dimension.x):
                x = self.grid_top_left.x + self.cell_size.x * col + self.cell_size.x / 2 + self.cell_spacing * col
                y = self.top_y + self.grid_top_left.y + self.cell_size.y * row + self.cell_size.y / 2 + self.cell_spacing * row

                self.cells[row][col] = InventoryCell(self.window, Vector(col, row), Vector(x, y), self.cell_size)

        self.update_screenshot()

    def has_changed(self):
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
                if self.cells[row][col].has_changed():
                    return True
        return False

    def scan_position(self):
        print(BCOLORS.grey('Scanning inventory height...'))

        self.scan_start_y = int(self.window.viewport_size.y * 0.1)

        # Search for not black pixel by step
        not_black_y = 0
        for y in range(self.scan_start_y, self.window.viewport_size.y, self.scan_step):
            color = get_pixel_color(self.window.viewport_rect.min.x + 10, self.window.viewport_rect.min.y + y)
            if not similar(color, (0, 0, 0)):
                not_black_y = y
                break
        if not_black_y == 0: raise Exception('Inventory not found')

        # Search for inventory top
        inventory_top_y = 0
        for y in range(not_black_y - self.scan_step, self.window.viewport_size.y, 1):
            color = get_pixel_color(self.window.viewport_rect.min.x + 10, self.window.viewport_rect.min.y + y)
            if not similar(color, (0, 0, 0)):
                inventory_top_y = y
                break
        if inventory_top_y == 0: raise Exception('Inventory not found')

        # Search for black by step
        black_y = 0
        for y in range(inventory_top_y, self.window.viewport_size.y, self.scan_step):
            color = get_pixel_color(self.window.viewport_rect.min.x + 10, self.window.viewport_rect.min.y + y)
            if similar(color, (0, 0, 0)):
                black_y = y
                break
        if black_y == 0: raise Exception('Inventory not found')

        # Search for inventory bottom
        inventory_bottom_y = 0
        for y in range(black_y - self.scan_step, self.window.viewport_size.y, 1):
            color = get_pixel_color(self.window.viewport_rect.min.x + 10, self.window.viewport_rect.min.y + y)
            if similar(color, (0, 0, 0)):
                inventory_bottom_y = y
                break
        if inventory_bottom_y == 0: raise Exception('Inventory not found')

        self.top_y = inventory_top_y
        self.bottom_y = inventory_bottom_y
        self.height = inventory_bottom_y - inventory_top_y

    def update_screenshot(self):
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
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

    def draw(self, painter: QPainter):
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
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
                self.cells[row][col].draw(painter)