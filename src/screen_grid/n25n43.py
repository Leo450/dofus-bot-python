from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (5, 5),
        (6, 6),
        (7, 4),
        (7, 5),
        (8, 6),
        (8, 7),
        (9, 5),
        (10, 6),
        (14, 2),
        (15, 2),
        (16, 2),
        (16, 3),
        (17, 1),
        (17, 3),
        (18, 1),
        (18, 3),
        (18, 4),
        (19, 1),
        (19, 2),
        (21, 2)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (35, 1),
        (35, 2),
        (36, 3),
        (37, 2)
    ])

    return grid