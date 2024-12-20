from src.lib.map_grid import MapGrid
from src.lib.struct import Vector


def clover_astrub(window, resource_filter=None):
    grid = MapGrid.build_from_maze(
        Vector(-3, -24),
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ],
        window
    )
    grid.apply_resource_filter(resource_filter)

    grid.debug_screen_grid()

    return grid