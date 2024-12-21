from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_MINT


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (12, 8))

    grid.set_resource_node(RESOURCE_MINT, (13, 9))

    return grid