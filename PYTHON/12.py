#  KEYS VALUES AND DICTIONARIES :
# 1. Create a dictionary with some key-value pairs and print it.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
# we create dictionaries with the help of flower or curly brackets {} and we can access the values of the dictionary with the help of keys.
# to get value from the dictionry we use the key of the dictionary and we can also use the get().
# 2. Add a new key-value pair to the dictionary and print it.
# example :
birthday = {"balajii": "11-11-2000"}
print(birthday) # it will print the birthday dictionary with the key and value."}
# example of keys and values :
birthday = {"balaji":  "11-05-2005"}
print(birthday["balaji"])   # it will print the value of the key "balaji" which is "11-05-2005".

# keys and values are very useful in programming because they allow us to store and retrieve date when we needed .
# another example of keys and values :
bhagesh = {"work": " cyber engineer", "hobby": "checking login details"}
print(bhagesh["work"]) # it will print the value of the key "work" which is "cyber engineer".

# there are some operations of dictionaries which are very useful in programmming :
# 1. update() : this method is used to update the value of a key in the dictionary.
bhagesh.update({"work": "cyber security analyst"}) # it will update the value of the key "work" to "cyber security analyst".
print(bhagesh["work"]) # now it will print the updated value of the key "work" which is "cyber security analyst".   
# 2. pop() : this method is used to remove a key-value pair from the dictionary.
bhagesh.pop("hobby") # it will remove the key "hobby" and its value from the dictionary.
print(bhagesh) # now it will print the dictionary without the key "hobby" and its value.
# 3. clear() : this method is used to remove all the key-value pairs from the dictionary.
bhagesh.clear() # it will remove all the key-value pairs from the dictionary.
print(bhagesh) # now it will print an empty dictionary because all the key-value
# pairs have been removed from the dictionary. 

# these are the some operations of dictrionaries which are very useful in programming because they allow us to manipulate the data stored in the dictionary. 
