from src.lib.map_grid import MapGrid
from src.lib.struct import Vector


def plant_bonta(window, resource_filter=None):
    grid = MapGrid.build_from_maze(
        Vector(-33, -65),
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        ],
        window
    )
    grid.apply_resource_filter(resource_filter)

    return grid