from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_HEMP

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WHEAT, (30, 10))

    grid.set_resource_nodes(RESOURCE_HEMP, [
        (13, 2),
        (13, 3),
        (14, 3),
        (15, 1),
        (16, 2),
        (16, 3),
        (17, 3)
    ])

    return grid