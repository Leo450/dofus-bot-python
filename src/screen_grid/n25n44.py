from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (14, 5),
        (14, 6),
        (15, 4),
        (16, 4),
        (17, 4),
        (18, 3),
        (19, 2),
        (19, 3),
        (20, 5),
        (21, 2),
        (22, 3),
        (22, 4)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (14, 9),
        (15, 7),
        (15, 9)
    ])

    return grid