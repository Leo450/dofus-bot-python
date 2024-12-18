from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE

def n31n64(window):
    grid = ScreenGrid(window)

    grid.get_cell(21, 1).set_resource_node(RESOURCE_NETTLE)

    return grid