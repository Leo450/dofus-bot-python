from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_MINT


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (33, 2))

    grid.set_resource_node(RESOURCE_MINT, (33, 11))

    return grid