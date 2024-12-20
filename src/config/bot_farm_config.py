from src.lib.resource import RESOURCE_PLANT, RESOURCE_CROP_60, RESOURCE_WATER, RESOURCE_BARLEY, RESOURCE_SAGE, RESOURCE_CLOVER
from src.lib.struct import Vector
from src.map_grid.crop_bonta import crop_bonta
from src.map_grid.plant_bonta import plant_bonta
from src.map_grid.clover_astrub import clover_astrub

config = {
    'start_coords': Vector(-30, -62),
    'map_grid': clover_astrub,
    'resource_filter': [RESOURCE_WATER, RESOURCE_SAGE, RESOURCE_CLOVER]
}