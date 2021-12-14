import numpy as np

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class Board():
    def __init__(self, numbers_string):
        self.numbers = np.array([[int(y) for y in x.split(" ") if y != ""] for x in numbers_string.split("\n")])
        self.unchecked = np.ones(self.numbers.shape)
        self.size = self.numbers.shape[0]

    def check_number(self, number):
        x, y = np.where(self.numbers == number)
        self.unchecked[x, y] = 0

    def check_winning(self):
        for i in range(self.size):
            if self.unchecked[:, i].sum() == 0:
                return True
            if self.unchecked[i, :].sum() == 0:
                return True
        return False

    def get_sum_of_remaining(self):
        return np.multiply(self.numbers,self.unchecked).sum()


def play(drawn_numbers, boards):
    for n in drawn_numbers:
        for b in boards:
            b.check_number(n)
            if b.check_winning():
                return b , n

def play_and_survive(drawn_numbers, boards):
    winning_boards = []
    for n in drawn_numbers:
        for b in boards:
            b.check_number(n)
            if b.check_winning():
                winning_boards.append(b)
                if len(set(winning_boards))==len(boards):
                    return  winning_boards[-1],n


if __name__ == '__main__':
    #all_input = test_input.split("\n\n")
    with open("input4.txt", "r") as f:
        all_input = f.read().split("\n\n")
    drawn_numbers = [int(x) for x in all_input[0].split(",")]
    boards = [Board(x) for x in all_input[1:]]
    b, n = play(drawn_numbers, boards)
    print(b.numbers)
    print(n)
    print(b.get_sum_of_remaining())
    print(b.get_sum_of_remaining()*n)

    drawn_numbers = [int(x) for x in all_input[0].split(",")]
    boards = [Board(x) for x in all_input[1:]]
    b, n = play_and_survive(drawn_numbers, boards)
    print(b.numbers)
    print(n)
    print(b.get_sum_of_remaining())
    print(b.get_sum_of_remaining()*n)




