import re
import win32gui
from src.lib.screen import get_screen_size, get_taskbar_height

class Window:
    hwnd = None
    screen_size = (0, 0)
    window_rect = (0, 0, 0, 0)
    viewport_rect = (0, 0, 0, 0)
    window_size = (0, 0)
    viewport_size = (0, 0)
    title_bar_height = 0
    handle_size = 8
    x_overflow = 0

    def __init__(self):
        self.hwnd = self.find_window()
        if self.hwnd is None:
            raise Exception('Dofus window not found')

        self.screen_size = get_screen_size()
        self.x_overflow = self.screen_size[0] / 6
        self.update()

    def move_dofus_window(self):
        self.move(
            int(-self.x_overflow),
            0,
            int(self.screen_size[0] + self.x_overflow * 2),
            int(self.screen_size[1] - get_taskbar_height())
        )

    def focus(self):
        win32gui.SetForegroundWindow(self.hwnd)

    def move(self, x, y, width, height):
        win32gui.MoveWindow(self.hwnd, x, y, width + self.handle_size * 2, height + self.handle_size, True)
        self.update()

    def update(self):
        window_rect_with_handles = win32gui.GetWindowRect(self.hwnd)
        self.window_rect = (
            window_rect_with_handles[0] + self.handle_size,
            window_rect_with_handles[1],
            window_rect_with_handles[2] - self.handle_size,
            window_rect_with_handles[3] - self.handle_size
        )
        self.window_size = self.window_rect[2] - self.window_rect[0], self.window_rect[3] - self.window_rect[1]

        relative_viewport_rect = win32gui.GetClientRect(self.hwnd)
        self.viewport_size = relative_viewport_rect[2] - relative_viewport_rect[0], relative_viewport_rect[3] - relative_viewport_rect[1]

        self.title_bar_height = self.window_size[1] - self.viewport_size[1]

        self.viewport_rect = (
            self.window_rect[0] + relative_viewport_rect[0],
            self.window_rect[1] + relative_viewport_rect[1] + self.title_bar_height,
            self.window_rect[0] + relative_viewport_rect[2],
            self.window_rect[1] + relative_viewport_rect[3] + self.title_bar_height
        )


        self.viewport_size = self.viewport_rect[2] - self.viewport_rect[0], self.viewport_rect[3] - self.viewport_rect[1]

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

    def to_screen(self, x, y):
        return self.viewport_rect[0] + x, self.viewport_rect[1] + y

    def to_viewport(self, x, y):
        return x - self.viewport_rect[0], y - self.viewport_rect[1]