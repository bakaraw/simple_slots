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
            self.draw_grid()
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def draw_grid(self):
        unit = int(SCREEN_WIDTH / COLS)
        for x in range(0, SCREEN_WIDTH, unit):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 10)

        for y in range(0, SCREEN_HEIGHT, unit):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 10)

        pygame.draw.line(self.screen, GRID_COLOR, (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 10)
if __name__ == "__main__":
    game = Game()
    game.run()
