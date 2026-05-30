# ERRORS AND EXCEPTION HANDLING IN PYTHON :
# what is error ?
# an error is an unexpected event  that occurs during the execution of a program.
# errors crash the program and stop the normal flow of execution.

# types of errors :
# 1. Syntax Error :
# syntax errors occur when the code does not follow the correct syntax of the programming language.
# example code :
# print("hello world"  # missing closing parenthesis    
# this will raise a syntax error.

# 2. Runtime Error :
# runtime errors occur during the execution of the program. 
# example code :
# a = 10    
# b = 0
# c = a / b  # division by zero error
# this will raise a runtime error.

# EXCEPTION HANDLING IN PYTHON :
# savuing the program from crashing due to errors using try and except blocks.
# four key words in exception handling :
# 1. try :
# 2. except :
# 3. finally :
# 4. raise :

# example code : 
a = int(input("enter a :"))
b = int(input("enter b :"))

try:
    print(a/b)
except Exception as  e:
    print(f"error bantho : {e}")
else:
    print("no error")
finally:
    print("program ended !")
    