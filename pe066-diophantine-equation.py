from time import time
import math

def incomplete():

    lim = 1000

    s = [i*i for i in range(math.ceil(lim**0.5+1))]
    D = [i for i in range(1001) if i not in s]

    x_max = 0
    
    for d in D:

        x = 2
        
        while True:

            y = math.sqrt((x*x-1)/d)
            if math.floor(y) == y:  break
            else: x+=1
        print(x,d,y,x_max)
        if x > x_max: x_max = x
        
    return x_max

if __name__=="__main__":
    print(compute())
