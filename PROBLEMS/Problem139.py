#Compare two strings lexicographically (like dictionary order).
# Take two strings as input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Compare strings
if str1 == str2:
    print("Both strings are equal.")
elif str1 < str2:
    print(str1, "comes before", str2)
else:
    print(str1, "comes after", str2)