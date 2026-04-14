password = "1234"

while True:
    user = input("Enter password: ")
    if user == password:
        print("Access Granted")
        break
    else:
        print("Try again")
