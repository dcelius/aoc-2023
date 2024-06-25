from .utils import read_file_lines, timing

# Map Expander
def expand_map():
    map = read_file_lines('inputs/11.txt')
    expanded_map = []
    row_indices = [0] * len(map) # any row indices with a value == 0 needs to add a row (y) at the given index
    col_indices = [0] * len(map[0]) # any col indices with a value == 0 needs to add a col (x) at the given index
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == '#':
                row_indices[i] += 1
                col_indices[j] += 1
    # for each row
    for i in range(0, len(map)):
        # add the new row
        expanded_map.append(list(map[i]))
        # if that row is clear, add another row
        if row_indices[i] == 0:
            expanded_map.append(['.'] * len(map[i]))
    # for each col
    offset = 0
    for j in range(0, len(map[0])):
        # if clear, add a column
        if col_indices[j] == 0:
            # need to add one . to each row at the given index
            # offset is because the expanded map is growing as we add columns
            # so the OG indices are no longer valid
            for i in range(0, len(expanded_map)):
                expanded_map[i].insert(j + offset, '.')
            offset += 1
    with open('inputs/11-expanded.txt', 'w') as f:
        for line in expanded_map:
            f.write(''.join(line) + '\n')
    return expanded_map

# Puzzle 21
@timing
def puzzle21():
    print('Puzzle 21')
    expand_map()
    map = read_file_lines('inputs/11-expanded.txt')
    galaxy_id = 0
    galaxies = {}
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == '#':
                galaxies[galaxy_id] = (j, i)
                galaxy_id += 1
    distance_total = 0
    for i in range(0, len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            # Manhattan distance between the two galaxies
            distance_total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    print(distance_total)

# Puzzle 21-d2
# better 
@timing
def puzzle21_d2():
    print('Puzzle 21-d2')
    # get the row/col index lists
    # for each 0 between the indices of the given galaxies, add 1million to the manhattan distance for that coordinate
    map = read_file_lines('inputs/11.txt')
    row_indices = [0] * len(map) # any row indices with a value == 0 needs to add a row (y) at the given index
    col_indices = [0] * len(map[0]) # any col indices with a value == 0 needs to add a col (x) at the given index
    galaxies = {}
    galaxy_id = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == '#':
                row_indices[i] += 1
                col_indices[j] += 1
                galaxies[galaxy_id] = (j, i)
                galaxy_id += 1
    distance_total = 0
    expansion_factor = 2 - 1
    for i in range(0, len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            expansion_count_row = 0
            expansion_count_col = 0
            greatest_col = max(galaxies[i][0], galaxies[j][0])
            smallest_col = min(galaxies[i][0], galaxies[j][0])
            greatest_row = max(galaxies[i][1], galaxies[j][1])
            smallest_row = min(galaxies[i][1], galaxies[j][1])
            for k in range(smallest_col + 1, greatest_col):
                if col_indices[k] == 0:
                    expansion_count_col += 1
            for k in range(smallest_row + 1, greatest_row):
                if row_indices[k] == 0:
                    expansion_count_row += 1
            # Manhattan distance between the two galaxies
            distance_total += expansion_count_col * expansion_factor + expansion_count_row * expansion_factor + abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
    print(distance_total)

# Puzzle 22
@timing
def puzzle22():
    print('Puzzle 22')
    # get the row/col index lists
    # for each 0 between the indices of the given galaxies, add 1million to the manhattan distance for that coordinate
    map = read_file_lines('inputs/11.txt')
    row_indices = [0] * len(map) # any row indices with a value == 0 needs to add a row (y) at the given index
    col_indices = [0] * len(map[0]) # any col indices with a value == 0 needs to add a col (x) at the given index
    galaxies = {}
    galaxy_id = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == '#':
                row_indices[i] += 1
                col_indices[j] += 1
                galaxies[galaxy_id] = (j, i)
                galaxy_id += 1
    distance_total = 0
    expansion_factor = 1000000 - 1
    for i in range(0, len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            expansion_count_row = 0
            expansion_count_col = 0
            # get the number of expansions between the two galaxies
            greatest_col = max(galaxies[i][0], galaxies[j][0])
            smallest_col = min(galaxies[i][0], galaxies[j][0])
            greatest_row = max(galaxies[i][1], galaxies[j][1])
            smallest_row = min(galaxies[i][1], galaxies[j][1])
            for k in range(smallest_col + 1, greatest_col):
                if col_indices[k] == 0:
                    expansion_count_col += 1
            for k in range(smallest_row + 1, greatest_row):
                if row_indices[k] == 0:
                    expansion_count_row += 1
            # Manhattan distance between the two galaxies
            # expansion values are always added to the distance
            distance_total += expansion_count_col * expansion_factor + expansion_count_row * expansion_factor + abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
    print(distance_total)

if __name__ == "__main__":
    #expand_map()
    puzzle21()
    puzzle21_d2()
    puzzle22()