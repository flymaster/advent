def getInput():
    f = open("advent/2021/input/10.txt", "r")
    data = f.read()
    data = data.split('\n')
    return data
    
def isOpen(char):
    opens = '({[<'
    return char in opens
    
def match(o, c):
    vals = {}
    vals[')'] = '('
    vals[']'] = '['
    vals['}'] = '{'
    vals['>'] = '<'
    return o == vals[c]
    
def parse(line):
    vals = {}
    vals['('] = 1
    vals['['] = 2
    vals['{'] = 3
    vals['<'] = 4
    stack = []
    for x in line:
        if isOpen(x):
            stack.append(x)
        else:
            last = stack.pop(-1)
            if not match(last, x):
                return 0
    rem = len(stack)
    tot = 0
    for x in range(rem, 0, -1):
        tot = tot * 5
        tot = tot + vals[stack[x-1]]
    return tot
            
i = getInput()

v = []
for s in i:
    ac = parse(s)
    if ac != 0:
        v.append(ac)
v = sorted(v)
print(v[len(v)//2])
    