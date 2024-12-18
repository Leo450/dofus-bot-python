from src.lib.map_grid import MapGrid
from src.lib.map_cell import MapCell
from src.screen_grid.n24n39 import n24n39
from src.screen_grid.n25n40 import n25n40
from src.screen_grid.n26n37 import n26n37
from src.screen_grid.n26n38 import n26n38
from src.screen_grid.n26n39 import n26n39
from src.screen_grid.n27n38 import n27n38
from src.screen_grid.n27n40 import n27n40
from src.screen_grid.n28n37 import n28n37
from src.screen_grid.n28n38 import n28n38
from src.screen_grid.n28n39 import n28n39
from src.screen_grid.n29n37 import n29n37
from src.screen_grid.n29n38 import n29n38
from src.screen_grid.n29n39 import n29n39

def crop_bonta(window, resource_filter):
    grid = MapGrid()

    grid.add_cell(MapCell((-24, -39)).set_screen_grid(n24n39(window)))

    grid.add_cell(MapCell((-25, -40)).set_screen_grid(n25n40(window)))

    grid.add_cell(MapCell((-26, -37)).set_screen_grid(n26n37(window)))
    grid.add_cell(MapCell((-26, -38)).set_screen_grid(n26n38(window)))
    grid.add_cell(MapCell((-26, -39)).set_screen_grid(n26n39(window)))

    grid.add_cell(MapCell((-27, -38)).set_screen_grid(n27n38(window)))
    grid.add_cell(MapCell((-27, -40)).set_screen_grid(n27n40(window)))

    grid.add_cell(MapCell((-28, -37)).set_screen_grid(n28n37(window)))
    grid.add_cell(MapCell((-28, -38)).set_screen_grid(n28n38(window)))
    grid.add_cell(MapCell((-28, -39)).set_screen_grid(n28n39(window)))

    grid.add_cell(MapCell((-29, -37)).set_screen_grid(n29n37(window)))
    grid.add_cell(MapCell((-29, -38)).set_screen_grid(n29n38(window)))
    grid.add_cell(MapCell((-29, -39)).set_screen_grid(n29n39(window)))

    grid.apply_resource_filter(resource_filter)

    return grid