import re

def part1():
    with open('input.txt', 'r') as f:
        score = 0
        for items in f.read().splitlines():
            cardscore = 0
            _, data = items.split(': ')
            winnrs, nrs = data.split(' | ')
            temp = re.findall(r'\d+', nrs)
            res_nrs = list(map(str, temp))
            temp = re.findall(r'\d+', winnrs)
            res_winnrs = list(map(str, temp))
            
            #print (res_winnrs, res_nrs)
            
            for m in res_nrs:
                if m in res_winnrs:
                    if cardscore == 0:
                        cardscore = 1
                    else:
                        cardscore = cardscore * 2
                #print (m, cardscore)
            
            score += cardscore
                        
        print (score)
            

def part2():
    with open('input.txt', 'r') as f:
        items = f.read().splitlines()

        cards = [1] * len(items)

        for item in items:
            cardwinnings = 0
            cardnr, data = item.split(': ')
            cardnr = int(cardnr[5:])
            # print(cardnr)
            winnrs, nrs = data.split(' | ')
            temp = re.findall(r'\d+', nrs)
            res_nrs = list(map(str, temp))
            temp = re.findall(r'\d+', winnrs)
            res_winnrs = list(map(str, temp))
            
            for m in res_nrs:
                if m in res_winnrs:
                    cardwinnings += 1
            
            for i in range(cardwinnings):
                # print(cardnr, i+cardnr-1)
                cards[i + cardnr] += 1 * cards[cardnr -1]
                
            #print(cards)
            


        print(sum(cards))

if __name__ == '__main__':
	part1()
	part2()