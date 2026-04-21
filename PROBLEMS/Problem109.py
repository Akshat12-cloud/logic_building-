#Copy one array to another manually.
arr1 = [1, 2, 3, 4, 5]

# Create empty list with same size
arr2 = [0] * len(arr1)

# Manual copy
for i in range(len(arr1)):
    arr2[i] = arr1[i]

print(arr2)