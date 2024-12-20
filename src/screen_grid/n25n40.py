from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (20, 4),
        (22, 3),
        (23, 3),
        (25, 2),
        (25, 3),
        (25, 4),
        (26, 5),
        (27, 3)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (7, 5),
        (7, 6),
        (9, 6)
    ])

    return grid