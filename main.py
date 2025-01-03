import pygame
import sys
from settings import *
from machine import Machine

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(SCREEN_TITLE)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.Surface((SCREEN_SIZE))
        self.bg_image.fill((66, 135, 245))
        self.delta_time = 0
        self.running = True
        self.machine = Machine()

    def run(self):
        self.start_time = pygame.time.get_ticks()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
