from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_MALT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_MALT, [
        (9, 9),
        (10, 9),
        (10, 10),
        (12, 10)
    ])

    return grid