#Check if all elements in an array are unique.
def is_unique(arr):
    if len(arr) == len(set(arr)):
        return True
    else:
        return False

# Example
arr = [1, 2, 3, 4, 5]
print(is_unique(arr))