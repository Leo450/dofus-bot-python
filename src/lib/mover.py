import asyncio

from PyQt5.QtCore import QPointF

import src.lib.keyboard as keyboard
import src.lib.mouse as mouse
from PyQt5.QtGui import QPen, QColor
from src.lib.console import BCOLORS
from src.lib.astar import PATH_LEFT, PATH_RIGHT, PATH_UP, PATH_DOWN
from src.lib.minimap import Minimap

class Mover:
    current_direction = None
    nb_direction_failed = 0

    def __init__(self, window, overlay, map_grid):
        self.window = window
        self.overlay = overlay
        self.map_grid = map_grid
        self.minimap = Minimap(self.window)

    def init(self):
        self.minimap.update_screenshot()

    async def go_to_map_cell(self, start_coords, end_coords):
        print(BCOLORS.colorize(' >> Moving: from {} to {} '.format(start_coords, end_coords), BCOLORS.BG_LIGHT_PURPLE + BCOLORS.BLACK + BCOLORS.BOLD))
        path = self.map_grid.get_path(start_coords, end_coords)
        print(BCOLORS.purple('> Path: {}'.format(path)))
        await self.go_to_path(path)
        print(BCOLORS.green('> Arrived at: {}'.format(end_coords)))

    async def go_to_path(self, path):
        if len(path) == 0:
            return

        #print(BCOLORS.grey('Going through path: {}'.format(path)))

        self.current_direction = path.pop(0)
        self.overlay.set_drawable('mover', self)
        await self.go_to_direction(self.current_direction)
        print(BCOLORS.green('> Moved direction: {}'.format(self.current_direction)))
        self.current_direction = None
        self.overlay.remove_drawable('mover')

        await asyncio.sleep(.5)
        await self.go_to_path(path)

    async def go_to_direction(self, direction):
        print(BCOLORS.cyan('> Moving direction: {}'.format(direction)))

        key = None
        if direction == PATH_LEFT:
            key = 'q'
        elif direction == PATH_RIGHT:
            key = 'd'
        elif direction == PATH_UP:
            key = 'z'
        elif direction == PATH_DOWN:
            key = 's'

        #print(BCOLORS.grey('Pressing key: {}'.format(key)))
        keyboard.controller.press(key)
        keyboard.controller.release(key)

        print(BCOLORS.grey('Waiting for minimap update...'))
        if not await self.minimap.wait_update():
            self.nb_direction_failed += 1
            if self.nb_direction_failed >= 3:
                raise Exception('Too many minimap update detection failed')
            print(BCOLORS.red('> No minimap update detected, retrying direction: {}'.format(direction)))
            self.window.focus()
            mouse.move(self.window.screen_size[0] / 2, self.window.screen_size[1] / 2)
            await self.go_to_direction(direction)
        else:
            self.nb_direction_failed = 0

    def draw(self, painter):
        if self.current_direction is None: return

        painter.setPen(QPen(QColor(255, 255, 255), 20))
        if self.current_direction == PATH_LEFT:
            # Draw arrow left
            point = (self.window.x_overflow, self.window.viewport_size[1] / 2)
            painter.drawLine(QPointF(*point), QPointF(point[0] + 100, point[1] - 100))
            painter.drawLine(QPointF(*point), QPointF(point[0] + 100, point[1] + 100))
        elif self.current_direction == PATH_RIGHT:
            # Draw arrow right
            point = (self.window.viewport_size[0] - self.window.x_overflow, self.window.viewport_size[1] / 2)
            painter.drawLine(QPointF(*point), QPointF(point[0] - 100, point[1] - 100))
            painter.drawLine(QPointF(*point), QPointF(point[0] - 100, point[1] + 100))
        elif self.current_direction == PATH_UP:
            # Draw arrow up
            point = (self.window.viewport_size[0] / 2, 0)
            painter.drawLine(QPointF(*point), QPointF(point[0] - 100, point[1] + 100))
            painter.drawLine(QPointF(*point), QPointF(point[0] + 100, point[1] + 100))
        elif self.current_direction == PATH_DOWN:
            # Draw arrow down
            point = (self.window.viewport_size[0] / 2, self.window.viewport_size[1])
            painter.drawLine(QPointF(*point), QPointF(point[0] - 100, point[1] - 100))
            painter.drawLine(QPointF(*point), QPointF(point[0] + 100, point[1] - 100))
