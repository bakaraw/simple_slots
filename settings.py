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
