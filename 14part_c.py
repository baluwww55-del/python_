# login system using python :
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted (Admin)")
elif username == "user" and password == "abcd":
    print("Access granted (User)")
elif username == "admin" or username == "user":
    print("Wrong password")
else:
    print("Access denied")

# this is the login system using python  using condition statements and logical and assignment operators as well .
