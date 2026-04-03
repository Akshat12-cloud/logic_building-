#Find the minimum element in an array.
# Find the minimum element in an array
def minelement(arr):
    minimum = arr[0]   # assume first element is minimum
    
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    
    return minimum


# Taking input from user
arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

result = minelement(arr)
print("The minimum element is:", result)