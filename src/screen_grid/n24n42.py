from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_HEMP

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (12, 10),
        (14, 8),
        (15, 9),
        (16, 8)
    ])

    grid.set_resource_nodes(RESOURCE_HEMP, [
        (11, 8),
        (11, 9),
        (13, 7),
        (13, 8),
        (13, 9),
        (13, 10),
        (14, 7),
        (14, 9),
        (14, 10),
        (15, 7),
        (15, 8),
        (15, 10),
        (16, 7),
        (16, 10),
        (17, 6),
        (17, 7),
        (17, 9),
        (18, 7),
        (18, 8),
        (18, 9)
    ])

    return grid