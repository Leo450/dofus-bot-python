from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_OAT, RESOURCE_MALT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (17, 9),
        (18, 9),
        (19, 9),
        (19, 10),
        (20, 9),
        (20, 10),
        (20, 11),
        (21, 10)
    ])

    grid.set_resource_nodes(RESOURCE_OAT, [
        (10, 4),
        (11, 4),
        (12, 4)
    ])

    grid.set_resource_nodes(RESOURCE_MALT, [
        (24, 7),
        (24, 8),
        (26, 8)
    ])

    return grid