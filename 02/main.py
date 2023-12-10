import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    records = [[] for l in range(len(data))]
    for game in range(len(data)):
        line = re.split(r';', data[game])
        for element in range(len(line)):
            records[game].append({})
            rec = re.findall(r'(\d+)+ +(red|green|blue)', line[element])
            for pair in range(len(rec)):
                records[game][element][rec[pair][1]] = int(rec[pair][0])
    
    return records


def solve1(records):
    reference = {'red': 12, 'green': 13, 'blue': 14}

    games_id_sum = 0

    for game in range(len(records)):
        valid_game = True
        for rec in range(len(records[game])):
            for pair in records[game][rec]:
                if records[game][rec][pair] > reference[pair]:
                    valid_game = False
        if valid_game:
            games_id_sum += game + 1
    
    return games_id_sum


def solve2(records):
    powers_sum = 0

    for game in range(len(records)):
        game_minimums = {'red': 0, 'green': 0, 'blue': 0}
        for rec in range(len(records[game])):
            for pair in records[game][rec]:
                current_min = game_minimums[pair]
                if records[game][rec][pair] > current_min:
                    game_minimums[pair] = records[game][rec][pair]

        prod = 1
        for m in game_minimums:
            prod *= game_minimums[m]
        
        powers_sum += prod
    
    return powers_sum


records = parseFile('02/input')

print(solve2(records))
