import re

def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    return data

def solve1(data):
    all_values = []
    for i in range(len(data)):
        numbers = re.findall(r'[0-9]', data[i])
        all_values.append(int(numbers[0] + numbers[-1]))
    
    return sum(all_values)


def solve2(data):
    all_values = []
    replacement_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for i in range(len(data)):
        line = data[i]

        split_line = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9))', line)
        for c in range(len(split_line)):
            split_line[c] = re.sub(r'one|two|three|four|five|six|seven|eight|nine', lambda x: replacement_dict[x.group()], split_line[c])

        first_n = split_line[0]
        last_n = split_line[-1]

        all_values.append(int(first_n + last_n))

    return sum(all_values)

data = parseFile('01/input')

print(solve2(data))
