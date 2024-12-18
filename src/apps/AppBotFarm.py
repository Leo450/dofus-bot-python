import asyncio
import threading
from PyQt5.QtWidgets import QApplication
from src.lib.console import BCOLORS
from src.lib.overlay import Overlay
from src.bot.BotFarm import BotFarm
from src.lib.window import Window
from src.lib.keyboard import add_handler as add_keyboard_handler

class AppBotFarm:
    bot = None
    bot_task = None
    qt_app = None
    overlay = None
    window = None

    def run(self):
        self.window = Window()
        self.window.move_dofus_window()

        self.init_overlay()
        self.init_bot()

        threading.Thread(target=self.run_bot).start()
        self.run_overlay()

    def init_overlay(self):
        self.qt_app = QApplication([])

        def on_stop():
            print('Stopping overlay...')
            self.qt_app.quit()
        add_keyboard_handler('²', on_stop)

        self.overlay = Overlay(self.window)

    def init_bot(self):
        self.bot = BotFarm(self.window, self.overlay)

        def on_stop():
            print('Stopping bot...')
            self.bot_task.cancel()
        add_keyboard_handler('²', on_stop)

    def run_overlay(self):
        self.qt_app.exec_()

    def run_bot(self):
        if threading.current_thread() is not threading.main_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        else:
            loop = asyncio.get_event_loop()

        self.bot_task = asyncio.ensure_future(self.run_bot_task())

        loop.run_until_complete(self.bot_task)

    async def run_bot_task(self):
        try:
            await self.bot.start()
        except asyncio.CancelledError:
            print(BCOLORS.colorize(' >>>> STOP <<<< ', BCOLORS.BG_WHITE + BCOLORS.BLACK + BCOLORS.BOLD))