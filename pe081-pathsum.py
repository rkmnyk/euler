from urllib.request import urlopen
import numpy as np

def compute():
    url = 'https://projecteuler.net/project/resources/p081_matrix.txt'
    txt = urlopen(url).read()
    strings = txt.decode().split('\n')
    data = np.zeros((80,80))

    for i in range(80):
        data[i, :] = [int(x) for x in strings[i].split(",")] 

    min_path = np.zeros((80,80))
    min_path[0, 0] = data[0, 0]

    
    for i in range(1, 80):
        min_path[0, i] = data[0, i] + min_path[0, i - 1]
        min_path[i, 0] = data[i, 0] + min_path[i - 1, 0]


    for i in range(1, len(data)):   
        for j in range(1, len(data[i])):
            min_path[i,j] = data[i,j] + min(min_path[i - 1,j], min_path[i,j - 1])

            
    return int(min_path[-1,-1])

if __name__== "__main__":
    print(compute())