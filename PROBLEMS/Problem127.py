#Find the second smallest element in an array. 
def second_smallest(arr):
    first = float('inf')
    second = float('inf')
    
    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    
    return second if second != float('inf') else None

# Example
arr = [4, 1, 3, 2, 5]
print(second_smallest(arr))  # Output: 2