import asyncio
import src.lib.mouse as mouse
from src.lib.console import BCOLORS
from src.lib.inventory import Inventory
from src.lib.map_grid_coords import MapGridCoords
from src.lib.mover import Mover
from src.lib.resource import RESOURCE_CROP, RESOURCE_PLANT
from src.config.bot_farm_config import config

class BotFarm:
    map_grid = None
    inventory = None
    map_grid_coords = None
    mover = None

    player_map_coords = None
    farm_speed = 0.1
    nb_loop = 0

    # Map
    visited_map_cells = []
    nb_direction_failed = 0

    # Screen
    current_map_cell = None
    current_screen_cell = None
    nb_screen_cell = 0
    nb_empty_cell = 0
    failed_screen_cells = []

    def __init__(self, window, overlay):
        self.window = window
        self.overlay = overlay

    async def start(self):
        self.map_grid = config['map_grid'](self.window, config['resource_filter'])
        self.map_grid_coords = MapGridCoords(self.window)
        self.inventory = Inventory(self.window)
        self.mover = Mover(self.window, self.overlay, self.map_grid)

        self.window.focus()
        await asyncio.sleep(1)

        self.map_grid_coords.init()
        self.inventory.init()
        self.mover.init()

        if self.map_grid_coords.start_coords is not None:
            self.player_map_coords = self.map_grid_coords.start_coords
            print(BCOLORS.colorize(' >>>> START at: {} (OCR) <<<< '.format(self.player_map_coords), BCOLORS.BG_WHITE + BCOLORS.BLACK + BCOLORS.BOLD))
        else:
            self.player_map_coords = config['start_coords']
            print(BCOLORS.colorize(' >>>> START at: {} (config) <<<< '.format(self.player_map_coords), BCOLORS.BG_WHITE + BCOLORS.BLACK + BCOLORS.BOLD))

        self.overlay.set_drawable('inventory', self.inventory)
        self.overlay.set_drawable('map_grid_coords', self.map_grid_coords)

        while True:
            print(BCOLORS.colorize(' -- NEW LOOP -- ', BCOLORS.BG_LIGHT_YELLOW + BCOLORS.BLACK))

            if self.nb_loop == 0:
                await asyncio.sleep(1)
                mouse.move(self.window.screen_size[0] / 2, self.window.screen_size[1] / 2)
                await asyncio.sleep(1)

            await self.farm_next_map_cell()
            self.nb_loop += 1

    async def farm_next_map_cell(self):
        if len(self.visited_map_cells) == self.map_grid.get_nb_enabled_cells():
            print(BCOLORS.yellow('> All map cells visited'))
            current_map_cell = self.current_map_cell
            self.reset_map()
            self.visited_map_cells.append(current_map_cell)
            return

        if self.map_grid.get_nb_enabled_cells() == 0:
            raise Exception('No enabled map cell')

        #print(BCOLORS.grey('Player is at: {}'.format(self.player_map_coords)))
        closest_cell = self.map_grid.get_closest_cell(*self.player_map_coords, self.visited_map_cells)
        #print(BCOLORS.grey('Closest cell: {}'.format(closest_cell.coords)))

        if closest_cell.coords != self.player_map_coords:
            print(BCOLORS.red('> Player is not on closest map cell'))
            await self.mover.go_to_map_cell(self.player_map_coords, closest_cell.coords)
            self.player_map_coords = closest_cell.coords
        else:
            print(BCOLORS.green('> Player is on closest map cell'))

        await self.farm_current_map_cell()
        await self.farm_next_map_cell()

    async def farm_current_map_cell(self):
        self.load_screen_grid(self.player_map_coords)
        await self.farm_next_screen_cell()
        self.reset_screen()

    def load_screen_grid(self, coords):
        print(BCOLORS.colorize(' >> Farming at: {} '.format(coords), BCOLORS.BG_LIGHT_PURPLE + BCOLORS.BLACK + BCOLORS.BOLD))

        self.current_map_cell = self.map_grid.get_cell(*coords)
        self.nb_screen_cell = self.current_map_cell.screen_grid.get_nb_enabled_cells()
        self.visited_map_cells.append(self.current_map_cell)
        #print(BCOLORS.grey('Number of screen cells: {}'.format(self.nb_screen_cell)))

        self.overlay.set_drawable('screen_grid', self.current_map_cell.screen_grid)

    async def farm_next_screen_cell(self):
        # Find current screen cell
        if self.current_screen_cell is None:
            self.current_screen_cell = self.current_map_cell.screen_grid.get_last_enabled_cell()
        else:
            self.current_screen_cell = self.current_map_cell.screen_grid.get_prev_cell(*self.current_screen_cell.coords)
            if self.current_screen_cell is None:
                self.current_screen_cell = self.current_map_cell.screen_grid.get_last_enabled_cell()

        #print(BCOLORS.grey('Farming next screen cell: {}'.format(self.current_screen_cell.coords)))

        if self.current_screen_cell in self.failed_screen_cells:
            if len(self.failed_screen_cells) >= self.nb_screen_cell:
                return
            await self.farm_next_screen_cell()
            return

        self.current_screen_cell.highlighted = True

        if await self.cursor_check():
            print(BCOLORS.cyan('> Gathering at: {}'.format(self.current_screen_cell.coords)))

            # Click on crop
            await mouse.click()
            self.nb_empty_cell = 0

            # Wait for inventory update
            print(BCOLORS.grey('Waiting for inventory update...'))
            success = await self.inventory.wait_update()
            if not success:
                print(BCOLORS.red('> Gathering failed at: {}'.format(self.current_screen_cell.coords)))
                self.failed_screen_cells.append(self.current_screen_cell)

            await asyncio.sleep(self.farm_speed)
            self.current_screen_cell.highlighted = False
            self.overlay.update()

            if self.nb_screen_cell == 1:
                print(BCOLORS.yellow('> No more crops on screen'))
                return

            await self.farm_next_screen_cell()
        else:
            self.nb_empty_cell += 1

            await asyncio.sleep(self.farm_speed)
            self.current_screen_cell.highlighted = False
            self.overlay.update()

            if self.nb_empty_cell >= self.nb_screen_cell:
                print(BCOLORS.yellow('> No more crops on screen'))
                return

            await self.farm_next_screen_cell()

    async def cursor_check(self):
        cell = self.current_screen_cell

        if cell.resource_node in RESOURCE_CROP:
            # Move mouse to top of cell
            mouse.move(
                *self.window.to_screen(
                    cell.vertices['top'][0] + cell.resource_mouse_offset[0],
                    cell.vertices['top'][1] - self.current_map_cell.screen_grid.cell_size[1] / 2 + cell.resource_mouse_offset[1]
                )
            )
            await asyncio.sleep(0.05)
            return mouse.cursor_is_gather_crop()

        if cell.resource_node in RESOURCE_PLANT:
            # Move mouse to cell center
            mouse.move(
                *self.window.to_screen(
                    cell.vertices['center'][0] + cell.resource_mouse_offset[0],
                    cell.vertices['center'][1] + cell.resource_mouse_offset[1]
                )
            )
            await asyncio.sleep(0.05)
            return mouse.cursor_is_gather_plant()

        return False

    def reset_screen(self):
        self.current_screen_cell = None
        self.nb_screen_cell = 0
        self.nb_empty_cell = 0
        self.failed_screen_cells = []
        self.overlay.remove_drawable('screen_grid')

    def reset_map(self):
        self.current_map_cell = None
        self.visited_map_cells = []