from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def n28n38(window):
    grid = ScreenGrid(window)

    grid.get_cell(7, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(7, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(8, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(8, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(8, 8).set_resource_node(RESOURCE_OAT)
    grid.get_cell(9, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(10, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(11, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(12, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(13, 8).set_resource_node(RESOURCE_OAT)
    grid.get_cell(13, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(14, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(15, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(16, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(17, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(17, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(18, 9).set_resource_node(RESOURCE_OAT)

    return grid