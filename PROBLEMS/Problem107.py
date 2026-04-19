#Rotate an array by one position to the right. 
def rotate_right(arr):
    if len(arr) == 0:
        return arr
    
    last = arr[-1]           # store last element
    
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]    # shift elements right
    
    arr[0] = last            # place last at first position
    return arr


# Example
arr = [1, 2, 3, 4, 5]
result = rotate_right(arr)
print("Rotated array:", result)