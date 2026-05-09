# Print all unique elements (those that occur exactly once). 
def print_unique(arr):
    n = len(arr)
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        
        if count == 1:
            print(arr[i])

# Example
arr = [4, 5, 6, 4, 7, 5, 8]
print_unique(arr)