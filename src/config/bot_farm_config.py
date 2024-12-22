from src.lib.resource import RESOURCE_WATER, RESOURCE_ORCHID
from src.lib.struct import Vector
from src.map_grid.crop_bonta import crop_bonta
from src.map_grid.plant_bonta import plant_bonta
from src.map_grid.clover_astrub import clover_astrub
from src.map_grid.orchid import orchid

config = {
    'start_coords': Vector(-30, -62),
    'map_grid': orchid,
    'resource_filter': [RESOURCE_WATER, RESOURCE_ORCHID]
}