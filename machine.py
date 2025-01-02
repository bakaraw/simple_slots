import pygame
from settings import *
from reel import *
from wins import *
from player import Player

class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.machine_balance = 10000
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.win_animation_ongoing = False
        self.prev_result = {}
        self.spin_result = {}
        self.create_reels()
        self.currentPlayer = Player()

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
                    print(self.win_data)

                # play sound
                # self.pay_player(self.win_data, self.current_player)
                # self.win_animation_ongoing = True
                # self.ui.win_text_angle = random.randint(-4, 4)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.can_toggle and self.currentPlayer.balance >= self.currentPlayer.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.currentPlayer.place_bet()
            self.machine_balance += self.currentPlayer.bet_size
            print(self.currentPlayer.get_data())
            # self.currentPlayer.last_payout = None

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
                print(x_topleft, y_topleft)

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft), REEL_FREQUENCY_MAP[self.reel_index])
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False
            
            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def check_wins(self, result):
        hits = {}
        horizontal = flip_horizontal(result)
        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2:
                    possible_win = [index for index, val in enumerate(row) if sym == val]
                    if len(longest_seq(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_seq(possible_win)]
        if hits:
            return hits

    def pay_player(self, win_data, curr_player):
        multiplier = 0
        spin_payout = 0

        for v in win_data.values():
            multiplier += len(v[1])
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

    def draw(self):
        pass
