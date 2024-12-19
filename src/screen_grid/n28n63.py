from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def n28n63(window):
    grid = ScreenGrid(window)

    grid.get_cell(32, 8).set_resource_node(RESOURCE_NETTLE).set_resource_mouse_offset(-grid.cell_size.x / 4, 0)
    grid.get_cell(36, 10).set_resource_node(RESOURCE_NETTLE)

    grid.get_cell(35, 1).set_resource_node(RESOURCE_SAGE)

    return grid