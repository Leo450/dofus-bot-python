from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_SAGE, [
        (4, 9),
        (16, 2)
    ])

    return grid