from src.lib.struct import Vector


class MapCell:
    enabled = False
    coords = None
    screen_grid = None
    resources = []
    walkable = True

    def __init__(self, x, y):
        self.coords = Vector(x, y)

    def set_screen_grid(self, screen_grid):
        self.screen_grid = screen_grid
        self.enabled = True
        return self

    def set_resources(self, resources):
        self.resources = resources
        return self

    def set_walkable(self, walkable):
        self.walkable = walkable
        if walkable is False:
            self.enabled = False
        return self

    def apply_resource_filter(self, resource_filter=None):
        if self.screen_grid is None or resource_filter is None: return
        self.screen_grid.apply_resource_filter(resource_filter)
        if self.screen_grid.get_nb_enabled_cells() == 0:
            self.enabled = False