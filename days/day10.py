from .utils import read_file_lines, timing, int_list_parse_from_string, int_try_parse

# Puzzle 19
@timing
def puzzle19():
    print('Puzzle 19')
    map = read_file_lines('inputs/10.txt')
    # find start tile
    start = None
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == 'S':
                start = [x, y]
    length = 1
    current_tile = '|'
    current_coords = [start[0], start[1] + 1]
    incoming_direction = 'S'
    while current_tile != 'S':
        #print(current_tile, current_coords, incoming_direction, length)
        length += 1
        match current_tile:
            case '|':
                # vertical movement, N-S
                if incoming_direction == 'S':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                elif incoming_direction == 'N':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case '-':
                # horizontal movement, W-E
                if incoming_direction == 'E':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case 'L':
                # 90 degree N-E turn
                if incoming_direction == 'S':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case 'J':
                # 90 degree N-W turn
                if incoming_direction == 'S':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                elif incoming_direction == 'E':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case 'F':
                # 90 degree S-E turn
                if incoming_direction == 'N':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case '7':
                # 90 degree S-W turn
                if incoming_direction == 'N':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                elif incoming_direction == 'E':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, length)
                    return
            case 'S':
                # start pos
                print("Steps:", length)
            case _:
                # error or ground tile
                print('Error: Invalid Tile', current_tile, current_coords, incoming_direction, length)
                return
        current_tile = map[current_coords[1]][current_coords[0]]
    print("Steps:", length)
    print("Steps to farthest:", length / 2)

# Puzzle 20 Helper
# increase the resolution of the map by 3x
# also add a 3x3 grid of 0s around the map to make bfs easier
# asterisks used for 'squeeze' tiles
# ex:
#            ...
#  F    -->  .F-
#            .|.
def map_expander(map):
    with open('inputs/10-2.txt', 'w') as file:
        for y in range(0, len(map)):
            line1 = ['0','0','0']
            line2 = ['0','0','0']
            line3 = ['0','0','0']
            for x in range(0, len(map[y])):
                if map[y][x] == 'F':
                    line1.append('*')
                    line1.append('*')
                    line1.append('*')
                    line2.append('*')
                    line2.append('F')
                    line2.append('-')
                    line3.append('*')
                    line3.append('|')
                    line3.append('*')
                elif map[y][x] == '7':
                    line1.append('*')
                    line1.append('*')
                    line1.append('*')
                    line2.append('-')
                    line2.append('7')
                    line2.append('*')
                    line3.append('*')
                    line3.append('|')
                    line3.append('*')
                elif map[y][x] == 'L':
                    line1.append('*')
                    line1.append('|')
                    line1.append('*')
                    line2.append('*')
                    line2.append('L')
                    line2.append('-')
                    line3.append('*')
                    line3.append('*')
                    line3.append('*')
                elif map[y][x] == 'J':
                    line1.append('*')
                    line1.append('|')
                    line1.append('*')
                    line2.append('-')
                    line2.append('J')
                    line2.append('*')
                    line3.append('*')
                    line3.append('*')
                    line3.append('*')
                elif map[y][x] == '|':
                    line1.append('*')
                    line1.append('|')
                    line1.append('*')
                    line2.append('*')
                    line2.append('|')
                    line2.append('*')
                    line3.append('*')
                    line3.append('|')
                    line3.append('*')
                elif map[y][x] == '-':
                    line1.append('*')
                    line1.append('*')
                    line1.append('*')
                    line2.append('-')
                    line2.append('-')
                    line2.append('-')
                    line3.append('*')
                    line3.append('*')
                    line3.append('*')
                elif map[y][x] == 'S':
                    line1.append('*')
                    line1.append('|')
                    line1.append('*')
                    line2.append('-')
                    line2.append('S')
                    line2.append('-')
                    line3.append('*')
                    line3.append('|')
                    line3.append('*')
                elif map[y][x] == '.':
                    line1.append('.')
                    line1.append('.')
                    line1.append('.')
                    line2.append('.')
                    line2.append('.')
                    line2.append('.')
                    line3.append('.')
                    line3.append('.')
                    line3.append('.')
                else:
                    print('Error: Invalid Tile', map[y][x])
                    return
            line1.append('0')
            line1.append('0')
            line1.append('0')
            line2.append('0')
            line2.append('0')
            line2.append('0')
            line3.append('0')
            line3.append('0')
            line3.append('0')
            if y == 0:
                chaser = ['0'] * len(line1)
                file.write("".join(chaser) + '\n')
                file.write("".join(chaser) + '\n')
                file.write("".join(chaser) + '\n')
            file.write("".join(line1) + '\n')
            file.write("".join(line2) + '\n')
            file.write("".join(line3) + '\n')
            if y == len(map) - 1:
                chaser = ['0'] * len(line1)
                file.write("".join(chaser) + '\n')
                file.write("".join(chaser) + '\n')
                file.write("".join(chaser) + '\n')
    return read_file_lines('inputs/10-2.txt')

# Do a BFS on the map to find the number of interior tiles
# If the tile is not a wall or a pipe, it is on the exterior since we start at a known exterior tile
# By painting the tiles we visit, we can avoid visiting them again without a separate visited list
# also it's a nice visual
def bfs(map):
    queue = [(0,0)]
    visited = 0
    while len(queue) > 0:
        current = queue.pop(0)
        if map[current[1]][current[0]] != 'O' and map[current[1]][current[0]] != 'X':
            visited += 1 if (current[1] - 1) % 3 == 0 and (current[0] - 1) % 3 == 0 and map[current[1]][current[0]] != '0' else 0
            map[current[1]][current[0]] = 'O'
            if current[1] - 1 >= 0:
                queue.append((current[0], current[1] - 1))
            if current[1] + 1 < len(map):
                queue.append((current[0], current[1] + 1))
            if current[0] - 1 >= 0:
                queue.append((current[0] - 1, current[1]))
            if current[0] + 1 < len(map[0]):
                queue.append((current[0] + 1, current[1]))
    return visited

# this is gross I hate it
def tile_counter(map):
    # count the number of interior tiles in the map
    tile_count = 0
    for y in range(0, len(map), 3):
        for x in range(0, len(map[y]), 3):
            if map[y][x] == 'O' or map[y][x] == 'X':
                continue
            elif map[y+1][x] == 'O' or map[y+1][x] == 'X':
                continue
            elif map[y+2][x] == 'O' or map[y+2][x] == 'X':
                continue
            elif map[y][x+1] == 'O' or map[y][x+1] == 'X':
                continue
            elif map[y][x+2] == 'O' or map[y][x+2] == 'X':
                continue
            elif map[y+1][x+1] == 'O' or map[y+1][x+1] == 'X':
                continue
            elif map[y+2][x+1] == 'O' or map[y+2][x+1] == 'X':
                continue
            elif map[y+1][x+2] == 'O' or map[y+1][x+2] == 'X':
                continue
            elif map[y+2][x+2] == 'O' or map[y+2][x+2] == 'X':
                continue
            else:
                tile_count += 1
                map[y][x] = 'I'
                map[y+1][x] = 'I'
                map[y+2][x] = 'I'
                map[y][x+1] = 'I'
                map[y][x+2] = 'I'
                map[y+1][x+1] = 'I'
                map[y+2][x+1] = 'I'
                map[y+1][x+2] = 'I'
                map[y+2][x+2] = 'I'
    return tile_count

# Puzzle 20
@timing
def puzzle20():
    print('Puzzle 20')
    # use 10-2 if the expanded map has already been generated otherwise use 10 and expand the map
    map = read_file_lines('inputs/10-2.txt')
    # this was already run once, doesn't need to be run again
    #map = map_expander(map)
    painted_map = []
    # find start tile
    start = None
    for y in range(0, len(map)):
        painted_map.append([])
        for x in range(0, len(map[y])):
            painted_map[y].append(map[y][x])
            if map[y][x] == 'S':
                start = [x, y]
    # it's easier to manually set the start direction of the loop
    # so we go south first
    steps = 1
    current_tile = '|'
    current_coords = [start[0], start[1] + 1]
    incoming_direction = 'S'
    while current_tile != 'S':
        painted_map[current_coords[1]][current_coords[0]] = 'X'
        steps += 1
        match current_tile:
            case '|':
                # vertical movement, N-S
                if incoming_direction == 'S':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                elif incoming_direction == 'N':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case '-':
                # horizontal movement, W-E
                if incoming_direction == 'E':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case 'L':
                # 90 degree N-E turn
                if incoming_direction == 'S':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case 'J':
                # 90 degree N-W turn
                if incoming_direction == 'S':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                elif incoming_direction == 'E':
                    current_coords[1] -= 1
                    incoming_direction = 'N'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case 'F':
                # 90 degree S-E turn
                if incoming_direction == 'N':
                    current_coords[0] += 1
                    incoming_direction = 'E'
                elif incoming_direction == 'W':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case '7':
                # 90 degree S-W turn
                if incoming_direction == 'N':
                    current_coords[0] -= 1
                    incoming_direction = 'W'
                elif incoming_direction == 'E':
                    current_coords[1] += 1
                    incoming_direction = 'S'
                else:
                    print('Error: Invalid Direction', current_tile, current_coords, incoming_direction, steps)
                    return
            case 'S':
                # start pos
                print("Steps:", steps)
            case _:
                # error or ground tile
                print('Error: Invalid Tile', current_tile, current_coords, incoming_direction, steps)
                return
        current_tile = map[current_coords[1]][current_coords[0]]
    # we need to manually paint the start tile since it's not part of the loop (otherwise BFS loses its mind)
    painted_map[start[1]][start[0]] = 'X'
    outside_count = bfs(painted_map)
    # since all pipe items have 3 "tiles", that means if we take the number of steps and divide by 3, we get the number of pipes
    pipes = int(steps / 3)
    # remove header rows and columns, then reduce the map by 3x to get the total number of tiles
    total_tiles = int((len(painted_map) - 6) * (len(painted_map[0]) - 6) / 9)
    print("Interior Tiles:", tile_counter(painted_map), "Exterior Tiles:", outside_count, "Pipes:", pipes, "Total Tiles:", total_tiles)
    # Save the painted map for visualization - it's honestly pretty cool
    with open('inputs/10-2-painted.txt', 'w') as file:
        for line in painted_map:
            file.write("".join(line) + '\n')

if __name__ == "__main__":
    puzzle19()
    puzzle20()