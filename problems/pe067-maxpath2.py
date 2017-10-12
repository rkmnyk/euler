from urllib.request import urlopen

def compute():
    url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
    txt = urlopen(url).read()
    strings = txt.decode().split('\n')
    data = [[int(x) for x in s.split(" ")] for s in strings[:-1]]
    maxima = data[-1]
    for d in reversed(data[:-1]):
        updated = [(d[i]+max(maxima[i], maxima[i+1])) for i in range(len(d))]
        maxima = updated
    return(maxima[0])

if __name__== "__main__":
    print(compute())