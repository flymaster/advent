def getInput():
    f = open("advent/2021/input/9.txt", "r")
    data = f.read()
    data = data.split('\n')
    return data
    
def lowPoint(y, x, d):
    h = int(d[y][x])
    if y > 0:
        n = int(d[y-1][x])
        if h >= n:
            return False
    if y + 1 < len(d):
        s = int(d[y+1][x])
        if h >= s:
            return False
    if x > 0:
        w = int(d[y][x-1])
        if h >= w:
            return False
    if x + 1 < len(d[0]):
        e = int(d[y][x+1])
        if h >= e:
            return False
    return True
        
def expandBasin(y, x, d, bnum, basins):
    pt = str(y) + "," + str(x)
    if not pt in basins:
        basins[pt] = bnum
        if y > 0:
            n = int(d[y-1][x])
            if n != 9:
                expandBasin(y-1, x, d, bnum, basins)
        if y + 1 < len(d):
            s = int(d[y+1][x])
            if s != 9:
                expandBasin(y+1, x, d, bnum, basins)
        if x > 0:
            w = int(d[y][x-1])
            if w != 9:
                expandBasin(y, x-1, d, bnum, basins)
        if x + 1 < len(d[0]):
            e = int(d[y][x+1])
            if e != 9:
                expandBasin(y, x+1, d, bnum, basins)

    
depth = getInput()
width = len(depth[0])
height = len(depth)

tot = 0

basins = {}

bnum = 0
for y in range(height):
    for x in range(width):
        if lowPoint(y, x, depth):
            expandBasin(y, x, depth, bnum, basins)
            bnum = bnum+1
            
sums = {}
for v in basins.values():
    t = sums.get(v, 0)
    sums[v] = t + 1
    
vals = sums.values()

vals = sorted(vals)

print(vals[-1] * vals[-2] * vals[-3])

            