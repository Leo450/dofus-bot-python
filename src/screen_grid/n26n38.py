from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_RYE

def n26n38(window):
    grid = ScreenGrid(window)

    grid.get_cell(6, 2).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(6, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(7, 2).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(8, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(8, 7).set_resource_node(RESOURCE_WHEAT)

    grid.get_cell(8, 9).set_resource_node(RESOURCE_RYE)
    grid.get_cell(9, 8).set_resource_node(RESOURCE_RYE)
    grid.get_cell(10, 9).set_resource_node(RESOURCE_RYE)

    return grid