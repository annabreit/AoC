import numpy as np

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def add_hor_vert_lines(grid, coordinates):
    for c_pair in coordinates:
        if (c_pair[0][0] == c_pair[1][0]) or (c_pair[0][1] == c_pair[1][1]):
            sorted_y_indx = sorted([c_pair[0][0], c_pair[1][0]])
            sorted_x_indx = sorted([c_pair[0][1], c_pair[1][1]])
            y_range = list(range(sorted_y_indx[0], sorted_y_indx[1] + 1))
            x_range = list(range(sorted_x_indx[0], sorted_x_indx[1] + 1))
            grid[x_range, y_range] += 1
    return grid


def add_hor_vert_diag_lines(grid, coordinates):
    for c_pair in coordinates:
        if (c_pair[0][0] == c_pair[1][0]) or (c_pair[0][1] == c_pair[1][1]) \
                or (abs(c_pair[0][0] - c_pair[0][1]) == abs(c_pair[1][0] - c_pair[1][1])) \
                or (abs(c_pair[0][0] + c_pair[0][1]) == abs(c_pair[1][0] + c_pair[1][1])):
            rev_x = c_pair[0][0] > c_pair[1][0]
            rev_y = c_pair[0][1] > c_pair[1][1]
            sorted_y_indx = sorted([c_pair[0][0], c_pair[1][0]])
            sorted_x_indx = sorted([c_pair[0][1], c_pair[1][1]])
            y_range = list(range(sorted_y_indx[0], sorted_y_indx[1] + 1))
            x_range = list(range(sorted_x_indx[0], sorted_x_indx[1] + 1))
            if len(x_range) == len(y_range):
                x_range = x_range if not rev_x else reversed(x_range)
                y_range = y_range if not rev_y else reversed(y_range)
                for x, y in zip(x_range, y_range):
                    grid[x, y] += 1
            else:
                grid[x_range, y_range] += 1
    return grid


if __name__ == '__main__':
    #inputs = [x.split(" -> ") for x in test_input.split("\n")]
    with open("input5.txt", "r") as f:
        inputs = [x.split(" -> ") for x in f.read().split("\n")]
    coordinates = np.array([[[int(el.split(",")[0]), int(el.split(",")[1])] for el in l] for l in inputs])
    max_size = coordinates.max() + 1

    grid = np.zeros((max_size, max_size))
    grid = add_hor_vert_lines(grid, coordinates)
    print(len(np.where(grid > 1)[0]))

    grid = np.zeros((max_size, max_size))
    grid = add_hor_vert_diag_lines(grid, coordinates)
    print(len(np.where(grid > 1)[0]))

