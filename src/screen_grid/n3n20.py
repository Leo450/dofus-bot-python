from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_CLOVER

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_SAGE, [
        (8, 10),
        (16, 6)
    ])

    grid.set_resource_node(RESOURCE_CLOVER, (5, 9))

    return grid