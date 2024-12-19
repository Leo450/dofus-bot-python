from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE


def n31n65(window):
    grid = ScreenGrid(window)

    grid.get_cell(20, 12).set_resource_node(RESOURCE_NETTLE).set_resource_mouse_offset(-grid.cell_size.x / 4, 0)

    return grid