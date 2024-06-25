from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 11 Helper
def check_race_win_cons(time, distance):
    race_win_conditions = 0
    race_time = time
    distance_to_beat = distance
    for sec_held in range(0, race_time):
        speed = sec_held
        time_remaining = race_time - sec_held
        distance_traveled = speed * time_remaining
        if distance_traveled > distance_to_beat:
            race_win_conditions += 1
    return race_win_conditions

# Puzzle 11
@timing
def puzzle11():
    print('Puzzle 11')
    lines = read_file_lines('inputs/6.txt')
    race_times = int_list_parse_from_string(lines[0].split(':')[1])
    distances = int_list_parse_from_string(lines[1].split(':')[1])
    total_win_conditions = 1
    for race in range(0, len(race_times)):
        race_win_conditions = check_race_win_cons(race_times[race], distances[race])
        total_win_conditions *= race_win_conditions
    print("total :", total_win_conditions)


# Puzzle 12
@timing
def puzzle12():
    print('Puzzle 12')
    lines = read_file_lines('inputs/6.txt')
    race_time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    print(check_race_win_cons(race_time, distance))

if __name__ == "__main__":
    puzzle11()
    puzzle12()
