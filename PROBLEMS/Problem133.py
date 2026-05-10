#Convert all characters of a string to uppercase.
s = "hello world"
result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)