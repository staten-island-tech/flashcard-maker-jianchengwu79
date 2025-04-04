import json
import random

try:
    with open("FlashCards.json", "r") as file:
        flashcards_data = json.load(file)
except FileNotFoundError:
    flashcards_data = []
class Mode:
    def switch_mode(self):
        pass

class TeacherMode(Mode):
    def __init__(self):
        self.mode_name = "Teacher"
    def switch_mode(self):
        print(f"Switching to {self.mode_name}. You can now create flashcards for your students.")
    def create_flashcards(self):
        flashcards = {}

        while True:
            word = input("Enter the word or phrase (or type 'exit' to stop): ").strip()
            if word.lower() == 'exit':
                break
            answer = input(f"Enter the answer for '{word}': ").strip()
            flashcards[word] = answer
        
        flashcards_data.extend(flashcards.items()) 
        with open("Flashcards.json", "w") as file:
            json.dump(flashcards_data, file, indent=4)
        print("The flashcards have been added to Flashcards.json.")

class StudentMode(Mode):
    def __init__(self):
        self.mode_name = "Student"
    def switch_mode(self):
        print(f"Switching to {self.mode_name}. You will now be quizzed on the flashcards created by your teacher.")
    def quiz_user(self):
        try:
            with open("FlashCards.json", "r") as file:
                flashcards_data = json.load(file)
        except FileNotFoundError:
                print("No flashcards found! Ask your teacher to create some!")
                return
        if not flashcards_data:
            print("No flashcards to quiz you on! Again, ask your teacher to create some!")
            return
        prompts = list(flashcards_data.items())
        random.shuffle(prompts)
        correct = 0
        total = len(prompts)

        for word, answer in prompts:
            useranswer = input(f"What is your answer for '{word}'?: ").strip()
            if useranswer.lower() == answer.lower():
                print("You got it correct!!")
                correct += 1
            else:
                print(f"Heh.. you got it wrong. LOSER! The correct answer is {answer}")
            print()
        percentage = (correct / total) * 100
        print(f"You finished your quiz... You got {correct} out of {total} correct. That is a {percentage}% score! ")

class SwitchingMode(Mode):
    def __init__(self):
        self.current_mode = None
    def switch(self, modechoice):
        if modechoice == '1':
            self.current_mode = TeacherMode()
        elif modechoice == '2':
            self.current_mode = StudentMode()
        else:
            print("Invalid mode choice, please choose 1 or 2.")
            return False
        self.current_mode.switch_mode()
        return True

def main():
    modeswitch = SwitchingMode()

    while True:
        print("\n1. Teacher Mode\n2. Student Mode\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1' or choice == '2':
            if modeswitch.switch(choice):
                if isinstance(modeswitch.current_mode, TeacherMode):
                    modeswitch.current_mode.create_flashcards()
            elif isinstance(modeswitch.current_mode, StudentMode):
                modeswitch.current_mode.quiz_user()

        elif choice == '3':
            print("Bye bye bye!!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
