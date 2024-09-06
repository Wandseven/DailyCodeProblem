list = [1,2,3,4,5,6,7]
k =10
notFound = True

# Check if any 2 numbers in the list add up to k

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == k:
            print(f'Numbers in the list that add up to {k} are: {list[i]} and {list[j]}')
            notFound = False
if notFound:
    print(f'No two numbers in the list add up to {k}')