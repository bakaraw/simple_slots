from settings import *


def flip_horizontal(result):
    horizontal_values = []
    for values in result.values():
        horizontal_values.append(values)

    rows, cols = len(horizontal_values), len(horizontal_values[0])
    hvals2 = [[""] * rows for _ in range(cols)]
    
    for x in range(rows):
        for y in range(cols):
            hvals2[y][rows - x -1] = horizontal_values[x][y]

    hvals3 = [item[::-1] for item in hvals2]
    return hvals3

def longest_seq(hit):
    sub_seq_length, longest = 1, 1
    start, end = 0, 0
    for i in range(len(hit) - 1):
        if hit[i] == hit[i + 1] - 1:
            sub_seq_length += 1
            if sub_seq_length > longest:
                longest = sub_seq_length
                start = i + 2 - sub_seq_length
                end = i + 2
        else:
            sub_seq_length = 1

    return hit[start:end]

def find_win_horizontal(hit, lines):
    win_lines = {}
    print(len(PAY_TABLE))
    pay_table = PAY_TABLE

    # append to table any symbols for cherry
    if len(PAY_TABLE) == 12:
        for sym in SYMBOLS.keys():
            if sym is not "cherry":
                pay_table.append([["cherry", "cherry", sym], 5])

        for sym in SYMBOLS.keys():
            for sym2 in SYMBOLS.keys():
                if sym is not "cherry":
                    pay_table.append([["cherry", sym, sym2], 2])

    # if selected lines is 3 or 5
    if lines > 1:
        for index, val in enumerate(hit):
            for win_line in PAY_TABLE:
                if val == win_line[0]:
                    win_lines[index + 1] = win_line

    print(win_lines)
    return win_lines



