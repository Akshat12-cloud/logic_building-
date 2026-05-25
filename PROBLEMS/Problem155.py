#Remove all vowels from a string.
# Remove all vowels from a string without using built-in functions

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and \
       ch != 'A' and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U':
        result = result + ch

print("String without vowels:", result)