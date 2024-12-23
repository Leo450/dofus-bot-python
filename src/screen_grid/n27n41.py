from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_FLAX


def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (9, 10)).set_resource_mouse_offset(-grid.cell_size.x / 4, 0)

    grid.set_resource_nodes(RESOURCE_FLAX, [
        (21, 4),
        (22, 4),
        (23, 3),
        (23, 4),
        (24, 3),
        (24, 4),
        (24, 5),
        (24, 6),
        (25, 3),
        (25, 5),
        (25, 6),
        (26, 6),
        (27, 4),
        (27, 5),
        (28, 5)
    ])

    return grid