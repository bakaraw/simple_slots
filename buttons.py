from collections.abc import Callable
from typing import Tuple, Optional
from settings import *
import pygame

class Button:
    def __init__(self, color, rect: Tuple, image=None)  -> None:
        self.screen = pygame.display.get_surface()
        self.color = color
        self.x, self.y, self.width, self.height = rect
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.clicked = False
        self.callback: Optional[Callable] = None
        self.is_active = False
        self.text_color = 'black'
        self.image = image

    def draw(self, text: str): 
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.screen.blit(text_surface, text_rect)
        if self.is_active:
            self.text_color = 'black'
            if self.is_hovered():
                self.color = (230, 230, 230)
            else:
                self.color = (255, 255, 255)
        else:
            self.color = 'black'
            self.text_color = 'white'

        if self.is_clicked():
            self.clicked = True
            if self.callback:
                self.callback()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def set_action(self, action):
        self.callback = action

    def is_hovered(self) -> bool:
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def is_clicked(self) -> bool:
        return self.is_hovered() and pygame.mouse.get_pressed()[0] == 1 and not self.clicked
