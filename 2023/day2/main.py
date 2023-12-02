
def part1():
	sumofgamenrs = 0
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			r = 0
			g = 0
			b = 0
			possible = True
			gamenr, data = items.split(': ')
			data = data.split('; ')
			# print (data)
			for i in data:
				i = i.split(', ')
				for j in i:
					j = j.split(' ')
					# print(j)
					
					if j[1] == 'red' and int(j[0]) > r:
						r = int(j[0])
					if j[1] == 'green' and int(j[0]) > g:
						g = int(j[0])
					if j[1] == 'blue' and int(j[0]) > b:
						b = int(j[0])

			if r > 12:
				possible = False
			if g > 13:
				possible = False
			if b > 14:
				possible = False

			if possible:
				sumofgamenrs += int(gamenr[5:])
	
	print (sumofgamenrs)


def part2():
	sumofpower = 0
	with open('input.txt', 'r') as f:
		for items in f.read().splitlines():
			r = 0
			g = 0
			b = 0
			_, data = items.split(': ')
			data = data.split('; ')
			# print (data)
			for i in data:
				i = i.split(', ')
				for j in i:
					j = j.split(' ')
					# print(j)
					
					if j[1] == 'red' and int(j[0]) > r:
						r = int(j[0])
					if j[1] == 'green' and int(j[0]) > g:
						g = int(j[0])
					if j[1] == 'blue' and int(j[0]) > b:
						b = int(j[0])
				
			sumofpower += r*g*b


	print (sumofpower)

if __name__ == '__main__':
	part1()
	part2()