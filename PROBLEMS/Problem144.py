# Count how many uppercase and lowercase letters a string has. Count how many uppercase and lowercase letters a string has. Count how many uppercase and lowercase letters a string has.
s = input("Enter a string: ")

upper_count = 0
lower_count = 0

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        upper_count += 1
    elif ch >= 'a' and ch <= 'z':
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)