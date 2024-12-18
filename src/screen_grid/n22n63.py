from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_NETTLE

def n22n63(window):
    grid = ScreenGrid(window)

    grid.get_cell(31, 10).set_resource_node(RESOURCE_NETTLE)

    return grid