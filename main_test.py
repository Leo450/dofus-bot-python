import numpy

from src.lib.window import Window
from src.map_grid.plant_bonta import plant_bonta

if __name__ == '__main__':
    window = Window()
    grid = plant_bonta(window)

    print(numpy.matrix(grid.to_coord_matrix()))