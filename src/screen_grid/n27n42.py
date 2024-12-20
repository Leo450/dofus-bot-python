from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_HOPS, RESOURCE_RYE, RESOURCE_MALT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (10, 3),
        (11, 2),
        (11, 3),
        (12, 3),
        (13, 1),
        (13, 2),
        (13, 3),
        (13, 4),
        (14, 2),
        (15, 2),
        (15, 3)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (24, 7),
        (18, 4),
        (19, 3),
        (19, 4),
        (20, 4),
        (23, 6),
        (24, 6),
        (24, 7),
        (25, 6)
    ])

    grid.set_resource_nodes(RESOURCE_MALT, [
        (9, 4),
        (10, 5),
        (11, 5)
    ])

    return grid