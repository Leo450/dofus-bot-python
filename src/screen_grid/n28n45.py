from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WHEAT, (25, 4))

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (25, 7),
        (26, 7),
        (27, 6),
        (27, 7),
        (27, 8),
        (28, 7),
        (28, 8),
        (29, 6),
        (29, 7),
        (30, 7),
    ])

    return grid