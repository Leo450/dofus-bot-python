from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def n31n62(window):
    grid = ScreenGrid(window)

    grid.get_cell(26, 2).set_resource_node(RESOURCE_SAGE)

    return grid