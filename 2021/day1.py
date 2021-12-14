test_input = """199
200
208
210
200
207
240
269
260
263"""


def count_increasing(values: list, window_size=1):
    increases = 0
    for i, el in enumerate(values):
        if i >= window_size:
            increases += 1 if sum(values[i - window_size:i]) > sum(values[i - 1 - window_size: i-1]) else 0
    return increases


if __name__ == '__main__':
    #values = [int(x) for x in test_input.split("\n")]

    with open("input1.txt", "r") as f:
        values = [int(x) for x in f.read().split("\n")]
    increases = count_increasing(values)
    print(increases)
    increases = count_increasing(values, 3)
    print(increases)