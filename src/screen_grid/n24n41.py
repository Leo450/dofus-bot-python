from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (27, 3),
        (28, 2),
        (28, 3),
        (28, 4),
        (29, 1),
        (29, 2),
        (29, 4),
        (30, 2),
        (31, 2),
        (31, 4),
        (32, 3)
    ])

    return grid