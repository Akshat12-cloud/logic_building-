#Convert all characters of a string to lowercase
s = "HELLO WORLD"
result = ""

for ch in s:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)