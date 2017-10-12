
def compute():

    numbers = []
    with open('input/pe_problem_013.csv') as data:
        for line in data:
            numbers.append(line.strip())
    cary=0
    x=1
    answer = ""
    carry = "0"
    while(x<=50):

        unit = 0
        for i in range(len(numbers)):
            s = numbers[i]
            unit += int(s[50-x])
        unit+=int(carry)
        carry = str(unit)
        answer = carry[len(carry)-1]+answer
        carry = carry[:len(carry)-1]
        x+=1
    return carry+answer

if __name__== "__main__":
    print(compute())