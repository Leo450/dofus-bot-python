from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE
from src.lib.struct import Vector


def n27n63(window):
    grid = ScreenGrid(window)

    grid.get_cell(37, 6).set_resource_node(RESOURCE_NETTLE).set_resource_mouse_offset(0, -grid.cell_size.y / 2)

    return grid