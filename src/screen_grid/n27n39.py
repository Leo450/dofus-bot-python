from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_FLAX

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (11, 7))

    grid.set_resource_nodes(RESOURCE_FLAX, [
        (11, 10),
        (12, 11),
        (12, 12),
        (13, 9),
        (13, 10),
        (13, 11),
        (13, 12),
        (14, 10),
        (14, 12),
        (15, 10),
        (15, 11),
        (16, 11),
        (22, 4),
        (22, 5),
        (23, 3),
        (23, 4),
        (23, 5),
        (24, 4),
        (24, 5)
    ])

    return grid