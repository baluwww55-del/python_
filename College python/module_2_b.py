# Tuples
L1 = ()  
L2 = (1, 2, 3, 4, 5, 6)
L3 = ("c program", "java", "python")

print(L1)
print(L2[2])
print(L3[1:3])

# Tuple Functions
t = (2, 3, 4, 4, 5, 6)
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
print(t.count(4))
print(t.index(3))

# LIST

L1 = []
L2 = [1, 2, 3, 4, 5, 6]
L3 = ["c", "java", "python"]
L4 = [123, "python", 3.7]

print(L1)
print(L2)
print(L3)
print(L4)

# LIST OPERATIONS

num = [1, 2, 3, 4, 5]
lang = ["python", "c", "java", "php"]

print(num + lang)
print(num * 2)
print(lang[2])
print(lang[1:4])
print("cpp" in lang)
print(6 not in num)   # fixed

# Iterating List
lang = ["python", "c", "java", "php"]
print("The list items are:\n")
for i in lang:
    print(i)

# List Functions
a = [1, 2, 3, 4, 4, 5]
a.append(6)
print(a)
a.reverse()
print(a)
print(a.count(4))   
a.extend(["b"])     
print(a)

print(a.index(2))   

a.insert(2, 10)
print(a)

a.pop(1)
print(a)

a.remove(3)
print(a)

a.clear()
print(a)

# SETS

days1 = {"mon", "tue", "wed", "sat"}
days2 = {"thu", "fri", "sat", "sun", "mon"}

print("days1 union days2 :", days1 | days2)
print("days1 intersection days2 :", days1 & days2)
print("days1 difference days2 :", days1 - days2)

d1 = {}  
d2 = {1: "one", 2: "two", 3: "three"}
d3 = {"name": "Ashu", "age": 20, "course": "BCA"}

print(d1)
print(d2)
print(d3)

# Dictionary Functions
d = {"a": 1, "b": 2, "c": 3}

print(len(d))
print(d.keys())
print(d.values())
print(d.items())

d.update({"d": 4})
print(d)

print(d.pop("a"))
print(d)

d.clear()
print(d)

# Dictionary Operations
d = {"a": 1, "b": 2, "c": 3}

d["d"] = 4          
d["a"] = 10         

print(d)

del d["b"]          
print(d)