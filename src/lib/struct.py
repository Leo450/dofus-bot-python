class Vector:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def tuple(self) -> tuple:
        return (self.x, self.y)

    def int(self):
        return Vector(int(self.x), int(self.y))

    def flip(self):
        return Vector(self.y, self.x)

class Rect:
    min = Vector(0, 0)
    max = Vector(0, 0)

    def __init__(self, min_x, min_y, max_x, max_y):
        self.min = Vector(min_x, min_y)
        self.max = Vector(max_x, max_y)

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max

    def __add__(self, other):
        return Rect(
            self.min.x + other.min.x,
            self.min.y + other.min.y,
            self.max.x + other.max.x,
            self.max.y + other.max.y
        )

    def __sub__(self, other):
        return Rect(
            self.min.x - other.min.x,
            self.min.y - other.min.y,
            self.max.x - other.max.x,
            self.max.y - other.max.y
        )

    def __mul__(self, other):
        return Rect(
            self.min.x * other,
            self.min.y * other,
            self.max.x * other,
            self.max.y * other
        )

    def __truediv__(self, other):
        return Rect(
            self.min.x / other,
            self.min.y / other,
            self.max.x / other,
            self.max.y / other
        )

    def __str__(self):
        return f'({self.min}, {self.max})'

    def center(self):
        return Vector((self.min.x + self.max.x) / 2, (self.min.y + self.max.y) / 2)

    def top_left(self):
        return self.min

    def top_right(self):
        return Vector(self.max.x, self.min.y)

    def bottom_right(self):
        return self.max

    def bottom_left(self):
        return Vector(self.min.x, self.max.y)

    def size(self):
        return Vector(self.max.x - self.min.x + 1, self.max.y - self.min.y + 1)

    def contains(self, point):
        return self.min.x <= point.x <= self.max.x and self.min.y <= point.y <= self.max.y

    def intersects(self, other):
        return self.min.x <= other.max.x and self.max.x >= other.min.x and self.min.y <= other.max.y and self.max.y >= other.min.y

    def intersection(self, other):
        return Rect(
            max(self.min.x, other.min.x),
            max(self.min.y, other.min.y),
            min(self.max.x, other.max.x),
            min(self.max.y, other.max.y)
        )

    def union(self, other):
        return Rect(
            min(self.min.x, other.min.x),
            min(self.min.y, other.min.y),
            max(self.max.x, other.max.x),
            max(self.max.y, other.max.y)
        )

    def expand(self, amount):
        return Rect(
            self.min.x - amount,
            self.min.y - amount,
            self.max.x + amount,
            self.max.y + amount
        )