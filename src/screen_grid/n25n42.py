from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT, RESOURCE_MALT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_OAT, [
        (5, 10),
        (5, 11),
        (7, 9),
        (7, 10),
        (7, 11),
        (7, 12),
        (8, 12),
        (9, 10),
        (9, 11)
    ])

    grid.set_resource_nodes(RESOURCE_MALT, [
        (21, 2),
        (22, 2),
        (23, 2),
        (31, 6),
        (31, 7),
        (32, 7)
    ])

    return grid