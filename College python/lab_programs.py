#python programming lab programs :
# using map function:
from functools import reduce


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("original list:", numbers)
print("squared list:", squared)

# using filter function:
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("original list:", numbers)
print("even numbers:", even_numbers)

# using reduce function:
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("original list:", numbers)
print("sum of numbers:", sum_of_numbers)

# using lambda sorting 2nd element of list :
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print("original data:", data)
print("sorted data:", sorted_data)

# program for recursion :
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = 5
print("Factorial of", number, "is", factorial(number))


# write a python program to read a student name, age and course and print the details in a formatted way.
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")
print(f"Student Name: {name}")
print(f"Student Age: {age}")
print(f"Student Course: {course}")

# write a python program to read to check the whether the give year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.") 
else:
    print(year, "is not a leap year.")

# write a python program that handles the following exceptions:
# division by error, invalid input , use try , except else , and finally blocks.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
try:
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
else:
    print("No exceptions occurred.")
finally:
    print("Finally block executed.")

# write a python program demonstrating single inheritance using a base class and a derived class .
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print(f"course: {self.course}")
    # creating a object of the student class and calling .
student1 = student("Alice", 20, "Computer Science")
student1.display()  

# data types in python :
a = 10 
b = 3.14
c = "Hello, World!"
print("Integer:", a)
print("Float:", b)
print("String:", c)
# these are the basic data types in python : integer. float and string .

a=int(input("Enter a value")); #input() takes data from console at runtime as string.
b=int(input("Enter b value")); #typecast the input string to int.
print("Addition of a and b ",a+b);
print("Subtraction of a and b ",a-b);
print("Multiplication of a and b ",a*b);
print("Division of a and b ",a/b);
print("Remainder of a and b ",a%b);
print("Exponent of a and b ",a**b); #exponent operator (a^b)
print("Float division of a and b ",a//b); # float division

# python program to concatenate two strings and find the substring of a given string.
s1=input("Enter first String : ");
s2=input("Enter second String : ");
print("First string is : ",s1);
print("Second string is : ",s2);
print("concatenations of two strings :",s1+s2);
print("Substring of given string :",s1[1:4]);

# program to create append remove and concatenate list in python.
pets = ['cat', 'dog', 'rat', 'pig', 'tiger']
snakes=['python','anaconda','fish','cobra','mamba']
print("Pets are :",pets)
print("Snakes are :",snakes)
animals=pets+snakes
print("Animals are :",animals)
snakes.remove("fish")
print("updated Snakes are :",snakes)

# program to demonstrate the working of a tuples in a python .
T = ("apple", "banana", "cherry","mango","grape","orange")
print("\n Created tuple is :",T)
print("\n Second fruit is :",T[1])
print("\n From 3-6 fruits are :",T[3:6])
print("\n List of all items in Tuple :")
for x in T:
  print(x)
if "apple" in T:
  print("\n Yes, 'apple' is in the fruits tuple")
print("\n Length of Tuple is :",len(T))

dict1 = {'StdNo':'532','StuName': 'Naveen', 'StuAge': 21, 'StuCity': 'Hyderabad'}
print("\n Dictionary is :",dict1)
#Accessing specific values 
print("\n Student Name is :",dict1['StuName'])
print("\n Student City is :",dict1['StuCity'])
#Display all Keys
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
#Display all values
print("\n All Values in Dictionary ")
for x in dict1:
    print(dict1[x])
#Adding items
dict1["Phno"]=85457854
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Change values
dict1["StuName"]="Madhu"
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Removing Items
dict1.pop("StuAge");
#Updated dictoinary
print("\n Uadated Dictionary is :",dict1)
#Length of Dictionary
print("Length of Dictionary is :",len(dict1))
#Copy a Dictionary
dict2=dict1.copy()
#New dictoinary
print("\n New Dictionary is :",dict2)
#empties the dictionary
dict1.clear()
print("\n Uadated Dictionary is :",dict1)

# write a python program to find the largest of three numbers  using condition statements .
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)

# write a python program to find the to convert the given temperature in celsius to fahrenheit and vice versa.
print("Options are \n")
print("1.Convert temperatures from Celsius to Fahrenheit \n")
print("2.Convert temperatures from Fahrenheit to Celsius \n")
opt=int(input("Choose any Option(1 or 2) : "))
if opt == 1:
    print("Convert temperatures from Celsius to Fahrenheit \n")
    cel = float(input("Enter Temperature in Celsius: "))
    fahr = (cel*9/5)+32
    print("Temperature in Fahrenheit =",fahr)
elif opt == 2:
    print("Convert temperatures from Fahrenheit to Celsius \n")
    fahr = float(input("Enter Temperature in Fahrenheit: "))
    cel=(fahr-32)*5/9;
    print("Temperature in Celsius =",cel)
else:
    print("Invalid Option")

# write a python program to find the print the stars using loops.
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# write a python program to find the scripts of prime number less than 20.
print("Prime numbers between 1 and 20 are:")
ulmt=20;
for num in range(ulmt):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

# THESE ARE THE BASIC PYTHON PROGRAMS FOR LAB PRACTICE .
# program to print plus pattern :
n=5;
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print('* ', end="")
        else:
            print('  ', end="")
    print('')

          

