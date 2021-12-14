import numpy as np
import scipy
from scipy import ndimage
from scipy.ndimage import label

test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

if __name__ == '__main__':
    #lines = test_input.split("\n")
    with open("input9.txt", "r") as f:
        lines = f.read().split("\n")
    grid = np.array([[int(n) for n in line[::1]] for line in lines])

    f1 = np.array([[0, 1, 0],[1, 0, 1],[0, 1, 0]])
    is_lowpoint = grid < ndimage.minimum_filter(grid, footprint=f1, mode='constant', cval=100)
    low_points = grid * is_lowpoint
    num_els = is_lowpoint.sum()
    print(low_points.sum() + num_els)

    basins = grid <9
    labels, num_labels = label(basins, structure=[[0,1,0],[1,1,1],[0,1,0]])
    basin_sizes = []
    for i in range(1, num_labels+1):
        basin_sizes.append((labels == i).sum())
    print(np.prod(sorted(basin_sizes)[-3:]))