# functions in python :
# 1. built in functions : print(), input(), len() , type() , int() , str() , float() , list() , dict() , set() , tuple() , etc
# 2. user defined functions : we can create our own functions using def keyword     
# syntax :
def greet():
    print("Hello, World!")
greet()  # calling the function

# function with parameters :
def greet(name):
    print("Hello, " + name + "!")   
greet("Alice")  # calling the function with argument    

# function with return value :
def add(a, b):
    return a + b
result = add(5, 3)  # calling the function and storing the return value in a variable
print(result)  # output: 8

# function with default parameters :
def greet(name="World"):
    print("Hello, " + name + "!")
greet()  # calling the function without argument, it will use the default value
greet("Alice")  # calling the function with argument, it will override the default value

# function with variable number of arguments :
def greet(*names):
    for name in names:
        print("Hello, " + name + "!")
greet("Alice", "Bob", "Charlie")  # calling the function with multiple arguments

# function with keyword arguments :
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")
greet("Alice")  # calling the function with positional argument, it will use the default value for greeting
greet("Alice", greeting="Hi")  # calling the function with keyword argument, it will override the default value for greeting