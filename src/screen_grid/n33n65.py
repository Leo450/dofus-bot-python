from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def n33n65(window):
    grid = ScreenGrid(window)

    grid.get_cell(8, 10).set_resource_node(RESOURCE_SAGE)

    return grid