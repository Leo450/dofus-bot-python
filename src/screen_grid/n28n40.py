from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (36, 5))

    grid.set_resource_nodes(RESOURCE_RYE, [
        (13, 1),
        (14, 1),
        (14, 2),
        (30, 5),
        (31, 5),
        (32, 6),
        (33, 6),
        (34, 7)
    ])

    return grid