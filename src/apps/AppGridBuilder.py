from PyQt5.QtWidgets import QApplication
from src.lib.overlay import Overlay
from src.lib.struct import Vector
from src.lib.window import Window
from src.lib.screen_grid import ScreenGrid
from src.lib.mouse import add_handler as add_mouse_handler
from src.lib.keyboard import add_handler as add_keyboard_handler

class AppGridBuilder:
    coords = []

    def run(self):
        app = QApplication([])

        window = Window()
        window.init()

        grid = ScreenGrid(window)
        grid.disable_all()
        overlay = Overlay(window)
        overlay.set_drawable('grid', grid)

        # Mouse
        def on_click(x, y):
            window_coords = window.to_viewport(Vector(x, y))
            closest_cell = grid.get_closest_cell(*window_coords.tuple(), False)

            if not closest_cell: return

            print(closest_cell.coords.flip())

            if closest_cell.enabled:
                grid.disable_cell(closest_cell.coords.y, closest_cell.coords.x)
            else:
                grid.enable_cell(closest_cell.coords.y, closest_cell.coords.x)
            overlay.set_drawable('grid', grid)
            overlay.update()

        def on_keyboard():
            for cell in grid.get_enabled_cells():
                print(f'{cell.coords.flip()},')
        add_keyboard_handler('²', on_keyboard)

        add_mouse_handler('click', on_click)

        app.exec_()