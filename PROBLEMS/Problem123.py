# Print all elements that appear more than once. 
# Function to print duplicate elements
def print_duplicates(arr):
    n = len(arr)
    found = False
    
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1
        
        # Check if element already checked before
        already_checked = False
        for k in range(i):
            if arr[k] == arr[i]:
                already_checked = True
                break
        
        if count > 1 and not already_checked:
            print(arr[i])
            found = True
    
    if not found:
        print("No duplicate elements")

# Example
arr = [1, 2, 3, 2, 4, 5, 1, 6]
print_duplicates(arr)