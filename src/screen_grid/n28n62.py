from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def n28n62(window):
    grid = ScreenGrid(window)

    grid.get_cell(9, 9).set_resource_node(RESOURCE_NETTLE)

    grid.get_cell(5, 10).set_resource_node(RESOURCE_SAGE)

    return grid