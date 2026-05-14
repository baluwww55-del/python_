# INTRODUCTION TO OOP IN PYTHON :
# OOP : object oriented programming
 
# why we use OOP in python ?
# OOP is a known for its reusability and modularity.
# OOP helps to structure code in a way that is easy to understand and maintain.
# OOP allows to model real world entities as objects with attributes and behaviors.

# OOP concepts in python :
# 1. Classes and Objects
# 2. abstraction
# 3. encapsulation  
# 4. inheritance
# 5. polymorphism

# what is a class ?
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# example code for class :
class human: 
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f"{self.name} is walking.")

chandan = human("chandan")
balaji = human("balaji")

chandan.walk()
balaji.walk()

# what is an object ?
# An object is an instance of a class. it is created using the class blueprint and has its own unique set of attributes and behavious.
