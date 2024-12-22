from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_ORCHID


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_ORCHID, [
        (6, 9),
        (19, 11),
        (23, 4),
        (30, 11)
    ])

    return grid