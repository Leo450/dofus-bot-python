from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY, RESOURCE_HOPS

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (2, 2),
        (3, 1),
        (4, 2),
        (4, 3),
        (5, 1)
    ])

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (9, 10),
        (9, 11),
        (10, 12),
        (11, 10),
        (11, 12),
        (12, 10),
        (12, 11),
        (12, 12),
        (12, 13),
        (13, 12),
        (14, 11),
        (15, 11),
        (15, 12),
        (17, 11)
    ])

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (26, 4),
        (27, 3),
        (27, 4),
        (28, 3),
        (28, 4),
        (28, 5),
        (29, 2),
        (29, 3),
        (29, 4),
        (30, 2),
        (30, 3),
        (30, 4),
        (30, 5),
        (31, 4),
        (32, 3),
        (32, 4)
    ])

    return grid