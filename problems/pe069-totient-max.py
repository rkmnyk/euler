from math_tools import tools
import numpy as np

def compute(r = 1000000):


    sieve = tools.prime_sieve(r)
    phi = np.zeros(r)
    primes = [i for i,c in enumerate(sieve) if c == 1]
    maxx = (0, 0)

    update = lambda m, x, p = phi: m if x/phi[x] < m[1] else (x, x/phi[x])

    for p in primes:
        phi[p] = p - 1
        maxx = update(maxx, p)

        xk = p ** 2
        xk1 = p
        # all powers of the prime
        while xk < r:
            phi[xk] = xk1 * (p - 1)
            maxx = update(maxx, xk)
            xk1 = xk
            xk *= p

    for m in range(2, r):

       # print(m, phi)

        for p in primes:
            x = p * m
            if x >= r:
                break
            phi[x] = (p - 1) * phi[m] if x % p == 0 else phi[x] # == 0 else phi[x]
            maxx = update(maxx, x)

    print(phi)
    return maxx


def compute2(r = 1000000):

    sieve = tools.prime_sieve(r)
    phi = {}
    maxx = (0, 0)

    primes = []

    for n in range(2, r):

        if sieve[n] == 1:
            primes.append(n)
            phi[n] = n - 1
        else:
            s = n
            for p in primes:
                if n % p == 0:
                    s *= (1 - 1/p)
            phi[n] = s
        maxx = maxx if n/phi[n] < maxx[1] else (n, n/phi[n])
    """
    keys = [key for key in phi]
    sorted(keys)
    for key in keys:
        print(phi[key])
        """
    return maxx


if __name__=="__main__":

    from time import time
    tic = time()
    print(compute(20), time() - tic)
    print(compute2(20))


""""""
