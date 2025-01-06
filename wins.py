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

def find_win(hit, lines):
    win_lines = {}
    diagonals = get_diagonals(hit)

    # append to table any symbols for cherry
    if len(PAY_TABLE) == 12:
        for sym in SYMBOLS.keys():
            if sym is not "cherry":
                PAY_TABLE.append([["cherry", "cherry", sym], 5])

        for sym in SYMBOLS.keys():
            for sym2 in SYMBOLS.keys():
                if sym is not "cherry":
                    PAY_TABLE.append([["cherry", sym, sym2], 2])

    # if selected lines is 1
    if lines == 1:
        for win_line in PAY_TABLE:
            if hit[1] == win_line[0]:
                win_lines[2] = win_line
    # if selected lines is 3 or 5
    elif lines > 1:
        for index, val in enumerate(hit):
            for win_line in PAY_TABLE:
                if val == win_line[0]:
                    win_lines[index + 1] = win_line

        if lines == 5:
            for index, val in enumerate(diagonals):
                for win_line in PAY_TABLE:
                    if val == win_line[0]:
                        win_lines[index + 4] = win_line
    return win_lines

def get_diagonals(results):
    diagonal_values = []
    diagonal_values1 = []
    diagonal_values2 = []

    for i in range(ROW):
        diagonal_values1.append(results[i][i])
        diagonal_values2.append(results[ROW - i - 1][i])

    diagonal_values.append(diagonal_values1)
    diagonal_values.append(diagonal_values2)
    return diagonal_values

