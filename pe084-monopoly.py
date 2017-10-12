import random
import numpy as np

# community chest and chance cards
class cards:

    cc = []
    ch = []
    a = 15
    b = 15

    def __init__(self):

        # init and shuffle cards
        self.cc = [lambda x: x] * 16
        self.ch = [lambda x: x] * 16

        self.cc[0] = lambda x: 0
        self.cc[1] = lambda x: 10

        self.ch[0] = lambda x: 0
        self.ch[1] = lambda x: 5
        self.ch[2] = lambda x: 10
        self.ch[3] = lambda x: 11
        self.ch[4] = lambda x: 24
        self.ch[5] = lambda p: 15 if p == 7 else 25 if p == 22 else 5  # railway
        self.ch[6] = lambda p: 15 if p == 7 else 25 if p == 22 else 5  # railway
        self.ch[7] = lambda p: 28 if p == 22 else 12  # utility
        self.ch[8] = lambda x: x - 3
        self.ch[9] = lambda x: 39

        random.shuffle(self.ch)
        random.shuffle(self.cc)

    def chance(self, p):
        if self.a == 15:
            self.a = 0
        else:
            self.a += 1
        return self.ch[self.a](p)

    def chest(self, p):
        if self.b == 15:
            self.b = 0
        else:
            self.b += 1
        return self.cc[self.b](p)


# some experimenting showed the answer to converge at 200k rolls
# n = number of rolls
# s = number of sides on the dice
def compute(n = 200000, s = 4):

    c = cards()

    board = [lambda p: p] * 40
    board[30] = lambda p: 10
    board[2] = lambda p: c.chest(p)
    board[7] = lambda p: c.chance(p)
    board[17] = lambda p: c.chest(p)
    board[22] = lambda p: c.chance(p)
    board[33] = lambda p: c.chest(p)
    board[36] = lambda p: c.chance(p)

    pos = 0
    doubles = 0
    counts = np.zeros(40)

    roll = lambda: [np.random.randint(1, s + 1) for i in range(2)]
    move = lambda p, b=board: b[p](p)
    evaluate = lambda x, d: x + 1 if d[0] == d[1] else 0

    for i in range(n):

        # roll dice and move around the board
        dice = roll()

        # keep track of doubles
        doubles = evaluate(doubles, dice)

        # go to jail
        if doubles == 3:
            pos = move(10)
            doubles = 0
        else:
            pos += dice[0] + dice[1]
            pos = pos if pos < 40 else pos - 40
            pos = move(pos)
        counts[pos] += 1

    return "".join([str(x).zfill(2) for x in (-counts).argsort()[:3]])

if __name__=="__main__":
    print(compute())
