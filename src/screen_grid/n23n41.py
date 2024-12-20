from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_HOPS

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (30, 10))

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (21, 7),
        (22, 7),
        (22, 8),
        (23, 6),
        (23, 7),
        (23, 8),
        (24, 7),
        (24, 8),
        (25, 7),
        (25, 8),
        (26, 8),
        (26, 9),
        (27, 7)
    ])

    return grid