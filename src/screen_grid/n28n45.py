from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (23, 4),
        (15, 3),
        (15, 4),
        (15, 5),
        (17, 2),
        (17, 3),
        (17, 4),
        (18, 6),
        (19, 2),
        (19, 3),
        (20, 5),
        (21, 2),
        (21, 3),
        (21, 4),
        (23, 4)
    ])

    return grid