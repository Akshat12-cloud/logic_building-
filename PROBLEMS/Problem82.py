#Find the sum of all elements in an array.
n = int(input("Enter the number of integers: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter an integer: ")))
print("Sum of all elements in the array is:", sum(arr))