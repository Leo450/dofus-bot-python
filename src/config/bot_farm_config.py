from src.lib.resource import RESOURCE_PLANT
from src.lib.struct import Vector
from src.map_grid.crop_bonta import crop_bonta
from src.map_grid.plant_bonta import plant_bonta

config = {
    'start_coords': Vector(-30, -62),
    'map_grid': plant_bonta,
    'resource_filter': RESOURCE_PLANT
}