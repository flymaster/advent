def getInput():
    f = open("advent/2021/input/6.txt", "r")
    data = f.read()
    return [int(x) for x in data.split(',')]
    
data = getInput()

days = [0,0,0,0,0,0,0,0,0]

for d in data:
    days[d] = days[d] + 1
print(days)

d=0
while d < 256:
    p = days.pop(0)
    days[6] = days[6] + p
    days.append(p)
    d = d+1
    
tot = 0

for d in days:
    tot = tot + d

print(tot)