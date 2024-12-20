from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WHEAT, (12, 3))

    grid.set_resource_nodes(RESOURCE_OAT, [
        (26, 3),
        (27, 1),
        (28, 2),
        (28, 3),
        (28, 4),
        (30, 4)
    ])

    return grid