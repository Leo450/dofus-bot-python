from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY, RESOURCE_OAT, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (25, 0),
        (27, 0),
        (27, 1),
        (28, 1),
        (28, 2)
    ])

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (8, 7),
        (9, 6),
        (9, 7),
        (10, 6),
        (10, 7),
        (11, 5),
        (11, 6),
        (11, 7),
        (12, 6),
        (12, 7),
        (13, 6)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (11, 10),
        (12, 12),
        (13, 10),
        (14, 13),
        (15, 11),
        (15, 12)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (23, 1),
        (24, 1),
        (24, 2)
    ])

    return grid