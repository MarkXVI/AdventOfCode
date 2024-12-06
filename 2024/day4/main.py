
def check_letter(puzzle, x, y):
	return puzzle[y][x]

def check_rest_of_word(WORD, puzzle, xmod, ymod, x, y):
	for wordcount in range(1, 4):
		if check_letter(puzzle, x+(xmod*wordcount), y+(ymod*wordcount)) == WORD[wordcount]:
			if wordcount == len(WORD)-1:
				# print(x,y)
				return 1
		else:
			return 0
	return 0

def part1():
	xmas = 0
	puzzle = []
	with open('input.txt', 'r') as f:
		for line in f.read().splitlines():
			puzzle.append(list(line))

	WORD = list("XMAS")

	"""
	1 look for x
	2 if x look for next letter M
	W SW S SE E NE N NW
	if xpos <= lenx-3 dont look NW W SW
	if xpos > 4 dont look NE E SE
	if ypos > 4 dont look NE N NW
	if ypos <= leny-3 dont look SE S SW
	"""

	for y in range(0, len(puzzle)):
		for x in range(0, len(puzzle[y])):
			if check_letter(puzzle, x, y) == WORD[0]:
				# check north
				if y > 2:
					xmas += check_rest_of_word(WORD, puzzle, 0, -1, x, y)
					# check north west
					if x < len(puzzle[y]) -3:
						xmas += check_rest_of_word(WORD, puzzle, 1, -1, x, y)
					# check north east
					if x > 2:
						xmas += check_rest_of_word(WORD, puzzle, -1, -1, x, y)

				#check east
				if x > 2:
					xmas += check_rest_of_word(WORD, puzzle, -1, 0, x, y)

				#check south
				if y < len(puzzle)-3:
					xmas += check_rest_of_word(WORD, puzzle, 0, 1, x, y)
					# check south west
					if x < len(puzzle[y]) -3:
						xmas += check_rest_of_word(WORD, puzzle, 1, 1, x, y)
					# check south east
					if x > 2:
						xmas += check_rest_of_word(WORD, puzzle, -1, 1, x, y)
				
				#check west
				if x < len(puzzle[y]) -3:
					xmas += check_rest_of_word(WORD, puzzle, 1, 0, x, y)

	print(xmas)

def part2():
	x_mas = 0
	puzzle = []
	with open('input.txt', 'r') as f:
		for line in f.read().splitlines():
			puzzle.append(list(line))

	"""
	1 look for A
	2 NE for M or S
	3 SW for M or S whichever step 2 isnt
	4 NW for M or S
	3 SE for M or S whichever step 2 isnt
	"""

	for y in range(0, len(puzzle)):
		for x in range(0, len(puzzle[y])):
			if 0 < y < len(puzzle)-1 and 0 < x < len(puzzle[y])-1 and check_letter(puzzle, x, y) == "A":
				print(x,y)
				NE_letter = check_letter(puzzle, x-1, y-1)
				if NE_letter in ["M", "S"]:
					SW_letter = check_letter(puzzle, x+1, y+1)
					if SW_letter in ["M", "S"] and SW_letter != NE_letter:
						NW_letter = check_letter(puzzle, x+1, y-1)
						if NW_letter in ["M", "S"]:
							SE_letter = check_letter(puzzle, x-1, y+1)
							if SE_letter in ["M", "S"] and SE_letter != NW_letter:
								x_mas += 1

	print(x_mas)

if __name__ == '__main__':
	# part1()
	part2()