from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (6, 9),
        (7, 8),
        (8, 8),
        (8, 9),
        (9, 7),
        (9, 8),
        (10, 8),
        (13, 6),
        (14, 6),
        (14, 7),
        (15, 5),
        (15, 6),
        (15, 7),
        (16, 6),
        (16, 7),
        (17, 5),
        (17, 6),
        (18, 6)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (19, 8),
        (20, 8),
        (21, 7),
        (21, 9),
        (22, 7),
        (22, 9),
        (22, 10),
        (23, 7),
        (23, 9),
        (24, 10),
        (25, 9)
    ])

    return grid