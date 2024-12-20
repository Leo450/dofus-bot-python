from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WATER, RESOURCE_WHEAT, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WATER, (33, 9))

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (6, 2),
        (6, 3),
        (7, 2),
        (8, 3),
        (8, 7)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (8, 9),
        (9, 8),
        (10, 9)
    ])

    return grid