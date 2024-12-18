import numpy
from astar.search import AStar

DEBUG_MAZE = False

PATH_LEFT = 'left'
PATH_RIGHT = 'right'
PATH_UP = 'up'
PATH_DOWN = 'down'

def astar(maze, start, end):
    if DEBUG_MAZE:
        print("Start: ", start)
        print("End: ", end)
        print(numpy.matrix(maze))

    return AStar(maze).search((start[1], start[0]), (end[1], end[0]))

def path_to_directions(path):
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