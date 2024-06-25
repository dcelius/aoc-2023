from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 3
@timing
def puzzle3():
    print('Puzzle 3')
    lines = read_file_lines('inputs/2.txt')
    total = 0
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    for line in lines:
        lineMaxRed = -1
        lineMaxGreen = -1
        lineMaxBlue = -1
        gamePrefix = line.split(':')[0]
        gameID = int(gamePrefix[5:])
        games = line.split(':')[1].split(';')
        for game in games:
            gameInfo = game.split(',')
            for item in gameInfo:
                item = item.strip()
                pair = item.split(' ')
                if pair[1] == 'red':
                    gameRed = int(pair[0])
                    if gameRed > lineMaxRed:
                        lineMaxRed = gameRed
                elif pair[1] == 'green':
                    gameGreen = int(pair[0])
                    if gameGreen > lineMaxGreen:
                        lineMaxGreen = gameGreen
                elif pair[1] == 'blue':
                    gameBlue = int(pair[0])
                    if gameBlue > lineMaxBlue:
                        lineMaxBlue = gameBlue
        print(" ".join([str(lineMaxRed), str(lineMaxGreen), str(lineMaxBlue)]))
        if lineMaxRed <= maxRed and lineMaxGreen <= maxGreen and lineMaxBlue <= maxBlue:
            total += gameID
    print(total)

# Puzzle 4
@timing
def puzzle4():
    print('Puzzle 4')
    lines = read_file_lines('inputs/2.txt')
    total = 0
    for line in lines:
        lineMaxRed = -1
        lineMaxGreen = -1
        lineMaxBlue = -1
        games = line.split(':')[1].split(';')
        for game in games:
            gameInfo = game.split(',')
            for item in gameInfo:
                item = item.strip()
                pair = item.split(' ')
                if pair[1] == 'red':
                    gameRed = int(pair[0])
                    if gameRed > lineMaxRed:
                        lineMaxRed = gameRed
                elif pair[1] == 'green':
                    gameGreen = int(pair[0])
                    if gameGreen > lineMaxGreen:
                        lineMaxGreen = gameGreen
                elif pair[1] == 'blue':
                    gameBlue = int(pair[0])
                    if gameBlue > lineMaxBlue:
                        lineMaxBlue = gameBlue
        print(" ".join([str(lineMaxRed), str(lineMaxGreen), str(lineMaxBlue)]))
        total += lineMaxRed * lineMaxGreen * lineMaxBlue
    print(total)

if __name__ == "__main__":
    puzzle3()
    puzzle4()