import re

def part1():
	with open('input.txt', 'r') as f:
		items = f.read().splitlines()
		for i in range(len(items)):
			items[i] = items[i].split(':')
			temp = re.findall(r'\d+', items[i][1])
			items[i][1] = list(map(int, temp))
		print (items[0][1])

		possibleList = []
		for x in range(len(items[0][1])):
			possible = 0

			for i in range(1, items[0][1][x]+1):
				if (items[0][1][x] - i) * i > items[1][1][x]:
					possible += 1
			
			possibleList.append(possible)

		res = 1
		for p in possibleList:
			res *= p
		print (res)
				

def part2():
	with open('input.txt', 'r') as f:
		items = f.read().splitlines()
		for i in range(len(items)):
			items[i] = items[i].split(':')
			items[i][1] = items[i][1].replace(' ','')
			temp = re.findall(r'\d+', items[i][1])
			items[i][1] = list(map(int, temp))
		print (items[0][1])

		possibleList = []
		for x in range(len(items[0][1])):
			possible = 0

			for i in range(1, items[0][1][x]+1):
				if (items[0][1][x] - i) * i > items[1][1][x]:
					possible += 1
			
			possibleList.append(possible)

		res = 1
		for p in possibleList:
			res *= p
		print (res)

if __name__ == '__main__':
	part1()
	part2()