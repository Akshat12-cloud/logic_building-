#Count how many characters (excluding spaces) are in the string. 
string = input("Enter a string: ")

count = 0

for ch in string:
    if ch != " ":
        count = count + 1

print("Number of characters (excluding spaces):", count)