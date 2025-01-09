# SLOTS MADE WITH PYTHON

## Description

- This is a classic slot machine with 3 reels and 3 rows. The player can bet for 1, 3, and 5 lines. 

- Players start with a default balance and can place bets to spin the reels.

- Winning combinations are based on traditional slot machine rules, and payouts are awarded accordingly.

- The game includes features such as random reel generation and balance tracking.

## How to Run
run the following command in the terminal

```sh
pip install -r requirements.txt
python main.py
```

## Pay table

```python

# the number on the right is the payout for the combination on the left
PAY_TABLE = [
    [["7", "7", "7"], 200],
    [["bar", "bar", "bar"], 100],
    [["melon", "melon", "melon"], 50],
    [["melon", "melon", "bar"], 50],
    [["bell", "bell", "bell"], 18],
    [["bell", "bell", "bar"], 18],
    [["grapes", "grapes", "grapes"], 14],
    [["grapes", "grapes", "bar"], 14],
    [["lemon", "lemon", "lemon"], 10],
    [["lemon", "lemon", "bar"], 10],
    [["cherry", "cherry", "any"], 5],
    [["cherry", "any", "any"], 2]
]
```
