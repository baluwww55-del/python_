# Simple ATM Withdrawal System

print("Welcome to Python Bank 🏦")

balance = float(input("Enter your account balance: ₹"))
withdraw = float(input("Enter amount to withdraw: ₹"))

if withdraw <= 0:
    print("Invalid amount. Please enter a positive number.")
elif withdraw > balance:
    print("Insufficient balance ❌")
else:
    balance -= withdraw
    print("Transaction successful ✅")
    print("Remaining balance: ₹", balance)
