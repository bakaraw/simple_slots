import pygame
from settings import *
from reel import *
from wins import *
from player import Player
from debug import debug
from ui import UI

class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.machine_balance = 10000
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.win_animation_ongoing = False
        self.can_animate = False
        self.prev_result = {}
        self.spin_result = {}
        self.create_reels()
        self.currentPlayer = Player()
        self.ui = UI(self.currentPlayer)

    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].is_spinning for reel in self.reel_list].count(False) == COLS:
            self.can_toggle = True

            if self.check_wins(self.get_result()):
                self.win_data = self.check_wins(self.get_result())
                if self.win_data:
                    self.win_animation_ongoing = True
                    self.pay_player(self.win_data, self.currentPlayer)

                # play sound
                self.win_animation_ongoing = True
                self.ui.win_text_angle = random.randint(-4, 4)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_toggle and self.currentPlayer.balance >= (self.currentPlayer.bet_size * self.currentPlayer.lines_selected):
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.currentPlayer.place_bet()
            self.machine_balance += self.currentPlayer.bet_size
            self.currentPlayer.last_payout = None

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def create_reels(self):
        x_topleft, y_topleft = 10, -UNIT
        # if not self.reel_list:
        #     x_topleft, y_topleft = 10, -UNIT

        while self.reel_index < COLS:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (UNIT + X_OFFSET), -UNIT

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft), REEL_FREQUENCY_MAP[self.reel_index])
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False
            
            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                self.win_animation_ongoing = False

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def check_wins(self, result):
        horizontal = flip_horizontal(result)
        hits = find_win(horizontal, self.currentPlayer.lines_selected)

        if hits:
            self.can_animate = True
            return hits

    def pay_player(self, win_data, curr_player):
        multiplier = 0
        spin_payout = 0

        for v in win_data.values():
            multiplier = v[1]
            spin_payout += (multiplier * curr_player.bet_size)
            curr_player.balance += spin_payout
            self.machine_balance -= spin_payout
            self.currentPlayer.last_payout = spin_payout
            self.currentPlayer.total_won += spin_payout
        
    def update(self, delta_time):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()

        self.draw_grid()
        # debugger for player data
        # self.debugger()
        self.ui.update()
        # commented for now
        # TODO: fix win animation
        self.win_animation()

    def debugger(self):
        # debugger
        debug_player_data = self.currentPlayer.get_data()
        machine_balance = "{:.2f}".format(self.machine_balance)
        if self.currentPlayer.last_payout:
            last_payout = "{:.2f}".format(self.currentPlayer.last_payout)
        else:
            last_payout = "N/A"
        debug(f"Player balance: {debug_player_data['balance']} | Machine balance: {machine_balance} | Last payout: {last_payout}")

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, UNIT):
            pygame.draw.line(self.display_surface, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 10)

        for y in range(0, SCREEN_HEIGHT, UNIT):
            pygame.draw.line(self.display_surface, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 10)

        pygame.draw.line(self.display_surface, GRID_COLOR, (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 10)

    def win_animation(self):
        if self.win_animation_ongoing and self.win_data:
            for k, v in self.win_data.items():
                animationRow = 0
                if k == 1:
                    animationRow = 3
                elif k == 3:
                    animationRow = 1
                elif k == 2:
                    animationRow = 2

                # animation for non diagonal wins
                # index 4 and 5 are indices for diagonal
                if k != 4 and k != 5:
                    for reel in self.reel_list:
                        if self.can_animate:
                            self.reel_list[reel].symbol_list.sprites()[animationRow].fade_in = True
                        for symbol in self.reel_list[reel].symbol_list:
                            if not symbol.fade_in:
                                symbol.fade_out = True

                else:
                    for i in range(ROW):
                        for reel_index, reel in enumerate(self.reel_list):
                            if k == 4:
                                if reel_index == ROW - i - 1:
                                    self.reel_list[reel].symbol_list.sprites()[i + 1].fade_in = True
                            elif k == 5:
                                if reel_index == i:
                                    self.reel_list[reel].symbol_list.sprites()[i + 1].fade_in = True

                    for reel in self.reel_list:
                        for symbol in self.reel_list[reel].symbol_list:
                            if not symbol.fade_in:
                                symbol.fade_out = True
