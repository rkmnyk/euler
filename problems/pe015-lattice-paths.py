import math

def arrangePQ(p,q):
    result = math.factorial(p+q)
    result/= math.factorial(p)
    result/= math.factorial(q)
    return result

# slower approach
def gridTable(p,q):

    grid = [[0 for x in range(p)] for y in range(q)]
    grid[0][0] = 2
    for x in range(1,p):
        grid[x][0] = grid[x-1][0]+1
    for x in range(1,q):
        grid[0][x] = grid[0][x-1]+1

    for x in range(1,p):
        for y in range(1,q):
            grid[x][y]=grid[x][y-1]+grid[x-1][y]

    return grid[p-1][q-1]
   


def compute():
    return arrangePQ(50, 50)

if __name__== "__main__":
    print(compute())