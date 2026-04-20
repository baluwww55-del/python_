# loops questions practice :

# 1 . print multiplication table of 7 :
for i in range(7,8):
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")

# 2. print number 1 to 100 :

for i in range(1,100):
    print(i)


# 3. print 100 to 1

i = 101
while i >= 1 :
    print(i)
    i = i-1


# 4. print 1 to 100 odd numbers:
for i in range(1,100,2):
    print(i)


# 5. print 1 to 100 even numbers :
for i in range(0,100,2):
    print(i)


# 6 . print sum of first n natural numbers:

n = 54
total = 0 
for i in range(1,n+1):
    total = total + i 
    print("sum:", total)


# we can make this code as simple :

n = 54
sum = n*(n+1)/2
print("sum", +sum)

