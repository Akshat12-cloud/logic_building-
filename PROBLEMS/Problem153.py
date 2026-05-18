#Check whether a string is a palindrome.
s = input("Enter a string: ")

length = 0
for char in s:
    length += 1

i = 0
j = length - 1
is_palindrome = True

while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")