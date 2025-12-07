# ******************************************************************************
# benchmarks:
#   - part1 = 0.01794980000704527 seconds
#   - part2 = 0.3357061999849975 seconds
#
# ******************************************************************************

import time

# INPUT_FILE = "test_input.txt"
INPUT_FILE = "day4_input.txt"

grid: list = []
with open(file=INPUT_FILE, mode="r", encoding="utf-8") as tf:
    for line in tf.read().split("\n"):
        tmp = []
        for char in line:
            tmp.append(char)
        grid.append(tmp)

total_rolls: int = 0                                                            # part 2 only
time_stamp = time.perf_counter()
while True:                                                                     # part 2 only
    to_remove: int = 0
    neighbors: int = 0
    to_be_removed: list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                neighbors = 0
                # check top left
                if (i > 0) and (j > 0) and (grid[i-1][j-1] == "@"):
                    neighbors += 1
                # check top
                if (i > 0) and (grid[i-1][j] == "@"):
                    neighbors += 1
                # check top right
                if (i > 0) and (j < len(grid[i])-1)  and (grid[i-1][j+1] == "@"):
                    neighbors += 1
                # check left
                if (j > 0)  and (grid[i][j-1] == "@"):
                    neighbors += 1
                # check right
                if (j < len(grid[i])-1)  and (grid[i][j+1] == "@"):
                    neighbors += 1
                # check bot left
                if (i < len(grid)-1) and (j > 0) and (grid[i+1][j-1] == "@"):
                    neighbors += 1
                # check bot
                if (i < len(grid)-1) and (grid[i+1][j] == "@"):
                    neighbors += 1
                # check bot right
                if (i < len(grid)-1) and (j < len(grid[i])-1)  and (grid[i+1][j+1] == "@"):
                    neighbors += 1
                
                if neighbors < 4:
                    to_remove += 1
                    to_be_removed.append((i, j))                                # part 2 only
    if to_remove == 0:                                                          # part 2 only
        break                                                                   # part 2 only
    else:                                                                       # part 2 only
        # remove rolls, update the grid                                         # part 2 only
        total_rolls += to_remove                                                # part 2 only
        for loc in to_be_removed:                                               # part 2 only
            grid[loc[0]][loc[1]] = "X"                                          # part 2 only

print(f"{time.perf_counter() - time_stamp}")
# print(f"ROLLS = {to_remove}")
print(f"ROLLS = {total_rolls}")                                                 # part 2 only
# for row in grid:
#     print(row)