import math

# using string math (like with any other language)
def stringMath(n):

    carry = ""
    x=n-1
    product = list(str(n))

    while(x>0):
        for i in range(len(product)):
            s = product[len(product)-1-i]
            
            unit = (int(s)*x)
            if(len(carry)>0):
                unit+=int(carry)
            
            carry = str(unit)
            product[len(product)-1-i] = carry[len(carry)-1]
            carry = carry[:len(carry)-1]
            if((i==len(product)-1) and len(carry)>0):
                product.insert(0,carry)
                carry=""
        x-=1

    s = product[0]
    product.remove(s)
    for i in range(len(s)):
        product.insert(0,s[len(s)-1-i])
        
    return product
    

def fact(n):
    return list(str(math.factorial(n)))

def digitSum(s):

    answer=0
    for i in range(0,len(s)):
        answer+=int(s[i])
    return answer

def listToString(s):

    answer=""
    for i in range(0,len(s)):
        answer+=s[i]
    return answer


def compute():
    n=100
    factF = fact(n)
    return digitSum(factF)

if __name__== "__main__":
    print(compute())