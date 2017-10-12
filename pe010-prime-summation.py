def sieveOfEratosthenes(n):
    sieve = [1]*(n+1)
    sieve[0]=0
    sieve[1]=0
    i=2
    while(i*i<n):
        k=i*i
        while(k<=n):
            if(sieve[k]==1):
                sieve[k]=0
            k+=i
        i+=1
    return sieve

def compute():
    n = 2000000
    sieve = sieveOfEratosthenes(n)
    answer = 0

    for i in range(n+1):
        if(sieve[i]==1):
            answer+=i

    return answer

if __name__== "__main__":
    print(compute())
