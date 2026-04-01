#Input n and take n integers into an array; print them.
n = int(input("Enter the number of integers: "))
arr = []
for _ in range(n):
    arr.append(int(input("Enter an integer: ")))
print("The integers are:")
for num in arr:
    print(num)