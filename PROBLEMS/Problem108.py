#Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.).
def swap_alternate(arr):
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]   # swap
    return arr


# Example
arr = [1, 2, 3, 4, 5, 6]
result = swap_alternate(arr)
print("After swapping:", result)