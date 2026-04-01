#Convert a string to uppercase recursively. 
def to_uppercase(s):
    # Base case
    if len(s) == 0:
        return ""
    
    # Convert first character to uppercase
    first_char = s[0]
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
    
    # Recursive call for rest of string
    return first_char + to_uppercase(s[1:])


# Input
text = input("Enter a string: ")
result = to_uppercase(text)

print("Uppercase string:", result)