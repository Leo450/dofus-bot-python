from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WATER, RESOURCE_WHEAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WATER, (32, 4))

    grid.set_resource_nodes(RESOURCE_WHEAT, [
        (7, 0),
        (9, 0),
        (10, 1),
        (14, 12)
    ])

    return grid