#1. Take a character and check if it is a letter, a digit, or neither.
char=input("enter the number:")
if char.isalpha():
    print(f"{char} is a letter")

elif char.isdigit():
    print(f"{char} is a digit")

else:
    print(f"{char} is neither a digit nor a letter")

