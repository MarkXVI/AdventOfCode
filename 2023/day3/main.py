import re

def part1():
    p = re.compile(r'\d+')
    p2 = re.compile(r"[$&+/,:;=?@#|'<>\-^*()%!]")
    partNrs = []
    with open('input.txt', 'r') as f:
        items = f.read().splitlines()
        #print(items)
    
    for i in range(len(items)):
        for m in p.finditer(items[i]):
            add = False
#            print(i, m.start(), m.group(), len(m.group()))
            
            for x in [-1,0,1]:
                if i == 0 and x == -1:
                    continue
                elif i == len(items)-1 and x == 1:
                    continue
                
                if re.search(p2, items[i+x][m.start() if m.start() == 0 else m.start()-1:m.start()+len(m.group()) if m.start()+len(m.group())+1 >= len(items[i+x]) else m.start()+len(m.group())+1]):
#                    print(items[i+x][m.start() if m.start() == 0 else m.start()-1:m.start()+len(m.group())+1])
#                    print ('Found:', m.group())
                    add = True
                    break
            
            if add:
                partNrs.append(int(m.group()))
            
    print(len(partNrs), sum(partNrs))
            

def part2():
    p = re.compile(r'\d+')
    p2 = re.compile(r"[*]")
    gearRatio = 0
    with open('test.txt', 'r') as f:
        items = f.read().splitlines()

    for i in range(len(items)):
        a,b=0,0
        for m in p2.finditer(items[i]):
            #print(items[i][m.start()-1:m.end()+1])
            for x in [-1,0,1]:
                if i == 0 and x == -1:
                    continue
                elif i == len(items)-1 and x == 1:
                    continue
                
                res = re.search(p, items[i+x])
                if res:
                    if (m.start() if m.start() == 0 else m.start() -1 <= res.start() <= m.end() if m.end() == len(items[i]) else m.end() +1 or m.start() if m.start() == 0 else m.start() -1 <= res.end() <= m.end() if m.end() == len(items[i]) else m.end() +1):
                    print(m.span())
                    print(res.span())
                    print('FOUND:', res.group())
                    if a == 0:
                        a = int(res.group())
                    elif b == 0:
                        b = int(res.group())
                    else:
                        print('TOO MANY GEARS')
                    print(a,b)
            
        if not a == 0 and not b == 0:
            gearRatio += a*b
    
    print(gearRatio)
                    
            

if __name__ == '__main__':
	part1()
	part2()