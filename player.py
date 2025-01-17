from settings import *

class Player:
    def __init__(self) -> None:
        self.balance = 1000
        self.bet_size = 10
        self.last_payout = None
        self.total_won = 0
        self.total_wager = 0
        self.lines_selected = 1

    def get_data(self):
        player_data = {
            "balance": "{:.2f}".format(self.balance),
            "bet_size": "{:.2f}".format(self.bet_size),
            "last_payout": "{:.2f}".format(self.last_payout) if self.last_payout else "N/A",
            "total_won": "{:.2f}".format(self.total_won),
            "total_wager": "{:.2f}".format(self.total_wager)
        }
        return player_data

    def place_bet(self):
        bet = self.bet_size
        wager = bet * self.lines_selected
        self.balance -= wager
        self.total_wager += wager

    def increase_bet(self):
        self.bet_size += 1

    def decrease_bet(self):
        if self.bet_size > 0:
            self.bet_size -= 1
