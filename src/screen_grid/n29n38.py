from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (12, 7),
        (13, 6),
        (13, 7),
        (14, 6),
        (14, 7),
        (14, 8),
        (15, 5),
        (15, 6),
        (15, 7),
        (15, 8),
        (16, 7),
        (16, 8),
        (17, 6),
        (17, 8),
        (18, 7),
        (18, 8),
        (19, 7)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (21, 4),
        (22, 5),
        (23, 3),
        (23, 4),
        (24, 4),
        (24, 9),
        (25, 10),
        (25, 11),
        (26, 10),
        (26, 11),
        (27, 10),
        (27, 11),
        (28, 11)
    ])

    return grid