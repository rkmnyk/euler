
def compute():
    grid = []

    with open('input/pe_problem_011.csv') as data:
        for line in data:
            grid.append(line.strip().split(','))

    horizontal = 0
    vertical = 0
    diagonalLtoR = 0
    diagonalRtoL = 0
    l = 4               #length of chain
    w = len(grid[0])    #width of grid
    h = len(grid)       #height of grid


    #horizontal
    for x in range(h):
        for y in range(w-l+1):
            chain = 1
            for z in range(l):
                chain*=int(grid[x][y+z])
            if(chain>horizontal):
                horizontal=chain


    #vertical
    for x in range(w):
        for y in range(h-l+1):
            chain = 1
            for z in range(l):
                chain*=int(grid[y+z][x])
            if(chain>vertical):
                vertical=chain

    #diagonal left to right
    for x in range(h-l+1):
        for y in range(w-l+1):
            chain = 1
            for z in range(l):
                chain*=int(grid[x+z][y+z])
            if(chain>diagonalLtoR):
                diagonalLtoR=chain

    #diagonal right to left
    for x in range(h-l):

        for y in range(w-1,l-1,-1):
            chain = 1
            for z in range(l):
                chain*=int(grid[x+z][y-z])
            if(chain>diagonalRtoL):
                diagonalRtoL=chain


    return max(vertical,horizontal,diagonalLtoR,diagonalRtoL)

if __name__== "__main__":
    print(compute())
