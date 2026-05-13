# Check whether the string is empty or not. 
s = input("Enter a string: ")

count = 0

for ch in s:
    count = count + 1

if count == 0:
    print("String is empty.")
else:
    print("String is not empty.")