from src.lib.mouse import save_cursor_image
from src.lib.keyboard import add_handler as add_keyboard_handler

class AppPrintCursor:
    def run(self):
        def on_keyboard():
            save_cursor_image('cursor.bmp')
        add_keyboard_handler('²', on_keyboard)

        while True:
            pass