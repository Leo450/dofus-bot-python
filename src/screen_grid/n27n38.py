from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def n27n38(window):
    grid = ScreenGrid(window)

    grid.get_cell(9, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(10, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(12, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(12, 12).set_resource_node(RESOURCE_OAT)
    grid.get_cell(14, 12).set_resource_node(RESOURCE_OAT)
    grid.get_cell(21, 2).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 3).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 1).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 2).set_resource_node(RESOURCE_OAT)
    grid.get_cell(24, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 1).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 2).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 2).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 3).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 4).set_resource_node(RESOURCE_OAT)

    return grid