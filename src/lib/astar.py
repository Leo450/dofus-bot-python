import numpy
from astar.search import AStar
from src.lib.struct import Vector


DEBUG_MAZE = False

PATH_LEFT = 'left'
PATH_RIGHT = 'right'
PATH_UP = 'up'
PATH_DOWN = 'down'

def astar(maze: list, start: Vector, end: Vector):
    if DEBUG_MAZE:
        print("Start: ", start)
        print("End: ", end)
        print(numpy.matrix(maze))

    return AStar(maze).search((start.y, start.x), (end.y, end.x))

def path_to_directions(path: list):
    directions = []
    for i in range(1, len(path)):
        prev_coords = (path[i-1][1], path[i-1][0])
        coords = (path[i][1], path[i][0])
        if coords[0] > prev_coords[0]:
            directions.append(PATH_RIGHT)
        elif coords[0] < prev_coords[0]:
            directions.append(PATH_LEFT)
        elif coords[1] > prev_coords[1]:
            directions.append(PATH_DOWN)
        elif coords[1] < prev_coords[1]:
            directions.append(PATH_UP)
    return directions