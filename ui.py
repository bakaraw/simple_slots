from player import Player
from settings import *
from buttons import Button
import pygame
import random

class UI:
    def __init__(self, player: Player) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE + 10)
        self.win_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE + 10)
        self.win_text_angle = random.randint(-4, 4)
        self.player = player

        # buttons for selecting lines
        self.button1 = Button((255, 255, 255), (20, self.display_surface.get_height() - 90, 80, 30))
        self.button1.is_active = True
        self.button1.set_action(self.select_line_1)
        self.button2 = Button((255, 255, 255), (110, self.display_surface.get_height() - 90, 80, 30))
        self.button2.set_action(self.select_line_3)
        self.button3 = Button((255, 255, 255), (200, self.display_surface.get_height() - 90, 80, 30))
        self.button3.set_action(self.select_line_5)

        # buttons for increasing and decreasing bet
        self.add_bet_button = Button((255, 255, 255), (self.display_surface.get_width() - 50, self.display_surface.get_height() - 60, 30, 30))
        self.add_bet_button.is_active = True
        self.add_bet_button.set_action(self.player.increase_bet)

        self.decrease_bet_button = Button((255, 255, 255), (self.display_surface.get_width() - 190, self.display_surface.get_height() - 60, 30, 30))
        self.decrease_bet_button.is_active = True
        self.decrease_bet_button.set_action(self.player.decrease_bet)

    def display_info(self):
        player_data = self.player.get_data()
        balance_surf = self.font.render(f"Balance: {player_data['balance']}", True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_height() - 30
        balance_rect = balance_surf.get_rect(bottomleft=(x, y))

        bet_surf = self.bet_font.render(f"{player_data['bet_size']}", True, TEXT_COLOR, None)
        x = self.display_surface.get_width() - 60
        bet_rect = bet_surf.get_rect(bottomright=(x, y))

        bet_text = self.font.render("Bet", True, TEXT_COLOR, None)
        x = self.display_surface.get_width() - bet_rect.width/2 + 10
        y = self.display_surface.get_height() - 55
        bet_text_rect = bet_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        pygame.draw.rect(self.display_surface, False, bet_text_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(bet_surf, bet_rect)
        self.display_surface.blit(bet_text, bet_text_rect)

        self.decrease_bet_button.x = self.display_surface.get_width() - (2 * bet_rect.width) - 10

        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render(f"Win: ${last_payout}", True, TEXT_COLOR, None)
            x1 = self.display_surface.get_width() / 2
            y1 = self.display_surface.get_height() - 60
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)
            win_rect = win_surf.get_rect(center=(x1, y1))
            self.display_surface.blit(win_surf, win_rect)

        # select lines
        if self.player.lines_selected == 1:
            self.button1.is_active = True
            self.button2.is_active = False
            self.button3.is_active = False
        elif self.player.lines_selected == 3:
            self.button1.is_active = False
            self.button2.is_active = True
            self.button3.is_active = False
        elif self.player.lines_selected == 5:
            self.button1.is_active = False
            self.button2.is_active = False
            self.button3.is_active = True

        self.button1.draw("1 Line")
        self.button2.draw("3 Lines")
        self.button3.draw("5 Lines")

        self.add_bet_button.draw("+")
        self.decrease_bet_button.draw("-")

    def select_line_1(self):
        self.player.lines_selected = 1

    def select_line_3(self):
        self.player.lines_selected = 3

    def select_line_5(self):
        self.player.lines_selected = 5

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 100))
        self.display_info()
