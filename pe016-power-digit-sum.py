
def compute():

    base = 2
    exponent = 1000
    product = list(str(base))
    carry = ""
    x=2

    while(x<=exponent):
        for i in range(len(product)):
            s = product[len(product)-1-i]

            unit = (int(s)*base)
            if(len(carry)>0):
                unit+=int(carry)

            carry = str(unit)
            product[len(product)-1-i] = carry[len(carry)-1]
            carry = carry[:len(carry)-1]
            if((i==(len(product)-1)) and len(carry)>0):
                product.insert(0,carry)
                carry=""
        x+=1
    if(len(carry)>0):
        product.insert(0,carry)

    answer=0
    for i in range(len(product)):
        answer+=int(product[i])

    return answer

if __name__== "__main__":
    print(compute())
