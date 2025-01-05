from settings import *
import random
import pygame

class Reel():
    def __init__(self, pos, reel_distribution) -> None:
        self.symbol_list = pygame.sprite.Group()
        self.reel_distribution = reel_distribution
        self.shuffled_keys = reel_distribution
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5]
        self.is_spinning = False
        for index, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(SYMBOLS[item], pos, index))
            pos = list(pos)
            pos[1] += UNIT
            pos = tuple(pos)

    def animate(self, delta_time):
        if self.is_spinning:
            self.delay_time -= (delta_time * 1000)
            self.spin_time -= (delta_time * 1000)
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True

            if self.delay_time <= 0:
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 100

                    if symbol.rect.top >= 1200:
                        if reel_is_stopping:
                            self.is_spinning = False

                        symbol_index = symbol.index
                        symbol.kill()
                        self.symbol_list.add(Symbol(SYMBOLS[random.choice(self.reel_distribution)], ((symbol.rect.x), -300), symbol_index))

    def start_spin(self, delay_time):
        self.delay_time = delay_time
        self.spin_time = 1000 + delay_time
        self.is_spinning = True

    def reel_spin_result(self):
        spin_result = []

        for i in GAME_INDICES:
            spin_result.append(self.symbol_list.sprites()[i].sym_type)

        return spin_result[::-1]


class Symbol(pygame.sprite.Sprite):
    def __init__(self, path_to_symbol: str, pos, index) -> None:
        super().__init__()
        self.sym_type = path_to_symbol.split("/")[2].split(".")[0]
        self.pos = pos
        self.index = index
        self.image = pygame.image.load(path_to_symbol).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        aspect_ratio = self.rect.width / self.rect.height
        new_width = 275
        new_height = int(new_width/aspect_ratio)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

        self.size_x = new_width
        self.size_y = new_height
        self.alpha = 255
        self.fade_out = False
        self.fade_in = False

    def update(self):
        if self.fade_in:
            if self.size_x < 300:
                self.size_x += 1
                self.size_y += 1
                self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        elif not self.fade_in and self.fade_out:
            if self.alpha > 115:
                self.alpha -= 7
                self.image.set_alpha(self.alpha)
