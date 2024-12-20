from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WATER


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WATER, (15, 10))

    return grid