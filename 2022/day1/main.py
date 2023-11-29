def puzzle1and2():
    with open('input.txt') as f:
        cal = f.read().splitlines()
        elf = 0
        elves = []
        for items in cal:
            if not items:
                elves.append(elf)
                elf = 0
            if items:
                elf = elf + int(items)
        elves.sort(reverse=True)
        print(str(elves[0]) + "\n" + str(sum(elves[0:3])))

if __name__ == '__main__':
    puzzle1and2()