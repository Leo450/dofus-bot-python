from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (13, 5),
        (15, 4),
        (15, 5),
        (16, 4),
        (16, 5),
        (16, 6),
        (16, 7),
        (17, 3),
        (17, 4),
        (17, 5),
        (17, 6),
        (18, 4),
        (18, 5),
        (18, 6),
        (19, 4),
        (19, 5),
        (20, 5),
        (26, 7)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (26, 9),
        (27, 8),
        (27, 9)
    ])

    return grid