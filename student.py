import json

def answer():
    with open('FlashCards.json', 'r') as file:
        data = json.load(file)

    for key, value in data.items():
        print(key)