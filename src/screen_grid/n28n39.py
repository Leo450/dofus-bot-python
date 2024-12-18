from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_BARLEY, RESOURCE_RYE

def n28n39(window):
    grid = ScreenGrid(window)

    grid.get_cell(12, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(13, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(14, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(15, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(16, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(17, 5).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(17, 6).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(18, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(19, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(19, 8).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(19, 9).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(20, 7).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(20, 9).set_resource_node(RESOURCE_BARLEY)

    grid.get_cell(30, 5).set_resource_node(RESOURCE_RYE)
    grid.get_cell(31, 4).set_resource_node(RESOURCE_RYE)
    grid.get_cell(31, 5).set_resource_node(RESOURCE_RYE)
    grid.get_cell(32, 5).set_resource_node(RESOURCE_RYE)

    return grid