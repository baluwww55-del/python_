days1 = {"mon", "tue", "wed", "sat"}
days2 = {"thu", "fri", "sat", "sun", "mon"}

print("symmetric diff :", days1 ^ days2)
print("is subset :", days1 <= days2)
print("is superset :", days1 >= days2)
print("is disjoint :", days1.isdisjoint(days2))