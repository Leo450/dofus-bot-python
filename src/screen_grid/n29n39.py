from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_BARLEY, RESOURCE_OAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (13, 1))

    grid.set_resource_nodes(RESOURCE_OAT, [
        (17, 5),
        (18, 5),
        (18, 6),
        (19, 6),
        (20, 7),
        (21, 7),
        (22, 7)
    ])

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (19, 10),
        (20, 10),
        (20, 11),
        (21, 9),
        (21, 10),
        (21, 11),
        (22, 9),
        (22, 10),
        (23, 9),
        (23, 10),
        (24, 10)
    ])

    return grid