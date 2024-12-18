class BCOLORS:
    """
    Colors for the console output.
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GREY = '\033[37m'
    LIGHT_GREY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_PURPLE = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_GREY = '\033[47m'
    BG_LIGHT_GREY = '\033[100m'
    BG_LIGHT_RED = '\033[101m'
    BG_LIGHT_GREEN = '\033[102m'
    BG_LIGHT_YELLOW = '\033[103m'
    BG_LIGHT_BLUE = '\033[104m'
    BG_LIGHT_PURPLE = '\033[105m'
    BG_LIGHT_CYAN = '\033[106m'
    BG_WHITE = '\033[107m'

    @staticmethod
    def colorize(text: str, color: str) -> str:
        return color + text + BCOLORS.ENDC

    @staticmethod
    def black(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BLACK)

    @staticmethod
    def red(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.RED)

    @staticmethod
    def green(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.GREEN)

    @staticmethod
    def yellow(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.YELLOW)

    @staticmethod
    def blue(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BLUE)

    @staticmethod
    def purple(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.PURPLE)

    @staticmethod
    def cyan(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.CYAN)

    @staticmethod
    def grey(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.GREY)

    @staticmethod
    def light_grey(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_GREY)

    @staticmethod
    def light_red(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_RED)

    @staticmethod
    def light_green(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_GREEN)

    @staticmethod
    def light_yellow(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_YELLOW)

    @staticmethod
    def light_blue(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_BLUE)

    @staticmethod
    def light_purple(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_PURPLE)

    @staticmethod
    def light_cyan(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.LIGHT_CYAN)

    @staticmethod
    def white(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.WHITE)

    @staticmethod
    def bold(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BOLD)

    @staticmethod
    def underline(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.UNDERLINE)

    @staticmethod
    def bg_black(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_BLACK)

    @staticmethod
    def bg_red(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_RED)

    @staticmethod
    def bg_green(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_GREEN)

    @staticmethod
    def bg_yellow(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_YELLOW)

    @staticmethod
    def bg_blue(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_BLUE)

    @staticmethod
    def bg_purple(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_PURPLE)

    @staticmethod
    def bg_cyan(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_CYAN)

    @staticmethod
    def bg_grey(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_GREY)

    @staticmethod
    def bg_light_grey(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_GREY)

    @staticmethod
    def bg_light_red(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_RED)

    @staticmethod
    def bg_light_green(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_GREEN)

    @staticmethod
    def bg_light_yellow(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_YELLOW)

    @staticmethod
    def bg_light_blue(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_BLUE)

    @staticmethod
    def bg_light_purple(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_PURPLE)

    @staticmethod
    def bg_light_cyan(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_LIGHT_CYAN)

    @staticmethod
    def bg_white(text: str) -> str:
        return BCOLORS.colorize(text, BCOLORS.BG_WHITE)