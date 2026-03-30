# atm withdrawl simulator :
balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient funds")
elif amount % 100 != 0:
    print("Amount must be multiple of 100")
elif amount > 5000:
    print("Daily limit exceeded")
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance - amount)

#