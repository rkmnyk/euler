def factorSum(n):

    fSum=1
    x=2
    while(x*x<n):
        if(n % x ==0):
            fSum+=x
            fSum+=int(n/x)
        x+=1
    if(x*x==n):
        fSum+=x
    return fSum

def compute():
    answer = 0
    target = 10000
    i=0

    while(i<target):

        a = factorSum(i)
        if(a>i):
            b = factorSum(a)

            if((b==i)and(b!=a)):
                answer+=i+a
        i+=1

    return answer

if __name__== "__main__":
    print(compute())
