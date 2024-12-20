import re
import win32gui
from src.lib.screen import get_screen_size, get_taskbar_height
from src.lib.struct import Rect, Vector


class Window:
    hwnd = None
    screen_size = None
    window_rect = None
    viewport_rect = None
    window_size = None
    viewport_size = None
    title_bar_height = 0
    handle_size = 8
    x_overflow = 0

    def __init__(self):
        self.screen_size = get_screen_size()
        self.x_overflow = self.screen_size.y / 3

    def init(self):
        self.hwnd = self.find_window()
        if self.hwnd is None:
            raise Exception('Dofus window not found')

        self.move_and_scale()
        self.focus()

    def move_and_scale(self):
        win32gui.MoveWindow(
            self.hwnd,
            int(-self.x_overflow),
            0,
            int(self.screen_size.x + self.x_overflow * 2) + self.handle_size * 2,
            int(self.screen_size.y - get_taskbar_height()) + self.handle_size,
            True
        )
        self.update()

    def focus(self):
        win32gui.SetForegroundWindow(self.hwnd)

    def update(self):
        window_rect_with_handles = Rect(*win32gui.GetWindowRect(self.hwnd))
        viewport_rect_relative_to_window = Rect(*win32gui.GetClientRect(self.hwnd))

        self.window_rect = window_rect_with_handles + Rect(self.handle_size, 0, -self.handle_size, -self.handle_size)
        self.window_size = self.window_rect.size()
        self.viewport_size = viewport_rect_relative_to_window.size()
        self.title_bar_height = self.window_size.y - self.viewport_size.y
        self.viewport_rect = Rect(
            self.window_rect.min.x + viewport_rect_relative_to_window.min.x,
            self.window_rect.min.y + viewport_rect_relative_to_window.min.y + self.title_bar_height,
            self.window_rect.min.x + viewport_rect_relative_to_window.max.x,
            self.window_rect.min.y + viewport_rect_relative_to_window.max.y + self.title_bar_height
        )

    def find_window(self):
        hwnd = None

        def win_enum_handler(_hwnd, ctx):
            if win32gui.IsWindowVisible(_hwnd):
                title = win32gui.GetWindowText(_hwnd)
                if re.search(r'[A-Za-z]+ - [A-Za-z]+ - [0-9.]+ - Release', title):
                    print(f'Found Dofus window: {title}')
                    nonlocal hwnd
                    hwnd = _hwnd
                    return False

        win32gui.EnumWindows(win_enum_handler, None)

        return hwnd

    def to_screen(self, coords: Vector) -> Vector:
        return Vector(self.viewport_rect.min.x + coords.x, self.viewport_rect.min.y + coords.y)

    def to_viewport(self, coords: Vector) -> Vector:
        return Vector(coords.x - self.viewport_rect.min.x, coords.y - self.viewport_rect.min.y)