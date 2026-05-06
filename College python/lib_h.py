# first one : without arguments and without return type:
def add():
    c = a + b
    print(c)
a = 10
b = 20 
add()

# second one : without arguments and with return type:
def add():
    c = a + b
    return c
a = 10
b = 20
add()

# third one : with arguments and without return type:
def add(a,b):
    c = a + b
    print(c)        
a = 10
b = 20
add(a,b)

# fourth one : with arguments and with return type:
def addn(num1 ,num2):
     c = num1 + num2 
     print("the addition is done")
     return c 
num1 = 10
num2 = 20
addn(num1,num2)
print("the addition is",addn(num1,num2))