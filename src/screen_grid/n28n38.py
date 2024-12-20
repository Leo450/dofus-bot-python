from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_OAT, [
        (7, 6),
        (7, 7),
        (8, 6),
        (8, 7),
        (8, 8),
        (9, 5),
        (10, 7),
        (11, 6),
        (12, 9),
        (13, 8),
        (13, 9),
        (14, 10),
        (15, 9),
        (16, 10),
        (17, 7),
        (17, 9),
        (18, 9)
    ])

    return grid