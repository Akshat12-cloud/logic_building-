#Print all characters of a string one by one recursively.
def print_chars(s):
    if len(s) == 0:   
        return
    print(s[0])       
    print_chars(s[1:])  


# Example
text = input("Enter a string: ")
print_chars(text)