from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_OAT, [
        (25, 7),
        (26, 7),
        (26, 8),
        (27, 6),
        (29, 5),
        (29, 6),
        (29, 7),
        (29, 8),
        (31, 6),
        (31, 7)
    ])

    return grid