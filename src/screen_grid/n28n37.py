from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_OAT

def n28n37(window):
    grid = ScreenGrid(window)

    grid.get_cell(25, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 8).set_resource_node(RESOURCE_OAT)
    grid.get_cell(27, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(29, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(29, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(29, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(29, 8).set_resource_node(RESOURCE_OAT)
    grid.get_cell(31, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(31, 7).set_resource_node(RESOURCE_OAT)

    return grid