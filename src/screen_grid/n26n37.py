from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (6, 5),
        (7, 5),
        (8, 4),
        (8, 5),
        (8, 6),
        (9, 4),
        (9, 5),
        (9, 6),
        (10, 5),
        (10, 6),
        (10, 7),
        (11, 5),
        (12, 6)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (20, 5),
        (21, 5),
        (22, 5),
        (22, 6),
        (23, 4),
        (23, 5),
        (24, 6),
        (25, 5)
    ])

    return grid