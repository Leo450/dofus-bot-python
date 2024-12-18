from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY, RESOURCE_RYE

def n25n40(window):
    grid = ScreenGrid(window)

    grid.get_cell(7, 5).set_resource_node(RESOURCE_RYE)
    grid.get_cell(7, 6).set_resource_node(RESOURCE_RYE)

    grid.get_cell(20, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(22, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(23, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(25, 2).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(25, 3).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(25, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(26, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(27, 3).set_resource_node(RESOURCE_WHEAT)

    return grid