# ENCAPSULATION :
# encapsulation is one of the fundamental concepts in oop(object oriented programming).
# involves wrapping data and methods into a single unit known as class.

# SIMPLE CODE :
class ATM:
    def __init__(self, balance):
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount
        print(f"deposited:{amount}.new balance:{self.__balance}")
    def withdraw(self, amount):
        if amount > self.__balance:
            self.__balance -= amount
            print(f"withdrawn:{amount}.new balance:{self.__balance}")
        else:
            print("insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(200)

# in the above example the balance attribute is private and cannot be accesed directly from outside the class.
# it can only be modified through the deposit and withdraw methods.
# this ensures that the balance is always in a valid state and cannot be modified directly from outside.
