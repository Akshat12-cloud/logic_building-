#Print the string in reverse order recursively (without using loops). 
def print_reverse(s):
    if len(s) == 0:
        return
    print_reverse(s[1:])
    print(s[0])

# Example
text = input("Enter a string: ")
print_reverse(text)