def getInput():
    f = open("advent/2021/input/3.txt", "r")
    data = f.read()
    dataArray = data.split('\n')
    return dataArray
    
def binToInt(arr):
    i = 0
    s = len(arr)
    for b in arr:
        s = s-1
        i = i + int(b)*(2**s)
    return i
        

def valAt(arr, x, y):
    return int(arr[x][y])
    
def a():
    gamma = []
    epsilon = []
    
    i = getInput()
    for x in range(len(i[0])):
        gamma.append(0)
        epsilon.append(0)
        
    xx = len(i)
    yy = len(i[0])
    for x in range(xx):
        for y in range(yy):
            bit = valAt(i, x, y)
            if bit:
                gamma[y] = gamma[y] + 1
                
    for y in range(len(gamma)):
        if gamma[y] > len(i) - gamma[y]:
            gamma[y] = 1
            epsilon[y] = 0
        else:
            gamma[y] = 0
            epsilon[y] = 1
    
    gammaInt = binToInt(gamma)
    epsilonInt = binToInt(epsilon)
    
    print(gammaInt)
    print(epsilonInt)
    print(gammaInt * epsilonInt)
   
   
def mostCommon(arr, col):
    h = len(arr)
    total = 0
    for r in arr:
        i = int(r[col])
        total = total + i
    if total * 2 >= h:
        return 0
    return 1
    
def leastCommon(arr, col):
    mc = mostCommon(arr, col)
    if mc == 1:
        return 0
    return 1
    
def trim(arr, col, common):
    i = []
    h = len(arr)
    total = 0
    for r in arr:
        if int(r[col]) == common:
            i.append(r)
    return i
    
def b():
    i = getInput()
    y = getInput()
    w = len(i[0])
    val1 = 0
    val2 = 0

    for col in range(w):
        common = mostCommon(i, col)
        i = trim(i, col, common)
        if len(i) == 1:
            val1 = binToInt(i[0])
            break
    for col in range(w):
        common = leastCommon(y, col)
        y = trim(y, col, common)
        if len(y) == 1:
            val2 = binToInt(y[0])
            break
        
    return val1 * val2
    
print(b())