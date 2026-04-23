#Find the common elements between two arrays. 
arr1 = [1, 2, 3, 4, 3]
arr2 = [3, 4, 5, 6, 3]

common = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            
            # Check if already added (to avoid duplicates)
            already_present = False
            for k in range(len(common)):
                if common[k] == arr1[i]:
                    already_present = True
                    break
            
            if not already_present:
                common.append(arr1[i])

print("Common elements:", common)