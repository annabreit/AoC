import numpy as np
import scipy
from scipy import ndimage

test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

input_day_10 = """6744638455
3135745418
4754123271
4224257161
8167186546
2268577674
7177768175
2662255275
4655343376
7852526168"""

NINE_GRID = np.ones((10, 10)) * 9
FILTER = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

if __name__ == '__main__':
    lines = input_day_10.split("\n")
    grid = np.array([[int(x) for x in line[::1]] for line in lines])

    steps = 2000

    flashes_in_round = []

    for i in range(steps):
        # increase 1
        grid += 1
        # check if
        current_is_flashing = np.zeros((10, 10), dtype=bool)
        new_is_flashing = np.ones((10, 10), dtype=bool)

        while (new_is_flashing).any():
            #where are we over 9?
            new_is_flashing = grid > 9
            diff = np.logical_xor(new_is_flashing, current_is_flashing)
            new_is_flashing = np.logical_and(new_is_flashing, diff)
            current_is_flashing += new_is_flashing
            #increase neighbours
            is_increasing = ndimage.convolve(new_is_flashing.astype(int), weights=FILTER, mode='constant', cval=0)
            grid += is_increasing

        grid[current_is_flashing] = 0
        flashes_in_round.append(current_is_flashing.sum())
        if current_is_flashing.sum() == 100:
            print(i+1)
    print(flashes_in_round)
    print(sum(flashes_in_round))

