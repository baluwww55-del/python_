# SETS :
# a set is a collection which is unordered, unchangeable and uninndexed.
# a set doesnot allow duplicate values. 
# example of duplicate values in sets :
myset = {"apple", "banana", "cherry", "apple"}
print(myset) # it will print ouput of apple only once because sets does not allow the duplicate variables.

# OPERATIONS OF SETS :

# 1. add() : this method is used to add an element to the set.
myset.add("orange") # add is the function which is used to add an element to the set.
print(myset) # now it will add orange to the myset elements .

myset.remove("banana") # remove is the function which is used to remove an element from the set.
print(myset) # now it will remove banana from the myset elements.

myset.pop() # pop is the function which is used to remove a random element from the set.
print(myset) # now it will remove a random element from the myset elements.

myset.clear() # clear is the function which is used to remove all the elements from the set.
print(myset) # now it will remove all the elements from the myset elements.
