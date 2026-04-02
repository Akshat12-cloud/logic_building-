#Find the maximum element in an array.
n = int(input("Enter the number of integers: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter an integer: ")))
print("Maximum element in the array is:", max(arr))