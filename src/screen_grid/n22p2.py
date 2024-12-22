from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_ORCHID


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_ORCHID, [
        (13, 11),
        (13, 13),
        (23, 3)
    ])

    return grid