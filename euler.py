import os
from time import time
import re
import sys

def format_time(tic, toc):
    t = toc - tic

    if t > 1:
        return "{:.1f}s".format(t)
    else:
        return "{:.0f}ms".format(t*1000)

def main():
    absolutePath = "{}/problems".format(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(absolutePath)
    problems = [f for f in os.listdir(absolutePath) if 'pe' in f]
    available = [int(re.findall('\d+', p)[0]) for p in problems]
    if len(sys.argv) > 1:
        s = [int(n) for n in sys.argv[1:]]
    else:
        s = available

    for p in s:
        if p in available:

            name = problems[available.index(p)][:-3]
            n = 4 - len(name) // 8

            tabs = "".join(["\t" for m in range(n) ])
            try:
                mod = __import__(name)
                tic = time()

                r = getattr(mod, "compute")()
                toc = time()

                print("{}{}-->\t{} in {}".format(name, tabs,  r, format_time(tic, toc)))
            except AttributeError:
                print("{}{}--> does not implement compute".format(name, tabs))

        else:
            print("no such problem {}".format(p))

if __name__ == '__main__':
    main()