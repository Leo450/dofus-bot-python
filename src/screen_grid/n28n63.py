from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE, RESOURCE_SAGE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_NETTLE, (32, 8)).set_resource_mouse_offset(-grid.cell_size.x / 4, 0)
    grid.set_resource_node(RESOURCE_NETTLE, (36, 10))

    grid.set_resource_node(RESOURCE_SAGE, (35, 1))

    return grid