#Find the average of array elements.
n = int(input("Enter the number of integers: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter an integer: ")))
print("Average of array elements is:", sum(arr)/n)