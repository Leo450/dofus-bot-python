from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_CLOVER

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (13, 8))

    grid.set_resource_node(RESOURCE_CLOVER, (1, 7))

    return grid