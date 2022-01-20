def getInput():
    f = open("advent/2021/input/7.txt", "r")
    data = f.read()
    return [int(x) for x in data.split(',')]
    
d = getInput()

sums = []

for x in range(min(d), max(d)+1):
    tot = 0
    for i in d:
        dist = abs(1-x)
        tot = tot + ((1+abs(i-x))*(abs(i-x)/2.0))
    sums.append(tot)
    
m = min(sums)
print(m)
    
for x in range(len(sums)):
    if sums[x] == m:
        print(x)