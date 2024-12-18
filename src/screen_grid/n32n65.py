from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def n32n65(window):
    grid = ScreenGrid(window)

    grid.get_cell(23, 1).set_resource_node(RESOURCE_NETTLE)

    grid.get_cell(34, 9).set_resource_node(RESOURCE_SAGE)

    return grid