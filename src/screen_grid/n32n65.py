from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_NETTLE, (23, 1))

    grid.set_resource_node(RESOURCE_SAGE, (34, 9)).set_resource_mouse_offset(-grid.cell_size.x / 4, -grid.cell_size.y / 4)

    return grid