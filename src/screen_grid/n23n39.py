from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_FLAX, RESOURCE_RYE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_FLAX, [
        (17, 7),
        (18, 7),
        (18, 8),
        (19, 6),
        (19, 7),
        (20, 6),
        (20, 7),
        (20, 8),
        (20, 9),
        (21, 6),
        (21, 7),
        (21, 8),
        (21, 9),
        (22, 7),
        (22, 9),
        (22, 10),
        (23, 7),
        (23, 8),
        (24, 7),
        (24, 8),
        (24, 9),
        (25, 8)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (8, 2),
        (9, 1),
        (9, 2),
        (10, 2)
    ])

    return grid