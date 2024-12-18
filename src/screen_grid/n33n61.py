from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def n33n61(window):
    grid = ScreenGrid(window)

    grid.get_cell(13, 11).set_resource_node(RESOURCE_SAGE)

    return grid