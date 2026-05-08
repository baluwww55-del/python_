a = [1, 2, 3, 4, 4, 5]

a.append(6)
print(a)

a.reverse()
print(a)

print(a.count(4))

a.extend(["b"]) # type: ignore
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