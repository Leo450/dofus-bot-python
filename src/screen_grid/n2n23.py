from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_SAGE, [
        (4, 11),
        (28, 5)
    ])

    return grid