from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def n29n39(window):
    grid = ScreenGrid(window)

    grid.get_cell(17, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(18, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(18, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(19, 6).set_resource_node(RESOURCE_OAT)
    grid.get_cell(20, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(21, 7).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 7).set_resource_node(RESOURCE_OAT)

    grid.get_cell(19, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(20, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(20, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(21, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(21, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(21, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(22, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(22, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(23, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(23, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(24, 10).set_resource_node(RESOURCE_BARLEY)

    return grid