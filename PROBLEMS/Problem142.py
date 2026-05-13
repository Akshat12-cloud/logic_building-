#Count the number of digits, letters, and special characters in a string. 
s = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for ch in s:
    # Check for letters (A-Z or a-z)
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        letters = letters + 1

    # Check for digits (0-9)
    elif ch >= '0' and ch <= '9':
        digits = digits + 1

    # Everything else is special character
    else:
        special = special + 1

print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of special characters:", special)