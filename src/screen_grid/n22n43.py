from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_WHEAT, (10, 13))

    return grid