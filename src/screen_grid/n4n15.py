from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_MINT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_MINT, (18, 12))

    return grid