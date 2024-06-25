from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 5 Helper
def symbol_search(first_line, last_line, first_index, last_index, lines, int_string):
    # All symbols
    symbol_list = ['+', '-', '*', '/', '%', '^', '!', '>', '<', '=', '&', '#', '@', '$']
    symbol_string = ''.join(symbol_list)
    is_engine_part = False
    # Check for out of bounds
    if first_line < 0:
        first_line = 0
    if last_line >= len(lines):
        last_line = len(lines) - 1
    if first_index < 0:
        first_index = 0
    if last_index >= len(lines[0]):
        last_index = len(lines[0]) - 1
    chars_searched = 0
    for i in range(first_line, last_line + 1):
        line = lines[i]
        for j in range(first_index, last_index + 1):
            char = line[j]
            chars_searched += 1
            if is_engine_part is False:
                is_engine_part = symbol_string.find(char) >= 0
    print(" ".join(["Int:", '{:<4}'.format(str(int_string)), "isEnginePart:", '{:<6}'.format(str(is_engine_part)), "numCharsSearched:", str(chars_searched)]))
    return is_engine_part

# Puzzle 5
@timing
def puzzle5():
    print('Puzzle 5')
    lines = read_file_lines('inputs/3.txt')
    total = 0
    num_ints_scanned = 0
    num_engine_parts = 0
    # find all ints first, determine their full values
    # determine the surrounding indices to search for symbols
    # search surrounding indices for symbols
    for i in range(0, len(lines)):
        line = lines[i]
        int_string = ''
        for j in range(0, len(line)):
            result, is_digit = int_try_parse(line[j])
            # Append to intString if the char is an int
            # This resets after a non-int char is found
            if is_digit:
                int_string += line[j]
            else:
                # If we have an intString, check for surrounding symbols
                if int_string != '':
                    # Provide the info required to create a search area
                    if symbol_search(i-1, i+1, j-len(int_string)-1, j, lines, int_string):
                        total += int(int_string)
                        num_engine_parts += 1
                    int_string = ''
                    num_ints_scanned += 1
        # catches edge case where int is at end of line
        if int_string != '': 
            if symbol_search(i-1, i+1, j-len(int_string)-1, j, lines, int_string):
                    total += int(int_string)
            int_string = ''
            num_ints_scanned += 1
    print(" ".join(["number of ints scanned:", str(num_ints_scanned), "number of engine parts found:", str(num_engine_parts), "total of engine parts:", str(total)]))

# Puzzle 6 Helper
def gear_ratio_search(first_search_line, last_search_line, first_search_index, last_search_index, ints_info):
    first_multiplier = -1
    second_multiplier = -1
    # int_info will map to the following:
    # [0] = int
    # [1] = line index
    # [2] = start index
    # [3] = end index
    # if the search area overlaps with an int's location, save the int's value
    # overlapping means that:
    # - the int's line index is between the first and last line
    # - the int's start or end index is between the first and last index
    for int_info in ints_info:
        int_value = int_info[0]
        int_line = int_info[1]
        int_start_index = int_info[2]
        int_end_index = int_info[3]

        within_line_bounds = int_line >= first_search_line and int_line <= last_search_line
        if not within_line_bounds:
            continue

        within_index_bounds = (int_start_index >= first_search_index and int_start_index <= last_search_index) or (int_end_index >= first_search_index and int_end_index <= last_search_index)
        if not within_index_bounds:
            continue
                
        if first_multiplier == -1:
            first_multiplier = int_value
        elif second_multiplier == -1:
            second_multiplier = int_value
        else:
            print("error! too many ints found!")
            return 0
    if first_multiplier == -1 or second_multiplier == -1:
        return 0
    else:
        return first_multiplier * second_multiplier

# Puzzle 6
@timing
def puzzle6():
    print('Puzzle 6')
    lines = read_file_lines('inputs/3.txt')
    gear_ratio_total = 0
    int_info = []
    multiply_symbol_num = 0
    # find all ints, save relevant info
    for i in range(0, len(lines)):
        line = lines[i]
        int_string = ''
        for j in range(0, len(line)):
            result, is_digit = int_try_parse(line[j])
            # Append to intString if the char is an int
            # This resets after a non-int char is found
            if is_digit:
                int_string += line[j]
            else:
                if int_string != '':
                    # Provide the info required to identify the int later
                    # this should be the int, the line index, and the start/end indices
                    # since j is the first NON-INTEGER char, we need to subtract 1 to get the end index of the integer
                    int_info.append([int(int_string), i, j-len(int_string), j-1])
                    int_string = ''
        # catches edge case where int is at end of line
        if int_string != '': 
            # since this is at the end of the line, we can use j as the end index
            int_info.append([int(int_string), i, j-len(int_string)+1, j])
            int_string = ''
    # now that all ints are found, scan for * symbols and add any gear ratios to total
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line)):
            char = line[j]
            if char == '*':
                multiply_symbol_num += 1
                # since we don't want to have to pass all of lines into the func, bound check before calling
                gear_ratio_total += gear_ratio_search(i-1 if i-1 >= 0 else i, i+1 if i+1 < len(lines) else i, j-1 if j-1 > 0 else j, j+1 if j+1 < len(line) else j, int_info)
    print(" ".join(["number of * symbols found:", str(multiply_symbol_num), "total of gear ratios:", str(gear_ratio_total)]))

if __name__ == "__main__":
    puzzle5()
    puzzle6()