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
    target = 28123
    abnums = []
    i=12

    while(i<target):

        a = factorSum(i)
        if(a>i):
            abnums.append(i)
        i+=1

    absums = [0]*target
    for j in range(len(abnums)):
        for k in range(j,len(abnums)):
            s = abnums[k]+abnums[j]
            if(s<target):
                absums[s]=1

    for x in range(target):
        if(absums[x]==0):
            answer+=x

    return answer

if __name__== "__main__":
    print(compute())