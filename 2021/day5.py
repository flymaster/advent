import attr

@attr.s
class Row:
    x1 = attr.ib()
    y1 = attr.ib()
    x2 = attr.ib()
    y2 = attr.ib()
    
    @classmethod
    def fromString(cls, s):
        
        pts = s.split(' -> ')
        
        pt1 = pts[0].split(',')
        x1 = int(pt1[0])
        y1 = int(pt1[1])
        
        pt2 = pts[1].split(',')
        x2 = int(pt2[0])
        y2 = int(pt2[1])
        
        return cls(x1, y1, x2, y2)
        
    def isHoriz(self):
        return self.y1 == self.y2
    
    def isVert(self):
        return self.x1 == self.x2
        
    def getPoints(self):
        pts = []
        if self.isVert():
            if self.y1 > self.y2:
                y3 = self.y1
                self.y1 = self.y2
                self.y2 = y3
            for y in range(self.y1, self.y2+1):
                pt = [self.x1, y]
                pts.append(pt)
                
        elif self.isHoriz():
            if self.x1 > self.x2:
                x3 = self.x1
                self.x1 = self.x2
                self.x2 = x3
            for x in range(self.x1, self.x2+1):
                pt = [x, self.y1]
                pts.append(pt)
        else:
            if self.x1 > self.x2:
                x3 = self.x1
                self.x1 = self.x2
                self.x2 = x3
                y3 = self.y1
                self.y1 = self.y2
                self.y2 = y3
            if self.y1 > self.y2:
                y = self.y1
                for x in range(self.x1, self.x2+1):
                    pt = [x, y]
                    y = y - 1
                    pts.append(pt)
            else:
                y = self.y1
                for x in range(self.x1, self.x2+1):
                    pt = [x, y]
                    y = y + 1
                    pts.append(pt)
        return pts
        
def getInput():
    f = open("advent/2021/input/5.txt", "r")
    data = f.read()
    return data.split('\n')
    
def a():
    data = getInput()
    pts = {}
    for r in data:
        row = Row.fromString(s=r)
        rowPts = row.getPoints()
        for p in rowPts:
            pstr = ','.join([str(i) for i in p])
            curr = pts.get(pstr, 0)
            pts[pstr] = curr + 1
            
    overlaps = 0
    print(len(pts))
    for i in pts.values():
        if i > 1:
            overlaps = overlaps + 1
    return overlaps
    
print(a())
        
    
            
            
        