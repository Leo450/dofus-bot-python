from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_SAGE, RESOURCE_BARLEY, RESOURCE_RYE

def screen_grid(window):
    grid = ScreenGrid(window)

    grid.set_resource_node(RESOURCE_SAGE, (36, 10)).set_resource_mouse_offset(-grid.cell_size.x / 4, -grid.cell_size.y / 4)

    grid.set_resource_nodes(RESOURCE_BARLEY, [
        (12, 7),
        (13, 6),
        (13, 7),
        (14, 7),
        (15, 7),
        (16, 6),
        (16, 7),
        (16, 8),
        (16, 9),
        (17, 5),
        (17, 6),
        (18, 8),
        (19, 7),
        (19, 8),
        (19, 9),
        (20, 7),
        (20, 9)
    ])

    grid.set_resource_nodes(RESOURCE_RYE, [
        (30, 5),
        (31, 4),
        (31, 5),
        (32, 5)
    ])

    return grid