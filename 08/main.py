import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    moves = data[0]
    elements = {}

    for i in range(2, len(data)):
        key = data[i][:3]
        t = tuple([data[i][7:10], data[i][12:15]])
        elements[key] = t

    return moves, elements

def solve1(moves, elements):
    moves_count = 0
    current_location = 'AAA'
    while current_location != 'ZZZ':
        next_move = moves[moves_count % len(moves)]
        if next_move == 'L':
            current_location = elements[current_location][0]
        else:
            current_location = elements[current_location][1]
        moves_count += 1
        print(current_location)
    
    return moves_count


def pgcd(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a

def ppcm(a, b):
    return (a * b) // pgcd(a, b)


def solve2(moves, elements):
    min_moves = []
    current_moves = []

    for e in elements:
        if e[2] == 'A':
            current_moves.append(e)

    for i in range(len(current_moves)):
     
        moves_count = 0
        end_reached = False

        while end_reached == False:
            next_move = moves[moves_count % len(moves)]

            if next_move == 'L':
                current_moves[i] = elements[current_moves[i]][0]
                if current_moves[i][2] == 'Z':
                    end_reached = True

            else:
                current_moves[i] = elements[current_moves[i]][1]
                if current_moves[i][2] == 'Z':
                    end_reached = True
            
            moves_count += 1
        
        min_moves.append(moves_count)

    current_ppcm = min_moves[0]
    for i in range(len(min_moves)):
        current_ppcm = ppcm(current_ppcm, min_moves[i])
    
    return current_ppcm

moves, elements = parseFile('08/input')

print(solve2(moves, elements))
