from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (14, 6),
        (15, 5),
        (16, 4),
        (16, 5),
        (16, 6),
        (16, 7),
        (17, 5),
        (17, 6),
        (18, 6),
        (18, 7),
        (19, 5)
    ])

    return grid