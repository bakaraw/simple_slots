from settings import *
import random
import pygame

class Reel():
    def __init__(self, pos) -> None:
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(SYMBOLS.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5]

        for index, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(SYMBOLS[item], pos, index))
            pos = list(pos)
            pos[1] += UNIT
            pos = tuple(pos)

class Symbol(pygame.sprite.Sprite):
    def __init__(self, path_to_symbol: str, pos, index) -> None:
        super().__init__()
        self.sym_type = path_to_symbol.split("/")[2].split(".")[0]
        self.pos = pos
        self.index = index
        self.image = pygame.image.load(path_to_symbol).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        aspect_ratio = self.rect.width / self.rect.height
        new_width = 200
        new_height = int(new_width/aspect_ratio)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def update(self):
        pass
