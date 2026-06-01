#. Reverse string but skip spaces.

s = input("Enter a string: ")


# Remove spaces and reverse remaining characters
chars = []
for ch in s:
    if ch != ' ':
        chars.append(ch)

chars.reverse()

result = ""
index = 0

for ch in s:
    if ch == ' ':
        result += ' '
    else:
        result += chars[index]
        index += 1

print("Reversed string:", result)
