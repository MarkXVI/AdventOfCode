import requests
from datetime import date
import os

def createfolder(today):
    print(today)
    if not os.path.exists("day" + str(today)):
        os.makedirs("day" + str(today))
        f = open("day" + str(today) + "/main.py", "a")
        f.write("\ndef part1():\n\twith open('input.txt', 'r') as f:\n\t\tfor items in f.read().splitlines():\n\t\t\tprint(items)\n\ndef part2():\n\twith open('input.txt', 'r') as f:\n\t\tfor items in f.read().splitlines():\n\t\t\tprint(items)\n\nif __name__ == '__main__':\n\tpart1()\n\tpart2()")
        f.close()

def download_input(today):
    uri = 'https://adventofcode.com/2023/day/'+ str(today) + '/input'
    response = requests.get(uri, cookies={
        'session': "53616c7465645f5fa60c8820179e743439b164f74c8d9646b628bac20a4ae8d0bbb635028e6c0171945925be8f77738574579addda89e2633d9e4d27626402b3"})
    if not os.path.exists("day" + str(today) + "/input.txt"):
        text_file = open("day" + str(today) + "/input.txt", "w")
        text_file.write(response.text)
        text_file.close()


def main(today = None):
    if not today:
        today = date.today().strftime("%d")
        if int(today)<10: today = today.replace("0","")
    createfolder(today)
    download_input(today)


if __name__ == '__main__':
    main()