from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_ORCHID


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_nodes(RESOURCE_ORCHID, [
        (10, 6),
        (29, 10),
        (37, 1)
    ])
    grid.get_cell(29, 10).set_resource_mouse_offset(0, -grid.cell_size.y / 4)

    return grid