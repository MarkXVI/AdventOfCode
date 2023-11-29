import requests
from datetime import date
import os

def createfolder(today):
    print(today)
    if not os.path.exists("day" + str(today)):
        os.makedirs("day" + str(today))
        f = open("day" + str(today) + "/main.py", "a")
        f.write("\ndef readfile():\n\twith open('input.txt', 'r') as k:\n\t\tfor items in k.read().splitlines():\n\t\t\tprint(items)\n\ndef main():\n\treadfile()\n\nif __name__ == '__main__':\n\tmain()")
        f.close()

def download_input(today):
    uri = 'https://adventofcode.com/2022/day/'+ str(today) + '/input'
    response = requests.get(uri, cookies={
        'session': "53616c7465645f5fe233abb71092fb5980da9509390027d557c95f28612dfca79dd54ea801bd035daab1b825dbe0c3d702afa3c05528b7eb071c6f10182e6314"})
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