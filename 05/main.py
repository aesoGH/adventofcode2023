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
    for i in range(len(map)):
        if item >= map[i][1] and item <= map[i][1] + map[i][2] - 1:

            return item - map[i][1] + map[i][0]
        
    return item

def reverseMapping(map: list, item: int) -> int:
    for i in range(len(map)):
        if item >= map[i][0] and item <= map[i][0] + map[i][2] - 1:

            return item - map[i][0] + map[i][1]
        
    return item


def solve1(seeds, maps):
    seeds_locations = []

    for s in seeds:
        current_item = s

        for i in range(len(maps)):
            current_item = findMapping(maps[i], current_item)
        
        seeds_locations.append(current_item)
    
    return seeds_locations

def solve2(seeds, maps):
    seeds_r_locations_min = findMapping(maps[0], seeds[0])
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i+1]):
            current_item = seeds[i] + j

            for k in range(len(maps)):
                current_item = findMapping(maps[k], current_item)

            if current_item < seeds_r_locations_min:
                print('nouveau min trouvé: ', current_item)
                seeds_r_locations_min = current_item

def reverse_solve2(seeds, maps):
    min_found = False
    value_to_find = 0

    while not min_found:

        print(value_to_find)

        current_item = value_to_find
        for k in range(len(maps)-1, 0, -1):
            current_item = reverseMapping(maps[k], current_item)

        for i in range(0, len(seeds), 2):
            if ( current_item >= seeds[i] ) and ( current_item < seeds[i] + seeds[i+1] ):
                min_found = True
                print('minimum found!')
                return value_to_find
        
        value_to_find += 1
            
    return

seeds, maps = parseFile('input')

print(reverse_solve2(seeds, maps))
