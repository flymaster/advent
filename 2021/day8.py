def getInput():
    f = open("advent/2021/input/8.txt", "r")
    data = f.read()
    data = data.split('\n')
    return data

def isInteresting(val):
    i = len(val)
    if i == 7:
        return True
    if i == 2:
        return True
    if i == 3:
        return True
    if i == 4:
        return True
    return False
    
def findOne(line):
    for x in line:
        if len(x) == 2:
            return x
    return ""

def findSeven(line):
    for x in line:
        if len(x) == 3:
            return x
    return ""

def findEight(line):
    for x in line:
        if len(x) == 7:
            return x
    return ""

def findFour(line):
    for x in line:
        if len(x) == 4:
            return x
    return ""

def findThree(one, line):
    for x in line:
        if len(x) == 5:
            if one[0] in x:
                if one[1] in x:
                    return x
    return ""
    
def findNine(three, line):
    for x in line:
        if len(x) == 6:
            if three[0] in x:
                if three[1] in x:
                    if three[2] in x:
                        if three[3] in x:
                            if three[4] in x:
                                return x
    return ""
    
def findZero(one, nine, line):
    for x in line:
        if len(x) == 6:
            if x != nine:
                if one[0] in x:
                    if one[1] in x:
                        return x
    return ""
    
def findSix(zero, nine, line):
    for x in line:
        if len(x) == 6:
            if x != nine:
                if x!= zero:
                    return x
    return ""
    
def findFive(six, line):
    for x in line:
        if len(x) == 5:
            isFive = True
            for y in x:
                if y not in six:
                    isFive = False
            if isFive:
                return x
                
    return ""
    
def findTwo(five, three, line):
    for x in line:
        if len(x) == 5:
            if x != five:
                if x != three:
                    return x
    return ""
        
    
def parseLine(line):
    line = line.split(' ')
    array = ["", "", "", "", "", "", "", "", "", ""]
    
    array[1] = findOne(line)
    array[4] = findFour(line) 
    array[7] = findSeven(line)
    array[8] = findEight(line)
    
    array[3] = findThree(array[1], line)
    array[9] = findNine(array[3], line)
    array[0] = findZero(array[1], array[9], line)
    array[6] = findSix(array[0], array[9], line)
    
    array[5] = findFive(array[6], line)
    array[2] = findTwo(array[5], array[3], line)
    return array
    
d = getInput()

mult = [1000, 100, 10, 1]
tot = 0
for x in d:
    sample = x.split(' | ')[0]
    out = x.split(' | ')[1]
    out = out.split(' ')
    mapping = parseLine(sample)
    this = 0
    for o in range(4):
        for x in range(10):
            if len(out[o]) == len(mapping[x]):
                if sorted(out[o]) == sorted(mapping[x]):
                    this  = this + x*mult[o]
    tot = tot + this
print(tot)
            
