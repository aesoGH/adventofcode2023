import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    parsed_data = [(data[i].split()[0], data[i].split()[1]) for i in range(len(data))]
    
    return parsed_data

data = parseFile('07/input')

score_to_hand_type = {6: 'Five of a kind', 5: 'Four of a kind', 4: 'Full house', 3: 'Three of a kind', 2:'Two pair', 1:'One pair', 0:'High card'}
card_to_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}

def solve1(data):
    hands_scores = []
    for hand in range(len(data)):

        hand_hist = {}

        for card in data[hand][0]:
            if card not in hand_hist:
                hand_hist[card] = 1
            else:
                hand_hist[card] += 1

        
        l = len(hand_hist)

        if l == 1:
            score = 6
        elif l == 2:
            if 4 in hand_hist.values():
                score = 5
            else:
                score = 4
        elif l == 3:
            if 3 in hand_hist.values():
                score = 3
            else:
                score = 2
        elif l == 4:
            score = 1
        else:
            score = 0
            
    
        cards_values = tuple([card_to_value[c] for c in data[hand][0]])

        hands_scores.append(((score, cards_values), int(data[hand][1])))

    hands_scores.sort(key=lambda x: x[0])

    print(hands_scores)

    total_score = 0
    for h in range(len(hands_scores)):
        total_score += (h+1) * hands_scores[h][1]
    
    return total_score

score = solve1(data)
print(score)
