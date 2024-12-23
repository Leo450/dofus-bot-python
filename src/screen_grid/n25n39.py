from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_FLAX, RESOURCE_MALT


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_FLAX, [
        (17, 4),
        (19, 3),
        (19, 4),
        (19, 5),
        (20, 3),
        (20, 4),
        (20, 5),
        (21, 2),
        (21, 5),
        (22, 4),
        (22, 5),
        (23, 3),
        (23, 4),
        (24, 3),
        (25, 3)
    ])

    grid.set_resource_nodes(RESOURCE_MALT, [
        (27, 5),
        (28, 5),
        (28, 6),
        (29, 5)
    ])

    return grid