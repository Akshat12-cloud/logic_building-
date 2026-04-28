#Find element-wise sum of two arrays (A[i] + B[i]). 
n = int(input("Enter size of arrays: "))

A = []
B = []
C = []

print("Enter elements of first array:")
for i in range(n):
    A.append(int(input()))

print("Enter elements of second array:")
for i in range(n):
    B.append(int(input()))

# Element-wise sum
for i in range(n):
    C.append(A[i] + B[i])

print("Element-wise sum array:")
for i in range(n):
    print(C[i], end=" ")