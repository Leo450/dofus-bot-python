from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_HOPS

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (11, 2),
        (7, 3),
        (8, 4),
        (9, 2),
        (10, 3),
        (10, 4),
        (11, 2),
        (11, 3),
        (11, 4),
        (11, 5),
        (13, 3),
        (13, 4),
        (18, 7),
        (18, 8),
        (19, 8),
        (20, 7),
        (21, 6),
        (21, 7),
        (21, 8),
        (21, 9),
        (22, 7),
        (22, 9),
        (22, 10),
        (23, 7),
        (23, 8),
        (24, 9)
    ])

    return grid