
def primeFactors(n):
    factors = [0]*(n+1)
    i=2
    while(i*i<=n):
        if(factors[i]==0):
            k=i*i
            while(k<=n):
                if(factors[k]==0):
                    factors[k]=i
                k+=i
        i+=1
    return factors

def compute():
    limit = 20
    factors = primeFactors(limit)
    multiples = [0]*(limit)

    for x in range(limit,1,-1):

        primes = [];
        index=x
        while(factors[index]>0):
            primes+=[factors[index]]
            index = ((index)/factors[index])
            index=int(index)
        primes+=[index]

        numFactors = [0]*(limit)
        for y in range(len(primes)):
            numFactors[primes[y]-1]+=1
        for y in range(len(multiples)):
            if(numFactors[y]>multiples[y]):
                multiples[y]=numFactors[y]

    answer = 1
    for x in range(len(multiples)):
        if(multiples[x]!=0):
            for y in range(multiples[x]):
                answer = answer*(x+1)

    return answer

if __name__=="__main__":
    print(compute())