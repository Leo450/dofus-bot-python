from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_FLAX

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (8, 10),
        (8, 11),
        (9, 10),
        (10, 11),
        (11, 9),
        (11, 11),
        (11, 12),
        (13, 11)
    ])

    grid.set_resource_nodes(RESOURCE_FLAX, [
        (20, 7),
        (18, 7),
        (18, 8),
        (19, 7),
        (19, 8),
        (20, 7),
        (20, 9),
        (21, 7),
        (21, 8),
        (22, 8)
    ])

    return grid