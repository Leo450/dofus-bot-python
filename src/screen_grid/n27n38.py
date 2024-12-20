from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_OAT, [
        (9, 11),
        (10, 11),
        (12, 11),
        (12, 12),
        (14, 12),
        (21, 2),
        (22, 3),
        (23, 1),
        (23, 2),
        (24, 4),
        (25, 1),
        (25, 2),
        (25, 4),
        (26, 2),
        (26, 3),
        (26, 4)
    ])

    return grid