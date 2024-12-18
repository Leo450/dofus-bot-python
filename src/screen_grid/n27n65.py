from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def n27n65(window):
    grid = ScreenGrid(window)

    grid.get_cell(15, 6).set_resource_node(RESOURCE_NETTLE)

    grid.get_cell(7, 11).set_resource_node(RESOURCE_SAGE)

    return grid