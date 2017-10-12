
def gcd(a,b):
    k=0
    while True:
        if(a==b):
            return int((2**k)*a)           
        if((a%2==0)and(b%2==0)):
            k+=1
            a/=2
            b/=2
        elif((a%2==0)and(b%2!=0)):
            a/=2
        elif((a%2!=0)and(b%2==0)):
            b/=2
        elif((a%2!=0)and(b%2!=0)):
            if(a>b):
                a=(a-b)/2
            elif(b>a):
                b=(b-a)/2

# brute force
def crunch(s):
    for a in range(1,s):
        for b in range(s,a,-1):
            c = math.sqrt(a*a + b*b)
            if(a+b+c==s):
                return int(a*b*c)
 

def compute():
    # a+b+c = 2m(m+n)d = s
    # find m and k=m+n
    # m (>1) is a divisor of s/2
    s = 1000
    s2 = s/2
    mlimit = (s2**0.5) - 1
    m=2
    while(m<mlimit):
        if(s2 % m==0):
            sm = s2 / m                 # sm = (m+n)*d
            while(sm % 2 == 0):         # remove all factors of 2
                sm /= 2
            if(m % 2 == 1):
                k=m+2
            else:
                k=m+1
            while(k<2*m and k<=sm):
                if((sm % k == 0) and (gcd(k,m) == 1)):
                    n=k-m
                    d=s2/(k*m)
                    a=d*(m*m-n*n)
                    b=2*d*m*n
                    c=d*(m*m+n*n)
                    return int(a*b*c)
                k+=2
        m+=1


if __name__== "__main__":
    print(compute())
