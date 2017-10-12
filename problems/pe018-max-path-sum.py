
def compute():

    grid = []
    with open('input/pe_problem_018.csv') as data:
        for line in data:
            grid.append(line.strip().split(' '))

    for x in range(len(grid) - 2, 0, -1):
        for y in range(len(grid[x])):
           grid[x][y] = int(grid[x][y]) + max(int(grid[x+1][y+1]),int(grid[x+1][y]))

    return int(grid[0][0]) + max(grid[1])

if __name__== "__main__":
    print(compute())
