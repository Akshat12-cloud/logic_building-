#Find the difference between the largest and smallest element.
def find_difference(arr):
    if len(arr) == 0:
        return None
    
    minimum = arr[0]
    maximum = arr[0]
    
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return maximum - minimum

# Example
arr = [4, 1, 9, 3, 7]
print(find_difference(arr))  # Output: 8