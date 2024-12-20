from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_NETTLE, (34, 1))

    return grid