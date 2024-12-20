from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE
from src.lib.struct import Vector


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_NETTLE, (37, 6)).set_resource_mouse_offset(0, -grid.cell_size.y / 2)

    return grid