def puzzle1():
    choices = {'X': 1, 'Y': 2, 'Z': 3}
    enemyChoices = {'A': 1, 'B': 2, 'C': 3}
    totalpoints = 0
    with open('input.txt') as f:
        turns = f.read().splitlines()

        for turn in turns:
            win = False
            draw = False

            points = choices[turn[-1]]
            if choices[turn[-1]] == enemyChoices[turn[0]]:
                draw = True
            if choices[turn[-1]] - enemyChoices[turn[0]] == 1 or choices[turn[-1]] - enemyChoices[turn[0]] == -2:
                win = True
            if win:
                points += 6;
            if draw:
                points += 3
            
            totalpoints += points

        print(totalpoints)

def puzzle2():
    enemyChoices = {'A': 1, 'B': 2, 'C': 3}
    totalpoints = 0
    with open('input.txt') as f:
        turns = f.read().splitlines()

        for turn in turns:
            win = False
            draw = False
            points = 0

            if turn[-1] == 'X':
                if enemyChoices[turn[0]] == 1:
                    points += 3
                else:
                    points += enemyChoices[turn[0]] - 1
            if turn[-1] == 'Y':
                draw = True
                points += enemyChoices[turn[0]]
            if turn[-1] == 'Z':
                win = True
                if enemyChoices[turn[0]] == 3:
                    points += 1
                else:
                    points += enemyChoices[turn[0]] + 1

            if win:
                points += 6;
            if draw:
                points += 3
            
            totalpoints += points

        print(totalpoints)

if __name__ == '__main__':
    puzzle1()
    puzzle2()