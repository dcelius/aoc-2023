from functools import cache
from .utils import read_file_lines, timing, int_list_parse_from_string

# Puzzle 23 Helper
def sequential_char_count(char_to_count, string_to_read):
    count = 0
    sequences = []
    #print(string_to_read)
    for char in string_to_read:
        if char == char_to_count:
            count += 1
        else:
            if count > 0:
                sequences.append(count)
            count = 0
    if count > 0:
        sequences.append(count)
    return sequences

def validate_sequence(sequence_test, sequence_truth):
    if len(sequence_test) != len(sequence_truth):
        return False
    for i in range(len(sequence_truth)):
        if sequence_truth[i] != sequence_test[i]:
            return False
    return True

def semi_validate_sequence(sequence_string, sequence_truth):
    q_index = sequence_string.find('?')
    # end early if it's a complete string or completely unprocessed
    if q_index == -1 or q_index == 0:
        return True
    substring = sequence_string[:q_index-1]
    sequence_test = sequential_char_count('#', substring)
    # still processing the current sequence
    if len(sequence_test) - 1 == 0:
        return True
    #print(substring, sequence_test)
    if len(sequence_test) > len(sequence_truth):
        return False
    for i in range(len(sequence_test) - 1):
        if sequence_truth[i] != sequence_test[i]:
            return False
    return True

def recursive_sequence_maker(current_string, sequence_truth):
    if not semi_validate_sequence(current_string, sequence_truth):
        return 0
    if '?' not in current_string:
        seq_test = sequential_char_count('#', current_string)
        valid = validate_sequence(seq_test, sequence_truth)
        #print(current_string, seq_test, sequence_truth, valid)
        return 1 if valid else 0
    return recursive_sequence_maker(current_string.replace('?', '#', 1), sequence_truth) + recursive_sequence_maker(current_string.replace('?', '.', 1), sequence_truth)

# Puzzle 23
@timing
def puzzle23():
    print('Puzzle 23')
    lines = read_file_lines('inputs/12.txt')
    total = 0
    for line in lines:
        data = line.split(' ')
        sequence_truth = int_list_parse_from_string(data[1], ',')
        line_total = recursive_sequence_maker(data[0], sequence_truth)
        #print(data[0], sequence_truth, line_total)
        total += line_total
    print(total)

# Puzzle 24 Helper
def expander(line):
    multiple = 5
    new_string = (line.split(' ')[0] + '?') * multiple
    new_string = new_string[:-1]
    new_sequence = (line.split(' ')[1] + ',') * multiple
    new_sequence = new_sequence[:-1]
    return new_string, int_list_parse_from_string(new_sequence, ',')

# Puzzle 24
@timing
def puzzle24():
    print('Puzzle 24')
    lines = read_file_lines('inputs/test.txt')
    total = 0
    for line in lines:
        sequence, sequence_truth = expander(line)
        print(sequence, sequence_truth, sequence.count('?'), pow(2,sequence.count('?')))
        line_total = recursive_sequence_maker(sequence, sequence_truth)
        if line_total > 0:
            print(sequence, sequence_truth, line_total)
        total += line_total
    print(total)

# Puzzle 24 - Solved
# This one was really tough - credit where credit is due:
# https://github.com/Domyy95/Challenges/blob/master/2023-12-Advent-of-code/12.py

# I understand how this works, but would not have gotten there on my own since I didn't know about the @cache decorator
# Had a similar approach, this just takes advantage of the @cache decorator. It still generates every valid permutation, just caches the results if it comes up again.

@cache # Saves any results from this function to memory, so if it's called again with the exact same arguments, it just returns the result from memory
       # The key to this method - saves so much time
def count_arrangements(conditions, rules):
    if not rules: # no more rules to parse. If there is still a damaged spring, this is not valid (too many damaged springs)
        return 0 if "#" in conditions else 1
    if not conditions: # no more conditions to parse. If there are still rules, this is not valid (not enough damaged springs)
        return 1 if not rules else 0

    result = 0

    if conditions[0] in ".?": # Schrodinger's spring - either damaged or not, check both - this evaluates as if ? is a . (spring not damaged)
        result += count_arrangements(conditions[1:], rules) # If this spring is not damaged, move on to the next spring
    if conditions[0] in "#?": # This evaluates as if ? is a # (spring damaged)
        if (
            rules[0] <= len(conditions) # Is there space for this seq to be valid at all?
            and "." not in conditions[: rules[0]] # Is this seq valid starting from index 0 - are the next rule number of springs either damaged or ?'s?
            and (rules[0] == len(conditions) or conditions[rules[0]] != "#") # Is the spring following this seq not damaged? Also catches edge case where last spring is damaged
        ):
            result += count_arrangements(conditions[rules[0] + 1 :], rules[1:]) # If this seq is valid, assume it's here and move on to the next rule seq

    return result

@timing
def puzzle24solved():
    with open("inputs/12.txt", "r") as file:
        input = file.read().splitlines()
    solution2 = 0
    for line in input:
        conditions, rules = line.split()
        rules = eval(rules)

        conditions = "?".join([conditions] * 5)
        rules = rules * 5
        solution2 += count_arrangements(conditions, rules)
    print("Solution 2:", solution2)

if __name__ == "__main__":
    puzzle23()
    #puzzle24()
    puzzle24solved()

