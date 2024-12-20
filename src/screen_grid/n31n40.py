from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (35, 8)).set_resource_mouse_offset(0, -grid.cell_size.y / 4)

    return grid