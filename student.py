import json

def answer():
    with open('FlashCards.json', 'r') as file:
        data = json.load(file)

    for prompt, answer in data.items():
        print(prompt)