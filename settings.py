SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_TITLE = "Slot Machine"
FPS = 60

ROW = 3
COLS = 3
UNIT = int(SCREEN_WIDTH / COLS)
X_OFFSET = 0
Y_OFFSET = 20
GAME_INDICES = [1, 2, 3]
UI_FONT = "assets/fonts/Daydream.ttf"
UI_FONT_SIZE = 12
TEXT_COLOR = 'white'
GRID_COLOR = (255, 255, 255)

SYMBOLS_PATH = "assets/symbols/"
SYMBOLS = {
    "7": f"{SYMBOLS_PATH}7.png",
    "bar": f"{SYMBOLS_PATH}bar.png",
    "bell": f"{SYMBOLS_PATH}bell.png",
    "cherry": f"{SYMBOLS_PATH}cherry.png",
    "grapes": f"{SYMBOLS_PATH}grapes.png",
    "lemon": f"{SYMBOLS_PATH}lemon.png",
    "melon": f"{SYMBOLS_PATH}melon.png",
}

REEL_FREQUENCY_MAP = [
                ["7", "bar", "bar", "bar", "melon", "melon", "bell", "grapes", "grapes", "grapes", "grapes", "grapes", "grapes", "grapes", "lemon", "lemon", "lemon", "lemon", "lemon", "cherry", "cherry"],
                ["7", "bar", "bar", "melon", "melon", "bell", "bell", "bell", "bell", "bell", "grapes", "grapes", "grapes", "lemon", "lemon", "lemon", "lemon", "lemon", "cherry", "cherry", "cherry", "cherry", "cherry", "cherry"],
                ["7", "bar", "melon", "melon", "bell", "bell", "bell", "bell", "bell", "bell", "bell", "bell", "grapes", "grapes", "grapes", "lemon", "lemon", "lemon", "lemon"]
            ]

PAY_TABLE = [
    [["7", "7", "7"], 200],
    [["bar", "bar", "bar"], 100],
    [["melon", "melon", "melon"], 50],
    [["melon", "melon", "bar"], 50],
    [["bell", "bell", "bell"], 18],
    [["bell", "bell", "bar"], 18],
    [["grapes", "grapes", "grapes"], 14],
    [["grapes", "grapes", "bar"], 14],
    [["lemon", "lemon", "lemon"], 10],
    [["lemon", "lemon", "bar"], 10],
    [["cherry", "cherry", "any"], 5],
    [["cherry", "any", "any"], 2]
]
