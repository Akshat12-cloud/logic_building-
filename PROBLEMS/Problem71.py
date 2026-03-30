#Reverse a string using recursion.
def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    else:
        # Recursive case
        return reverse_string(s[1:]) + s[0]

# Input
text = input("Enter a string: ")
result = reverse_string(text)

print("Reversed string:", result)
