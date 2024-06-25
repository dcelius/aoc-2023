from .utils import read_file_lines, timing
import numpy as np

def mirror_truth(truth_list, test_list):
    #print (truth_list, test_list)
    if len(truth_list) > len(test_list):
        return False
    for i in range(len(truth_list)):
        if truth_list[i] != test_list[i]:
            return False
    return True

def note_processor(note):
    forward_mirror_pattern = []
    reverse_mirror_pattern = []
    forward_indices = []
    reverse_indices = []
    first = note[0]
    reversed_first = first[::-1]
    for i in range(len(first) - 1):
        forward_mirror_pattern.insert(0, first[i])
        reverse_mirror_pattern.insert(0, reversed_first[i])
        if mirror_truth(forward_mirror_pattern, first[i + 1:]):
            forward_indices.insert(0, i)
        if mirror_truth(reverse_mirror_pattern, reversed_first[i + 1:]):
            reverse_indices.insert(0, i)
    if len(forward_indices) == 0 and len(reverse_indices) == 0:
        return 0
    for index in forward_indices:
        is_mirror = True
        for line in note[1:]:
            truth_list = line[:index + 1]
            truth_list.reverse()
            test_list = line[index + 1:]
            if not mirror_truth(truth_list, test_list): 
                is_mirror = False
                break
        if is_mirror:
            return index + 1
    for index in reverse_indices:
        is_mirror = True
        for line in note[1:]:
            line = line[::-1]
            truth_list = line[:index + 1]
            truth_list.reverse()
            test_list = line[index + 1:]
            if not mirror_truth(truth_list, test_list): 
                is_mirror = False
                break
        if is_mirror:
            return len(first) - (index + 1)
    return 0

# Puzzle 25
@timing
def puzzle25():
    lines = read_file_lines('inputs/13.txt')
    note = []
    notes = []
    id = 1
    total = 0
    for line in lines:
        if line != '' and line != '\n':
            list_line = list(line)
            note.append(list_line)
        else:
            notes.append(note)
            note = []
            id += 1
    if len(note) > 0:
        notes.append(note)
    id = 0
    for note in notes:
        id += 1
        pretotal = total
        total += note_processor(note)
        if pretotal != total:
            print(id, "has a column mirror")
            continue
        total += note_processor(np.transpose(note).tolist()) * 100
        if pretotal != total:
            print(id, "has a row mirror")
        else:
            print(id, "has no mirrors")

    print(total)

if __name__ == "__main__":
    puzzle25()