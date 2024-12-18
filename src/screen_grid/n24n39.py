from src.lib.screen_grid import ScreenGrid
from src.lib.resource import RESOURCE_WHEAT, RESOURCE_BARLEY, RESOURCE_HOPS

def n24n39(window):
    grid = ScreenGrid(window)

    grid.get_cell(2, 2).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(3, 1).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(4, 2).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(4, 3).set_resource_node(RESOURCE_BARLEY)
    grid.get_cell(5, 1).set_resource_node(RESOURCE_BARLEY)

    grid.get_cell(9, 10).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(9, 11).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(10, 12).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(11, 10).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(11, 12).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(12, 10).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(12, 11).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(12, 12).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(12, 13).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(13, 12).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(14, 11).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(15, 11).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(15, 12).set_resource_node(RESOURCE_HOPS)
    grid.get_cell(17, 11).set_resource_node(RESOURCE_HOPS)

    grid.get_cell(26, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(27, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(27, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(28, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(28, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(28, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(29, 2).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(29, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(29, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(30, 2).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(30, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(30, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(30, 5).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(31, 4).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(32, 3).set_resource_node(RESOURCE_WHEAT)
    grid.get_cell(32, 4).set_resource_node(RESOURCE_WHEAT)

    return grid