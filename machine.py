import pygame
from settings import *
from reel import *

class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.create_reels()

    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].is_spinning for reel in self.reel_list].count(False) == 3:
            self.can_toggle = True

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()

        # if keys[pygame.K_SPACE] and self.can_toggle and self.currentPlayer.balance >= self.currentPlayer.bet_size:
        #     self.toggle_spinning()
        #     self.spin_time = pygame.time.get_ticks()
            # self.currentPlayer.place_bet()
            # self.machine_balance += self.currentPlayer.bet_size
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

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False
            
            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
        
    def update(self, delta_time):
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()

    def draw(self):
        pass
