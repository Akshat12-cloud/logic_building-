#Compare two arrays — check if they are equal (same elements & order).  
def are_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print("Arrays are equal" if are_equal(a, b) else "Arrays are not equal")