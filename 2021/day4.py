import attr

@attr.s
class Board:
    card = attr.ib(factory=list)
    call = attr.ib(factory=list)
    done = attr.ib(default=False)
    
    def Init(self, c):
        c = c.split('\n')
        for r in c:
            r = r.split(' ')
            row = []
            for num in r:
                if num == '':
                    continue
                row.append(int(num))
            self.card.append(row)
            
    def Call(self, c):
        if self.done:
            return -1
        self.call.append(c)
        if len(self.call) > 4:
            for y in range(5):
                for x in range(5):
                    if self.card[x][y] in self.call:
                        if x == 4:
                            self.done = True
                            return self.Score()
                    else:
                        break
            for x in range(5):
                for y in range(5):
                    if self.card[x][y] in self.call:
                        if y == 4:
                            self.done = True
                            return self.Score()
                    else:
                        break
        return -1
    
    def Score(self):
        sum = 0
        for x in range(5):
            for y in range(5):
                if self.card[x][y] not in self.call:
                    sum = sum + self.card[x][y]
        return sum * self.call[-1]
            
    

def getInput():
    f = open("advent/2021/input/4.txt", "r")
    data = f.read()
    dataArray = data.split('\n\n')
    return dataArray
 
def getCallsArray(i):
    i = i.split(',')
    c = []
    for j in i:
        c.append(int(j))
    return c

def a():
    data = getInput()
    
    calls = getCallsArray(data[0])
    boards = []
    
    for b in data[1:]:
        newBd = Board()
        newBd.Init(b)
        boards.append(newBd)
    for c in calls:
        for b in boards:
            score = b.Call(c)
            if score >= 0:
                print(score)

a()
    
    


