import pygame
from settings import *
from reel import *

class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.create_reels()

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
        
    def update(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()

    def draw(self):
        pass
