from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE

def n26n64(window):
    grid = ScreenGrid(window)

    grid.get_cell(12, 1).set_resource_node(RESOURCE_NETTLE).set_resource_mouse_offset((-grid.cell_size[0] / 4, 0))

    return grid