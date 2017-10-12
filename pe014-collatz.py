
def compute():

    target=1000000
    maxCount=0

    for x in range(1,target+1):
        i=x
        count=1
        while(i!=1):
            if(i%2==0):
                i/=2
                count+=1
            elif(i%2!=0):
                i=3*i+1
                count+=1
        if(count>maxCount):
            maxCount = count
            answer = x

    return answer

if __name__== "__main__":
    print(compute())