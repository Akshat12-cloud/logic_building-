# Find the sum of all elements except the largest and smallest.
def sum_except_min_max(arr):
    if len(arr) <= 2:
        return 0   # Not enough elements
    
    total = 0
    minimum = arr[0]
    maximum = arr[0]
    
    for num in arr:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return total - minimum - maximum

# Example
arr = [4, 1, 9, 3, 7]
print(sum_except_min_max(arr))  # Output: 14