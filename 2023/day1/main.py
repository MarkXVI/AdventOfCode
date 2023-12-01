import re

def part1():
	totalvalue = 0
	with open('input.txt', 'r') as f:
		for item in f.read().splitlines():
			temp = re.findall(r'\d', item)
			res = list(map(str, temp))

			# print (res)
			totalvalue += (int("".join([res[0], res[-1]])))
	
	print (totalvalue)

def part2():
	wordValues = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
	totalvalue = 0

	with open('input.txt', 'r') as f:
		for item in f.read().splitlines():
			temp = re.findall(r'(?=(?<!0)(one|two|three|four|five|six|seven|eight|nine|\d))', item)
			res = list(map(str, temp))

			for i in range(len(res)):
				if not res[i].isnumeric():
					res[i] = wordValues[res[i]]

			# print (res)
			totalvalue += (int("".join([res[0], res[-1]])))
	
	print (totalvalue)

if __name__ == '__main__':
	part1()
	part2()