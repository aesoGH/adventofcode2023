def parseFile(inputfile):
    with open(inputfile, 'r') as f:
        data = f.read().splitlines()
    
    sequences = [[int(j) for j in data[i].split()] for i in range(len(data))]

    return sequences

def solve1(sequences):
    all_values = []
    for seq in range(len(sequences)):
        last_values = [sequences[seq][-1]]
        init_seq = sequences[seq].copy()
        
        seq_end = False

        while not seq_end:
            diff_seq = []
            seq_end = True
            for i in range(1, len(init_seq)):
                diff = init_seq[i] - init_seq[i-1]
                diff_seq.append(diff)
                if diff != 0:
                    seq_end = False

            last_values.append(diff_seq[-1])
            init_seq = diff_seq

        all_values.append(sum(last_values))
    
    return sum(all_values)


def solve2(sequences):
    all_values = []
    for seq in range(len(sequences)):
        first_values = [sequences[seq][0]]
        init_seq = sequences[seq].copy()
        
        seq_end = False

        while not seq_end:
            diff_seq = []
            seq_end = True
            for i in range(1, len(init_seq)):
                diff = init_seq[i] - init_seq[i-1]
                diff_seq.append(diff)
                if diff != 0:
                    seq_end = False

            first_values.append(diff_seq[0])
            init_seq = diff_seq

        s = 0
        for v in range(len(first_values)-2, -1, -1):
            s = first_values[v] - s
        
        all_values.append(s)
    
    return sum(all_values)

sequences = parseFile('09/input')

print(solve2(sequences))
