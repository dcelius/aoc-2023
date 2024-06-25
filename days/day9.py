from .utils import read_file_lines, timing, int_list_parse_from_string, int_try_parse

# Puzzle 17 Helpers
def is_all_zeros(sequence):
    for num in sequence:
        if num != 0:
            return False
    return True

def recursive_seq_finder(sequence, sequences):
    # Don't include the 0 sequence
    if is_all_zeros(sequence):
        return sequences
    else:
        sequences.append(sequence)
        new_sequence = []
        for i in range(0, len(sequence) - 1):
            new_sequence.append(sequence[i+1] - sequence[i])
        return recursive_seq_finder(new_sequence, sequences)

def iterative_seq_solver(sequences, start_extrapolate):
    current = 0
    # Apply the last element of each sequence to the next sequence in reverse order starting with 0
    # or the first element if we're extrapolating from the start
    for i in range(1, len(sequences)):
        if start_extrapolate:
            current = sequences[-i][0] - current
        else:
            current = sequences[-i][-1] + current
    return current

# Puzzle 17
@timing
def puzzle17():
    print('Puzzle 17')
    lines = read_file_lines('inputs/9.txt')
    total = 0
    for line in lines:
        sequence = int_list_parse_from_string(line)
        sequences = recursive_seq_finder(sequence, [sequence])
        seq_val = iterative_seq_solver(sequences, start_extrapolate=False)
        print("Sequence Num:", lines.index(line), "Sequence Value:", seq_val)
        total += seq_val
    print("Total of Predicted Values:", total)

# Puzzle 18
@timing
def puzzle18():
    print('Puzzle 18')
    lines = read_file_lines('inputs/9.txt')
    total = 0
    for line in lines:
        sequence = int_list_parse_from_string(line)
        sequences = recursive_seq_finder(sequence, [sequence])
        seq_val = iterative_seq_solver(sequences, start_extrapolate=True)
        print("Sequence Num:", lines.index(line), "Sequence Value:", seq_val)
        total += seq_val
    print("Total of Predicted Values:", total)

if __name__ == "__main__":
    puzzle17()
    puzzle18()