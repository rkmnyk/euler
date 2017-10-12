
def isPalendrome(n):
    mstr = str(n)
    if mstr == mstr[::-1]:
        return 1
    else:
        return 0

def compute():
    for x in range(100):
        a = 999-x
        for y in range(100):
            b = a-y
            product = str(a*b)
            if isPalendrome(product) == 1:
                return product

if __name__=="__main__":
    print(compute())
