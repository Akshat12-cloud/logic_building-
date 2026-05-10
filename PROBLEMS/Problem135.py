#Count how many characters (excluding spaces) are in the string.
s = "Hello World"
count = 0

for ch in s:
    if ch != ' ':
        count += 1

print("Number of characters (excluding spaces):", count)