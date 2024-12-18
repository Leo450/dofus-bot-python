class MapCell:
    enabled = True
    coords = (0, 0)
    screen_grid = None
    resources = []
    walkable = True

    def __init__(self, coords):
        self.coords = coords

    def set_screen_grid(self, screen_grid):
        self.screen_grid = screen_grid
        return self

    def set_resources(self, resources):
        self.resources = resources
        return self

    def set_walkable(self, walkable):
        self.walkable = walkable
        self.enabled = walkable
        return self