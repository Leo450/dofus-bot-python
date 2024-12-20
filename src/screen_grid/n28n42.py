from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_HOPS, RESOURCE_HEMP

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (6, 7),
        (6, 8),
        (7, 6),
        (9, 6),
        (12, 5)
    ])

    grid.set_resource_nodes(RESOURCE_HEMP, [
        (23, 8),
        (24, 9),
        (25, 7),
        (25, 8),
        (25, 9),
        (26, 7),
        (26, 8),
        (26, 9),
        (26, 10),
        (27, 6),
        (27, 8),
        (27, 9),
        (27, 10),
        (28, 6),
        (28, 7),
        (28, 8),
        (29, 6),
        (29, 8),
        (29, 9),
        (29, 10),
        (30, 7),
        (30, 8),
        (30, 9),
        (30, 10),
        (31, 8),
        (32, 8),
        (32, 9)
    ])

    return grid