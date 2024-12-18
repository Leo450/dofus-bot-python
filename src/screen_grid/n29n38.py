from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def n29n38(window):
    grid = ScreenGrid(window)

    grid.get_cell(12, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(14, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(14, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(14, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(15, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(15, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(15, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(15, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(17, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(17, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(18, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(18, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(19, 7).set_resource_node(RESOURCE_BARLEY)

    grid.get_cell(21, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(22, 5).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 3).set_resource_node(RESOURCE_OAT)
    grid.get_cell(23, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(24, 4).set_resource_node(RESOURCE_OAT)
    grid.get_cell(24, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(25, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(26, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(27, 10).set_resource_node(RESOURCE_OAT)
    grid.get_cell(27, 11).set_resource_node(RESOURCE_OAT)
    grid.get_cell(28, 11).set_resource_node(RESOURCE_OAT)

    return grid