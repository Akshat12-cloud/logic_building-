# Count how many elements are common between two arrays.
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

count = 0

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            count += 1
            break   # avoid counting duplicates multiple times

print("Number of common elements:", count)