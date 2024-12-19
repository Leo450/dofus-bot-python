import win32api
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from src.lib.struct import Vector


def get_screen_size() -> Vector:
    return Vector(win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))

def get_taskbar_height() -> int:
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    return monitor_area[3] - work_area[3]

def get_region_pixmap(top_left: Vector, size: Vector) -> QPixmap:
    try:
        return QApplication.primaryScreen().grabWindow(0, *top_left.int().tuple(), *size.int().tuple())
    except Exception as e:
        print('Could not get region pixmap')
        print(e)
        raise Exception('Could not get region pixmap')

def get_region_pixels(top_left: Vector, size: Vector) -> list:
    return pixmap_to_pixels(get_region_pixmap(top_left, size))

def pixmap_to_pixels(pixmap) -> list:
    pixels = []
    image = pixmap.toImage()
    for y in range(pixmap.height()):
        for x in range(pixmap.width()):
            color = image.pixelColor(x, y)
            pixels.append((color.red(), color.green(), color.blue()))
    return pixels

def get_pixel_color(x, y) -> tuple:
    return get_region_pixels(Vector(x, y), Vector(1, 1))[0]