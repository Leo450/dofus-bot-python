from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_CLOVER

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_CLOVER, (31, 7))

    return grid