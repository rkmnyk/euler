import numpy as np

class tools:

    # binary gcd
    @staticmethod
    def gcd(u, v):

        k = 0
        while True:
            if u == v:
                break
            if u == 0:
                break
            if v == 0:
                break

            if u % 2 == 0:
                if v % 2 == 0:
                    k += 1
                    u //= 2
                    v //= 2
                else:
                    u //= 2
            else:
                if v % 2 == 0:
                    v //= 2
                elif u >= v:
                    u = (u - v) // 2
                else:
                    v = (v - u) // 2
        return (2 ** k) * v

    #sieve of eratosthenes
    @staticmethod
    def prime_sieve(n):
        s = np.ones(n + 1)
        s[0] = 0
        s[1] = 0
        i = 2
        while (i * i < n):
            k = i * i
            while (k <= n):
                if (s[k] == 1):
                    s[k] = 0
                k += i
            i += 1
        return s