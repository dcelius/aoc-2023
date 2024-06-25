from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 1
@timing
def puzzle1():
    print('Puzzle 1')
    lines = read_file_lines('inputs/1.txt')
    total = 0
    for line in lines:
        firstInt = -1
        lastInt = -1
        splitLine = list(line)
        for char in splitLine:
            value, isInt = int_try_parse(char)
            if isInt:
                if firstInt == -1:
                    firstInt = value
                lastInt = value
        if firstInt == -1:
            print("error! no ints found!")
        else:
            lineTotal = (firstInt * 10) + lastInt
            print(lineTotal)
            total += lineTotal
    print(total)

# Puzzle 2
@timing
def puzzle2():
    print('Puzzle 2')
    lines = read_file_lines('inputs/1.txt')
    total = 0
    searchTerms = { 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9 }
    for line in lines:
        firstInt = -1
        lastInt = -1
        minIndex = 999999999
        maxIndex = -1
        for term in searchTerms:
            # is it here at all?
            # catches first instance
            result = line.find(term)
            if result >= 0:
                if result < minIndex:
                    minIndex = result
                    firstInt = searchTerms[term]
                if result > maxIndex:
                    maxIndex = result
                    lastInt = searchTerms[term]
            # check for multiple instances
            # will only search if found a first instance
            while result >= 0:
                result = line.find(term, result + 1)
                if result < minIndex and result >= 0:
                    minIndex = result
                    firstInt = searchTerms[term]
                if result > maxIndex and result >= 0:
                    maxIndex = result
                    lastInt = searchTerms[term]
        if firstInt == -1:
            print("error! no ints found!")
        else:
            lineTotal = (firstInt * 10) + lastInt
            print(" ".join([str(lineTotal), line]))
            total += lineTotal
    print(total)