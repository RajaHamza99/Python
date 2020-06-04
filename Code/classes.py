"""class Dog:
    energy = "high"

    def speak(self):
        print("Woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak() """

"""class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

bilbo_waggins = Dog("Bilbo_waggins", "Rottweiler", "high")"""

import pytest


class Student:
    class_ = "Student"

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def score(self):
        test_one = int(input("Please enter a test score: "))
        test_two = int(input("Please enter your second test score: "))
        test_three = int(input("Please enter your third test score: "))
        test_score = (test_one + test_two + test_three) / 3
        print(test_score)




John = Student("John", "17")
John.score()
print(John.class_)

