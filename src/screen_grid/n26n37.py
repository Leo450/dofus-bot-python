from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def n26n37(window):
    grid = ScreenGrid(window)

    grid.get_cell(6, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(7, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(8, 4).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(8, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(8, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(9, 4).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(9, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(9, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(10, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(10, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(10, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(11, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(12, 6).set_resource_node(RESOURCE_BARLEY)

    grid.get_cell(20, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(21, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(24, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 5).set_resource_node(RESOURCE_OAT)

    return grid