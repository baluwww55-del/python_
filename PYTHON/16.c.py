# introduction to a functions in a python :
# 1. what is functions in a python programming language :
# functions is a block of code which is used to perform a specific task and it can be reused .
# 2. how to define a function in a python programming language :
# we can define a function in a python using a def .
# simple code 
def addition(a,b):
    return a + b
# calling a function :
a = 5
b = 10
result = addition(a,b)
print(result)
# this is the simple code of a function using a python programming language.

# we have some advanced python functions :
def add(*a):
    print(a)
add(1,2,3,4,5)
# by using this function we can see variables in a tuple form .

def add(numbers):
    return sum(numbers)
print(add([1,2,3,4,5]))
# by using this function we can see the sum of a list of a numbers :
# so this is the part one a simple function programs using python programming language.