from player import Player
from settings import *
import pygame
import random

class UI:
    def __init__(self, player: Player) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE + 10)
        self.win_text_angle = random.randint(-4, 4)
        self.player = player

    def display_info(self):
        player_data = self.player.get_data()
        balance_surf = self.font.render(f"Balance: {player_data['balance']}", True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_height() - 30
        balance_rect = balance_surf.get_rect(bottomleft=(x, y))

        bet_surf = self.bet_font.render(f"Bet size: {player_data['bet_size']}", True, TEXT_COLOR, None)
        x = self.display_surface.get_width() - 20
        bet_rect = bet_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(bet_surf, bet_rect)

        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render(f"Win: ${last_payout}", True, TEXT_COLOR, None)
            x1 = self.display_surface.get_width() / 2
            y1 = self.display_surface.get_height() - 60
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)
            win_rect = win_surf.get_rect(center=(x1, y1))
            self.display_surface.blit(win_surf, win_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 100))
        self.display_info()
