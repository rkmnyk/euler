def divisors(n):
    i=1
    count=0;
    while(i*i<=n):
        if(n%i==0 and i*i!=n):
            count+=2
        elif(i*i==n):
            count+=1
        i+=1
    return count

def compute():

    limit = 500
    prefix = 0
    i=1
    while True:
        prefix+=i
        div = divisors(prefix)
        if(div>limit):
            break
        i+=1
    return prefix

if __name__== "__main__":
    print(compute())
