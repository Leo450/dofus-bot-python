import time
import asyncio
from src.lib.console import BCOLORS
from src.lib.screen import get_region_pixmap, pixmap_to_pixels
from src.lib.struct import Vector

DEBUG_SCREENSHOTS = False

class Minimap:
    window = None
    screenshot = None
    wait_update_start_time = None

    def __init__(self, window):
        self.window = window

    def get_screenshot_pixmap(self):
        screen_bottom_right = self.window.viewport_rect.bottom_right()
        return get_region_pixmap(screen_bottom_right + Vector(-100, -100), Vector(90, 90))

    def update_screenshot(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('minimap.png')
        self.screenshot = pixmap_to_pixels(pixmap)

    def has_changed(self):
        pixmap = self.get_screenshot_pixmap()
        if DEBUG_SCREENSHOTS: pixmap.save('minimap_check.png')
        return self.screenshot != pixmap_to_pixels(pixmap)

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
        painter.drawPixmap(0, 0, self.screenshot)