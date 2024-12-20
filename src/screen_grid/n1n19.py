from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WATER, RESOURCE_CLOVER

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WATER, (13, 8))

    grid.set_resource_node(RESOURCE_CLOVER, (24, 4))

    return grid