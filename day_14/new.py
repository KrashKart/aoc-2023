import copy

def swap(grid, loc1, loc2):
    grid[loc1[1]][loc1[0]], grid[loc2[1]][loc2[0]] = grid[loc2[1]][loc2[0]], grid[loc1[1]][loc1[0]]

def spincycle(grid):
    # North
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == 'O':
                curr_row = row_idx - 1
                while (curr_row >= 0 and grid[curr_row][col_idx] == '.'):
                    curr_row += -1
                swap(grid, (col_idx, row_idx), (col_idx, curr_row+1))
    # West
    for col_idx in range(len(grid[0])):
        for row_idx in range(len(grid)):
            if grid[row_idx][col_idx] == 'O':
                curr_col = col_idx - 1
                while (curr_col >= 0 and grid[row_idx][curr_col] == '.'):
                    curr_col += -1
                swap(grid, (col_idx, row_idx), (curr_col+1, row_idx))
    # South
    for row_idx in range(len(grid)-1,-1,-1):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == 'O':
                curr_row = row_idx + 1
                while (curr_row < len(grid) and grid[curr_row][col_idx] == '.'):
                    curr_row += 1
                swap(grid, (col_idx, row_idx), (col_idx, curr_row-1))
    # East
    for col_idx in range(len(grid[0])-1,-1,-1):
        for row_idx in range(len(grid)):
            if grid[row_idx][col_idx] == 'O':
                curr_col = col_idx + 1
                while (curr_col < len(grid[0]) and grid[row_idx][curr_col] == '.'):
                    curr_col += 1
                swap(grid, (col_idx, row_idx), (curr_col-1, row_idx))    

# Part 1
f = open('day_14.txt', 'r')
grid = [list(row) for row in f.read().strip().split('\n')]
for row_idx in range(len(grid)):
    for col_idx in range(len(grid[0])):
        if grid[row_idx][col_idx] == 'O':
            curr_row = row_idx - 1
            while (curr_row >= 0 and grid[curr_row][col_idx] == '.'):
                curr_row += -1
            swap(grid, (col_idx, row_idx), (col_idx, curr_row+1))
total1 = sum([len(grid)-row_idx for row_idx in range(len(grid)) for col_idx in range(len(grid[0])) if grid[row_idx][col_idx] == 'O'])
print(total1)
# Part 2
f = open('day_14.txt', 'r')
grid = [list(row) for row in f.read().strip().split('\n')]
history = []
count = 0
while (grid not in history):
    history.append(copy.deepcopy(grid))
    spincycle(grid)
repeat_idx = history.index(grid)
final_grid = history[(1000000000-repeat_idx)%(len(history)-repeat_idx) + repeat_idx]
total2 = sum([len(final_grid)-row_idx for row_idx in range(len(final_grid)) for col_idx in range(len(final_grid[0])) if final_grid[row_idx][col_idx] == 'O'])
print(total2)