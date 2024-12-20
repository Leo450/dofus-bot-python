from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (13, 12))

    return grid