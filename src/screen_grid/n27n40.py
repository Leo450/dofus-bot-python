from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (9, 11),
        (10, 11),
        (10, 12),
        (11, 10),
        (11, 11),
        (11, 12),
        (12, 11),
        (12, 12),
        (13, 10),
        (13, 11),
        (14, 11)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (8, 9),
        (9, 9)
    ])

    return grid