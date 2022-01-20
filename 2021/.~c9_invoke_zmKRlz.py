def getInput():
    f = open("advent/2021/input/6.txt", "r")
    data = f.read()
    return [int(x) for x in data.split(',')]
    
data = getInput()

fish = []

day = []
for d in data:
    day.append(d)

fish.append(day)
    
for d in range(256):
    nextDay = []
    for f in fish[d]:
        if f == 0:
            nextDay.append(8)
            f = 7
        f = f - 1
        nextDay.append(f)

    fish.append(nextDay)
    if d > 1:
        fish[d] = 0

        
print(len(fish[256]))

