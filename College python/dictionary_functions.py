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