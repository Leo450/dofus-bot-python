from src.lib.astar import astar, path_to_directions

class MapGrid:
    cells = []
    maze = None

    def get_cell(self, x, y):
        for cell in self.cells:
            if cell.coords[0] == x and cell.coords[1] == y:
                return cell
        return None

    def add_cell(self, cell):
        self.cells.append(cell)

    def cell_exists(self, x, y):
        return self.get_cell(x, y) is not None

    def get_nb_enabled_cells(self):
        nb_cells = 0
        for cell in self.cells:
            if cell.enabled:
                nb_cells += 1
        return nb_cells

    def get_closest_cell(self, x, y, excludes=None):
        closest_cell = None
        min_distance = float('inf')

        for cell in self.cells:
            if (excludes is not None and cell in excludes) or cell.enabled == False: continue

            # Manhattan distance
            distance = abs(cell.coords[0] - x) + abs(cell.coords[1] - y)
            # Euclidean distance
            # distance = (cell.coords[0] - x) ** 2 + (cell.coords[1] - y) ** 2
            if distance < min_distance:
                min_distance = distance
                closest_cell = cell

        return closest_cell

    def get_rect(self):
        min_x = int(999)
        max_x = int(-999)
        min_y = int(999)
        max_y = int(-999)

        for cell in self.cells:
            if cell.coords[0] < min_x:
                min_x = cell.coords[0]
            if cell.coords[0] > max_x:
                max_x = cell.coords[0]
            if cell.coords[1] < min_y:
                min_y = cell.coords[1]
            if cell.coords[1] > max_y:
                max_y = cell.coords[1]

        return (min_x, min_y, max_x, max_y)

    def get_path(self, start_coords, end_coords):
        rect = self.get_rect()

        if start_coords[0] < rect[0]:
            rect = (start_coords[0], rect[1], rect[2], rect[3])
        elif start_coords[0] > rect[2]:
            rect = (rect[0], rect[1], start_coords[0], rect[3])
        if start_coords[1] < rect[1]:
            rect = (rect[0], start_coords[1], rect[2], rect[3])
        elif start_coords[1] > rect[3]:
            rect = (rect[0], rect[1], rect[2], start_coords[1])

        if self.maze is None:
            size = (rect[2] - rect[0] + 1, rect[3] - rect[1] + 1)
            self.maze = [[0 for x in range(size[0])] for y in range(size[1])]
            for cell in self.cells:
                if not cell.walkable:
                    cell_x = cell.coords[0] - rect[0]
                    cell_y = cell.coords[1] - rect[1]
                    self.maze[cell_y][cell_x] = 1

        start = (start_coords[0] - rect[0], start_coords[1] - rect[1])
        end = (end_coords[0] - rect[0], end_coords[1] - rect[1])

        path = astar(self.maze, start, end)
        if path is None:
            raise Exception('No path found')

        return path_to_directions(path)

    def apply_resource_filter(self, resource_filter):
        for cell in self.cells:
            if not cell.enabled: continue
            cell.screen_grid.apply_resource_filter(resource_filter)
            if cell.screen_grid.get_nb_enabled_cells() == 0:
                cell.enabled = False