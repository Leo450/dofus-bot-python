from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_WHEAT, RESOURCE_OAT, RESOURCE_HOPS, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (24, 12))

    grid.set_resource_node(RESOURCE_WHEAT, (13, 4))

    grid.set_resource_nodes(RESOURCE_OAT, [
        (33, 5),
        (34, 5),
        (34, 6),
        (35, 4),
        (35, 5),
        (35, 6),
        (36, 5),
        (36, 6),
        (36, 7),
        (37, 5),
        (37, 6),
        (38, 6)
    ])

    grid.set_resource_nodes(RESOURCE_HOPS, [
        (21, 4),
        (22, 4),
        (23, 3),
        (24, 3),
        (25, 1),
        (26, 1),
        (26, 2),
        (26, 3),
        (27, 1),
        (27, 2),
        (28, 2)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (22, 9),
        (24, 8),
        (25, 9),
        (25, 10)
    ])

    return grid