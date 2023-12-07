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

def solve(seeds, maps):
    intervals = []
    for i in range(0, len(seeds), 2):
        intervals.append((seeds[i], seeds[i] + seeds[i+1] - 1))

    
    unmapped = intervals.copy()

    for map in range(len(maps)):
        mapped_intervals = []

        for l in range(len(maps[map])):

            unmapped_len = len(unmapped)

            for u in range(unmapped_len):
                inf = maps[map][l][1]
                sup = inf + maps[map][l][2]

                dest_inf = maps[map][l][0]
                dest_sup = dest_inf + maps[map][l][2]

                a = unmapped[0][0]
                b = unmapped[0][1]

                unmapped.pop(0)

                # print(f'inf {inf}, sup {sup}, a {a}, b {b}')

                if a >= inf and b < sup:
                    # print(f'interval {(a,b)} entirely included in {(inf, sup)}')
                    mapped_intervals.append((a - inf + dest_inf, b - inf + dest_inf))

                elif a < inf and b >= sup:
                    # print(f'interval {(a,b)} entirely around {(inf, sup)}')
                    unmapped.append((a, inf-1))
                    mapped_intervals.append((dest_inf, dest_sup-1))
                    unmapped.append((sup, b))

                elif a < inf and b < sup and b >= inf:
                    # print(f'interval {(a,b)} partially included (right side) in {(inf, sup)}')
                    unmapped.append((a, inf-1))
                    mapped_intervals.append((dest_inf, b - inf + dest_inf))
                    
                elif a >= inf  and a < sup and b >= sup:
                    # print(f'interval {(a,b)} partially included (left side) in {(inf, sup)}')
                    mapped_intervals.append((a - inf + dest_inf, dest_sup-1))
                    unmapped.append((sup, b))

                else:
                    # print(f'interval {(a,b)} not in {(inf, sup)}')
                    unmapped.append((a, b))
        
        mapped_intervals += unmapped
        
        unmapped = mapped_intervals.copy()
    
    return mapped_intervals


seeds, maps = parseFile('05/input')

intervals = solve(seeds, maps)
print('minimum: ', min(intervals)[0])
