from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE

def n24n64(window):
    grid = ScreenGrid(window)

    grid.get_cell(5, 1).set_resource_node(RESOURCE_NETTLE)

    return grid