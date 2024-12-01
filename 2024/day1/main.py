
def part1():

	left_list = []
	right_list = []

	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			# print(items)
			l, r = items.split("   ")
			left_list.append(int(l))
			right_list.append(int(r))
	
	left_list.sort()
	right_list.sort()

	difference = []
	for i in range(0, len(left_list)):
		if left_list[i] < right_list[i]:
			print(f"RIGHT {right_list[i]} - {left_list[i]} =", right_list[i] - left_list[i])
			difference.append(right_list[i] - left_list[i])
		else:
			print(f"LEFT {left_list[i]} - {right_list[i]} =", left_list[i] - right_list[i])
			difference.append(left_list[i] - right_list[i])

	# print (difference)
	total = sum(difference)
	print(total)


def part2():
	left_list = []
	right_list = []
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			l, r = items.split("   ")
			left_list.append(int(l))
			right_list.append(int(r))

	left_list.sort()
	right_list.sort()

	similarity = []
	for i in left_list:
		count = right_list.count(i)
		similarity.append(i * count)

	print(sum(similarity))


if __name__ == '__main__':
	# part1()
	part2()