from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT

def n26n39(window):
    grid = ScreenGrid(window)

    grid.get_cell(14, 6).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(15, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(16, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(16, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(16, 6).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(16, 7).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(17, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(17, 6).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(18, 6).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(18, 7).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(19, 5).set_resource_node(RESOURCE_WHEAT)

    return grid