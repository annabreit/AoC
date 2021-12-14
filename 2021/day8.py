test_input = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""


if __name__ == '__main__':
    #all_digits = [[set(digit) for digit in line.split(" | ")[0].split(" ")] for line in test_input.split("\n") if line != ""]
    #all_signals = [[set(digit) for digit in line.split(" | ")[1].split(" ")] for line in test_input.split("\n") if line != ""]

    with open("input8.txt", "r") as f:
        lines = f.read().split("\n")
        all_digits = [[set(digit) for digit in line.split(" | ")[0].split(" ")] for line in lines if line != ""]
        all_signals = [[set(digit) for digit in line.split(" | ")[1].split(" ")] for line in lines if line != ""]

    output = []

    for digits, signal in zip (all_digits, all_signals):
        ONE = [d for d in digits if (len(d) == 2)][0]
        FOUR = [d for d in digits if (len(d) == 4)][0]
        SEVEN = [d for d in digits if (len(d) == 3)][0]
        EIGHT = [d for d in digits if (len(d) == 7)][0]

        SIX = [d for d in digits if (len(d) == 6) and len(d.intersection(ONE)) == 1][0]
        THREE = [d for d in digits if (len(d) == 5) and len(d.intersection(ONE)) == 2][0]

        NINE = [d for d in digits if (len(d) == 6) and len(d.intersection(THREE)) == 5][0]
        ZERO = [d for d in digits if (len(d) == 6) and len(d.intersection(THREE)) == 4 and len(d.intersection(SIX)) == 5][0]

        FIVE = [d for d in digits if (len(d) == 5) and len(d.intersection(SIX)) == 5][0]
        TWO = [d for d in digits if (len(d) == 5) and len(d.intersection(FIVE)) != 5 and len(d.intersection(THREE)) != 5][0]

        digits = {
            0: ZERO,
            1: ONE,
            2: TWO,
            3: THREE,
            4: FOUR,
            5: FIVE,
            6: SIX,
            7: SEVEN,
            8: EIGHT,
            9: NINE
        }

        num = []
        for s in signal:
            num.append([str(k) for k,v in digits.items() if v==set(s)][0])
        output.append(int("".join(num)))

    print(output)
    print(sum(output))