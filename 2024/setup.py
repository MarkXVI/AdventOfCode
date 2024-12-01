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
    uri = 'https://adventofcode.com/2024/day/'+ str(today) + '/input'
    response = requests.get(uri, cookies={
        'session': "53616c7465645f5f3c47a349bbc2f41aa0e891a932b9087b00665aaf9ada9cd1d59834fb0b5074d832bff7fea79c69929fe6f2d3186086e5c089152a11d4dd22"})
    if not os.path.exists("day" + str(today) + "/input.txt"):
        text_file = open("day" + str(today) + "/input.txt", "w")
        text_file.write(response.text)
        text_file.close()
    if not os.path.exists("day" + str(today) + "/test.txt"):
        text_file = open("day" + str(today) + "/test.txt", "w")
        text_file.close()


def main(today = None):
    if not today:
        today = date.today().strftime("%d")
        if int(today)<10: today = today.replace("0","")
    createfolder(today)
    download_input(today)


if __name__ == '__main__':
    main()