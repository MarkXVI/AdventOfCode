
def part1():
	unsafe = 0
	safe = 0
	lines = []
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			lines.append(items.split(' '))

	int_lines = [[int(x) for x in line] for line in lines]

	for line in int_lines:
		print (line)
		n = len(line)
		if (line[0] <= line[1] and
			line[n - 2] <= line[n - 1]) :
			print("Increasing"); 

		elif (line[0] >= line[1] and
			line[n - 2] >= line[n - 1]) :
			print("Decreasing"); 
		else:
			continue
		for i in range(len(line)): 
			difference = 0

			if line[i-1] < line[i]:
				difference = line[i] - line[i-1]
			else:
				difference = line[i-1] - line[i]
			
			print (line)

			if difference >= 4:
				print("unsafe")
				unsafe += 1
				break

			if line[i] == line[-1] and difference <= 3: 
				print("safe")
				safe += 1

	print(unsafe)
	print(safe)


def part2():
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			print(items)

if __name__ == '__main__':
	part1()
	# part2()+