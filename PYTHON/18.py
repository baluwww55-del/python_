#  CONSTRUCTOR AND THE SELF KEYWORDS :

# __init__ () is a built in constructor in python.
# it is startup setting for objects 

# using the self method in class .
# self is jst a variable name .
# self can be changed but its convential it stores the data 
# self is the instance of the class.
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

chandan = human("chandan", 25)
balaji = human("balaji", 30)
chandan.introduce()
balaji.introduce() 

# in the above example __init__ () is the constructor that initializes the name and age attributes of the human class.
# the self keyword is used to refer to the instance of the class and access its attributes and methods.