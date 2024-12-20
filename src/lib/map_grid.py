import importlib

import numpy

from src.lib.astar import astar, path_to_directions
from src.lib.map_cell import MapCell
from src.lib.struct import Vector, Rect


class MapGrid:
    top_left = None
    size = None
    cells = []
    maze = None

    def __init__(self, top_left: Vector, size: Vector):
        self.top_left = top_left
        self.size = size
        self.cells = [[None for x in range(size.x)] for y in range(size.y)]

    def to_absolute_coords(self, x, y):
        return Vector(self.top_left.x + x, self.top_left.y + y)

    def to_relative_coords(self, x, y):
        return Vector(x - self.top_left.x, y - self.top_left.y)

    def get_cell_relative(self, x, y):
        return self.cells[y][x]

    def get_cell_absolute(self, x, y):
        relative_coords = self.to_relative_coords(x, y)
        return self.cells[relative_coords.y][relative_coords.x]

    def get_cell(self, x, y):
        return self.get_cell_absolute(x, y)

    def set_cell(self, cell):
        relative_coords = self.to_relative_coords(*cell.coords.tuple())
        self.cells[relative_coords.y][relative_coords.x] = cell

    def get_nb_enabled_cells(self):
        count = 0
        for row in self.cells:
            for cell in row:
                if cell.enabled:
                    count += 1
        return count

    def get_closest_cell(self, x, y, excludes=None):
        closest_cell = None
        min_distance = float('inf')

        for row in self.cells:
            for cell in row:
                if (excludes is not None and cell in excludes) or cell.enabled == False: continue

                # Manhattan distance
                distance = abs(cell.coords.x - x) + abs(cell.coords.y - y)
                # Euclidean distance
                # distance = (cell.coords.x - x) ** 2 + (cell.coords.y - y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_cell = cell

        return closest_cell

    def get_absolute_rect(self):
        min_x = self.cells[0][0].coords.x
        min_y = self.cells[0][0].coords.y
        max_x = self.cells[0][self.size.x - 1].coords.x
        max_y = self.cells[self.size.y - 1][0].coords.y

        return Rect(min_x, min_y, max_x, max_y)

    def get_path(self, start: Vector, end: Vector):
        absolute_rect = self.get_absolute_rect()

        if start.x < absolute_rect.min.x:
            absolute_rect.min.x = start.x
        elif start.x > absolute_rect.max.x:
            absolute_rect.max.x = start.x
        if start.y < absolute_rect.min.y:
            absolute_rect.min.y = start.y
        elif start.y > absolute_rect.max.y:
            absolute_rect.max.y = start.y

        size = absolute_rect.size()

        if self.maze is None:
            self.maze = [[0 for x in range(size.x)] for y in range(size.y)]
            for row in self.cells:
                for cell in row:
                    if not cell.walkable:
                        relative_coords = Vector(
                            cell.coords.x - absolute_rect.min.x,
                            cell.coords.y - absolute_rect.min.y
                        )
                        self.maze[relative_coords.y][relative_coords.x] = 1

        maze_start = Vector(
            start.x - absolute_rect.min.x,
            start.y - absolute_rect.min.y
        )
        maze_end = Vector(
            end.x - absolute_rect.min.x,
            end.y - absolute_rect.min.y
        )

        path = astar(self.maze, maze_start, maze_end)
        if path is None:
            raise Exception('No path found')

        return path_to_directions(path)

    def apply_resource_filter(self, resource_filter=None):
        if resource_filter is None: return
        for row in self.cells:
            for cell in row:
                if not cell.enabled: continue
                cell.apply_resource_filter(resource_filter)

    def debug_coords(self):
        matrix = [[(0, 0) for x in range(self.size.x)] for y in range(self.size.y)]
        for row in range(self.size.y):
            for col in range(self.size.x):
                matrix[row][col] = f'{self.cells[row][col].coords.x},{self.cells[row][col].coords.y}'

        print(numpy.matrix(matrix))

    def debug_screen_grid(self):
        matrix = [[0 for x in range(self.size.x)] for y in range(self.size.y)]
        for row in range(self.size.y):
            for col in range(self.size.x):
                matrix[row][col] = 1 if self.cells[row][col].screen_grid is not None and self.cells[row][col].screen_grid.get_nb_enabled_cells() > 0 else 0

        print(numpy.matrix(matrix))

    @staticmethod
    def build_from_maze(top_left: Vector, maze: list, window):
        grid = MapGrid(top_left, Vector(len(maze[0]), len(maze)))

        for row in range(len(maze)):
            for col in range(len(maze[row])):
                coords = Vector(top_left.x + col, top_left.y + row)
                cell = MapCell(coords.x, coords.y)

                if maze[row][col] == 0:
                    cell.set_walkable(False)
                    grid.set_cell(cell)
                    continue

                x_prefix = 'n' if coords.x < 0 else 'p'
                y_prefix = 'n' if coords.y < 0 else 'p'
                name = f'{x_prefix}{abs(coords.x)}{y_prefix}{abs(coords.y)}'
                exists = importlib.util.find_spec(f'src.screen_grid.{name}')
                if exists is not None:
                    screen_grid_module = importlib.import_module(f'src.screen_grid.{name}')
                    cell.set_screen_grid(screen_grid_module.screen_grid(window))

                grid.set_cell(cell)

        return grid