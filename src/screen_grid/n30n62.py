from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_NETTLE, (17, 2))

    grid.set_resource_node(RESOURCE_SAGE, (5, 12))

    return grid