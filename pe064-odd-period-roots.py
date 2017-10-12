#stop when a_n = 2*a_0
#biggest issue is floating point precision.

from time import time
import math
from fractions import Fraction

def compute():

    counter = 0
    maxx = 0
    
    for n in range(537,538):
        
        a = math.sqrt(n)
        a_0 = math.floor(math.sqrt(n))
        a -= a_0
        
        if a != 0:
            log = []
            period = 1

            while True:

                a_n = float(a**-1)
                b_0 = math.floor(a_n)
                a = a_n - b_0
                log.append(b_0)
                
                if b_0 == 2*a_0: break
                else: period += 1

            if period % 2 != 0: counter+=1
            #print(n,a_0,log,period)
                    
    return counter


if __name__== "__main__":
    print(compute())

