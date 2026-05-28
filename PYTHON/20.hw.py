# create a class mobile that has attributes brand, model and price.

class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price 


    def display(self):
        print(f"brand:{self.brand} costs:{self.price}")

m1 = mobile("redmi 15 5g", 175000)
m2 = mobile("samsung s24 fe", 85000)

m1.display()
m2.display()

# in this program we learnt about how to define the class and its attributes.
# we also learnt about the constructor __init__() and the self keyword.
# we created a class mobile with attributes brand and price.
# we accessed the class attributes using the display method.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        

    def display_info(self):
        print(f"student:{self.name} scored:{self.marks} marks")
        

s1 = student("bhagesh", 95)
s2 = student("narsingh", 92)

s1.display_info()
s2.display_info()

# in this program we did a method definition by creating a class student with attributes name and marks.
# now entering too oops concept.

# 1. ENCAPSULATION :
# create a bank account class with private attribute balance and methods to deposit and withdraw money.

class bankaccount:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance 

    def check_balance(self):
        print(f"current balance:{self.__balance}")
        
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("insufficient funds")

a = bankaccount("acc_no = 123456", 5000)
a.check_balance()
a.deposit(2000)
a.check_balance()
a.withdraw(1000)
a.check_balance()

# in this program we created a bank account class with private attribute balance. 
# __balance is private and cannot be accesed directly from outside the class.
# we created methods to check balance, deposit and withdraw money.


# 2. ABSTRACTION :
# programming example of abstraction using the class and methods.

class phone:
    def take_picture(self):
        # call os to api to open camera. 
        # wait for users to click picture.
        # process image
        # store image in memory
        # return preview of image
        print("picture taken")

p = phone()
p.take_picture()

# 3. INHERITANCE :
# create a base class vehicle and derived class bike from vehicle and additon of new method ride in bike class.
class vehicle:
    def start(self):
        print("vehicle starting")

class bike(vehicle):
    def __init__(self, brand):
        self.brand = brand

    def ride(self):
            print(f"riding the {self.brand} bike")

b = bike("harley davidson")
b.start()
b.ride()

# this is the programming example of inheritance where bike class inherits from vehicle class.
# bike class has i0ts own method ride in addition to the start method inherited from vehicle class.

# 4.POLYMORPHISM :
# simple example of polymorphism using method overriding in python.

class shape:
    print("area is calculated")

class circle(shape):
    def __init__(self, radius):
        self.radius =radius
    def calculate_area(self):
            print(f"area of circle:(3.14 * {self.radius}^2)")

class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        print(f"area of rectangle:({self.length * self.breadth})")
        
c = circle(5)
r = rectangle(4, 6)
c.calculate_area()
r.calculate_area()

#  GETTERS AND SETTERS 
#  simple example of getters and setters in python.

class bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def get__balance(self):
        return self.__balance
    def set__balance(self, updated_balance):
        self.updated_balance = updated_balance
     
        if updated_balance >= 0:
            print(" ERROR : balance cannot be negative")
            return 
        
        self.__balance = updated_balance

