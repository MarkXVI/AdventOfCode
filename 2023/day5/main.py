
def part1():
    
    seedValues=[]
    with open('input.txt', 'r') as f:
        items = f.read().splitlines()
    
    values = [[]]
    for i in items:
        if not i:
            values.append([])
        else:
            values[-1].append(i)
    
    seeds = values[0][0].split(': ')
    values[0][0] = seeds[0]
    values[0].append(seeds[1])
    
    for n in range(len(values)):
        if not n == 0:
            values[n][0] = values[n][0][:-5]
        for m in range(1, len(values[n])):
            values[n][m] = list(map(int, values[n][m].split(' ')))
    
    # print(values)
    
    minLocation = 0
    for n in range(len(values[0][1])):
        data = []
        data.append(values[0][1][n])
        for i in range(1, len(values)):
            for j in range(1, len(values[i])):
                if values[i][j][1] <= data[-1] <= values[i][j][1] + values[i][j][2]:
                    diff = data[-1] - values[i][j][1]
                    data.append(values[i][j][0]+diff)
                    break
                elif j == len(values[i])-1:
                    data.append(data[-1])
                    
                
        
        if n == 0:
            minLocation = data[-1]
        elif minLocation > data[-1]:
            minLocation = data[-1]
        if not len(data) == 8:
            print('Not all data added...')
        
        seedValues.append(data)
        
    # print(seedValues)
    print(minLocation)
                
def part2():
    
    seedValues=[]
    with open('input.txt', 'r') as f:
        items = f.read().splitlines()
    
    values = [[]]
    for i in items:
        if not i:
            values.append([])
        else:
            values[-1].append(i)
    
    seeds = values[0][0].split(': ')
    values[0][0] = seeds[0]
    values[0].append(seeds[1])
    
    for n in range(len(values)):
        if not n == 0:
            values[n][0] = values[n][0][:-5]
        for m in range(1, len(values[n])):
            values[n][m] = list(map(int, values[n][m].split(' ')))
    
    # print(values)
    
    minLocation = None
    for n in range(0, len(values[0][1]), 2):
        for m in range(values[0][1][n], values[0][1][n] + values[0][1][n+1]):
            print(m)
            data = []
            data.append(m)
            for i in range(1, len(values)):
                for j in range(1, len(values[i])):
                    if values[i][j][1] <= data[-1] <= values[i][j][1] + values[i][j][2]:
                        diff = data[-1] - values[i][j][1]
                        data.append(values[i][j][0]+diff)
                        break
                    elif j == len(values[i])-1:
                        data.append(data[-1])
                    
            if minLocation == None:
                minLocation = data[-1]
            elif minLocation > data[-1]:
                minLocation = data[-1]
            if not len(data) == 8:
                print('Not all data added...')
            
            seedValues.append(data)
        
    print(seedValues)
    print(minLocation)

if __name__ == '__main__':
	part1()
	part2()