import numpy as np
test_intput = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def oxygen_generator_rate(lines):
    line_indices = list(range(len(lines)))
    i = -1
    while len(line_indices)>1:
        i += 1
        col = [lines[x][i] for x in line_indices]
        most_common = str(int(col.count('0')<=col.count('1')))
        line_indices = [inx for inx in line_indices if lines[inx][i]==most_common]
    print(lines[line_indices[0]])
    return int(lines[line_indices[0]],2)



def co2_scrubber_rate(lines):
    indices = list(range(len(lines)))
    i = -1
    while len(indices)>1:
        i += 1
        col = [lines[x][i] for x in indices]
        most_common = str(int(col.count('0')>col.count('1')))
        indices = [inx for inx in indices if lines[inx][i]==most_common]
    print(lines[indices[0]])
    return int(lines[indices[0]],2)



def get_gamma_rate(lines):
    bits = []
    for i in range(len(lines[0])):
        col = [x[i] for x in lines]
        bits.append(str(int(col.count('0')<col.count('1'))))
    print(bits)
    return int("".join(bits),2)

def get_epsilon_rate(lines):
    bits = []
    for i in range(len(lines[0])):
        col = [x[i] for x in lines]
        bits.append(str(int(col.count('0')>col.count('1'))))
    print(bits)
    return int("".join(bits),2)



if __name__ == '__main__':
    #lines = [x[::1] for x in test_intput.split("\n")]
    with open("input3.txt", "r") as f:
        lines = [x[::1] for x in f.read().split("\n")]
    gamma = get_gamma_rate(lines)
    epsilon = get_epsilon_rate(lines)

    print(gamma, epsilon)
    print(gamma*epsilon)

    oxy = oxygen_generator_rate(lines)
    co2 = co2_scrubber_rate(lines)
    print(oxy, co2)
    print(oxy*co2)