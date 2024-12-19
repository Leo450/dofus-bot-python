import asyncio
import win32gui, win32ui
from pynput import mouse
from PIL import Image
from src.lib.console import BCOLORS
from src.lib.screen import get_screen_size

# Read cursor images
cursor_gather_crop_image = Image.open("assets/cursor_gather_crop.bmp")
cursor_gather_crop_pixels = list(cursor_gather_crop_image.getdata())
cursor_gather_plant_image = Image.open("assets/cursor_gather_plant.bmp")
cursor_gather_plant_pixels = list(cursor_gather_plant_image.getdata())

# Event handlers
listening = False
handlers = {}

def on_click(screen_x, screen_y, button, pressed):
    if 'click' not in handlers: return
    screen_size = get_screen_size()
    if pressed and screen_x >= 0 and screen_y >= 0 and screen_x < screen_size.x and screen_y < screen_size.y:
        print('Mouse clicked at ({0}, {1})'.format(screen_x, screen_y))
        for handler in handlers['click']:
            handler(screen_x, screen_y)

listener = mouse.Listener(on_click=on_click)

def add_handler(action, handler):
    if action not in handlers:
        handlers[action] = []
    handlers[action].append(handler)
    global listening
    if not listening:
        listener.start()
        listening = True

# Controller
controller = mouse.Controller()

# Functions
def get_cursor_code():
    return win32gui.GetCursorInfo()[1]

def cursor_is_gather_crop():
    return get_cursor_pixels() == cursor_gather_crop_pixels

def cursor_is_gather_plant():
    return get_cursor_pixels() == cursor_gather_plant_pixels

def move(x, y):
    controller.position = (x, y)

async def click():
    controller.press(mouse.Button.left)
    await asyncio.sleep(0.05)
    controller.release(mouse.Button.left)

def save_cursor_image(name='cursor.bmp'):
    def callback(hdc, hbmp):
        hbmp.SaveBitmapFile(hdc, name)
    _do_cursor_handle(callback)

def get_cursor_pixels():
    pixels = []
    def callback(hdc, hbmp):
        for i in range(30):
            for j in range(30):
                pixels.append(_rgba(hdc.GetPixel(j, i)))
    _do_cursor_handle(callback)
    return pixels

# Private functions
def _do_cursor_handle(callback):
    info = win32gui.GetCursorInfo()
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, 30, 30)
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(hbmp)
    try:
        hdc.DrawIcon((0, 0), info[1])
        callback(hdc, hbmp)
    except Exception as e:
        pass
    finally:
        win32gui.DeleteObject(hbmp.GetHandle())
        hdc.DeleteDC()

def _rgba(colorref):
    mask = 0xff
    return tuple([(colorref & (mask << (i * 8))) >> (i * 8) for i in range(3)])