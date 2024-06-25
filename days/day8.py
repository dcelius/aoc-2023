from .utils import read_file_lines, timing
from math import gcd

# Puzzle 15
@timing
def puzzle15():
    print('Puzzle 15')
    lines = read_file_lines('inputs/8.txt')
    instructions = lines[0]
    maps = {}
    for line in lines[2:]:
        data = line.split('=')
        key = data[0].strip()
        left = data[1].strip()[1:4]
        right = data[1].strip()[6:9]
        maps[key] = (left, right)
    start = 'AAA'
    current = start
    end = 'ZZZ'
    steps = 0
    while current != end:
        for i in range(0, len(instructions)):
            steps += 1
            if instructions[i] == 'L':
                #print("L", current, "=>", maps[current][0])
                current = maps[current][0]
            else:
                #print("R", current, "=>", maps[current][1])
                current = maps[current][1]
            if (current == end):
                break
    print("Steps:", steps)

def end_checker(input):
    for item in input:
        if item == "":
            return False
    return True

# Puzzle 16
@timing
def puzzle16():
    print('Puzzle 16')
    lines = read_file_lines('inputs/8.txt')
    instructions = lines[0]
    maps = {}
    for line in lines[2:]:
        data = line.split('=')
        key = data[0].strip()
        left = data[1].strip()[1:4]
        right = data[1].strip()[6:9]
        maps[key] = (left, right)
    running_list = []
    initial_steps = []
    loop_steps = []
    for route in maps:
        if route[-1] == 'A':
            running_list.append(route)
            loop_steps.append("")
            initial_steps.append("")
    steps = 0
    print("Starts:", running_list)
    while True:
        for i in range(0, len(instructions)):
            steps += 1
            l_or_r = 0 if instructions[i] == 'L' else 1
            for j in range(0, len(running_list)):
                running_list[j] = maps[running_list[j]][l_or_r]
                if running_list[j][-1] == 'Z' and initial_steps[j] != "" and loop_steps[j] == "":
                    print("Loop:", running_list[j], initial_steps[j], steps, steps - initial_steps[j])
                    loop_steps[j] = steps - initial_steps[j]
                if running_list[j][-1] == 'Z' and initial_steps[j] == "":
                    initial_steps[j] = steps
            if end_checker(loop_steps):
                print(running_list, initial_steps, loop_steps)
                lcm = 1
                for i in loop_steps:
                    lcm = lcm*i//gcd(lcm, i)
                print(lcm)
                return

if __name__ == "__main__":
    puzzle15()
    puzzle16()