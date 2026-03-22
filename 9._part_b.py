# LIST OPERATIONS :
# 1) slicing the list :
l = ["a","b","c","d","e"]
print(l[3])

# common functions of list :
l = ["a","b","c","d","e"]
print(len(l)) # it will print the length of the list which is 5 because there are 5 items in the list.
print(max(l)) # it will print the maximum item in the list which is e because e is the maximum item in the list.
print(min(l)) # it will print the minimum item in the list which is a because a is the minimum item in the list.

# SORT IN LISTS :
l = [5, 2, 9, 1, 5, 6]
l.sort() # it will sort the list in ascending order.
print(l) # it will print the sorted list which is [1, 2, 5, 5, 6, 9].
l.sort(reverse=True) # it will sort the list in descending order.       
print(l) # it will print the sorted list in descending order which is [9, 6, 5, 5, 2, 1].

#  SUM ONF NUMBERS IN A LIST :
items = [90, 95, 85, 80, 75]
total = sum(items) # it will calculate the sum of the items in the list which is 425.
print(total) # it will print the total which is 425.
print(items.index(95)) # it will print the index of the item 95 in the list which is 1 because 95 is at the index of 1 in the list.
print(items.count(85)) # it will print the count of the item 85 in the list which is 1 because there is only one 85 in the list.

# MATRIX IN A LIST :
# LIST IN A LIST IN KNOWN AS MATRIX.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # this is a matrix which is a list of lists.
print(matrix[0]) # it will print the first list in the matrix which is [1, 2, 3] because the first list is at the index of 0 in the matrix.
print(matrix[1][2]) # it will print the item at the index of 2 in the second list in the matrix which is 6 because the item at the index of 2 in the second list is 6.      

# THESE ARE THE BASIC OPERATIONS OF LISTS IN  PYTHON LANGUAGE . 