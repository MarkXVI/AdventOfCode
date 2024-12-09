
def diskmap_to_blockline(diskmap):
	blockline_list = []
	id = 0
	#iterate through diskmap
	for index in range(1, len(diskmap)+1):
		l = []
		if index % 2 != 0:
			l = [id] * int(diskmap[index-1])
		else:
			l = [-1] * int(diskmap[index-1])
			id += 1
		blockline_list.extend(l)

	return blockline_list

def part1():
	"""
	convert diskmap to blockline
		id = 0 ++
		blocks filled
		blocks empty
		create list with blocks filled + blocks empty places for all blocks
		fill the blocks filled spaces with id 
	move the right most filled space to the left most empty space
	calculate the result
	sum of posistions * id values
	"""
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			diskmap = items

	blockline_list = diskmap_to_blockline(diskmap)
	# print("".join(str(e) if e != -1 else "." for e in blockline_list))

	for i in range(len(blockline_list)-1, 0, -1):
		if blockline_list[i] != -1:
			for j in range(0, len(blockline_list)-1):
				if blockline_list[j] == -1 and i > j:
					blockline_list[j], blockline_list[i] = blockline_list[i], blockline_list[j]
					# print("".join(str(e) if e != -1 else "." for e in blockline_list))
					break
	
	checksum = 0
	for index, item in enumerate(blockline_list):
		if item != -1:
			checksum += item * index
	print (checksum)

def part2():
	"""
	convert diskmap to blockline
		id = 0 ++
		blocks filled
		blocks empty
		create list with blocks filled + blocks empty places for all blocks
		fill the blocks filled spaces with id 
	move the right most full block to the left most empty block of the same size 
	calculate the result
	sum of posistions * id values
	"""
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			diskmap = items

	blockline_list = diskmap_to_blockline(diskmap)
	# print("".join(str(e) if e != -1 else "." for e in blockline_list))

	for i in range(len(blockline_list)-1, 0, -1):
		if blockline_list[i] != -1:
			free_space_needed = blockline_list.count(blockline_list[i])
			for j in range(0, len(blockline_list)-1):
				if blockline_list[j] == -1 and i > j:
					free = True
					for k in range(1, free_space_needed):
						if blockline_list[j+k] != -1:
							free = False
							break
					if free:
						for k in range(0, free_space_needed):
							blockline_list[j+k], blockline_list[i-k] = blockline_list[i-k], blockline_list[j+k]
						# print("".join(str(e) if e != -1 else "." for e in blockline_list))
						break

	checksum = 0
	for index, item in enumerate(blockline_list):
		if item != -1:
			checksum += item * index
	print (checksum)

if __name__ == '__main__':
	# part1()
	part2()