import random

# Find the lowest positive integer not present in the list


list = random.sample(range(-5, 5), 5)   # Generate a random list of 5 integers between -5 and 5
positive = [0]  # Initialize an list to store positive integers in the original list, we need value 0 in case the list is not start with 1.
sort = []   # Initialize an empty list to store the sorted positive integers

# Separate positive integers from the original list and sort them in ascending order
for i in range(len(list)):
    if list[i] > 0:
        positive.append(list[i]) 
sort = sorted(positive)

# Find the lowest positive integer not present in the original list. Because the list is sorted, we need to check if 2 numbers next to each other is consecutive, if not then the missing number is the number next to the left one. If all numbers in the list are consecutive, then the missing number is the last number in the list + 1.
for j in range(len(sort)):
    a = sort[j] - sort[j-1]
    if a > 1:
        res = sort[j-1] + 1 
        break
    else:
        res = sort[j] + 1  


print(list)
print(sort)
print(res)