from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 7
@timing
def puzzle7():
    print('Puzzle 7')
    cards = read_file_lines('inputs/4.txt')
    total = 0
    for card in cards:
        card_points = 0
        card_prefix = card.split(':')[0]
        winning_numbers_string = card.split(':')[1].split('|')[0]
        numbers_string = card.split(':')[1].split('|')[1]
        winning_numbers = int_list_parse_from_string(winning_numbers_string)
        numbers = int_list_parse_from_string(numbers_string)
        winning_numbers.sort()
        numbers.sort()
        min_num = numbers[0]
        max_num = numbers[-1]
        matched_numbers = []
        for winning_number in winning_numbers:
            # save a bit of time by skipping numbers that are out of range
            if winning_number < min_num:
                continue
            elif winning_number > max_num:
                break
            if winning_number in numbers:
                matched_numbers.append(winning_number)
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
        print(" ".join([card_prefix, "Points:", str(card_points), "Matched Numbers:", str(matched_numbers)]))
        total += card_points
    print(total)

# Puzzle 8
@timing
def puzzle8():
    print('Puzzle 8')
    cards = read_file_lines('inputs/4.txt')
    card_match_dictionary = {}
    card_count_dictionary = {}
    # first pass, find the number of matches for each card
    for card in cards:
        card_prefix = card.split(':')[0]
        card_id = int(card_prefix[5:])
        winning_numbers_string = card.split(':')[1].split('|')[0]
        numbers_string = card.split(':')[1].split('|')[1]
        winning_numbers = int_list_parse_from_string(winning_numbers_string)
        numbers = int_list_parse_from_string(numbers_string)
        winning_numbers.sort()
        numbers.sort()
        min_num = numbers[0]
        max_num = numbers[-1]
        matches = 0
        for winning_number in winning_numbers:
            # save a bit of time by skipping numbers that are out of range
            if winning_number < min_num:
                continue
            elif winning_number > max_num:
                break
            if winning_number in numbers:
                matches += 1
        card_match_dictionary[card_id] = matches
        card_count_dictionary[card_id] = 1
    # second pass, update total number of copies for each card
    for card_id in card_match_dictionary:
        # for each card, add 'k' copies to the next 'j' cards
        # where k is the number of copies of the current card
        # where j is the number of matches on the current card
        for j in range(1, card_match_dictionary[card_id] + 1):
            card_count_dictionary[card_id + j] += card_count_dictionary[card_id]
    # last pass, calculate total cards processed
    total_cards_processed = 0
    for card_id in card_count_dictionary:
        total_cards_processed += card_count_dictionary[card_id]
    print(total_cards_processed)

if __name__ == "__main__":
    puzzle7()
    puzzle8()