#Check if the array is sorted in ascending order. 
def is_sorted(arr):
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True


# Example
arr = [1, 2, 3, 4, 5]

if is_sorted(arr):
    print("Array is sorted in ascending order")
else:
    print("Array is NOT sorted in ascending order")