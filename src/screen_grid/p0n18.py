from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_CLOVER

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_CLOVER, [
        (4, 4),
        (17, 7)
    ])

    return grid