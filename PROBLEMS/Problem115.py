#Find elements that are in one array but not in the other. 
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7]

# Elements in arr1 but not in arr2
unique1 = []
for i in range(len(arr1)):
    found = False
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            found = True
            break
    if not found:
        unique1.append(arr1[i])

# Elements in arr2 but not in arr1
unique2 = []
for i in range(len(arr2)):
    found = False
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            found = True
            break
    if not found:
        unique2.append(arr2[i])

print("Elements in arr1 but not in arr2:", unique1)
print("Elements in arr2 but not in arr1:", unique2)