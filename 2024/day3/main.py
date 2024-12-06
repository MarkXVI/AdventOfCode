import re

def part1():
	muls= []
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			muls.append(re.findall("(?:mul)([(](\d+),(\d+)[)])", items))
	
	muls_total = 0

	for i in muls:
		for j in i:
			muls_total += int(j[1]) * int(j[2])
	
	print(muls_total)
	


def part2():
	muls= []
	with open('test.txt', 'r') as f:
		for items in f.read().splitlines():
			muls.append(re.findall("(do[(][)])|(don't[(][)])|(?:mul[(])((\d+),(\d+))(?:[)])", items))
	
	muls_total = 0

	do = True

	for i in muls:
		for j in i:
			print(j)
			if j[0] != '':
				do = True
				continue
			if j[1] != '':
				do = False
			if do:
				muls_total += int(j[3]) * int(j[4])
	
	print(muls_total)

if __name__ == '__main__':
	part1()
	part2()