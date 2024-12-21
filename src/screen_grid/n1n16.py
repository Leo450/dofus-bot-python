from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_CLOVER, RESOURCE_MINT


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_CLOVER, (31, 12))

    grid.set_resource_nodes(RESOURCE_MINT, [
        (6, 6),
        (20, 11)
    ])

    return grid