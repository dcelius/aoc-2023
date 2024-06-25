from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 13 Helper
def parse_hand_type(hand, is_jokers_wild=False):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
    if is_jokers_wild and 'J' in card_counts:
        for card in card_counts:
            if card != 'J':
                card_counts[card] += card_counts['J']
    # 5 of a kind
    if 5 in card_counts.values():
        return '7'
    # 4 of a kind
    elif 4 in card_counts.values():
        return '6'
    # Full House
    # 3 of a kind
    elif 3 in card_counts.values():
        # catch case where J is wild and there are 2 pairs
        if is_jokers_wild and 'J' in card_counts and len(card_counts) == 3:
            return '5'
        # the len check is to catch the case where J is wild but it would apply to multiple items at once
        elif len(card_counts) == 2 and 2 in card_counts.values():
            return '5'
        else:
            # 3 of a kind
            return '4'
    # 2 pair
    # KQJT4 
    elif 2 in card_counts.values():
        # only way to have 2 pair is if there are only 3 unique cards
        if (is_jokers_wild and 'J' in card_counts and len(card_counts) <= 4) or len(card_counts) == 3:
            return '3'
        else:
    # 1 pair
            return '2'
    # High Card
    return '1'

def score_hand(hand, is_jokers_wild=False):
    # A card's unique score value should be an integer with the first digit being the type
    # and each card being listed in order of appearance. Single digit cards should be padded with a 0 for comparison
    # Ex. KKKQQ = 51313131212
    # Types are as follows: 7 = 5ofakind, 6 = 4ofakind, 5 = fullhouse, 4 = 3ofakind, 3 = 2pair, 2 = pair, 1 = highcard
    face_card_values = {'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10'}
    if is_jokers_wild:
        face_card_values['J'] = '01'
    score = parse_hand_type(hand, is_jokers_wild)
    for card in hand:
        if card in face_card_values:
            score += face_card_values[card]
        else:
            score += '0' + card
    #print(score)
    return score

# Puzzle 13
@timing
def puzzle13():
    print('Puzzle 13')
    lines = read_file_lines('inputs/7.txt')
    bids_by_hand = {}
    hands_by_score = {}
    total_score = 0
    for line in lines:
        hand_data = line.split(' ')
        bids_by_hand[hand_data[0]] = int(hand_data[1])
    for hand in bids_by_hand:
        hands_by_score[score_hand(hand)] = hand
    ranking = sorted(hands_by_score)
    i = 1
    for score in ranking:
        print("hand:", hands_by_score[score], "score:", score, "bid:", bids_by_hand[hands_by_score[score]], "rank:", i, "of", len(ranking))
        total_score += bids_by_hand[hands_by_score[score]] * i
        i += 1
    print("Total Winnings:", total_score)

# Puzzle 14
@timing
def puzzle14():
    print('Puzzle 14')
    lines = read_file_lines('inputs/7.txt')
    bids_by_hand = {}
    hands_by_score = {}
    total_score = 0
    for line in lines:
        hand_data = line.split(' ')
        bids_by_hand[hand_data[0]] = int(hand_data[1])
    for hand in bids_by_hand:
        hands_by_score[score_hand(hand, True)] = hand
    ranking = sorted(hands_by_score)
    i = 1
    for score in ranking:
        print("hand:", hands_by_score[score], "score:", score, "bid:", bids_by_hand[hands_by_score[score]], "rank:", i, "of", len(ranking))
        total_score += bids_by_hand[hands_by_score[score]] * i
        i += 1
    print("Total Winnings:", total_score)


if __name__ == "__main__":
    puzzle13()
    puzzle14()
