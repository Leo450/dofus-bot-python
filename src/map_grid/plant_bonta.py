from src.lib.map_grid import MapGrid
from src.lib.map_cell import MapCell
from src.screen_grid.n22n63 import n22n63
from src.screen_grid.n23n63 import n23n63
from src.screen_grid.n24n62 import n24n62
from src.screen_grid.n24n63 import n24n63
from src.screen_grid.n24n64 import n24n64
from src.screen_grid.n25n61 import n25n61
from src.screen_grid.n25n62 import n25n62
from src.screen_grid.n26n63 import n26n63
from src.screen_grid.n26n64 import n26n64
from src.screen_grid.n27n62 import n27n62
from src.screen_grid.n27n63 import n27n63
from src.screen_grid.n27n65 import n27n65
from src.screen_grid.n28n62 import n28n62
from src.screen_grid.n28n63 import n28n63
from src.screen_grid.n28n64 import n28n64
from src.screen_grid.n28n65 import n28n65
from src.screen_grid.n29n63 import n29n63
from src.screen_grid.n29n64 import n29n64
from src.screen_grid.n29n65 import n29n65
from src.screen_grid.n30n62 import n30n62
from src.screen_grid.n30n63 import n30n63
from src.screen_grid.n31n62 import n31n62
from src.screen_grid.n31n64 import n31n64
from src.screen_grid.n31n65 import n31n65
from src.screen_grid.n32n62 import n32n62
from src.screen_grid.n32n64 import n32n64
from src.screen_grid.n32n65 import n32n65
from src.screen_grid.n33n61 import n33n61
from src.screen_grid.n33n63 import n33n63
from src.screen_grid.n33n64 import n33n64
from src.screen_grid.n33n65 import n33n65

def plant_bonta(window, resource_filter):
    grid = MapGrid()

    grid.add_cell(MapCell((-22, -63)).set_screen_grid(n22n63(window)))
    grid.add_cell(MapCell((-22, -65)).set_walkable(False))

    grid.add_cell(MapCell((-23, -63)).set_screen_grid(n23n63(window)))
    grid.add_cell(MapCell((-23, -65)).set_walkable(False))

    grid.add_cell(MapCell((-24, -62)).set_screen_grid(n24n62(window)))
    grid.add_cell(MapCell((-24, -63)).set_screen_grid(n24n63(window)))
    grid.add_cell(MapCell((-24, -64)).set_screen_grid(n24n64(window)))

    grid.add_cell(MapCell((-25, -61)).set_screen_grid(n25n61(window)))
    grid.add_cell(MapCell((-25, -62)).set_screen_grid(n25n62(window)))

    grid.add_cell(MapCell((-26, -61)).set_walkable(False))
    grid.add_cell(MapCell((-26, -63)).set_screen_grid(n26n63(window)))
    grid.add_cell(MapCell((-26, -64)).set_screen_grid(n26n64(window)))

    grid.add_cell(MapCell((-27, -61)).set_walkable(False))
    grid.add_cell(MapCell((-27, -62)).set_screen_grid(n27n62(window)))
    grid.add_cell(MapCell((-27, -63)).set_screen_grid(n27n63(window)))
    grid.add_cell(MapCell((-27, -65)).set_screen_grid(n27n65(window)))

    grid.add_cell(MapCell((-28, -61)).set_walkable(False))
    grid.add_cell(MapCell((-28, -62)).set_screen_grid(n28n62(window)))
    grid.add_cell(MapCell((-28, -63)).set_screen_grid(n28n63(window)))
    grid.add_cell(MapCell((-28, -64)).set_screen_grid(n28n64(window)))
    grid.add_cell(MapCell((-28, -65)).set_screen_grid(n28n65(window)))

    grid.add_cell(MapCell((-29, -61)).set_walkable(False))
    grid.add_cell(MapCell((-29, -62)).set_walkable(False))
    grid.add_cell(MapCell((-29, -63)).set_screen_grid(n29n63(window)))
    grid.add_cell(MapCell((-29, -64)).set_screen_grid(n29n64(window)))
    grid.add_cell(MapCell((-29, -65)).set_screen_grid(n29n65(window)))

    grid.add_cell(MapCell((-30, -61)).set_walkable(False))
    grid.add_cell(MapCell((-30, -62)).set_screen_grid(n30n62(window)))
    grid.add_cell(MapCell((-30, -63)).set_screen_grid(n30n63(window)))

    grid.add_cell(MapCell((-31, -61)).set_walkable(False))
    grid.add_cell(MapCell((-31, -62)).set_screen_grid(n31n62(window)))
    grid.add_cell(MapCell((-31, -64)).set_screen_grid(n31n64(window)))
    grid.add_cell(MapCell((-31, -65)).set_screen_grid(n31n65(window)))

    grid.add_cell(MapCell((-32, -62)).set_screen_grid(n32n62(window)))
    grid.add_cell(MapCell((-32, -64)).set_screen_grid(n32n64(window)))
    grid.add_cell(MapCell((-32, -65)).set_screen_grid(n32n65(window)))

    grid.add_cell(MapCell((-33, -61)).set_screen_grid(n33n61(window)))
    grid.add_cell(MapCell((-33, -63)).set_screen_grid(n33n63(window)))
    grid.add_cell(MapCell((-33, -64)).set_screen_grid(n33n64(window)))
    grid.add_cell(MapCell((-33, -65)).set_screen_grid(n33n65(window)))

    grid.apply_resource_filter(resource_filter)

    return grid