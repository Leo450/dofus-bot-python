from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_OAT, [
        (15, 7),
        (17, 6),
        (17, 8),
        (18, 9),
        (19, 5),
        (19, 7),
        (19, 9),
        (20, 9),
        (20, 10),
        (21, 6),
        (21, 7),
        (22, 7),
        (22, 8)
    ])

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (31, 7),
        (32, 7),
        (32, 8),
        (33, 6),
        (33, 7),
        (33, 8),
        (34, 7),
        (34, 9),
        (35, 7),
        (35, 8),
        (35, 9),
        (36, 9),
        (37, 8),
        (37, 9)
    ])

    return grid