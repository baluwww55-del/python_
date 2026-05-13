# so this is the functions part 2 
# in this session we are going to use some important functions in python programming language :
# we have lambda functions and recursions and sometimes we use dictionary in python :
# 1. what is meant by lambda function ?
# lambda function is a function which is we use to compare the anonymous functions :
# 2 . what is recursion ?
# when a function calls itself it is known as recursion 
# simple program to lambda function :
# ============================================
# Python Lambda Functions - Basics Programs
# ============================================

# A lambda function is a small anonymous function.
# Syntax:
# lambda arguments: expression

# --------------------------------------------
# 1. Simple Lambda Function
# --------------------------------------------

square = lambda x: x * x
print("Square of 5:", square(5))   # Output: 25


# --------------------------------------------
# 2. Lambda with Two Arguments
# --------------------------------------------

add = lambda a, b: a + b
print("Sum of 10 and 20:", add(10, 20))   # Output: 30


# --------------------------------------------
# 3. Lambda with Three Arguments
# --------------------------------------------

multiply = lambda a, b, c: a * b * c
print("Product:", multiply(2, 3, 4))   # Output: 24


# --------------------------------------------
# 4. Lambda to Check Even or Odd
# --------------------------------------------

is_even = lambda n: n % 2 == 0
print("Is 8 even?", is_even(8))   # Output: True


# --------------------------------------------
# 5. Lambda to Find Maximum of Two Numbers
# --------------------------------------------

maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(15, 9))   # Output: 15


# --------------------------------------------
# 6. Using Lambda with map()
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)
# Output: [1, 4, 9, 16, 25]


# --------------------------------------------
# 7. Using Lambda with filter()
# --------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)
# Output: [2, 4, 6]


# --------------------------------------------
# 8. Using Lambda with sorted()
# --------------------------------------------

students = [
    ("Balu", 85),
    ("Ravi", 92),
    ("Kiran", 78)
]

sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by marks:", sorted_students)


# --------------------------------------------
# 9. Lambda Returning String
# --------------------------------------------

greet = lambda name: f"Hello, {name}!"
print(greet("Balu"))
# Output: Hello, Balu!


# --------------------------------------------
# 10. Nested Lambda
# --------------------------------------------

multiply_by = lambda n: lambda x: x * n
double = multiply_by(2)
triple = multiply_by(3)

print("Double of 5:", double(5))   # Output: 10
print("Triple of 5:", triple(5))   # Output: 15


# ============================================
# Quick Summary
# ============================================

# lambda x: x * x
# lambda a, b: a + b
# map(lambda x: x*x, list)
# filter(lambda x: condition, list)
# sorted(list, key=lambda x: x[index])

# recursion example programs :
# ============================================
# Python Recursion - Basic Examples
# ============================================

# Recursion is when a function calls itself.
# Every recursive function must have:
# 1. Base Case      -> Stops recursion
# 2. Recursive Case -> Function calls itself

# --------------------------------------------
# 1. Print Numbers from 1 to N
# --------------------------------------------

def print_numbers(n):
    if n == 0:      # Base case
        return
    print_numbers(n - 1)
    print(n)

print("Numbers from 1 to 5:")
print_numbers(5)


# --------------------------------------------
# 2. Factorial Using Recursion
# --------------------------------------------

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))   # 120


# --------------------------------------------
# 3. Sum of First N Natural Numbers
# --------------------------------------------

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum of first 5 numbers:", sum_n(5))   # 15


# --------------------------------------------
# 4. Fibonacci Series Using Recursion
# --------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6:", fibonacci(6))   # 8


# --------------------------------------------
# 5. Reverse a String Using Recursion
# --------------------------------------------

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("Reverse of 'hello':", reverse_string("hello"))


# --------------------------------------------
# 6. Power of a Number
# --------------------------------------------

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("2^5 =", power(2, 5))   # 32


# ============================================
# Quick Summary
# ============================================

# factorial(n) = n * factorial(n-1)
# sum_n(n)     = n + sum_n(n-1)
# fibonacci(n) = fib(n-1) + fib(n-2)
# power(a, b)  = a * power(a, b-1)