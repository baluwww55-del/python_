#  CONDITION STATEMENTS :
# there are three condition staments :
# 1. if 2. elif 3.else
#ex:
x = 10
if x == 10:
    print("i can buy soya chips")
# this is the simple example of if condition.

# else :
# example :
x = int(input())
if x == 10:
    print(" yes i can buy soya chips ")
else:
    print(" you cant buy soya chips ")

# elif is for multiple condition :
# one of the most used statements in python programming language .
# example code:
signal = str(input())
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("ready")
else:
    print("go")

# these are the condition statements which is used in python .
# these are used for multiple condition statements .
# and another condition is there which is used widely .
# NESTED IF:
# example program :
signal = str(input())
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("ready")
elif signal == "blue":
    print("on vehicle")
else:
    print("go")
# this is the example of nested if structure .
# this condition is used for multiple condition staments .
# which makes code readable and modularity programming .
