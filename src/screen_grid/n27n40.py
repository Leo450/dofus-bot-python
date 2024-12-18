from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_OAT

def n27n40(window):
    grid = ScreenGrid(window)

    grid.get_cell(8, 9).set_resource_node(RESOURCE_OAT)
    grid.get_cell(9, 9).set_resource_node(RESOURCE_OAT)

    grid.get_cell(9, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(10, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(10, 12).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(11, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(11, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(11, 12).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(12, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(12, 12).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 10).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 11).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(14, 11).set_resource_node(RESOURCE_BARLEY)

    return grid