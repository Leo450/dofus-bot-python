from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def n24n62(window):
    grid = ScreenGrid(window)

    grid.get_cell(10, 8).set_resource_node(RESOURCE_NETTLE)

    grid.get_cell(22, 6).set_resource_node(RESOURCE_SAGE)

    return grid