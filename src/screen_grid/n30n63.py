from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def n30n63(window):
    grid = ScreenGrid(window)

    grid.get_cell(5, 9).set_resource_node(RESOURCE_SAGE)

    return grid