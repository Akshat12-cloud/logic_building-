# Check if two strings are the reverse of each other
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Step 1: Find length manually
len1 = 0
for ch in s1:
    len1 += 1

len2 = 0
for ch in s2:
    len2 += 1

# Step 2: Check length
if len1 != len2:
    print("Not reverse of each other")
else:
    i = 0
    j = len2 - 1
    flag = True

    while i < len1:
        if s1[i] != s2[j]:
            flag = False
            break
        i += 1
        j -= 1

    if flag:
        print("Strings are reverse of each other")
    else:
        print("Not reverse of each other")