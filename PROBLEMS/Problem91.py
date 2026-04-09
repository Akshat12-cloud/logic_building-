#Input an element x — check if it exists in the array. 
def check_element(arr, x):
    if x in arr:
        return "Element exists in the array."
    else:
        return "Element does not exist in the array."

# Example
arr = [10, 20, 30, 40, 50]
x = 30

result = check_element(arr, x)
print(result)   
