
def part1():
	safe = 0
	lines = []
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			lines.append(items.split(' '))

	int_lines = [[int(x) for x in line] for line in lines]
	# print(len(int_lines))

	for line in int_lines:
		increasing = True
		decreasing = True
		for i in range(1, len(line)):
			diff = line[i - 1] - line[i]
			if not (1 <= diff <= 3):
				increasing = False
			if not (1 <= -diff <= 3):
				decreasing = False
		if increasing ^ decreasing:
			safe += 1

	print(safe)


def part2():
	safe = 0
	lines = []
	with open('test.txt', 'r') as f:
		for items in f.read().splitlines():
			lines.append(items.split(' '))

	int_lines = [[int(x) for x in line] for line in lines]
	# print(len(int_lines))

	for line in int_lines:
		increasing = True
		decreasing = True
		difference = []
		popped = False
		for i in range(1, len(line)):
			diff = line[i - 1] - line[i]
			if difference == []:
				difference.append(diff)
			elif not popped and not difference[-1] * diff >= 1:
				difference.append(diff)
				popped = True
				continue
			if not (1 <= diff <= 3):
				increasing = False
			if not (1 <= -diff <= 3):
				decreasing = False
		if increasing ^ decreasing:
			print("safe", line)
			safe += 1
	
	print(safe)

if __name__ == '__main__':
	part1()
	part2()