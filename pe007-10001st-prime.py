
def compute():
    n = 10001
    lim = n*50
    sieve = [1]*(lim)
    sieve[0]=0
    sieve[1]=0
    i=2
    while(i*i<lim):
        k=i*i
        while(k<lim):
            if(sieve[k]==1):
                sieve[k]=0
            k+=i
        i+=1
    count =0
    ans=0
    for x in range(len(sieve)):
        if(sieve[x]==1):
            count+=1
        if(count==n):
            ans=x
            break
    return x

if __name__== "__main__":
    print(compute())
