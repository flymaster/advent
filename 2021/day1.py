def getInput():
    f = open("advent/2021/input/1a.txt", "r")
    data = f.read()
    dataArray = data.split('\n')
    return dataArray
    
day1in = getInput()

def a():
    increase = 0
    prev = None
    for n in day1in:
        n = int(n)
        if prev == None:
            prev = n
            continue
        if n > prev:
            increase = increase + 1
        prev = n
    return increase
    
def get3(data, x):
    return int(data[x]) + int(data[x+1]) + int(data[x+2])
def b():
    increase = 0
    curr = 0
    prev = None
    for curr in range(len(day1in)-2):
        s = get3(day1in, curr)
        if prev == None:
            prev = s
            continue
        if s > prev:
            increase = increase + 1
        prev = s
    return increase
        
print(b())
    