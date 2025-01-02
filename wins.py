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
