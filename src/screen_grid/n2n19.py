from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_CLOVER, RESOURCE_MINT


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_CLOVER, (18, 11))

    grid.set_resource_node(RESOURCE_MINT, (4, 9))

    return grid