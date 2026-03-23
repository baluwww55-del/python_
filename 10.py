#  TUPLES :
#TUPLES IN PYTHON:
# a tuple is a collection which is ordered and unchangeable. 
# in python list are changed / modified .
# a tuple is defined by using parentheses () and list is defined by using square brackets [].
# example of tuple:
genders = ("male", "female", "others")
print(genders)
print(type(genders))
# if we have too add tuples :
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)
# tuples are repeated :
tuple4 = ("python",) * 3
print(tuple4)
# ADVANTAGES OF TUPLES :
# 1. tuples are immutable, which means that once a tuple is created it cant be changed/modified.
# 2. tuples are faster than lists because of their immutability.
# 3. tuples can be used as keys in dictionaries because they are immutable, while lists cannot be used as keys in dictionaries because they are mutable.
# 4. tuples can be used as dimension in sets because they are immutable, while lists cannot be used as dimension in sets because they are mutable.
# we can see index in tuples :
tuple5 = ("python", "java", "c++")
print(tuple5[0]) # output: python
print(tuple5[1]) # output: java
# these are the some operations about tuples. 
