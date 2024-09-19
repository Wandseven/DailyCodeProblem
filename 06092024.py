import random

#list = [1,2,3,4,5,6,7]
#k = 10

list = random.sample(range(1, 50), 10) # Generate a list of 10 random integers between 1 and 50 (inclusive)
k = random.randint(1, 50) # Generate a random integer between 1 and 50 (inclusive)

notFound = True

# Check if any 2 numbers in the list add up to k
print('Numbers in the list:', list)
print('Target sum:', k)
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == k:
            print(f'Numbers in the list that add up to {k} are: {list[i]} and {list[j]}')
            notFound = False
if notFound:
    print(f'No two numbers in the list add up to {k}')