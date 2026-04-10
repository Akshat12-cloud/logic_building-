#Find the first occurrence of a given number.
def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index of first occurrence
    return -1   # if element not found

# Example
arr = [2, 5, 7, 5, 9, 5]
target = int(input("Enter number: "))
result = first_occurrence(arr, target)

if result != -1:
    print("First occurrence is at index:", result)
else:
    print("Element not found")
