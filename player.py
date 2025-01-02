from settings import *

class Player:
    def __init__(self) -> None:
        self.balance = 1000
        self.bet_size = 10
        self.last_payout = 0
        self.total_won = 0
        self.total_wager = 0

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
        self.balance -= bet
        self.total_wager += bet
