import json

"""class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"




class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal
"""

import json

def create_flashcards():
    flashcards = {}

    while True:
        word = input("Enter the word or phrase (or type 'exit' to stop): ").strip()
        if word.lower() == 'exit':
            break
        answer = input(f"Enter the answer for '{word}': ").strip()
        flashcards[word] = answer

    with open('FlashCards.json', 'w') as f:
        json.dump(flashcards, f, indent=4)
    print("The flashcards have been added to FlashCards.json.")

create_flashcards()
