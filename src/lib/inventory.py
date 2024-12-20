import time
import asyncio
from PyQt5.QtGui import QPen, QColor, QPainter
from src.lib.console import BCOLORS
from src.lib.color import similar
from src.lib.inventory_gauge import InventoryGauge
from src.lib.inventory_slot import InventorySlot
from src.lib.screen import get_pixel_color
from src.lib.struct import Vector


class Inventory:
    window = None

    top_y = 0
    bottom_y = 0
    height = 0
    scan_start_y = 0
    scan_step = 10

    dimension = Vector(5, 8)
    grid_top_left = None
    slot_size = None
    slot_spacing = 0
    slots = {}
    
    gauge = None

    wait_update_start_time = None

    def __init__(self, window):
        self.window = window

    def init(self):
        self.scan_position()

        self.grid_top_left = Vector(
            self.height * 0.702,
            self.height * 0.196
        )
        self.slot_size = Vector(
            self.height * 0.078,
            self.height * 0.078,
        )
        self.slot_spacing = self.slot_size.x * 0.115

        self.slots = {}
        for row in range(self.dimension.y):
            self.slots[row] = {}
            for col in range(self.dimension.x):
                self.slots[row][col] = InventorySlot(
                    self.window,
                    Vector(col, row),
                    Vector(
                        self.grid_top_left.x + self.slot_size.x * col + self.slot_size.x / 2 + self.slot_spacing * col,
                        self.top_y + self.grid_top_left.y + self.slot_size.y * row + self.slot_size.y / 2 + self.slot_spacing * row
                    ),
                    self.slot_size
                )
        self.update_slots_screenshots()

        self.gauge = InventoryGauge(
            self.window,
            Vector(
                self.grid_top_left.x - self.height * 0.022,
                self.top_y + self.grid_top_left.y + self.height * 0.778
            ),
            Vector(self.height * 0.022, self.height * 0.022)
        )
        if self.gauge.is_full(): raise Exception('Inventory is full')

    def has_changed(self):
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
                if self.slots[row][col].has_changed():
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

    def update_slots_screenshots(self):
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
                self.slots[row][col].update_screenshot()

    async def wait_update(self, max_time=10):
        if self.wait_update_start_time is None:
            self.wait_update_start_time = time.time()

        if time.time() - self.wait_update_start_time > max_time:
            self.wait_update_start_time = None
            return False

        if self.has_changed():
            self.update_slots_screenshots()
            self.wait_update_start_time = None
            return True

        await asyncio.sleep(1)
        return await self.wait_update(max_time)

    def is_full(self):
        return self.gauge.is_full()

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

        # Draw slots
        for row in range(self.dimension.y):
            for col in range(self.dimension.x):
                self.slots[row][col].draw(painter)

        # Draw gauge
        self.gauge.draw(painter)