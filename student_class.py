# Exercise 1: Creating a Student Class

# Instructions:

# Define a Student class with attributes like name and age. Include a method to display student information.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_information(self):
        return f"My name is {self.name} and I am {self.age} years old"

my_student = Student("Meshack Ruto", 24)
print(my_student.student_information())
print(my_student.name)