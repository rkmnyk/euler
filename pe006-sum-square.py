def sumSquare(n):
    ans = 0
    for x in range(1,n+1):
        ans+=(x*x)
    return ans

def squareSum(n):
    ans = 0
    for x in range(1,n+1):
        ans+=x
    ans*=ans
    return ans

def compute():
    n = 100
    return squareSum(n)-sumSquare(n)

if __name__== "__main__":
    print(compute())
