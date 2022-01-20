def getInput():
    f = open("advent/2021/input/2.txt", "r")
    data = f.read()
    dataArray = data.split('\n')
    return dataArray
    

def a():
    i = getInput()
    dep = 0
    dist = 0
    for n in i:
        d = n.split(" ")[0][0]
        m = int(n.split(" ")[1])
        
        if d == "f":
            dist = dist + m
        if d == "d":
            dep = dep + m
        if d == "u":
            dep = dep - m

    return dep * dist
    
def b():
    i = getInput()
    dep = 0
    dist = 0
    aim = 0
    for n in i:
        d = n.split(" ")[0][0]
        m = int(n.split(" ")[1])
        
        if d == "f":
            dist = dist + m
            dep = dep + (m * aim)
        if d == "d":
            aim = aim + m
        if d == "u":
            aim = aim - m

    return dep * dist
    
        
print(b())
    