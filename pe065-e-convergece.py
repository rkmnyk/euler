from time import time

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def compute():

    k = 1
    c_frac = [2]

    #last value is 1, skip it
    for i in range(2,100):

        if i % 3 == 0:

            c_frac.append(2*k)
            k += 1
        else:
            c_frac.append(1)

    num = 1
    den = 1
    
    for val in reversed(c_frac):

        
        num = val*den + num
        num,den = den,num

    return sum_digits(den)
       
if __name__=="__main__":
    print(compute())
