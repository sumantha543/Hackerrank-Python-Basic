import math
import os
import random
import re
import sys

def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(n):
        for j in range(m):
            cell_value = grid[i][j]
            is_dominant = True

            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    if x == i and y == j:
                        continue
                    if grid[x][y] >= cell_value:
                        is_dominant = False
                        break

            if is_dominant:
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()