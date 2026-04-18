# LISTS IN PYTHON :
# lists in python is used to store the multiple data types / items .
# ex :
item1 = "apple"
item2 = "banana"    
print(item2) # it will print banana because the banana is stored in item2 variable.

# we can store the mulitple items in a single list .
# example :
items = ["apple", "banana", "orange", 10, 20, 30] # so these are the items in the list.
print(items[2]) # it will print orange because the orange is stored in the index of 2 in the list.
# the index will start from 0 .
items = ["apple", "banana", "orange", 10, 20, 30]
print(items)
items.pop() # it will remove the last item from the list which is 30.
print(items) # it will print the list without 30 because we removed it from the list.
items.append("grape") # it will add the grape to the end of the list.
print(items) # it will print the list with grape because we added it to the list.
items.insert(1, "mango") # it will insert the mango at the index of 1 in the list.
print(items) # it will print the list with mango because we inserted it at the index of 1 in the list.
items.remove("banana") # it will remove the banana from the list.
print(items) # it will print the list without banana because we removed it from the list.
items.clear() # it will remove all the items from the list.
print(items) # it will print an empty list because we cleared all the items from the list.
