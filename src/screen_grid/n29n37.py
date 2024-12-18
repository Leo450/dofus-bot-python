from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def n29n37(window):
    grid = ScreenGrid(window)

    grid.get_cell(15, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(17, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(17, 8).set_resource_node(RESOURCE_OAT)
    grid.get_cell(18, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(19, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(19, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(19, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(20, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(20, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(21, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(21, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 8).set_resource_node(RESOURCE_OAT)

    grid.get_cell(31, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(32, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(32, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(33, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(33, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(33, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(34, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(34, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(35, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(35, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(35, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(36, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(37, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(37, 9).set_resource_node(RESOURCE_BARLEY)

    return grid