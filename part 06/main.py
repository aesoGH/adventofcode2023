import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    times = list(map(lambda x: int(x), re.findall(r'(\d+)', data[0])))
    distances = list(map(lambda x: int(x), re.findall(r'(\d+)', data[1])))
    
    return times, distances

def parseFile2(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    times = re.findall(r'(\d+)', data[0])
    distances = re.findall(r'(\d+)', data[1])

    times = int(''.join(times))
    distances = int(''.join(distances))
    
    return times, distances

def solve1(times, distances):
    result = 1
    for time, distance in zip(times, distances):
        wins_count = 0
        for t in range(time):
            if t*(time-t) > distance:
                wins_count += 1
        result *= wins_count

    return result

def solve2(time, distance):
    wins_count = 0
    for t in range(time):
        if t*(time-t) > distance:
            wins_count += 1

    return wins_count


times, distances = parseFile2('part 06/input')

print(solve2(times, distances))