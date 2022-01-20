def getInput():
    f = open("advent/2021/input/6.txt", "r")
    data = f.read()
    return [int(x) for x in data.split(',')]
    
data = getInput()

fish = []

day = []
total = 0

for d in data:
    fish = []
    fish.append([d])
    for n in range(256):
        for f in fish[n]:
            if f == 0:
                nextDay.append(8)
                f = 7
            f = f - 1
            nextDay.append(f)
    
        fish.append(nextDay)
        if n > 1:
            fish[n] = 0

        
print(len(fish[256]))

