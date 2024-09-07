import random

list = random.sample(range(1, 50), 10) # Generate a list of 10 random integers between 1 and 50 (inclusive)
res = []
prod = 1

for i in range(len(list)):
    prod = prod*list[i]

for i in range(len(list)):
    b = prod // list[i]
    res.append(b)

print("Original List:", list)
print("Resultant List:", res)
