#Merge two arrays into a third array.
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

size1 = len(arr1)
size2 = len(arr2)

arr3 = [0] * (size1 + size2)

# Copy first array
for i in range(size1):
    arr3[i] = arr1[i]

# Copy second array
for i in range(size2):
    arr3[size1 + i] = arr2[i]

print(arr3)