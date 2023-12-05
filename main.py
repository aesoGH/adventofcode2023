import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    seeds = list(map(lambda x: int(x), re.findall(r'(\d+)', data[0])))

    maps = [[] for i in range(7)]
    #seeds/soil, soil/fertilizer, fertilizer/water, water/light, light/temperature, temperature/humidity, humidity/location

    category = 0
    l_index = 3

    while l_index < len(data):
        line = data[l_index]

        if line == '':
            category += 1
            l_index += 2
        
        else:
            maps[category].append(list(map(lambda x: int(x), re.findall(r'(\d+)', data[l_index]))))
            l_index += 1
    
    return seeds, maps


def findMapping(map: list, item: int) -> int:
    print(map)
    for i in range(len(map)):
        if item >= map[i][1] and item <= map[i][1] + map[i][2] - 1:

            return item - map[i][1] + map[i][0]
        
    return item


def solve1(seeds, maps):
    seeds_locations = []

    for s in seeds:
        current_item = s

        for i in range(len(maps)):
            current_item = findMapping(maps[i], current_item)
        
        seeds_locations.append(current_item)
    
    return seeds_locations
        
        

seeds, maps = parseFile('input')

print(min(solve1(seeds, maps)))