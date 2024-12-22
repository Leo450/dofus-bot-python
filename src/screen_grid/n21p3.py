from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_ORCHID


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_ORCHID, [
        (15, 10),
        (16, 10),
        (31, 4)
    ])

    return grid